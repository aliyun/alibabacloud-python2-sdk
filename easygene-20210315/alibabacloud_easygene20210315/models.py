# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AbortRunRequest(TeaModel):
    def __init__(self, run_id=None, workspace=None):
        self.run_id = run_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbortRunRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class AbortRunResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbortRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbortRunResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AbortRunResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AbortRunResponse, self).to_map()
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
            temp_model = AbortRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbortSubmissionRequest(TeaModel):
    def __init__(self, submission_id=None, workspace=None):
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbortSubmissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class AbortSubmissionResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbortSubmissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbortSubmissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AbortSubmissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AbortSubmissionResponse, self).to_map()
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
            temp_model = AbortSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyPublicEntityRequest(TeaModel):
    def __init__(self, dataset=None, entity_type=None, workspace=None):
        self.dataset = dataset  # type: str
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyPublicEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dataset') is not None:
            self.dataset = m.get('Dataset')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CopyPublicEntityResponseBody(TeaModel):
    def __init__(self, entity_type=None, host_id=None, request_id=None, workspace=None):
        self.entity_type = entity_type  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyPublicEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CopyPublicEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CopyPublicEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CopyPublicEntityResponse, self).to_map()
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
            temp_model = CopyPublicEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequestConfigs(TeaModel):
    def __init__(self, content=None, path=None):
        self.content = content  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequestConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateAppRequestDependencies(TeaModel):
    def __init__(self, content=None, path=None):
        self.content = content  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequestDependencies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, app_name=None, app_type=None, client_token=None, configs=None, definition=None,
                 dependencies=None, description=None, documentation=None, labels=None, language=None, language_version=None,
                 path=None, revision_comment=None, revision_tag=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.client_token = client_token  # type: str
        self.configs = configs  # type: list[CreateAppRequestConfigs]
        self.definition = definition  # type: str
        self.dependencies = dependencies  # type: list[CreateAppRequestDependencies]
        self.description = description  # type: str
        self.documentation = documentation  # type: str
        self.labels = labels  # type: str
        self.language = language  # type: str
        self.language_version = language_version  # type: str
        self.path = path  # type: str
        self.revision_comment = revision_comment  # type: str
        self.revision_tag = revision_tag  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.dependencies:
            for k in self.dependencies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.definition is not None:
            result['Definition'] = self.definition
        result['Dependencies'] = []
        if self.dependencies is not None:
            for k in self.dependencies:
                result['Dependencies'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.documentation is not None:
            result['Documentation'] = self.documentation
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.path is not None:
            result['Path'] = self.path
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = CreateAppRequestConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k in m.get('Dependencies'):
                temp_model = CreateAppRequestDependencies()
                self.dependencies.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Documentation') is not None:
            self.documentation = m.get('Documentation')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateAppShrinkRequest(TeaModel):
    def __init__(self, app_name=None, app_type=None, client_token=None, configs_shrink=None, definition=None,
                 dependencies_shrink=None, description=None, documentation=None, labels=None, language=None, language_version=None,
                 path=None, revision_comment=None, revision_tag=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.client_token = client_token  # type: str
        self.configs_shrink = configs_shrink  # type: str
        self.definition = definition  # type: str
        self.dependencies_shrink = dependencies_shrink  # type: str
        self.description = description  # type: str
        self.documentation = documentation  # type: str
        self.labels = labels  # type: str
        self.language = language  # type: str
        self.language_version = language_version  # type: str
        self.path = path  # type: str
        self.revision_comment = revision_comment  # type: str
        self.revision_tag = revision_tag  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.dependencies_shrink is not None:
            result['Dependencies'] = self.dependencies_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.documentation is not None:
            result['Documentation'] = self.documentation
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.path is not None:
            result['Path'] = self.path
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Dependencies') is not None:
            self.dependencies_shrink = m.get('Dependencies')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Documentation') is not None:
            self.documentation = m.get('Documentation')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(self, app_name=None, host_id=None, request_id=None, revision=None, revision_tag=None,
                 workspace=None):
        self.app_name = app_name  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.revision = revision  # type: str
        self.revision_tag = revision_tag  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppResponse, self).to_map()
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEntityRequestEntityItems(TeaModel):
    def __init__(self, entity_data=None, entity_name=None):
        self.entity_data = entity_data  # type: dict[str, str]
        self.entity_name = entity_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEntityRequestEntityItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class CreateEntityRequest(TeaModel):
    def __init__(self, client_token=None, entity_items=None, entity_type=None, workspace=None):
        self.client_token = client_token  # type: str
        self.entity_items = entity_items  # type: list[CreateEntityRequestEntityItems]
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = CreateEntityRequestEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateEntityShrinkRequest(TeaModel):
    def __init__(self, client_token=None, entity_items_shrink=None, entity_type=None, workspace=None):
        self.client_token = client_token  # type: str
        self.entity_items_shrink = entity_items_shrink  # type: str
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEntityShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.entity_items_shrink is not None:
            result['EntityItems'] = self.entity_items_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EntityItems') is not None:
            self.entity_items_shrink = m.get('EntityItems')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateEntityResponseBody(TeaModel):
    def __init__(self, entity_type=None, host_id=None, request_id=None, workspace=None):
        self.entity_type = entity_type  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEntityResponse, self).to_map()
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
            temp_model = CreateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRunRequestExecuteOptions(TeaModel):
    def __init__(self, call_caching=None, delete_intermediate_results=None, failure_mode=None,
                 use_relative_output_paths=None):
        self.call_caching = call_caching  # type: bool
        self.delete_intermediate_results = delete_intermediate_results  # type: bool
        self.failure_mode = failure_mode  # type: str
        self.use_relative_output_paths = use_relative_output_paths  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRunRequestExecuteOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_caching is not None:
            result['CallCaching'] = self.call_caching
        if self.delete_intermediate_results is not None:
            result['DeleteIntermediateResults'] = self.delete_intermediate_results
        if self.failure_mode is not None:
            result['FailureMode'] = self.failure_mode
        if self.use_relative_output_paths is not None:
            result['UseRelativeOutputPaths'] = self.use_relative_output_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        if m.get('UseRelativeOutputPaths') is not None:
            self.use_relative_output_paths = m.get('UseRelativeOutputPaths')
        return self


class CreateRunRequest(TeaModel):
    def __init__(self, app_name=None, app_revision=None, client_token=None, default_runtime=None, description=None,
                 execute_directory=None, execute_options=None, inputs=None, labels=None, output_folder=None, revision_tag=None,
                 role=None, run_name=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.client_token = client_token  # type: str
        self.default_runtime = default_runtime  # type: str
        self.description = description  # type: str
        self.execute_directory = execute_directory  # type: str
        self.execute_options = execute_options  # type: CreateRunRequestExecuteOptions
        self.inputs = inputs  # type: str
        self.labels = labels  # type: str
        self.output_folder = output_folder  # type: str
        self.revision_tag = revision_tag  # type: str
        self.role = role  # type: str
        self.run_name = run_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.execute_options:
            self.execute_options.validate()

    def to_map(self):
        _map = super(CreateRunRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.description is not None:
            result['Description'] = self.description
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.role is not None:
            result['Role'] = self.role
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            temp_model = CreateRunRequestExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateRunShrinkRequest(TeaModel):
    def __init__(self, app_name=None, app_revision=None, client_token=None, default_runtime=None, description=None,
                 execute_directory=None, execute_options_shrink=None, inputs=None, labels=None, output_folder=None, revision_tag=None,
                 role=None, run_name=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.client_token = client_token  # type: str
        self.default_runtime = default_runtime  # type: str
        self.description = description  # type: str
        self.execute_directory = execute_directory  # type: str
        self.execute_options_shrink = execute_options_shrink  # type: str
        self.inputs = inputs  # type: str
        self.labels = labels  # type: str
        self.output_folder = output_folder  # type: str
        self.revision_tag = revision_tag  # type: str
        self.role = role  # type: str
        self.run_name = run_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRunShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.description is not None:
            result['Description'] = self.description
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options_shrink is not None:
            result['ExecuteOptions'] = self.execute_options_shrink
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.role is not None:
            result['Role'] = self.role
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            self.execute_options_shrink = m.get('ExecuteOptions')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateRunResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None, run_id=None, workspace=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.run_id = run_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateRunResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRunResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRunResponse, self).to_map()
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
            temp_model = CreateRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubmissionRequest(TeaModel):
    def __init__(self, app_name=None, client_token=None, default_runtime=None, entity_names=None, entity_type=None,
                 execute_directory=None, execute_options=None, inputs=None, output_folder=None, outputs=None, revision=None,
                 revision_tag=None, workspace=None):
        self.app_name = app_name  # type: str
        self.client_token = client_token  # type: str
        self.default_runtime = default_runtime  # type: str
        self.entity_names = entity_names  # type: list[str]
        self.entity_type = entity_type  # type: str
        self.execute_directory = execute_directory  # type: str
        self.execute_options = execute_options  # type: str
        self.inputs = inputs  # type: str
        self.output_folder = output_folder  # type: str
        self.outputs = outputs  # type: str
        self.revision = revision  # type: str
        self.revision_tag = revision_tag  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubmissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            self.execute_options = m.get('ExecuteOptions')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateSubmissionShrinkRequest(TeaModel):
    def __init__(self, app_name=None, client_token=None, default_runtime=None, entity_names_shrink=None,
                 entity_type=None, execute_directory=None, execute_options=None, inputs=None, output_folder=None, outputs=None,
                 revision=None, revision_tag=None, workspace=None):
        self.app_name = app_name  # type: str
        self.client_token = client_token  # type: str
        self.default_runtime = default_runtime  # type: str
        self.entity_names_shrink = entity_names_shrink  # type: str
        self.entity_type = entity_type  # type: str
        self.execute_directory = execute_directory  # type: str
        self.execute_options = execute_options  # type: str
        self.inputs = inputs  # type: str
        self.output_folder = output_folder  # type: str
        self.outputs = outputs  # type: str
        self.revision = revision  # type: str
        self.revision_tag = revision_tag  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubmissionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            self.execute_options = m.get('ExecuteOptions')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateSubmissionResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None, submission_id=None, workspace=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubmissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateSubmissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSubmissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSubmissionResponse, self).to_map()
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
            temp_model = CreateSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequestInputsExpression(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: int
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequestInputsExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class CreateTemplateRequestOutputsExpression(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: int
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequestOutputsExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, app_name=None, app_revision=None, client_token=None, description=None,
                 inputs_expression=None, labels=None, outputs_expression=None, revision_tag=None, root_entity=None,
                 template_name=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.inputs_expression = inputs_expression  # type: list[CreateTemplateRequestInputsExpression]
        self.labels = labels  # type: str
        self.outputs_expression = outputs_expression  # type: list[CreateTemplateRequestOutputsExpression]
        self.revision_tag = revision_tag  # type: str
        self.root_entity = root_entity  # type: str
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.inputs_expression:
            for k in self.inputs_expression:
                if k:
                    k.validate()
        if self.outputs_expression:
            for k in self.outputs_expression:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        result['InputsExpression'] = []
        if self.inputs_expression is not None:
            for k in self.inputs_expression:
                result['InputsExpression'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        result['OutputsExpression'] = []
        if self.outputs_expression is not None:
            for k in self.outputs_expression:
                result['OutputsExpression'].append(k.to_map() if k else None)
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.inputs_expression = []
        if m.get('InputsExpression') is not None:
            for k in m.get('InputsExpression'):
                temp_model = CreateTemplateRequestInputsExpression()
                self.inputs_expression.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        self.outputs_expression = []
        if m.get('OutputsExpression') is not None:
            for k in m.get('OutputsExpression'):
                temp_model = CreateTemplateRequestOutputsExpression()
                self.outputs_expression.append(temp_model.from_map(k))
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateTemplateShrinkRequest(TeaModel):
    def __init__(self, app_name=None, app_revision=None, client_token=None, description=None,
                 inputs_expression_shrink=None, labels=None, outputs_expression_shrink=None, revision_tag=None, root_entity=None,
                 template_name=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.inputs_expression_shrink = inputs_expression_shrink  # type: str
        self.labels = labels  # type: str
        self.outputs_expression_shrink = outputs_expression_shrink  # type: str
        self.revision_tag = revision_tag  # type: str
        self.root_entity = root_entity  # type: str
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.inputs_expression_shrink is not None:
            result['InputsExpression'] = self.inputs_expression_shrink
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.outputs_expression_shrink is not None:
            result['OutputsExpression'] = self.outputs_expression_shrink
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputsExpression') is not None:
            self.inputs_expression_shrink = m.get('InputsExpression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputsExpression') is not None:
            self.outputs_expression_shrink = m.get('OutputsExpression')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None, template_name=None, workspace=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateResponse, self).to_map()
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceRequest(TeaModel):
    def __init__(self, client_token=None, description=None, job_lifecycle=None, labels=None, role=None, storage=None,
                 workspace=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.job_lifecycle = job_lifecycle  # type: int
        self.labels = labels  # type: str
        self.role = role  # type: str
        self.storage = storage  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.role is not None:
            result['Role'] = self.role
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None, workspace=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWorkspaceResponseBody

    def validate(self):
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


class DeleteAppRequest(TeaModel):
    def __init__(self, app_name=None, revision=None, workspace=None):
        self.app_name = app_name  # type: str
        self.revision = revision  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppResponse, self).to_map()
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityRequest(TeaModel):
    def __init__(self, entity_type=None, workspace=None):
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteEntityResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEntityResponse, self).to_map()
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
            temp_model = DeleteEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityItemsRequest(TeaModel):
    def __init__(self, entity_names=None, entity_type=None, workspace=None):
        self.entity_names = entity_names  # type: list[str]
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEntityItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteEntityItemsShrinkRequest(TeaModel):
    def __init__(self, entity_names_shrink=None, entity_type=None, workspace=None):
        self.entity_names_shrink = entity_names_shrink  # type: str
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEntityItemsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteEntityItemsResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEntityItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEntityItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEntityItemsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEntityItemsResponse, self).to_map()
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
            temp_model = DeleteEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRunRequest(TeaModel):
    def __init__(self, run_id=None, workspace=None):
        self.run_id = run_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRunRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteRunResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRunResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRunResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRunResponse, self).to_map()
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
            temp_model = DeleteRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubmissionRequest(TeaModel):
    def __init__(self, submission_id=None, workspace=None):
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubmissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteSubmissionResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubmissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSubmissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSubmissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSubmissionResponse, self).to_map()
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
            temp_model = DeleteSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, template_name=None, workspace=None):
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTemplateResponse, self).to_map()
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceRequest(TeaModel):
    def __init__(self, workspace=None):
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteWorkspaceResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWorkspaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWorkspaceResponse, self).to_map()
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
            temp_model = DeleteWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadEntityRequest(TeaModel):
    def __init__(self, entity_names=None, entity_type=None, workspace=None):
        self.entity_names = entity_names  # type: list[str]
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DownloadEntityShrinkRequest(TeaModel):
    def __init__(self, entity_names_shrink=None, entity_type=None, workspace=None):
        self.entity_names_shrink = entity_names_shrink  # type: str
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadEntityShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DownloadEntityResponseBody(TeaModel):
    def __init__(self, entity_csvfile=None, host_id=None, request_id=None):
        self.entity_csvfile = entity_csvfile  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_csvfile is not None:
            result['EntityCSVFile'] = self.entity_csvfile
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityCSVFile') is not None:
            self.entity_csvfile = m.get('EntityCSVFile')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DownloadEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DownloadEntityResponse, self).to_map()
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
            temp_model = DownloadEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(self, app_name=None, revision=None, revision_tag=None, workspace=None):
        self.app_name = app_name  # type: str
        self.revision = revision  # type: str
        self.revision_tag = revision_tag  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetAppResponseBodyConfigs(TeaModel):
    def __init__(self, content=None, path=None):
        self.content = content  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBodyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetAppResponseBodyDependencies(TeaModel):
    def __init__(self, content=None, path=None):
        self.content = content  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBodyDependencies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetAppResponseBodyInputs(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: long
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBodyInputs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class GetAppResponseBodyOutputs(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: long
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBodyOutputs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class GetAppResponseBodyRevisions(TeaModel):
    def __init__(self, create_time=None, revision=None, revision_comment=None, revision_tag=None):
        self.create_time = create_time  # type: str
        self.revision = revision  # type: str
        self.revision_comment = revision_comment  # type: str
        self.revision_tag = revision_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBodyRevisions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(self, app_name=None, app_type=None, configs=None, create_time=None, definition=None,
                 dependencies=None, description=None, documentation=None, host_id=None, inputs=None, labels=None, language=None,
                 language_version=None, last_modified_time=None, outputs=None, path=None, request_id=None, revision=None,
                 revision_comment=None, revision_tag=None, revisions=None, scope=None, source=None, url=None, workflow_name=None,
                 workspace=None):
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.configs = configs  # type: list[GetAppResponseBodyConfigs]
        self.create_time = create_time  # type: str
        self.definition = definition  # type: str
        self.dependencies = dependencies  # type: list[GetAppResponseBodyDependencies]
        self.description = description  # type: str
        self.documentation = documentation  # type: str
        self.host_id = host_id  # type: str
        self.inputs = inputs  # type: list[GetAppResponseBodyInputs]
        self.labels = labels  # type: dict[str, str]
        self.language = language  # type: str
        self.language_version = language_version  # type: str
        self.last_modified_time = last_modified_time  # type: str
        self.outputs = outputs  # type: list[GetAppResponseBodyOutputs]
        self.path = path  # type: str
        self.request_id = request_id  # type: str
        self.revision = revision  # type: str
        self.revision_comment = revision_comment  # type: str
        self.revision_tag = revision_tag  # type: str
        self.revisions = revisions  # type: list[GetAppResponseBodyRevisions]
        self.scope = scope  # type: str
        self.source = source  # type: str
        self.url = url  # type: str
        self.workflow_name = workflow_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.dependencies:
            for k in self.dependencies:
                if k:
                    k.validate()
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.revisions:
            for k in self.revisions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.definition is not None:
            result['Definition'] = self.definition
        result['Dependencies'] = []
        if self.dependencies is not None:
            for k in self.dependencies:
                result['Dependencies'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.documentation is not None:
            result['Documentation'] = self.documentation
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.path is not None:
            result['Path'] = self.path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        result['Revisions'] = []
        if self.revisions is not None:
            for k in self.revisions:
                result['Revisions'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.url is not None:
            result['URL'] = self.url
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = GetAppResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k in m.get('Dependencies'):
                temp_model = GetAppResponseBodyDependencies()
                self.dependencies.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Documentation') is not None:
            self.documentation = m.get('Documentation')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = GetAppResponseBodyInputs()
                self.inputs.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = GetAppResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        self.revisions = []
        if m.get('Revisions') is not None:
            for k in m.get('Revisions'):
                temp_model = GetAppResponseBodyRevisions()
                self.revisions.append(temp_model.from_map(k))
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppResponse, self).to_map()
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEntityRequest(TeaModel):
    def __init__(self, entity_type=None, workspace=None):
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetEntityResponseBody(TeaModel):
    def __init__(self, attributes=None, entity_type=None, host_id=None, request_id=None, total_count=None,
                 workspace=None):
        self.attributes = attributes  # type: list[str]
        self.entity_type = entity_type  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEntityResponse, self).to_map()
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
            temp_model = GetEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGlobalAppRequest(TeaModel):
    def __init__(self, app_name=None, app_version=None, attributes=None, location=None, namespace_name=None):
        self.app_name = app_name  # type: str
        self.app_version = app_version  # type: str
        self.attributes = attributes  # type: list[str]
        self.location = location  # type: str
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGlobalAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.location is not None:
            result['Location'] = self.location
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetGlobalAppShrinkRequest(TeaModel):
    def __init__(self, app_name=None, app_version=None, attributes_shrink=None, location=None, namespace_name=None):
        self.app_name = app_name  # type: str
        self.app_version = app_version  # type: str
        self.attributes_shrink = attributes_shrink  # type: str
        self.location = location  # type: str
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGlobalAppShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.location is not None:
            result['Location'] = self.location
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetGlobalAppResponseBodyAppDescriptorFiles(TeaModel):
    def __init__(self, checksum=None, content=None, file_type=None, path=None, url=None):
        self.checksum = checksum  # type: str
        self.content = content  # type: str
        self.file_type = file_type  # type: str
        self.path = path  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGlobalAppResponseBodyAppDescriptorFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['Checksum'] = self.checksum
        if self.content is not None:
            result['Content'] = self.content
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.path is not None:
            result['Path'] = self.path
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetGlobalAppResponseBodyAppVersions(TeaModel):
    def __init__(self, app_version=None, comment=None, last_modified=None):
        self.app_version = app_version  # type: str
        self.comment = comment  # type: str
        self.last_modified = last_modified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGlobalAppResponseBodyAppVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class GetGlobalAppResponseBody(TeaModel):
    def __init__(self, app_default_version=None, app_description=None, app_descriptor_files=None,
                 app_descriptor_type=None, app_fee=None, app_name=None, app_scope=None, app_type=None, app_version=None,
                 app_versions=None, categories=None, comment=None, contact=None, dag=None, document=None, host_id=None,
                 last_modified=None, links=None, locations=None, namespace_name=None, pinned=None, request_id=None, toolkit=None):
        self.app_default_version = app_default_version  # type: str
        self.app_description = app_description  # type: str
        self.app_descriptor_files = app_descriptor_files  # type: list[GetGlobalAppResponseBodyAppDescriptorFiles]
        self.app_descriptor_type = app_descriptor_type  # type: str
        self.app_fee = app_fee  # type: str
        self.app_name = app_name  # type: str
        self.app_scope = app_scope  # type: str
        self.app_type = app_type  # type: str
        self.app_version = app_version  # type: str
        self.app_versions = app_versions  # type: list[GetGlobalAppResponseBodyAppVersions]
        self.categories = categories  # type: list[str]
        self.comment = comment  # type: str
        self.contact = contact  # type: str
        self.dag = dag  # type: str
        self.document = document  # type: str
        self.host_id = host_id  # type: str
        self.last_modified = last_modified  # type: str
        self.links = links  # type: list[str]
        self.locations = locations  # type: list[str]
        self.namespace_name = namespace_name  # type: str
        self.pinned = pinned  # type: bool
        self.request_id = request_id  # type: str
        self.toolkit = toolkit  # type: str

    def validate(self):
        if self.app_descriptor_files:
            for k in self.app_descriptor_files:
                if k:
                    k.validate()
        if self.app_versions:
            for k in self.app_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGlobalAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        result['AppDescriptorFiles'] = []
        if self.app_descriptor_files is not None:
            for k in self.app_descriptor_files:
                result['AppDescriptorFiles'].append(k.to_map() if k else None)
        if self.app_descriptor_type is not None:
            result['AppDescriptorType'] = self.app_descriptor_type
        if self.app_fee is not None:
            result['AppFee'] = self.app_fee
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        result['AppVersions'] = []
        if self.app_versions is not None:
            for k in self.app_versions:
                result['AppVersions'].append(k.to_map() if k else None)
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.dag is not None:
            result['DAG'] = self.dag
        if self.document is not None:
            result['Document'] = self.document
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.links is not None:
            result['Links'] = self.links
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.pinned is not None:
            result['Pinned'] = self.pinned
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        self.app_descriptor_files = []
        if m.get('AppDescriptorFiles') is not None:
            for k in m.get('AppDescriptorFiles'):
                temp_model = GetGlobalAppResponseBodyAppDescriptorFiles()
                self.app_descriptor_files.append(temp_model.from_map(k))
        if m.get('AppDescriptorType') is not None:
            self.app_descriptor_type = m.get('AppDescriptorType')
        if m.get('AppFee') is not None:
            self.app_fee = m.get('AppFee')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        self.app_versions = []
        if m.get('AppVersions') is not None:
            for k in m.get('AppVersions'):
                temp_model = GetGlobalAppResponseBodyAppVersions()
                self.app_versions.append(temp_model.from_map(k))
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('DAG') is not None:
            self.dag = m.get('DAG')
        if m.get('Document') is not None:
            self.document = m.get('Document')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
        return self


class GetGlobalAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGlobalAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGlobalAppResponse, self).to_map()
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
            temp_model = GetGlobalAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicDatasetRequest(TeaModel):
    def __init__(self, attributes=None, dataset_name=None):
        self.attributes = attributes  # type: list[str]
        self.dataset_name = dataset_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublicDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        return self


class GetPublicDatasetShrinkRequest(TeaModel):
    def __init__(self, attributes_shrink=None, dataset_name=None):
        self.attributes_shrink = attributes_shrink  # type: str
        self.dataset_name = dataset_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublicDatasetShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        return self


class GetPublicDatasetResponseBody(TeaModel):
    def __init__(self, about=None, access_requirements=None, copyright=None, dataset_description=None,
                 dataset_name=None, host_id=None, last_modified=None, locations=None, request_id=None, tags=None,
                 update_frequency=None):
        self.about = about  # type: str
        self.access_requirements = access_requirements  # type: str
        self.copyright = copyright  # type: str
        self.dataset_description = dataset_description  # type: str
        self.dataset_name = dataset_name  # type: str
        self.host_id = host_id  # type: str
        self.last_modified = last_modified  # type: str
        self.locations = locations  # type: list[str]
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[str]
        self.update_frequency = update_frequency  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublicDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.access_requirements is not None:
            result['AccessRequirements'] = self.access_requirements
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_frequency is not None:
            result['UpdateFrequency'] = self.update_frequency
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('AccessRequirements') is not None:
            self.access_requirements = m.get('AccessRequirements')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateFrequency') is not None:
            self.update_frequency = m.get('UpdateFrequency')
        return self


class GetPublicDatasetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPublicDatasetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPublicDatasetResponse, self).to_map()
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
            temp_model = GetPublicDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicDatasetEntityRequest(TeaModel):
    def __init__(self, dataset_name=None, entity_type=None, location=None):
        self.dataset_name = dataset_name  # type: str
        self.entity_type = entity_type  # type: str
        self.location = location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublicDatasetEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class GetPublicDatasetEntityResponseBody(TeaModel):
    def __init__(self, attributes=None, dataset_name=None, entity_type=None, host_id=None, request_id=None,
                 total_count=None):
        self.attributes = attributes  # type: list[str]
        self.dataset_name = dataset_name  # type: str
        self.entity_type = entity_type  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPublicDatasetEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetPublicDatasetEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPublicDatasetEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPublicDatasetEntityResponse, self).to_map()
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
            temp_model = GetPublicDatasetEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunRequest(TeaModel):
    def __init__(self, run_id=None, workspace=None):
        self.run_id = run_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRunRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetRunResponseBodyExecuteOptions(TeaModel):
    def __init__(self, call_caching=None, delete_intermediate_results=None, failure_mode=None,
                 use_relative_output_paths=None):
        self.call_caching = call_caching  # type: bool
        self.delete_intermediate_results = delete_intermediate_results  # type: bool
        self.failure_mode = failure_mode  # type: str
        self.use_relative_output_paths = use_relative_output_paths  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRunResponseBodyExecuteOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_caching is not None:
            result['CallCaching'] = self.call_caching
        if self.delete_intermediate_results is not None:
            result['DeleteIntermediateResults'] = self.delete_intermediate_results
        if self.failure_mode is not None:
            result['FailureMode'] = self.failure_mode
        if self.use_relative_output_paths is not None:
            result['UseRelativeOutputPaths'] = self.use_relative_output_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        if m.get('UseRelativeOutputPaths') is not None:
            self.use_relative_output_paths = m.get('UseRelativeOutputPaths')
        return self


class GetRunResponseBody(TeaModel):
    def __init__(self, app_name=None, app_revision=None, billing_instance_ids=None, calls=None, create_time=None,
                 default_runtime=None, description=None, end_time=None, entity_name=None, entity_type=None, execute_directory=None,
                 execute_options=None, failures=None, host_id=None, inputs=None, labels=None, output_folder=None, outputs=None,
                 request_id=None, run_id=None, run_name=None, source=None, start_time=None, status=None, submission_id=None,
                 timing=None, user=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.billing_instance_ids = billing_instance_ids  # type: list[str]
        self.calls = calls  # type: str
        self.create_time = create_time  # type: str
        self.default_runtime = default_runtime  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: str
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.execute_directory = execute_directory  # type: str
        self.execute_options = execute_options  # type: GetRunResponseBodyExecuteOptions
        self.failures = failures  # type: str
        self.host_id = host_id  # type: str
        self.inputs = inputs  # type: str
        self.labels = labels  # type: dict[str, str]
        self.output_folder = output_folder  # type: str
        self.outputs = outputs  # type: str
        self.request_id = request_id  # type: str
        self.run_id = run_id  # type: str
        self.run_name = run_name  # type: str
        self.source = source  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.submission_id = submission_id  # type: str
        self.timing = timing  # type: str
        self.user = user  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.execute_options:
            self.execute_options.validate()

    def to_map(self):
        _map = super(GetRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.billing_instance_ids is not None:
            result['BillingInstanceIds'] = self.billing_instance_ids
        if self.calls is not None:
            result['Calls'] = self.calls
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.failures is not None:
            result['Failures'] = self.failures
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.timing is not None:
            result['Timing'] = self.timing
        if self.user is not None:
            result['User'] = self.user
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('BillingInstanceIds') is not None:
            self.billing_instance_ids = m.get('BillingInstanceIds')
        if m.get('Calls') is not None:
            self.calls = m.get('Calls')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            temp_model = GetRunResponseBodyExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Failures') is not None:
            self.failures = m.get('Failures')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Timing') is not None:
            self.timing = m.get('Timing')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetRunResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRunResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRunResponse, self).to_map()
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
            temp_model = GetRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubmissionRequest(TeaModel):
    def __init__(self, submission_id=None, workspace=None):
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubmissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetSubmissionResponseBodySubmissionRunStats(TeaModel):
    def __init__(self, aborted=None, aborting=None, failed=None, pending=None, running=None, submitted=None,
                 succeeded=None):
        self.aborted = aborted  # type: long
        self.aborting = aborting  # type: long
        self.failed = failed  # type: long
        self.pending = pending  # type: long
        self.running = running  # type: long
        self.submitted = submitted  # type: long
        self.succeeded = succeeded  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubmissionResponseBodySubmissionRunStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aborted is not None:
            result['Aborted'] = self.aborted
        if self.aborting is not None:
            result['Aborting'] = self.aborting
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.running is not None:
            result['Running'] = self.running
        if self.submitted is not None:
            result['Submitted'] = self.submitted
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aborted') is not None:
            self.aborted = m.get('Aborted')
        if m.get('Aborting') is not None:
            self.aborting = m.get('Aborting')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class GetSubmissionResponseBodySubmission(TeaModel):
    def __init__(self, create_time=None, end_time=None, entity_type=None, run_stats=None, start_time=None,
                 status=None, submission_id=None, workspace=None):
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.entity_type = entity_type  # type: str
        self.run_stats = run_stats  # type: GetSubmissionResponseBodySubmissionRunStats
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.run_stats:
            self.run_stats.validate()

    def to_map(self):
        _map = super(GetSubmissionResponseBodySubmission, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.run_stats is not None:
            result['RunStats'] = self.run_stats.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RunStats') is not None:
            temp_model = GetSubmissionResponseBodySubmissionRunStats()
            self.run_stats = temp_model.from_map(m['RunStats'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetSubmissionResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None, submission=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.submission = submission  # type: GetSubmissionResponseBodySubmission

    def validate(self):
        if self.submission:
            self.submission.validate()

    def to_map(self):
        _map = super(GetSubmissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submission is not None:
            result['Submission'] = self.submission.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Submission') is not None:
            temp_model = GetSubmissionResponseBodySubmission()
            self.submission = temp_model.from_map(m['Submission'])
        return self


class GetSubmissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSubmissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubmissionResponse, self).to_map()
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
            temp_model = GetSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, template_name=None, workspace=None):
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetTemplateResponseBodyInputsExpression(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: long
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyInputsExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class GetTemplateResponseBodyOutputsExpression(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: long
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyOutputsExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, app_name=None, app_revision=None, create_time=None, description=None, host_id=None,
                 inputs_expression=None, labels=None, last_modified_time=None, outputs_expression=None, request_id=None,
                 revision_tag=None, root_entity=None, source=None, template_name=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.host_id = host_id  # type: str
        self.inputs_expression = inputs_expression  # type: list[GetTemplateResponseBodyInputsExpression]
        self.labels = labels  # type: dict[str, str]
        self.last_modified_time = last_modified_time  # type: str
        self.outputs_expression = outputs_expression  # type: list[GetTemplateResponseBodyOutputsExpression]
        self.request_id = request_id  # type: str
        self.revision_tag = revision_tag  # type: str
        self.root_entity = root_entity  # type: str
        self.source = source  # type: str
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.inputs_expression:
            for k in self.inputs_expression:
                if k:
                    k.validate()
        if self.outputs_expression:
            for k in self.outputs_expression:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['InputsExpression'] = []
        if self.inputs_expression is not None:
            for k in self.inputs_expression:
                result['InputsExpression'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        result['OutputsExpression'] = []
        if self.outputs_expression is not None:
            for k in self.outputs_expression:
                result['OutputsExpression'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.source is not None:
            result['Source'] = self.source
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.inputs_expression = []
        if m.get('InputsExpression') is not None:
            for k in m.get('InputsExpression'):
                temp_model = GetTemplateResponseBodyInputsExpression()
                self.inputs_expression.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        self.outputs_expression = []
        if m.get('OutputsExpression') is not None:
            for k in m.get('OutputsExpression'):
                temp_model = GetTemplateResponseBodyOutputsExpression()
                self.outputs_expression.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateResponse, self).to_map()
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkspaceRequest(TeaModel):
    def __init__(self, workspace=None):
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetWorkspaceResponseBody(TeaModel):
    def __init__(self, bucket_name=None, create_time=None, description=None, host_id=None, job_lifecycle=None,
                 labels=None, last_modified_time=None, location=None, request_id=None, role=None, status=None, storage=None,
                 workspace=None):
        self.bucket_name = bucket_name  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.host_id = host_id  # type: str
        self.job_lifecycle = job_lifecycle  # type: int
        self.labels = labels  # type: dict[str, str]
        self.last_modified_time = last_modified_time  # type: str
        self.location = location  # type: str
        self.request_id = request_id  # type: str
        self.role = role  # type: str
        self.status = status  # type: str
        self.storage = storage  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.location is not None:
            result['Location'] = self.location
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWorkspaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkspaceResponse, self).to_map()
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
            temp_model = GetWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportAppRequest(TeaModel):
    def __init__(self, app_name=None, source=None, workspace=None):
        self.app_name = app_name  # type: str
        self.source = source  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ImportAppResponseBody(TeaModel):
    def __init__(self, app_name=None, host_id=None, region_id=None, request_id=None, workspace=None):
        self.app_name = app_name  # type: str
        self.host_id = host_id  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ImportAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportAppResponse, self).to_map()
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
            temp_model = ImportAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallGlobalAppRequest(TeaModel):
    def __init__(self, app_name=None, installed_app_name=None, namespace_name=None, source=None, workspace=None):
        self.app_name = app_name  # type: str
        self.installed_app_name = installed_app_name  # type: str
        self.namespace_name = namespace_name  # type: str
        self.source = source  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallGlobalAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.installed_app_name is not None:
            result['InstalledAppName'] = self.installed_app_name
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('InstalledAppName') is not None:
            self.installed_app_name = m.get('InstalledAppName')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class InstallGlobalAppResponseBody(TeaModel):
    def __init__(self, host_id=None, installed_app_name=None, region_id=None, request_id=None, workspace=None):
        self.host_id = host_id  # type: str
        self.installed_app_name = installed_app_name  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallGlobalAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.installed_app_name is not None:
            result['InstalledAppName'] = self.installed_app_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstalledAppName') is not None:
            self.installed_app_name = m.get('InstalledAppName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class InstallGlobalAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InstallGlobalAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallGlobalAppResponse, self).to_map()
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
            temp_model = InstallGlobalAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(self, app_type=None, is_reversed=None, label_selector=None, language=None, max_results=None,
                 next_token=None, order_by=None, scope=None, search=None, workspace=None):
        self.app_type = app_type  # type: str
        self.is_reversed = is_reversed  # type: bool
        self.label_selector = label_selector  # type: str
        self.language = language  # type: str
        self.max_results = max_results  # type: int
        # Next Token
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.scope = scope  # type: str
        self.search = search  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.language is not None:
            result['Language'] = self.language
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.search is not None:
            result['Search'] = self.search
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListAppsResponseBodyApps(TeaModel):
    def __init__(self, app_default_version=None, app_name=None, app_type=None, create_time=None, description=None,
                 labels=None, language=None, scope=None, source=None, workspace=None):
        self.app_default_version = app_default_version  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.labels = labels  # type: dict[str, str]
        self.language = language  # type: str
        self.scope = scope  # type: str
        self.source = source  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsResponseBodyApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.language is not None:
            result['Language'] = self.language
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(self, apps=None, host_id=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.apps = apps  # type: list[ListAppsResponseBodyApps]
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        # Next Token
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppsResponseBodyApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppsResponse, self).to_map()
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
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizedSoftwareRequest(TeaModel):
    def __init__(self, is_reversed=None, location=None, max_results=None, next_token=None, order_by=None,
                 search=None):
        self.is_reversed = is_reversed  # type: bool
        self.location = location  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizedSoftwareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListAuthorizedSoftwareResponseBodySoftwares(TeaModel):
    def __init__(self, help_link=None, last_modified=None, locations=None, promotion=None,
                 software_default_version=None, software_description=None, software_icon=None, software_license_fee=None,
                 software_long_name=None, software_name=None, software_versions=None):
        self.help_link = help_link  # type: str
        self.last_modified = last_modified  # type: str
        self.locations = locations  # type: list[str]
        self.promotion = promotion  # type: str
        self.software_default_version = software_default_version  # type: str
        self.software_description = software_description  # type: str
        self.software_icon = software_icon  # type: str
        self.software_license_fee = software_license_fee  # type: float
        self.software_long_name = software_long_name  # type: str
        self.software_name = software_name  # type: str
        self.software_versions = software_versions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizedSoftwareResponseBodySoftwares, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help_link is not None:
            result['HelpLink'] = self.help_link
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.promotion is not None:
            result['Promotion'] = self.promotion
        if self.software_default_version is not None:
            result['SoftwareDefaultVersion'] = self.software_default_version
        if self.software_description is not None:
            result['SoftwareDescription'] = self.software_description
        if self.software_icon is not None:
            result['SoftwareIcon'] = self.software_icon
        if self.software_license_fee is not None:
            result['SoftwareLicenseFee'] = self.software_license_fee
        if self.software_long_name is not None:
            result['SoftwareLongName'] = self.software_long_name
        if self.software_name is not None:
            result['SoftwareName'] = self.software_name
        if self.software_versions is not None:
            result['SoftwareVersions'] = self.software_versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HelpLink') is not None:
            self.help_link = m.get('HelpLink')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('Promotion') is not None:
            self.promotion = m.get('Promotion')
        if m.get('SoftwareDefaultVersion') is not None:
            self.software_default_version = m.get('SoftwareDefaultVersion')
        if m.get('SoftwareDescription') is not None:
            self.software_description = m.get('SoftwareDescription')
        if m.get('SoftwareIcon') is not None:
            self.software_icon = m.get('SoftwareIcon')
        if m.get('SoftwareLicenseFee') is not None:
            self.software_license_fee = m.get('SoftwareLicenseFee')
        if m.get('SoftwareLongName') is not None:
            self.software_long_name = m.get('SoftwareLongName')
        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')
        if m.get('SoftwareVersions') is not None:
            self.software_versions = m.get('SoftwareVersions')
        return self


class ListAuthorizedSoftwareResponseBody(TeaModel):
    def __init__(self, host_id=None, max_results=None, next_token=None, request_id=None, softwares=None,
                 total_count=None):
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.softwares = softwares  # type: list[ListAuthorizedSoftwareResponseBodySoftwares]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.softwares:
            for k in self.softwares:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthorizedSoftwareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Softwares'] = []
        if self.softwares is not None:
            for k in self.softwares:
                result['Softwares'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.softwares = []
        if m.get('Softwares') is not None:
            for k in m.get('Softwares'):
                temp_model = ListAuthorizedSoftwareResponseBodySoftwares()
                self.softwares.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthorizedSoftwareResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAuthorizedSoftwareResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthorizedSoftwareResponse, self).to_map()
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
            temp_model = ListAuthorizedSoftwareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContainerImagesRequest(TeaModel):
    def __init__(self, location=None, max_results=None, next_token=None):
        self.location = location  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListContainerImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListContainerImagesResponseBodyContainerImages(TeaModel):
    def __init__(self, container_image_description=None, container_image_name=None,
                 container_image_namespace=None, container_image_versions=None, container_registry=None, last_modified=None, location=None):
        self.container_image_description = container_image_description  # type: str
        self.container_image_name = container_image_name  # type: str
        self.container_image_namespace = container_image_namespace  # type: str
        self.container_image_versions = container_image_versions  # type: list[str]
        self.container_registry = container_registry  # type: str
        self.last_modified = last_modified  # type: str
        self.location = location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListContainerImagesResponseBodyContainerImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_image_description is not None:
            result['ContainerImageDescription'] = self.container_image_description
        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name
        if self.container_image_namespace is not None:
            result['ContainerImageNamespace'] = self.container_image_namespace
        if self.container_image_versions is not None:
            result['ContainerImageVersions'] = self.container_image_versions
        if self.container_registry is not None:
            result['ContainerRegistry'] = self.container_registry
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerImageDescription') is not None:
            self.container_image_description = m.get('ContainerImageDescription')
        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')
        if m.get('ContainerImageNamespace') is not None:
            self.container_image_namespace = m.get('ContainerImageNamespace')
        if m.get('ContainerImageVersions') is not None:
            self.container_image_versions = m.get('ContainerImageVersions')
        if m.get('ContainerRegistry') is not None:
            self.container_registry = m.get('ContainerRegistry')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ListContainerImagesResponseBody(TeaModel):
    def __init__(self, container_images=None, host_id=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.container_images = container_images  # type: list[ListContainerImagesResponseBodyContainerImages]
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.container_images:
            for k in self.container_images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListContainerImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerImages'] = []
        if self.container_images is not None:
            for k in self.container_images:
                result['ContainerImages'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.container_images = []
        if m.get('ContainerImages') is not None:
            for k in m.get('ContainerImages'):
                temp_model = ListContainerImagesResponseBodyContainerImages()
                self.container_images.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListContainerImagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListContainerImagesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListContainerImagesResponse, self).to_map()
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
            temp_model = ListContainerImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEntitiesRequest(TeaModel):
    def __init__(self, is_reversed=None, max_results=None, next_token=None, order_by=None, workspace=None):
        self.is_reversed = is_reversed  # type: bool
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEntitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListEntitiesResponseBodyEntities(TeaModel):
    def __init__(self, entity_type=None):
        self.entity_type = entity_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEntitiesResponseBodyEntities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class ListEntitiesResponseBody(TeaModel):
    def __init__(self, entities=None, host_id=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.entities = entities  # type: list[ListEntitiesResponseBodyEntities]
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEntitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEntitiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEntitiesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEntitiesResponse, self).to_map()
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
            temp_model = ListEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEntityItemsRequest(TeaModel):
    def __init__(self, entity_type=None, is_reversed=None, max_results=None, next_token=None, order_by=None,
                 search=None, workspace=None):
        self.entity_type = entity_type  # type: str
        self.is_reversed = is_reversed  # type: bool
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEntityItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListEntityItemsResponseBodyEntityItems(TeaModel):
    def __init__(self, entity_data=None, entity_name=None):
        self.entity_data = entity_data  # type: dict[str, str]
        self.entity_name = entity_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEntityItemsResponseBodyEntityItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class ListEntityItemsResponseBody(TeaModel):
    def __init__(self, entity_items=None, host_id=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.entity_items = entity_items  # type: list[ListEntityItemsResponseBodyEntityItems]
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEntityItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = ListEntityItemsResponseBodyEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEntityItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEntityItemsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEntityItemsResponse, self).to_map()
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
            temp_model = ListEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGlobalAppsRequest(TeaModel):
    def __init__(self, app_scope=None, category=None, is_reversed=None, location=None, max_results=None,
                 next_token=None, order_by=None, search=None, toolkit=None):
        self.app_scope = app_scope  # type: str
        self.category = category  # type: str
        self.is_reversed = is_reversed  # type: bool
        self.location = location  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str
        self.toolkit = toolkit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGlobalAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.category is not None:
            result['Category'] = self.category
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
        return self


class ListGlobalAppsResponseBodyGlobalApps(TeaModel):
    def __init__(self, app_default_version=None, app_description=None, app_fee=None, app_name=None, app_scope=None,
                 categories=None, last_modified=None, locations=None, namespace_name=None, pinned=None, toolkit=None):
        self.app_default_version = app_default_version  # type: str
        self.app_description = app_description  # type: str
        self.app_fee = app_fee  # type: str
        self.app_name = app_name  # type: str
        self.app_scope = app_scope  # type: str
        self.categories = categories  # type: list[str]
        self.last_modified = last_modified  # type: str
        self.locations = locations  # type: list[str]
        self.namespace_name = namespace_name  # type: str
        self.pinned = pinned  # type: bool
        self.toolkit = toolkit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGlobalAppsResponseBodyGlobalApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_fee is not None:
            result['AppFee'] = self.app_fee
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.pinned is not None:
            result['Pinned'] = self.pinned
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppFee') is not None:
            self.app_fee = m.get('AppFee')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
        return self


class ListGlobalAppsResponseBody(TeaModel):
    def __init__(self, global_apps=None, host_id=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.global_apps = global_apps  # type: list[ListGlobalAppsResponseBodyGlobalApps]
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.global_apps:
            for k in self.global_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGlobalAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GlobalApps'] = []
        if self.global_apps is not None:
            for k in self.global_apps:
                result['GlobalApps'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.global_apps = []
        if m.get('GlobalApps') is not None:
            for k in m.get('GlobalApps'):
                temp_model = ListGlobalAppsResponseBodyGlobalApps()
                self.global_apps.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGlobalAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGlobalAppsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGlobalAppsResponse, self).to_map()
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
            temp_model = ListGlobalAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicDatasetRequest(TeaModel):
    def __init__(self, is_reversed=None, max_results=None, next_token=None, order_by=None, search=None, tag=None):
        self.is_reversed = is_reversed  # type: bool
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListPublicDatasetResponseBodyDatasets(TeaModel):
    def __init__(self, about=None, access_requirements=None, copyright=None, dataset_description=None,
                 dataset_id=None, dataset_name=None, last_modified=None, locations=None, tags=None, update_frequency=None):
        self.about = about  # type: str
        self.access_requirements = access_requirements  # type: str
        self.copyright = copyright  # type: str
        self.dataset_description = dataset_description  # type: str
        self.dataset_id = dataset_id  # type: str
        self.dataset_name = dataset_name  # type: str
        self.last_modified = last_modified  # type: str
        self.locations = locations  # type: list[str]
        self.tags = tags  # type: list[str]
        self.update_frequency = update_frequency  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicDatasetResponseBodyDatasets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.access_requirements is not None:
            result['AccessRequirements'] = self.access_requirements
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_frequency is not None:
            result['UpdateFrequency'] = self.update_frequency
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('AccessRequirements') is not None:
            self.access_requirements = m.get('AccessRequirements')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateFrequency') is not None:
            self.update_frequency = m.get('UpdateFrequency')
        return self


class ListPublicDatasetResponseBody(TeaModel):
    def __init__(self, datasets=None, host_id=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.datasets = datasets  # type: list[ListPublicDatasetResponseBodyDatasets]
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublicDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = ListPublicDatasetResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublicDatasetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPublicDatasetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublicDatasetResponse, self).to_map()
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
            temp_model = ListPublicDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicDatasetEntitiesRequest(TeaModel):
    def __init__(self, dataset_name=None, is_reversed=None, location=None, max_results=None, next_token=None,
                 order_by=None):
        self.dataset_name = dataset_name  # type: str
        self.is_reversed = is_reversed  # type: bool
        self.location = location  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicDatasetEntitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        return self


class ListPublicDatasetEntitiesResponseBodyEntities(TeaModel):
    def __init__(self, entity_type=None):
        self.entity_type = entity_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicDatasetEntitiesResponseBodyEntities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class ListPublicDatasetEntitiesResponseBody(TeaModel):
    def __init__(self, dataset_name=None, entities=None, host_id=None, max_results=None, next_token=None,
                 request_id=None, total_count=None):
        self.dataset_name = dataset_name  # type: str
        self.entities = entities  # type: list[ListPublicDatasetEntitiesResponseBodyEntities]
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublicDatasetEntitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListPublicDatasetEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublicDatasetEntitiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPublicDatasetEntitiesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublicDatasetEntitiesResponse, self).to_map()
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
            temp_model = ListPublicDatasetEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicDatasetEntityItemsRequest(TeaModel):
    def __init__(self, dataset_name=None, entity_type=None, is_reversed=None, location=None, max_results=None,
                 next_token=None, order_by=None, search=None):
        self.dataset_name = dataset_name  # type: str
        self.entity_type = entity_type  # type: str
        self.is_reversed = is_reversed  # type: bool
        self.location = location  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicDatasetEntityItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListPublicDatasetEntityItemsResponseBodyEntityItems(TeaModel):
    def __init__(self, entity_data=None, entity_name=None):
        self.entity_data = entity_data  # type: dict[str, str]
        self.entity_name = entity_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicDatasetEntityItemsResponseBodyEntityItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class ListPublicDatasetEntityItemsResponseBody(TeaModel):
    def __init__(self, dataset_name=None, entity_items=None, host_id=None, max_results=None, next_token=None,
                 request_id=None, total_count=None):
        self.dataset_name = dataset_name  # type: str
        self.entity_items = entity_items  # type: list[ListPublicDatasetEntityItemsResponseBodyEntityItems]
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublicDatasetEntityItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = ListPublicDatasetEntityItemsResponseBodyEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublicDatasetEntityItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPublicDatasetEntityItemsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublicDatasetEntityItemsResponse, self).to_map()
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
            temp_model = ListPublicDatasetEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicDatasetTagsRequest(TeaModel):
    def __init__(self, is_reversed=None, max_results=None, next_token=None, order_by=None, search=None):
        self.is_reversed = is_reversed  # type: bool
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicDatasetTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListPublicDatasetTagsResponseBody(TeaModel):
    def __init__(self, host_id=None, max_results=None, next_token=None, request_id=None, tags=None, total_count=None):
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[str]
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicDatasetTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublicDatasetTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPublicDatasetTagsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublicDatasetTagsResponse, self).to_map()
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
            temp_model = ListPublicDatasetTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, host_id=None, regions=None, request_id=None):
        self.host_id = host_id  # type: str
        self.regions = regions  # type: list[ListRegionsResponseBodyRegions]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunsRequest(TeaModel):
    def __init__(self, app_name=None, app_revision=None, entity_name=None, entity_type=None, get_total=None,
                 is_reversed=None, label_selector=None, max_results=None, next_token=None, order_by=None, search=None,
                 status=None, submission_id=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.get_total = get_total  # type: bool
        self.is_reversed = is_reversed  # type: bool
        self.label_selector = label_selector  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str
        self.status = status  # type: str
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRunsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.get_total is not None:
            result['GetTotal'] = self.get_total
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('GetTotal') is not None:
            self.get_total = m.get('GetTotal')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListRunsResponseBodyRunsExecuteOptions(TeaModel):
    def __init__(self, call_caching=None, delete_intermediate_results=None, failure_mode=None,
                 use_relative_output_paths=None):
        self.call_caching = call_caching  # type: bool
        self.delete_intermediate_results = delete_intermediate_results  # type: bool
        self.failure_mode = failure_mode  # type: str
        self.use_relative_output_paths = use_relative_output_paths  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRunsResponseBodyRunsExecuteOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_caching is not None:
            result['CallCaching'] = self.call_caching
        if self.delete_intermediate_results is not None:
            result['DeleteIntermediateResults'] = self.delete_intermediate_results
        if self.failure_mode is not None:
            result['FailureMode'] = self.failure_mode
        if self.use_relative_output_paths is not None:
            result['UseRelativeOutputPaths'] = self.use_relative_output_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        if m.get('UseRelativeOutputPaths') is not None:
            self.use_relative_output_paths = m.get('UseRelativeOutputPaths')
        return self


class ListRunsResponseBodyRuns(TeaModel):
    def __init__(self, app_name=None, app_revision=None, create_time=None, default_runtime=None, end_time=None,
                 entity_name=None, entity_type=None, execute_directory=None, execute_options=None, inputs=None, labels=None,
                 region_id=None, run_id=None, run_name=None, source=None, start_time=None, status=None, submission_id=None,
                 workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.create_time = create_time  # type: str
        self.default_runtime = default_runtime  # type: str
        self.end_time = end_time  # type: str
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.execute_directory = execute_directory  # type: str
        self.execute_options = execute_options  # type: ListRunsResponseBodyRunsExecuteOptions
        self.inputs = inputs  # type: str
        self.labels = labels  # type: dict[str, str]
        self.region_id = region_id  # type: str
        self.run_id = run_id  # type: str
        self.run_name = run_name  # type: str
        self.source = source  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.execute_options:
            self.execute_options.validate()

    def to_map(self):
        _map = super(ListRunsResponseBodyRuns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            temp_model = ListRunsResponseBodyRunsExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListRunsResponseBody(TeaModel):
    def __init__(self, host_id=None, max_results=None, next_token=None, request_id=None, runs=None, total_count=None):
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.runs = runs  # type: list[ListRunsResponseBodyRuns]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.runs:
            for k in self.runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRunsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['Runs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.runs = []
        if m.get('Runs') is not None:
            for k in m.get('Runs'):
                temp_model = ListRunsResponseBodyRuns()
                self.runs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRunsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRunsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRunsResponse, self).to_map()
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
            temp_model = ListRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubmissionsRequest(TeaModel):
    def __init__(self, is_reversed=None, max_results=None, next_token=None, order_by=None, search=None, status=None,
                 workspace=None):
        self.is_reversed = is_reversed  # type: bool
        self.max_results = max_results  # type: int
        # Next Token
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str
        self.status = status  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubmissionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListSubmissionsResponseBodySubmissionsRunStats(TeaModel):
    def __init__(self, aborted=None, aborting=None, failed=None, pending=None, running=None, submitted=None,
                 succeeded=None):
        self.aborted = aborted  # type: long
        self.aborting = aborting  # type: long
        self.failed = failed  # type: long
        self.pending = pending  # type: long
        self.running = running  # type: long
        self.submitted = submitted  # type: long
        self.succeeded = succeeded  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubmissionsResponseBodySubmissionsRunStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aborted is not None:
            result['Aborted'] = self.aborted
        if self.aborting is not None:
            result['Aborting'] = self.aborting
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.running is not None:
            result['Running'] = self.running
        if self.submitted is not None:
            result['Submitted'] = self.submitted
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aborted') is not None:
            self.aborted = m.get('Aborted')
        if m.get('Aborting') is not None:
            self.aborting = m.get('Aborting')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class ListSubmissionsResponseBodySubmissions(TeaModel):
    def __init__(self, create_time=None, end_time=None, entity_type=None, run_stats=None, start_time=None,
                 status=None, submission_id=None, workspace=None):
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.entity_type = entity_type  # type: str
        self.run_stats = run_stats  # type: ListSubmissionsResponseBodySubmissionsRunStats
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.run_stats:
            self.run_stats.validate()

    def to_map(self):
        _map = super(ListSubmissionsResponseBodySubmissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.run_stats is not None:
            result['RunStats'] = self.run_stats.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RunStats') is not None:
            temp_model = ListSubmissionsResponseBodySubmissionsRunStats()
            self.run_stats = temp_model.from_map(m['RunStats'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListSubmissionsResponseBody(TeaModel):
    def __init__(self, host_id=None, max_results=None, next_token=None, request_id=None, submissions=None,
                 total_count=None):
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.submissions = submissions  # type: list[ListSubmissionsResponseBodySubmissions]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.submissions:
            for k in self.submissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubmissionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Submissions'] = []
        if self.submissions is not None:
            for k in self.submissions:
                result['Submissions'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.submissions = []
        if m.get('Submissions') is not None:
            for k in m.get('Submissions'):
                temp_model = ListSubmissionsResponseBodySubmissions()
                self.submissions.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSubmissionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubmissionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubmissionsResponse, self).to_map()
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
            temp_model = ListSubmissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, is_reversed=None, label_selector=None, max_results=None, next_token=None, order_by=None,
                 search=None, workspace=None):
        self.is_reversed = is_reversed  # type: bool
        self.label_selector = label_selector  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListTemplatesResponseBodyTemplatesInputsExpression(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: long
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplatesInputsExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class ListTemplatesResponseBodyTemplatesOutputsExpression(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: long
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplatesOutputsExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, app_name=None, app_revision=None, create_time=None, description=None, inputs_expression=None,
                 labels=None, last_modified_time=None, outputs_expression=None, revision_tag=None, root_entity=None,
                 template_name=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.inputs_expression = inputs_expression  # type: list[ListTemplatesResponseBodyTemplatesInputsExpression]
        self.labels = labels  # type: dict[str, str]
        self.last_modified_time = last_modified_time  # type: str
        self.outputs_expression = outputs_expression  # type: list[ListTemplatesResponseBodyTemplatesOutputsExpression]
        self.revision_tag = revision_tag  # type: str
        self.root_entity = root_entity  # type: str
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.inputs_expression:
            for k in self.inputs_expression:
                if k:
                    k.validate()
        if self.outputs_expression:
            for k in self.outputs_expression:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['InputsExpression'] = []
        if self.inputs_expression is not None:
            for k in self.inputs_expression:
                result['InputsExpression'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        result['OutputsExpression'] = []
        if self.outputs_expression is not None:
            for k in self.outputs_expression:
                result['OutputsExpression'].append(k.to_map() if k else None)
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.inputs_expression = []
        if m.get('InputsExpression') is not None:
            for k in m.get('InputsExpression'):
                temp_model = ListTemplatesResponseBodyTemplatesInputsExpression()
                self.inputs_expression.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        self.outputs_expression = []
        if m.get('OutputsExpression') is not None:
            for k in m.get('OutputsExpression'):
                temp_model = ListTemplatesResponseBodyTemplatesOutputsExpression()
                self.outputs_expression.append(temp_model.from_map(k))
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, host_id=None, max_results=None, next_token=None, request_id=None, templates=None,
                 total_count=None):
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.templates = templates  # type: list[ListTemplatesResponseBodyTemplates]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplatesResponse, self).to_map()
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserActiveRunsRequest(TeaModel):
    def __init__(self, max_results=None):
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserActiveRunsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListUserActiveRunsResponseBodyRunsExecuteOptions(TeaModel):
    def __init__(self, call_caching=None, delete_intermediate_results=None, failure_mode=None,
                 use_relative_output_paths=None):
        self.call_caching = call_caching  # type: bool
        self.delete_intermediate_results = delete_intermediate_results  # type: bool
        self.failure_mode = failure_mode  # type: str
        self.use_relative_output_paths = use_relative_output_paths  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserActiveRunsResponseBodyRunsExecuteOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_caching is not None:
            result['CallCaching'] = self.call_caching
        if self.delete_intermediate_results is not None:
            result['DeleteIntermediateResults'] = self.delete_intermediate_results
        if self.failure_mode is not None:
            result['FailureMode'] = self.failure_mode
        if self.use_relative_output_paths is not None:
            result['UseRelativeOutputPaths'] = self.use_relative_output_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        if m.get('UseRelativeOutputPaths') is not None:
            self.use_relative_output_paths = m.get('UseRelativeOutputPaths')
        return self


class ListUserActiveRunsResponseBodyRuns(TeaModel):
    def __init__(self, app_name=None, app_revision=None, create_time=None, default_runtime=None, end_time=None,
                 entity_name=None, entity_type=None, execute_directory=None, execute_options=None, inputs=None, labels=None,
                 region_id=None, run_id=None, run_name=None, source=None, start_time=None, status=None, submission_id=None,
                 workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.create_time = create_time  # type: str
        self.default_runtime = default_runtime  # type: str
        self.end_time = end_time  # type: str
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.execute_directory = execute_directory  # type: str
        self.execute_options = execute_options  # type: ListUserActiveRunsResponseBodyRunsExecuteOptions
        self.inputs = inputs  # type: str
        self.labels = labels  # type: dict[str, str]
        self.region_id = region_id  # type: str
        self.run_id = run_id  # type: str
        self.run_name = run_name  # type: str
        self.source = source  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.execute_options:
            self.execute_options.validate()

    def to_map(self):
        _map = super(ListUserActiveRunsResponseBodyRuns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            temp_model = ListUserActiveRunsResponseBodyRunsExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListUserActiveRunsResponseBody(TeaModel):
    def __init__(self, host_id=None, max_results=None, next_token=None, request_id=None, runs=None, total_count=None):
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.runs = runs  # type: list[ListUserActiveRunsResponseBodyRuns]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.runs:
            for k in self.runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserActiveRunsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['Runs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.runs = []
        if m.get('Runs') is not None:
            for k in m.get('Runs'):
                temp_model = ListUserActiveRunsResponseBodyRuns()
                self.runs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserActiveRunsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserActiveRunsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserActiveRunsResponse, self).to_map()
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
            temp_model = ListUserActiveRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspacesRequest(TeaModel):
    def __init__(self, is_reversed=None, label_selector=None, max_results=None, next_token=None, order_by=None,
                 search=None):
        self.is_reversed = is_reversed  # type: bool
        self.label_selector = label_selector  # type: str
        self.max_results = max_results  # type: int
        # NextToken
        self.next_token = next_token  # type: str
        self.order_by = order_by  # type: str
        self.search = search  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkspacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(self, bucket_name=None, create_time=None, description=None, job_lifecycle=None, labels=None,
                 last_modified_time=None, location=None, role=None, status=None, storage=None, workspace=None):
        self.bucket_name = bucket_name  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.job_lifecycle = job_lifecycle  # type: int
        self.labels = labels  # type: dict[str, str]
        self.last_modified_time = last_modified_time  # type: str
        self.location = location  # type: str
        # RAM Role
        self.role = role  # type: str
        self.status = status  # type: str
        self.storage = storage  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkspacesResponseBodyWorkspaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.location is not None:
            result['Location'] = self.location
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(self, host_id=None, max_results=None, next_token=None, request_id=None, total_count=None,
                 workspaces=None):
        self.host_id = host_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.workspaces = workspaces  # type: list[ListWorkspacesResponseBodyWorkspaces]

    def validate(self):
        if self.workspaces:
            for k in self.workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkspacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['Workspaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k in m.get('Workspaces'):
                temp_model = ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k))
        return self


class ListWorkspacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListWorkspacesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkspacesResponse, self).to_map()
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeSubmissionRequest(TeaModel):
    def __init__(self, submission_id=None, workspace=None):
        self.submission_id = submission_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeSubmissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ResumeSubmissionResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeSubmissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeSubmissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeSubmissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeSubmissionResponse, self).to_map()
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
            temp_model = ResumeSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagAppRequest(TeaModel):
    def __init__(self, app_name=None, app_revision=None, revision_tag=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.revision_tag = revision_tag  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class TagAppResponseBody(TeaModel):
    def __init__(self, app_name=None, app_revision=None, former_revision=None, former_tag=None, request_id=None,
                 revision_tag=None, workspace=None):
        self.app_name = app_name  # type: str
        self.app_revision = app_revision  # type: str
        self.former_revision = former_revision  # type: str
        self.former_tag = former_tag  # type: str
        self.request_id = request_id  # type: str
        self.revision_tag = revision_tag  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.former_revision is not None:
            result['FormerRevision'] = self.former_revision
        if self.former_tag is not None:
            result['FormerTag'] = self.former_tag
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('FormerRevision') is not None:
            self.former_revision = m.get('FormerRevision')
        if m.get('FormerTag') is not None:
            self.former_tag = m.get('FormerTag')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class TagAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagAppResponse, self).to_map()
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
            temp_model = TagAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEntityRequestEntityItems(TeaModel):
    def __init__(self, entity_data=None, entity_name=None):
        self.entity_data = entity_data  # type: dict[str, str]
        self.entity_name = entity_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityRequestEntityItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class UpdateEntityRequest(TeaModel):
    def __init__(self, entity_items=None, entity_type=None, workspace=None):
        self.entity_items = entity_items  # type: list[UpdateEntityRequestEntityItems]
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = UpdateEntityRequestEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityShrinkRequest(TeaModel):
    def __init__(self, entity_items_shrink=None, entity_type=None, workspace=None):
        self.entity_items_shrink = entity_items_shrink  # type: str
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_items_shrink is not None:
            result['EntityItems'] = self.entity_items_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityItems') is not None:
            self.entity_items_shrink = m.get('EntityItems')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityResponseBody(TeaModel):
    def __init__(self, entity_type=None, host_id=None, request_id=None, workspace=None):
        self.entity_type = entity_type  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEntityResponse, self).to_map()
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
            temp_model = UpdateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEntityItemsRequestEntityItems(TeaModel):
    def __init__(self, entity_data=None, entity_name=None):
        self.entity_data = entity_data  # type: dict[str, str]
        self.entity_name = entity_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityItemsRequestEntityItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class UpdateEntityItemsRequest(TeaModel):
    def __init__(self, entity_items=None, entity_type=None, workspace=None):
        self.entity_items = entity_items  # type: list[UpdateEntityItemsRequestEntityItems]
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEntityItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = UpdateEntityItemsRequestEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityItemsShrinkRequest(TeaModel):
    def __init__(self, entity_items_shrink=None, entity_type=None, workspace=None):
        self.entity_items_shrink = entity_items_shrink  # type: str
        self.entity_type = entity_type  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityItemsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_items_shrink is not None:
            result['EntityItems'] = self.entity_items_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityItems') is not None:
            self.entity_items_shrink = m.get('EntityItems')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityItemsResponseBody(TeaModel):
    def __init__(self, entity_type=None, host_id=None, request_id=None, workspace=None):
        self.entity_type = entity_type  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEntityItemsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEntityItemsResponse, self).to_map()
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
            temp_model = UpdateEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequestInputsExpression(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: int
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateRequestInputsExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class UpdateTemplateRequestOutputsExpression(TeaModel):
    def __init__(self, help=None, required=None, step_order=None, task_name=None, variable_name=None,
                 variable_type=None, variable_value=None):
        self.help = help  # type: str
        self.required = required  # type: bool
        self.step_order = step_order  # type: int
        self.task_name = task_name  # type: str
        self.variable_name = variable_name  # type: str
        self.variable_type = variable_type  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateRequestOutputsExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, description=None, inputs_expression=None, labels=None, outputs_expression=None,
                 root_entity=None, template_name=None, workspace=None):
        self.description = description  # type: str
        self.inputs_expression = inputs_expression  # type: list[UpdateTemplateRequestInputsExpression]
        self.labels = labels  # type: str
        self.outputs_expression = outputs_expression  # type: list[UpdateTemplateRequestOutputsExpression]
        self.root_entity = root_entity  # type: str
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        if self.inputs_expression:
            for k in self.inputs_expression:
                if k:
                    k.validate()
        if self.outputs_expression:
            for k in self.outputs_expression:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['InputsExpression'] = []
        if self.inputs_expression is not None:
            for k in self.inputs_expression:
                result['InputsExpression'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        result['OutputsExpression'] = []
        if self.outputs_expression is not None:
            for k in self.outputs_expression:
                result['OutputsExpression'].append(k.to_map() if k else None)
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.inputs_expression = []
        if m.get('InputsExpression') is not None:
            for k in m.get('InputsExpression'):
                temp_model = UpdateTemplateRequestInputsExpression()
                self.inputs_expression.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        self.outputs_expression = []
        if m.get('OutputsExpression') is not None:
            for k in m.get('OutputsExpression'):
                temp_model = UpdateTemplateRequestOutputsExpression()
                self.outputs_expression.append(temp_model.from_map(k))
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateTemplateShrinkRequest(TeaModel):
    def __init__(self, description=None, inputs_expression_shrink=None, labels=None,
                 outputs_expression_shrink=None, root_entity=None, template_name=None, workspace=None):
        self.description = description  # type: str
        self.inputs_expression_shrink = inputs_expression_shrink  # type: str
        self.labels = labels  # type: str
        self.outputs_expression_shrink = outputs_expression_shrink  # type: str
        self.root_entity = root_entity  # type: str
        self.template_name = template_name  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.inputs_expression_shrink is not None:
            result['InputsExpression'] = self.inputs_expression_shrink
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.outputs_expression_shrink is not None:
            result['OutputsExpression'] = self.outputs_expression_shrink
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputsExpression') is not None:
            self.inputs_expression_shrink = m.get('InputsExpression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputsExpression') is not None:
            self.outputs_expression_shrink = m.get('OutputsExpression')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTemplateResponse, self).to_map()
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceRequest(TeaModel):
    def __init__(self, description=None, job_lifecycle=None, labels=None, role=None, workspace=None):
        self.description = description  # type: str
        self.job_lifecycle = job_lifecycle  # type: int
        self.labels = labels  # type: str
        self.role = role  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.role is not None:
            result['Role'] = self.role
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateWorkspaceResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWorkspaceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWorkspaceResponse, self).to_map()
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
            temp_model = UpdateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadEntityRequest(TeaModel):
    def __init__(self, entity_csvfile=None, workspace=None):
        self.entity_csvfile = entity_csvfile  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_csvfile is not None:
            result['EntityCSVFile'] = self.entity_csvfile
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityCSVFile') is not None:
            self.entity_csvfile = m.get('EntityCSVFile')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UploadEntityResponseBody(TeaModel):
    def __init__(self, entity_type=None, host_id=None, request_id=None, workspace=None):
        self.entity_type = entity_type  # type: str
        self.host_id = host_id  # type: str
        self.request_id = request_id  # type: str
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UploadEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadEntityResponse, self).to_map()
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
            temp_model = UploadEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


