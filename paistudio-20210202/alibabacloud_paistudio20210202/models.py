# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateExperimentRequest(TeaModel):
    def __init__(self, name=None, description=None, source=None, folder_id=None, workspace_id=None, template_id=None,
                 options=None):
        self.name = name  # type: str
        self.description = description  # type: str
        self.source = source  # type: str
        self.folder_id = folder_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.template_id = template_id  # type: str
        self.options = options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExperimentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.source is not None:
            result['Source'] = self.source
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None, experiment_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.experiment_id = experiment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateExperimentResponse, self).to_map()
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
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceResponseBody, self).to_map()
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


class DeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceResponse, self).to_map()
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentStatusResponseBodyNodes(TeaModel):
    def __init__(self, node_id=None, job_id=None, run_id=None, run_node_id=None, status=None, started_at=None,
                 finished_at=None):
        self.node_id = node_id  # type: str
        self.job_id = job_id  # type: str
        self.run_id = run_id  # type: str
        self.run_node_id = run_node_id  # type: str
        self.status = status  # type: str
        self.started_at = started_at  # type: str
        self.finished_at = finished_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentStatusResponseBodyNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_node_id is not None:
            result['RunNodeId'] = self.run_node_id
        if self.status is not None:
            result['Status'] = self.status
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunNodeId') is not None:
            self.run_node_id = m.get('RunNodeId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        return self


class GetExperimentStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None, nodes=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.nodes = nodes  # type: list[GetExperimentStatusResponseBodyNodes]

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetExperimentStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GetExperimentStatusResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class GetExperimentStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetExperimentStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExperimentStatusResponse, self).to_map()
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
            temp_model = GetExperimentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentFolderChildrenRequest(TeaModel):
    def __init__(self, workspace_id=None, only_folder=None):
        self.workspace_id = workspace_id  # type: str
        self.only_folder = only_folder  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentFolderChildrenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.only_folder is not None:
            result['OnlyFolder'] = self.only_folder
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('OnlyFolder') is not None:
            self.only_folder = m.get('OnlyFolder')
        return self


class GetExperimentFolderChildrenResponseBodyItems(TeaModel):
    def __init__(self, id=None, name=None, type=None, icon=None, empty=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.icon = icon  # type: str
        self.empty = empty  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentFolderChildrenResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.empty is not None:
            result['Empty'] = self.empty
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Empty') is not None:
            self.empty = m.get('Empty')
        return self


class GetExperimentFolderChildrenResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, items=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.items = items  # type: list[GetExperimentFolderChildrenResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetExperimentFolderChildrenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetExperimentFolderChildrenResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class GetExperimentFolderChildrenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetExperimentFolderChildrenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExperimentFolderChildrenResponse, self).to_map()
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
            temp_model = GetExperimentFolderChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthRolesRequest(TeaModel):
    def __init__(self, workspace_id=None, is_generate_token=None):
        self.workspace_id = workspace_id  # type: str
        self.is_generate_token = is_generate_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthRolesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.is_generate_token is not None:
            result['IsGenerateToken'] = self.is_generate_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('IsGenerateToken') is not None:
            self.is_generate_token = m.get('IsGenerateToken')
        return self


class ListAuthRolesResponseBodyRolesToken(TeaModel):
    def __init__(self, security_token=None, access_key_id=None, access_key_secret=None, expiration=None):
        self.security_token = security_token  # type: str
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.expiration = expiration  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthRolesResponseBodyRolesToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        return self


class ListAuthRolesResponseBodyRoles(TeaModel):
    def __init__(self, role_name=None, role_arn=None, is_enabled=None, token=None, role_type=None):
        self.role_name = role_name  # type: str
        self.role_arn = role_arn  # type: str
        self.is_enabled = is_enabled  # type: str
        self.token = token  # type: ListAuthRolesResponseBodyRolesToken
        self.role_type = role_type  # type: str

    def validate(self):
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super(ListAuthRolesResponseBodyRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.token is not None:
            result['Token'] = self.token.to_map()
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('Token') is not None:
            temp_model = ListAuthRolesResponseBodyRolesToken()
            self.token = temp_model.from_map(m['Token'])
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class ListAuthRolesResponseBody(TeaModel):
    def __init__(self, request_id=None, roles=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.roles = roles  # type: list[ListAuthRolesResponseBodyRoles]

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthRolesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = ListAuthRolesResponseBodyRoles()
                self.roles.append(temp_model.from_map(k))
        return self


class ListAuthRolesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAuthRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthRolesResponse, self).to_map()
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
            temp_model = ListAuthRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeInputSchemaRequest(TeaModel):
    def __init__(self, input_id=None, input_index=None):
        self.input_id = input_id  # type: str
        self.input_index = input_index  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeInputSchemaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_id is not None:
            result['InputId'] = self.input_id
        if self.input_index is not None:
            result['InputIndex'] = self.input_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputId') is not None:
            self.input_id = m.get('InputId')
        if m.get('InputIndex') is not None:
            self.input_index = m.get('InputIndex')
        return self


class GetNodeInputSchemaResponseBody(TeaModel):
    def __init__(self, request_id=None, col_names=None, col_types=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.col_names = col_names  # type: list[str]
        self.col_types = col_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeInputSchemaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.col_names is not None:
            result['ColNames'] = self.col_names
        if self.col_types is not None:
            result['ColTypes'] = self.col_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ColNames') is not None:
            self.col_names = m.get('ColNames')
        if m.get('ColTypes') is not None:
            self.col_types = m.get('ColTypes')
        return self


class GetNodeInputSchemaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNodeInputSchemaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNodeInputSchemaResponse, self).to_map()
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
            temp_model = GetNodeInputSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlgoDefsRequestBody(TeaModel):
    def __init__(self, provider=None, identifier=None, version=None, signature=None):
        self.provider = provider  # type: str
        self.identifier = identifier  # type: str
        self.version = version  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlgoDefsRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.version is not None:
            result['Version'] = self.version
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class ListAlgoDefsRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: list[ListAlgoDefsRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlgoDefsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ListAlgoDefsRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class ListAlgoDefsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlgoDefsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListAlgoDefsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlgoDefsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlgoDefsResponse, self).to_map()
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
            temp_model = ListAlgoDefsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageLabelsRequestLabels(TeaModel):
    def __init__(self, key=None, value=None):
        # Key
        self.key = key  # type: str
        # Value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageLabelsRequestLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddImageLabelsRequest(TeaModel):
    def __init__(self, labels=None):
        # 标签
        self.labels = labels  # type: list[AddImageLabelsRequestLabels]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddImageLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AddImageLabelsRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class AddImageLabelsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageLabelsResponseBody, self).to_map()
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


class AddImageLabelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddImageLabelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddImageLabelsResponse, self).to_map()
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
            temp_model = AddImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, order=None, experiment_id=None, name=None, creator=None,
                 source=None, workspace_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.order = order  # type: str
        self.experiment_id = experiment_id  # type: str
        self.name = name  # type: str
        self.creator = creator  # type: str
        self.source = source  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExperimentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.order is not None:
            result['Order'] = self.order
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name is not None:
            result['Name'] = self.name
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListExperimentsResponseBodyExperiments(TeaModel):
    def __init__(self, experiment_id=None, name=None, description=None, gmt_create_time=None,
                 gmt_modified_time=None, creator=None, source=None, version=None, workspace_id=None):
        self.experiment_id = experiment_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.creator = creator  # type: str
        self.source = source  # type: str
        self.version = version  # type: long
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExperimentsResponseBodyExperiments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(self, request_id=None, experiments=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.experiments = experiments  # type: list[ListExperimentsResponseBodyExperiments]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExperimentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListExperimentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExperimentsResponse, self).to_map()
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
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmTreeRequest(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgorithmTreeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAlgorithmTreeResponseBody(TeaModel):
    def __init__(self, request_id=None, tree=None, timestamp=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.tree = tree  # type: list[dict[str, any]]
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgorithmTreeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tree is not None:
            result['Tree'] = self.tree
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tree') is not None:
            self.tree = m.get('Tree')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetAlgorithmTreeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAlgorithmTreeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlgorithmTreeResponse, self).to_map()
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
            temp_model = GetAlgorithmTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentFolderRequest(TeaModel):
    def __init__(self, workspace_id=None, name=None, parent_folder_id=None, source=None):
        self.workspace_id = workspace_id  # type: str
        self.name = name  # type: str
        self.parent_folder_id = parent_folder_id  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExperimentFolderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateExperimentFolderResponseBody(TeaModel):
    def __init__(self, request_id=None, folder_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.folder_id = folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExperimentFolderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class CreateExperimentFolderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateExperimentFolderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateExperimentFolderResponse, self).to_map()
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
            temp_model = CreateExperimentFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(self, verbose=None):
        self.verbose = verbose  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(self, request_id=None, experiment_id=None, workspace_id=None, job_id=None, snapshot=None,
                 execute_type=None, node_id=None, run_info=None, run_id=None, paiflow_node_id=None, creator=None, status=None,
                 gmt_create_time=None, arguments=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.experiment_id = experiment_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.job_id = job_id  # type: str
        self.snapshot = snapshot  # type: str
        self.execute_type = execute_type  # type: str
        self.node_id = node_id  # type: str
        self.run_info = run_info  # type: str
        self.run_id = run_id  # type: str
        self.paiflow_node_id = paiflow_node_id  # type: str
        self.creator = creator  # type: str
        self.status = status  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.arguments = arguments  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.run_info is not None:
            result['RunInfo'] = self.run_info
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.paiflow_node_id is not None:
            result['PaiflowNodeId'] = self.paiflow_node_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RunInfo') is not None:
            self.run_info = m.get('RunInfo')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('PaiflowNodeId') is not None:
            self.paiflow_node_id = m.get('PaiflowNodeId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        return self


class GetJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobResponse, self).to_map()
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
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentMetaResponseBody(TeaModel):
    def __init__(self, request_id=None, experiment_id=None, name=None, description=None, gmt_create_time=None,
                 gmt_modified_time=None, creator=None, source=None, version=None, workspace_id=None, options=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.experiment_id = experiment_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.creator = creator  # type: str
        self.source = source  # type: str
        self.version = version  # type: str
        self.workspace_id = workspace_id  # type: str
        self.options = options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class GetExperimentMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetExperimentMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExperimentMetaResponse, self).to_map()
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
            temp_model = GetExperimentMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeOutputsResponseBodyOutputs(TeaModel):
    def __init__(self, display_name=None, type=None, output_id=None, output_index=None, value=None, node_name=None,
                 algo_name=None, location_type=None):
        self.display_name = display_name  # type: str
        self.type = type  # type: str
        self.output_id = output_id  # type: str
        self.output_index = output_index  # type: str
        self.value = value  # type: dict[str, any]
        self.node_name = node_name  # type: str
        self.algo_name = algo_name  # type: str
        self.location_type = location_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeOutputsResponseBodyOutputs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.output_id is not None:
            result['OutputId'] = self.output_id
        if self.output_index is not None:
            result['OutputIndex'] = self.output_index
        if self.value is not None:
            result['Value'] = self.value
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.location_type is not None:
            result['LocationType'] = self.location_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OutputId') is not None:
            self.output_id = m.get('OutputId')
        if m.get('OutputIndex') is not None:
            self.output_index = m.get('OutputIndex')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('LocationType') is not None:
            self.location_type = m.get('LocationType')
        return self


class ListNodeOutputsResponseBody(TeaModel):
    def __init__(self, request_id=None, outputs=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.outputs = outputs  # type: list[ListNodeOutputsResponseBodyOutputs]

    def validate(self):
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodeOutputsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ListNodeOutputsResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        return self


class ListNodeOutputsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNodeOutputsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodeOutputsResponse, self).to_map()
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
            temp_model = ListNodeOutputsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, source=None, list=None, tag_id=None, order=None,
                 type_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.source = source  # type: str
        self.list = list  # type: str
        self.tag_id = tag_id  # type: str
        self.order = order  # type: str
        self.type_id = type_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        if self.list is not None:
            result['List'] = self.list
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.order is not None:
            result['Order'] = self.order
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('List') is not None:
            self.list = m.get('List')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        return self


class ListTemplatesResponseBodyTemplateDataTemplate(TeaModel):
    def __init__(self, template_id=None, content=None, description=None, detail=None, doc_link=None, image_link=None,
                 name=None):
        self.template_id = template_id  # type: str
        self.content = content  # type: str
        self.description = description  # type: str
        self.detail = detail  # type: str
        self.doc_link = doc_link  # type: str
        self.image_link = image_link  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplateDataTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.doc_link is not None:
            result['DocLink'] = self.doc_link
        if self.image_link is not None:
            result['ImageLink'] = self.image_link
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DocLink') is not None:
            self.doc_link = m.get('DocLink')
        if m.get('ImageLink') is not None:
            self.image_link = m.get('ImageLink')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListTemplatesResponseBodyTemplateDataTemplateTag(TeaModel):
    def __init__(self, name=None, tag_id=None, type_id=None):
        self.name = name  # type: str
        self.tag_id = tag_id  # type: str
        self.type_id = type_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplateDataTemplateTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        return self


class ListTemplatesResponseBodyTemplateDataTemplateType(TeaModel):
    def __init__(self, type_id=None, name=None):
        self.type_id = type_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplateDataTemplateType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListTemplatesResponseBodyTemplateData(TeaModel):
    def __init__(self, template=None, template_tag=None, template_type=None):
        self.template = template  # type: ListTemplatesResponseBodyTemplateDataTemplate
        self.template_tag = template_tag  # type: ListTemplatesResponseBodyTemplateDataTemplateTag
        self.template_type = template_type  # type: ListTemplatesResponseBodyTemplateDataTemplateType

    def validate(self):
        if self.template:
            self.template.validate()
        if self.template_tag:
            self.template_tag.validate()
        if self.template_type:
            self.template_type.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplateData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template is not None:
            result['Template'] = self.template.to_map()
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag.to_map()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Template') is not None:
            temp_model = ListTemplatesResponseBodyTemplateDataTemplate()
            self.template = temp_model.from_map(m['Template'])
        if m.get('TemplateTag') is not None:
            temp_model = ListTemplatesResponseBodyTemplateDataTemplateTag()
            self.template_tag = temp_model.from_map(m['TemplateTag'])
        if m.get('TemplateType') is not None:
            temp_model = ListTemplatesResponseBodyTemplateDataTemplateType()
            self.template_type = temp_model.from_map(m['TemplateType'])
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, template_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.template_data = template_data  # type: list[ListTemplatesResponseBodyTemplateData]

    def validate(self):
        if self.template_data:
            for k in self.template_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TemplateData'] = []
        if self.template_data is not None:
            for k in self.template_data:
                result['TemplateData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.template_data = []
        if m.get('TemplateData') is not None:
            for k in m.get('TemplateData'):
                temp_model = ListTemplatesResponseBodyTemplateData()
                self.template_data.append(temp_model.from_map(k))
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplatesResponse, self).to_map()
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentMetaRequest(TeaModel):
    def __init__(self, name=None, description=None, folder_id=None, options=None):
        self.name = name  # type: str
        self.description = description  # type: str
        self.folder_id = folder_id  # type: str
        self.options = options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class UpdateExperimentMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentMetaResponseBody, self).to_map()
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


class UpdateExperimentMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateExperimentMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExperimentMetaResponse, self).to_map()
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
            temp_model = UpdateExperimentMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, sort_by=None, order=None, labels=None,
                 verbose=None):
        # 镜像名称，支持模糊搜索
        self.name = name  # type: str
        # 分页，从1开始，默认1
        self.page_number = page_number  # type: int
        # 页大小，默认20
        self.page_size = page_size  # type: int
        # 排序字段
        self.sort_by = sort_by  # type: str
        # 排序方向： ASC - 升序 DESC - 降序
        self.order = order  # type: str
        # 过滤值 以逗号分隔
        self.labels = labels  # type: str
        # 是否显示非必要信息：Labels
        self.verbose = verbose  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class ListImagesResponseBodyImagesLabels(TeaModel):
    def __init__(self, key=None, value=None):
        # Key
        self.key = key  # type: str
        # Value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(self, name=None, gmt_create_time=None, description=None, image_uri=None, labels=None, image_id=None):
        # 镜像名称
        self.name = name  # type: str
        # 创建 UTC 时间，日期格式 iso8601
        self.gmt_create_time = gmt_create_time  # type: str
        # 镜像描述
        self.description = description  # type: str
        # 镜像地址，包含版本号
        self.image_uri = image_uri  # type: str
        # 镜像标签，是个map
        self.labels = labels  # type: list[ListImagesResponseBodyImagesLabels]
        # 镜像id
        self.image_id = image_id  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListImagesResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListImagesResponseBodyImagesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, images=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 总数
        self.total_count = total_count  # type: long
        # 镜像列表
        self.images = images  # type: list[ListImagesResponseBodyImages]

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class ListImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListImagesResponse, self).to_map()
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDefsRequest(TeaModel):
    def __init__(self, timestamp=None):
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgorithmDefsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetAlgorithmDefsResponseBody(TeaModel):
    def __init__(self, request_id=None, specs=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.specs = specs  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgorithmDefsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.specs is not None:
            result['Specs'] = self.specs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Specs') is not None:
            self.specs = m.get('Specs')
        return self


class GetAlgorithmDefsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAlgorithmDefsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlgorithmDefsResponse, self).to_map()
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
            temp_model = GetAlgorithmDefsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentFolderResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExperimentFolderResponseBody, self).to_map()
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


class DeleteExperimentFolderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteExperimentFolderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteExperimentFolderResponse, self).to_map()
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
            temp_model = DeleteExperimentFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageLabelsRequest(TeaModel):
    def __init__(self, label_keys=None, label_filter=None, image_id=None):
        # 标签列表，以逗号分隔
        self.label_keys = label_keys  # type: str
        # image过滤条件，获取满足条件的image的所有label
        self.label_filter = label_filter  # type: str
        # 镜像id
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImageLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        if self.label_filter is not None:
            result['LabelFilter'] = self.label_filter
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        if m.get('LabelFilter') is not None:
            self.label_filter = m.get('LabelFilter')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ListImageLabelsResponseBodyLabels(TeaModel):
    def __init__(self, key=None, value=None):
        # 键
        self.key = key  # type: str
        # 值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImageLabelsResponseBodyLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListImageLabelsResponseBody(TeaModel):
    def __init__(self, request_id=None, labels=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 镜像标签
        self.labels = labels  # type: list[ListImageLabelsResponseBodyLabels]
        # 符合过滤条件的数量
        self.total_count = total_count  # type: long

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListImageLabelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListImageLabelsResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImageLabelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListImageLabelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListImageLabelsResponse, self).to_map()
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
            temp_model = ListImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgoTreeRequest(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgoTreeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAlgoTreeResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.data = data  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgoTreeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAlgoTreeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAlgoTreeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlgoTreeResponse, self).to_map()
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
            temp_model = GetAlgoTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None, experiment_id=None, name=None, description=None, gmt_create_time=None,
                 gmt_modified_time=None, creator=None, source=None, version=None, workspace_id=None, content=None, options=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.experiment_id = experiment_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.creator = creator  # type: str
        self.source = source  # type: str
        self.version = version  # type: long
        self.workspace_id = workspace_id  # type: str
        self.content = content  # type: str
        self.options = options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.content is not None:
            result['Content'] = self.content
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class GetExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExperimentResponse, self).to_map()
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
            temp_model = GetExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyExperimentRequest(TeaModel):
    def __init__(self, name=None, description=None, source=None, folder_id=None, workspace_id=None):
        # 实验名称，最大长度 128，可包含中英文
        self.name = name  # type: str
        # 实验描述
        self.description = description  # type: str
        # 实验来源，目前 PaiStudio，data-airec（推荐白盒）
        self.source = source  # type: str
        # 实验创建的目录 id
        self.folder_id = folder_id  # type: str
        # 实验创建的Workspace
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyExperimentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.source is not None:
            result['Source'] = self.source
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CopyExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None, experiment_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.experiment_id = experiment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        return self


class CopyExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CopyExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CopyExperimentResponse, self).to_map()
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
            temp_model = CopyExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopJobResponseBody, self).to_map()
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


class StopJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopJobResponse, self).to_map()
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
            temp_model = StopJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(self, experiment_id=None, execute_type=None, node_id=None, options=None):
        self.experiment_id = experiment_id  # type: str
        self.execute_type = execute_type  # type: str
        self.node_id = node_id  # type: str
        self.options = options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateJobResponse, self).to_map()
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
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeVisualizationRequest(TeaModel):
    def __init__(self, config=None):
        self.config = config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeVisualizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class GetNodeVisualizationResponseBody(TeaModel):
    def __init__(self, request_id=None, visualization_type=None, content=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.visualization_type = visualization_type  # type: str
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeVisualizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.visualization_type is not None:
            result['VisualizationType'] = self.visualization_type
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VisualizationType') is not None:
            self.visualization_type = m.get('VisualizationType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetNodeVisualizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNodeVisualizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNodeVisualizationResponse, self).to_map()
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
            temp_model = GetNodeVisualizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeOutputRequest(TeaModel):
    def __init__(self, output_index=None):
        self.output_index = output_index  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeOutputRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_index is not None:
            result['OutputIndex'] = self.output_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutputIndex') is not None:
            self.output_index = m.get('OutputIndex')
        return self


class GetNodeOutputResponseBody(TeaModel):
    def __init__(self, request_id=None, node_name=None, algo_name=None, display_name=None, type=None, value=None,
                 location_type=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.node_name = node_name  # type: str
        self.algo_name = algo_name  # type: str
        self.display_name = display_name  # type: str
        self.type = type  # type: str
        self.value = value  # type: dict[str, any]
        self.location_type = location_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeOutputResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.location_type is not None:
            result['LocationType'] = self.location_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('LocationType') is not None:
            self.location_type = m.get('LocationType')
        return self


class GetNodeOutputResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNodeOutputResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNodeOutputResponse, self).to_map()
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
            temp_model = GetNodeOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageLabelsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageLabelsResponseBody, self).to_map()
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


class RemoveImageLabelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveImageLabelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveImageLabelsResponse, self).to_map()
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
            temp_model = RemoveImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewMCTableRequest(TeaModel):
    def __init__(self, workspace_id=None, endpoint=None):
        self.workspace_id = workspace_id  # type: str
        self.endpoint = endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviewMCTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        return self


class PreviewMCTableResponseBody(TeaModel):
    def __init__(self, request_id=None, content=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.content = content  # type: list[list[str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviewMCTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class PreviewMCTableResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PreviewMCTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PreviewMCTableResponse, self).to_map()
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
            temp_model = PreviewMCTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(self, workspace_id=None, service_type=None):
        self.workspace_id = workspace_id  # type: str
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(self, url=None, service_id=None):
        self.url = url  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesResponseBodyServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, services=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.services = services  # type: list[ListServicesResponseBodyServices]

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServicesResponse, self).to_map()
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageResponseBody, self).to_map()
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


class RemoveImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveImageResponse, self).to_map()
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
            temp_model = RemoveImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopExperimentResponseBody, self).to_map()
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


class StopExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopExperimentResponse, self).to_map()
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
            temp_model = StopExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageRequestLabels(TeaModel):
    def __init__(self, key=None, value=None):
        # Key
        self.key = key  # type: str
        # Value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageRequestLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddImageRequest(TeaModel):
    def __init__(self, name=None, description=None, image_uri=None, labels=None):
        # 镜像名称
        self.name = name  # type: str
        # 镜像描述
        self.description = description  # type: str
        # 镜像地址
        self.image_uri = image_uri  # type: str
        # 镜像标签，是个数组
        self.labels = labels  # type: list[AddImageRequestLabels]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AddImageRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class AddImageResponseBody(TeaModel):
    def __init__(self, request_id=None, image_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 镜像 id
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class AddImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddImageResponse, self).to_map()
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchMCTablesRequest(TeaModel):
    def __init__(self, workspace_id=None, keyword=None):
        self.workspace_id = workspace_id  # type: str
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchMCTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class SearchMCTablesResponseBody(TeaModel):
    def __init__(self, request_id=None, tables=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.tables = tables  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchMCTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class SearchMCTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SearchMCTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchMCTablesResponse, self).to_map()
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
            temp_model = SearchMCTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None, name=None, image_link=None, doc_link=None, detail=None,
                 description=None, content=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str
        self.name = name  # type: str
        self.image_link = image_link  # type: str
        self.doc_link = doc_link  # type: str
        self.detail = detail  # type: str
        self.description = description  # type: str
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.image_link is not None:
            result['ImageLink'] = self.image_link
        if self.doc_link is not None:
            result['DocLink'] = self.doc_link
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.description is not None:
            result['Description'] = self.description
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageLink') is not None:
            self.image_link = m.get('ImageLink')
        if m.get('DocLink') is not None:
            self.doc_link = m.get('DocLink')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateResponse, self).to_map()
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExperimentResponseBody, self).to_map()
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


class DeleteExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteExperimentResponse, self).to_map()
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
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequestConfig(TeaModel):
    def __init__(self, log_directory=None):
        self.log_directory = log_directory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceRequestConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_directory is not None:
            result['LogDirectory'] = self.log_directory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogDirectory') is not None:
            self.log_directory = m.get('LogDirectory')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, service_type=None, config=None):
        self.service_type = service_type  # type: str
        self.config = config  # type: CreateServiceRequestConfig

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super(CreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Config') is not None:
            temp_model = CreateServiceRequestConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, url=None, service_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.url = url  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceResponse, self).to_map()
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentFolderRequest(TeaModel):
    def __init__(self, name=None, parent_folder_id=None):
        self.name = name  # type: str
        self.parent_folder_id = parent_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentFolderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class UpdateExperimentFolderResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentFolderResponseBody, self).to_map()
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


class UpdateExperimentFolderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateExperimentFolderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExperimentFolderResponse, self).to_map()
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
            temp_model = UpdateExperimentFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMCTableSchemaRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMCTableSchemaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMCTableSchemaResponseBodyColumns(TeaModel):
    def __init__(self, name=None, type=None, preview=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.preview = preview  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMCTableSchemaResponseBodyColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.preview is not None:
            result['Preview'] = self.preview
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Preview') is not None:
            self.preview = m.get('Preview')
        return self


class GetMCTableSchemaResponseBody(TeaModel):
    def __init__(self, request_id=None, columns=None, partition_columns=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.columns = columns  # type: list[GetMCTableSchemaResponseBodyColumns]
        self.partition_columns = partition_columns  # type: list[str]

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMCTableSchemaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.partition_columns is not None:
            result['PartitionColumns'] = self.partition_columns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetMCTableSchemaResponseBodyColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('PartitionColumns') is not None:
            self.partition_columns = m.get('PartitionColumns')
        return self


class GetMCTableSchemaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMCTableSchemaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMCTableSchemaResponse, self).to_map()
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
            temp_model = GetMCTableSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentContentRequest(TeaModel):
    def __init__(self, content=None, version=None):
        self.content = content  # type: str
        self.version = version  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateExperimentContentResponseBody(TeaModel):
    def __init__(self, request_id=None, version=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.version = version  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateExperimentContentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateExperimentContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExperimentContentResponse, self).to_map()
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
            temp_model = UpdateExperimentContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDefRequest(TeaModel):
    def __init__(self, provider=None, identifier=None, version=None, signature=None):
        self.provider = provider  # type: str
        self.identifier = identifier  # type: str
        self.version = version  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgorithmDefRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.version is not None:
            result['Version'] = self.version
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetAlgorithmDefResponseBody(TeaModel):
    def __init__(self, request_id=None, spec=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.spec = spec  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgorithmDefResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class GetAlgorithmDefResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAlgorithmDefResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlgorithmDefResponse, self).to_map()
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
            temp_model = GetAlgorithmDefResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(self, verbose=None):
        # 是否显示非必要信息：Labels
        self.verbose = verbose  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetImageResponseBodyLabels(TeaModel):
    def __init__(self, key=None, value=None):
        # Key
        self.key = key  # type: str
        # Value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(self, request_id=None, gmt_create_time=None, gmt_modified_time=None, name=None, description=None,
                 image_uri=None, operator_create=None, parent_operator_create=None, labels=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 创建 UTC 时间，日期格式 iso8601
        self.gmt_create_time = gmt_create_time  # type: str
        # 创建 UTC 时间，日期格式 iso8601
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 镜像名称
        self.name = name  # type: str
        # 描述
        self.description = description  # type: str
        # 镜像地址，包含版本号
        self.image_uri = image_uri  # type: str
        # 创建人
        self.operator_create = operator_create  # type: str
        # 创建人父账户
        self.parent_operator_create = parent_operator_create  # type: str
        # 镜像标签
        self.labels = labels  # type: list[GetImageResponseBodyLabels]

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.operator_create is not None:
            result['OperatorCreate'] = self.operator_create
        if self.parent_operator_create is not None:
            result['ParentOperatorCreate'] = self.parent_operator_create
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('OperatorCreate') is not None:
            self.operator_create = m.get('OperatorCreate')
        if m.get('ParentOperatorCreate') is not None:
            self.parent_operator_create = m.get('ParentOperatorCreate')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetImageResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class GetImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageResponse, self).to_map()
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
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRequest(TeaModel):
    def __init__(self, service_type=None):
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, url=None, service_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.url = url  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class GetServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceResponse, self).to_map()
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, experiment_id=None, creator=None, order=None, page_number=None, page_size=None):
        self.experiment_id = experiment_id  # type: str
        self.creator = creator  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(self, experiment_id=None, workspace_id=None, job_id=None, execute_type=None, node_id=None,
                 run_id=None, paiflow_node_id=None, creator=None, status=None, gmt_create_time=None):
        self.experiment_id = experiment_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.job_id = job_id  # type: str
        self.execute_type = execute_type  # type: str
        self.node_id = node_id  # type: str
        self.run_id = run_id  # type: str
        self.paiflow_node_id = paiflow_node_id  # type: str
        self.creator = creator  # type: str
        self.status = status  # type: str
        self.gmt_create_time = gmt_create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.paiflow_node_id is not None:
            result['PaiflowNodeId'] = self.paiflow_node_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('PaiflowNodeId') is not None:
            self.paiflow_node_id = m.get('PaiflowNodeId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, request_id=None, jobs=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.jobs = jobs  # type: list[ListJobsResponseBodyJobs]

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        return self


class ListJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobsResponse, self).to_map()
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
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


