# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreatePackageRequest(TeaModel):
    def __init__(self, body=None, is_install=None):
        self.body = body  # type: str
        self.is_install = is_install  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.is_install is not None:
            result['isInstall'] = self.is_install
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('isInstall') is not None:
            self.is_install = m.get('isInstall')
        return self


class CreatePackageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreatePackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePackageResponse, self).to_map()
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
            temp_model = CreatePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaPlanRequest(TeaModel):
    def __init__(self, body=None, region=None, tenant_id=None):
        self.body = body  # type: str
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQuotaPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateQuotaPlanResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQuotaPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateQuotaPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateQuotaPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQuotaPlanResponse, self).to_map()
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
            temp_model = CreateQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaScheduleRequest(TeaModel):
    def __init__(self, body=None, region=None, tenant_id=None):
        self.body = body  # type: str
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQuotaScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateQuotaScheduleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQuotaScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateQuotaScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateQuotaScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQuotaScheduleResponse, self).to_map()
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
            temp_model = CreateQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateRoleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRoleResponse, self).to_map()
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
            temp_model = CreateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuotaPlanRequest(TeaModel):
    def __init__(self, region=None, tenant_id=None):
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQuotaPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DeleteQuotaPlanResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQuotaPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteQuotaPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteQuotaPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQuotaPlanResponse, self).to_map()
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
            temp_model = DeleteQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPackageRequest(TeaModel):
    def __init__(self, source_project=None):
        self.source_project = source_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_project is not None:
            result['sourceProject'] = self.source_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sourceProject') is not None:
            self.source_project = m.get('sourceProject')
        return self


class GetPackageResponseBodyDataAllowedProjectList(TeaModel):
    def __init__(self, label=None, project=None):
        self.label = label  # type: str
        self.project = project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPackageResponseBodyDataAllowedProjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class GetPackageResponseBodyDataResourceListFunction(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPackageResponseBodyDataResourceListFunction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetPackageResponseBodyDataResourceListResource(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPackageResponseBodyDataResourceListResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetPackageResponseBodyDataResourceListTable(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPackageResponseBodyDataResourceListTable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetPackageResponseBodyDataResourceList(TeaModel):
    def __init__(self, function=None, resource=None, table=None):
        self.function = function  # type: list[GetPackageResponseBodyDataResourceListFunction]
        self.resource = resource  # type: list[GetPackageResponseBodyDataResourceListResource]
        self.table = table  # type: list[GetPackageResponseBodyDataResourceListTable]

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPackageResponseBodyDataResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = GetPackageResponseBodyDataResourceListFunction()
                self.function.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = GetPackageResponseBodyDataResourceListResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = GetPackageResponseBodyDataResourceListTable()
                self.table.append(temp_model.from_map(k))
        return self


class GetPackageResponseBodyData(TeaModel):
    def __init__(self, allowed_project_list=None, resource_list=None):
        self.allowed_project_list = allowed_project_list  # type: list[GetPackageResponseBodyDataAllowedProjectList]
        self.resource_list = resource_list  # type: GetPackageResponseBodyDataResourceList

    def validate(self):
        if self.allowed_project_list:
            for k in self.allowed_project_list:
                if k:
                    k.validate()
        if self.resource_list:
            self.resource_list.validate()

    def to_map(self):
        _map = super(GetPackageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['allowedProjectList'] = []
        if self.allowed_project_list is not None:
            for k in self.allowed_project_list:
                result['allowedProjectList'].append(k.to_map() if k else None)
        if self.resource_list is not None:
            result['resourceList'] = self.resource_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.allowed_project_list = []
        if m.get('allowedProjectList') is not None:
            for k in m.get('allowedProjectList'):
                temp_model = GetPackageResponseBodyDataAllowedProjectList()
                self.allowed_project_list.append(temp_model.from_map(k))
        if m.get('resourceList') is not None:
            temp_model = GetPackageResponseBodyDataResourceList()
            self.resource_list = temp_model.from_map(m['resourceList'])
        return self


class GetPackageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetPackageResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPackageResponse, self).to_map()
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
            temp_model = GetPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponseBodyDataIpWhiteList(TeaModel):
    def __init__(self, ip_list=None, vpc_ip_list=None):
        self.ip_list = ip_list  # type: str
        self.vpc_ip_list = vpc_ip_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBodyDataIpWhiteList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.vpc_ip_list is not None:
            result['vpcIpList'] = self.vpc_ip_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('vpcIpList') is not None:
            self.vpc_ip_list = m.get('vpcIpList')
        return self


class GetProjectResponseBodyDataPropertiesEncryption(TeaModel):
    def __init__(self, algorithm=None, enable=None, key=None):
        self.algorithm = algorithm  # type: str
        self.enable = enable  # type: bool
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBodyDataPropertiesEncryption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.enable is not None:
            result['enable'] = self.enable
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycle(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBodyDataPropertiesTableLifecycle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataProperties(TeaModel):
    def __init__(self, allow_full_scan=None, elder_tunnel_quota=None, enable_decimal_2=None,
                 enable_tunnel_quota_route=None, encryption=None, retention_days=None, sql_metering_max=None, table_lifecycle=None,
                 timezone=None, tunnel_quota=None, type_system=None):
        self.allow_full_scan = allow_full_scan  # type: bool
        self.elder_tunnel_quota = elder_tunnel_quota  # type: str
        self.enable_decimal_2 = enable_decimal_2  # type: bool
        self.enable_tunnel_quota_route = enable_tunnel_quota_route  # type: bool
        self.encryption = encryption  # type: GetProjectResponseBodyDataPropertiesEncryption
        self.retention_days = retention_days  # type: long
        self.sql_metering_max = sql_metering_max  # type: str
        self.table_lifecycle = table_lifecycle  # type: GetProjectResponseBodyDataPropertiesTableLifecycle
        self.timezone = timezone  # type: str
        self.tunnel_quota = tunnel_quota  # type: str
        self.type_system = type_system  # type: str

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()

    def to_map(self):
        _map = super(GetProjectResponseBodyDataProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan
        if self.elder_tunnel_quota is not None:
            result['elderTunnelQuota'] = self.elder_tunnel_quota
        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2
        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route
        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max
        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        if self.type_system is not None:
            result['typeSystem'] = self.type_system
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')
        if m.get('elderTunnelQuota') is not None:
            self.elder_tunnel_quota = m.get('elderTunnelQuota')
        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')
        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')
        if m.get('encryption') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesEncryption()
            self.encryption = temp_model.from_map(m['encryption'])
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')
        if m.get('tableLifecycle') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m['tableLifecycle'])
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')
        return self


class GetProjectResponseBodyDataSaleTag(TeaModel):
    def __init__(self, resource_id=None, resource_type=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBodyDataSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetProjectResponseBodyDataSecurityPropertiesProjectProtection(TeaModel):
    def __init__(self, exception_policy=None, protected=None):
        self.exception_policy = exception_policy  # type: str
        self.protected = protected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBodyDataSecurityPropertiesProjectProtection, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_policy is not None:
            result['exceptionPolicy'] = self.exception_policy
        if self.protected is not None:
            result['protected'] = self.protected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exceptionPolicy') is not None:
            self.exception_policy = m.get('exceptionPolicy')
        if m.get('protected') is not None:
            self.protected = m.get('protected')
        return self


class GetProjectResponseBodyDataSecurityProperties(TeaModel):
    def __init__(self, enable_download_privilege=None, label_security=None,
                 object_creator_has_access_permission=None, object_creator_has_grant_permission=None, project_protection=None, using_acl=None,
                 using_policy=None):
        self.enable_download_privilege = enable_download_privilege  # type: bool
        self.label_security = label_security  # type: bool
        self.object_creator_has_access_permission = object_creator_has_access_permission  # type: bool
        self.object_creator_has_grant_permission = object_creator_has_grant_permission  # type: bool
        self.project_protection = project_protection  # type: GetProjectResponseBodyDataSecurityPropertiesProjectProtection
        self.using_acl = using_acl  # type: bool
        self.using_policy = using_policy  # type: bool

    def validate(self):
        if self.project_protection:
            self.project_protection.validate()

    def to_map(self):
        _map = super(GetProjectResponseBodyDataSecurityProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_download_privilege is not None:
            result['enableDownloadPrivilege'] = self.enable_download_privilege
        if self.label_security is not None:
            result['labelSecurity'] = self.label_security
        if self.object_creator_has_access_permission is not None:
            result['objectCreatorHasAccessPermission'] = self.object_creator_has_access_permission
        if self.object_creator_has_grant_permission is not None:
            result['objectCreatorHasGrantPermission'] = self.object_creator_has_grant_permission
        if self.project_protection is not None:
            result['projectProtection'] = self.project_protection.to_map()
        if self.using_acl is not None:
            result['usingAcl'] = self.using_acl
        if self.using_policy is not None:
            result['usingPolicy'] = self.using_policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableDownloadPrivilege') is not None:
            self.enable_download_privilege = m.get('enableDownloadPrivilege')
        if m.get('labelSecurity') is not None:
            self.label_security = m.get('labelSecurity')
        if m.get('objectCreatorHasAccessPermission') is not None:
            self.object_creator_has_access_permission = m.get('objectCreatorHasAccessPermission')
        if m.get('objectCreatorHasGrantPermission') is not None:
            self.object_creator_has_grant_permission = m.get('objectCreatorHasGrantPermission')
        if m.get('projectProtection') is not None:
            temp_model = GetProjectResponseBodyDataSecurityPropertiesProjectProtection()
            self.project_protection = temp_model.from_map(m['projectProtection'])
        if m.get('usingAcl') is not None:
            self.using_acl = m.get('usingAcl')
        if m.get('usingPolicy') is not None:
            self.using_policy = m.get('usingPolicy')
        return self


class GetProjectResponseBodyData(TeaModel):
    def __init__(self, comment=None, cost_storage=None, default_quota=None, ip_white_list=None, name=None,
                 owner=None, product_type=None, properties=None, sale_tag=None, security_properties=None, status=None,
                 type=None):
        self.comment = comment  # type: str
        self.cost_storage = cost_storage  # type: str
        self.default_quota = default_quota  # type: str
        self.ip_white_list = ip_white_list  # type: GetProjectResponseBodyDataIpWhiteList
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.product_type = product_type  # type: str
        self.properties = properties  # type: GetProjectResponseBodyDataProperties
        self.sale_tag = sale_tag  # type: GetProjectResponseBodyDataSaleTag
        self.security_properties = security_properties  # type: GetProjectResponseBodyDataSecurityProperties
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.ip_white_list:
            self.ip_white_list.validate()
        if self.properties:
            self.properties.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.security_properties:
            self.security_properties.validate()

    def to_map(self):
        _map = super(GetProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.cost_storage is not None:
            result['costStorage'] = self.cost_storage
        if self.default_quota is not None:
            result['defaultQuota'] = self.default_quota
        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.properties is not None:
            result['properties'] = self.properties.to_map()
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.security_properties is not None:
            result['securityProperties'] = self.security_properties.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('costStorage') is not None:
            self.cost_storage = m.get('costStorage')
        if m.get('defaultQuota') is not None:
            self.default_quota = m.get('defaultQuota')
        if m.get('ipWhiteList') is not None:
            temp_model = GetProjectResponseBodyDataIpWhiteList()
            self.ip_white_list = temp_model.from_map(m['ipWhiteList'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('properties') is not None:
            temp_model = GetProjectResponseBodyDataProperties()
            self.properties = temp_model.from_map(m['properties'])
        if m.get('saleTag') is not None:
            temp_model = GetProjectResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('securityProperties') is not None:
            temp_model = GetProjectResponseBodyDataSecurityProperties()
            self.security_properties = temp_model.from_map(m['securityProperties'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(self, data=None, http_code=None, request_id=None):
        self.data = data  # type: GetProjectResponseBodyData
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProjectResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectResponse, self).to_map()
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaRequest(TeaModel):
    def __init__(self, ak_proven=None, mock=None, region=None, tenant_id=None):
        self.ak_proven = ak_proven  # type: str
        self.mock = mock  # type: bool
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak_proven is not None:
            result['AkProven'] = self.ak_proven
        if self.mock is not None:
            result['mock'] = self.mock
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AkProven') is not None:
            self.ak_proven = m.get('AkProven')
        if m.get('mock') is not None:
            self.mock = m.get('mock')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaResponseBodyBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodyBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodyDataBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataSaleTag(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None):
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodyDataSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyDataScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodyDataScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListSaleTag(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None):
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodyDataSubQuotaInfoListSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoList(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, group_name=None,
                 id=None, name=None, nick_name=None, parameter=None, parent_id=None, region_id=None, sale_tag=None,
                 schedule_info=None, status=None, tag=None, tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.group_name = group_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.sale_tag = sale_tag  # type: GetQuotaResponseBodyDataSubQuotaInfoListSaleTag
        self.schedule_info = schedule_info  # type: GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo
        self.status = status  # type: str
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(GetQuotaResponseBodyDataSubQuotaInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBodyData(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, group_name=None,
                 id=None, name=None, nick_name=None, parameter=None, parent_id=None, region_id=None, sale_tag=None,
                 schedule_info=None, status=None, sub_quota_info_list=None, tag=None, tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: GetQuotaResponseBodyDataBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.group_name = group_name  # type: str
        # quota ID
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.sale_tag = sale_tag  # type: GetQuotaResponseBodyDataSaleTag
        self.schedule_info = schedule_info  # type: GetQuotaResponseBodyDataScheduleInfo
        self.status = status  # type: str
        self.sub_quota_info_list = sub_quota_info_list  # type: list[GetQuotaResponseBodyDataSubQuotaInfoList]
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQuotaResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyDataBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyDataScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaResponseBodyDataSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBodySaleTag(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None):
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodySaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodyScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaResponseBodySubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodySubQuotaInfoListBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodySubQuotaInfoListSaleTag(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None):
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodySubQuotaInfoListSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodySubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaResponseBodySubQuotaInfoListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaResponseBodySubQuotaInfoList(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, id=None, name=None,
                 nick_name=None, parameter=None, parent_id=None, region_id=None, sale_tag=None, schedule_info=None,
                 status=None, tag=None, tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: GetQuotaResponseBodySubQuotaInfoListBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.sale_tag = sale_tag  # type: GetQuotaResponseBodySubQuotaInfoListSaleTag
        self.schedule_info = schedule_info  # type: GetQuotaResponseBodySubQuotaInfoListScheduleInfo
        self.status = status  # type: str
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(GetQuotaResponseBodySubQuotaInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBody(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, data=None, id=None,
                 name=None, nick_name=None, parameter=None, parent_id=None, region_id=None, request_id=None,
                 sale_tag=None, schedule_info=None, status=None, sub_quota_info_list=None, tag=None, tenant_id=None,
                 type=None, version=None):
        self.billing_policy = billing_policy  # type: GetQuotaResponseBodyBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.data = data  # type: GetQuotaResponseBodyData
        # quota ID
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.sale_tag = sale_tag  # type: GetQuotaResponseBodySaleTag
        self.schedule_info = schedule_info  # type: GetQuotaResponseBodyScheduleInfo
        self.status = status  # type: str
        self.sub_quota_info_list = sub_quota_info_list  # type: list[GetQuotaResponseBodySubQuotaInfoList]
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.data:
            self.data.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('data') is not None:
            temp_model = GetQuotaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodySaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaResponseBodySubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQuotaResponse, self).to_map()
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
            temp_model = GetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaPlanRequest(TeaModel):
    def __init__(self, region=None, tenant_id=None):
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaPlanResponseBodyDataQuotaBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaPlanResponseBodyDataQuotaBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaPlanResponseBodyDataQuotaScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaPlanResponseBodyDataQuotaScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, id=None, name=None,
                 nick_name=None, parameter=None, parent_id=None, region_id=None, schedule_info=None, status=None, tag=None,
                 tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.schedule_info = schedule_info  # type: GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo
        self.status = status  # type: str
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaPlanResponseBodyDataQuota(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, id=None, name=None,
                 nick_name=None, parameter=None, parent_id=None, region_id=None, schedule_info=None, status=None,
                 sub_quota_info_list=None, tag=None, tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: GetQuotaPlanResponseBodyDataQuotaBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        # quota ID
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.schedule_info = schedule_info  # type: GetQuotaPlanResponseBodyDataQuotaScheduleInfo
        self.status = status  # type: str
        self.sub_quota_info_list = sub_quota_info_list  # type: list[GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList]
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQuotaPlanResponseBodyDataQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaPlanResponseBodyData(TeaModel):
    def __init__(self, create_time=None, name=None, quota=None):
        self.create_time = create_time  # type: str
        self.name = name  # type: str
        self.quota = quota  # type: GetQuotaPlanResponseBodyDataQuota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(GetQuotaPlanResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class GetQuotaPlanResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetQuotaPlanResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQuotaPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetQuotaPlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetQuotaPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQuotaPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQuotaPlanResponse, self).to_map()
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
            temp_model = GetQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaScheduleRequest(TeaModel):
    def __init__(self, region=None, tenant_id=None):
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaScheduleResponseBodyDataCondition(TeaModel):
    def __init__(self, after=None, at=None):
        self.after = after  # type: str
        self.at = at  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuotaScheduleResponseBodyDataCondition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['after'] = self.after
        if self.at is not None:
            result['at'] = self.at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('after') is not None:
            self.after = m.get('after')
        if m.get('at') is not None:
            self.at = m.get('at')
        return self


class GetQuotaScheduleResponseBodyData(TeaModel):
    def __init__(self, condition=None, id=None, operator=None, plan=None, type=None):
        self.condition = condition  # type: GetQuotaScheduleResponseBodyDataCondition
        self.id = id  # type: str
        self.operator = operator  # type: str
        self.plan = plan  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        _map = super(GetQuotaScheduleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.operator is not None:
            result['operator'] = self.operator
        if self.plan is not None:
            result['plan'] = self.plan
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('condition') is not None:
            temp_model = GetQuotaScheduleResponseBodyDataCondition()
            self.condition = temp_model.from_map(m['condition'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('plan') is not None:
            self.plan = m.get('plan')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetQuotaScheduleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[GetQuotaScheduleResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQuotaScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetQuotaScheduleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetQuotaScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQuotaScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQuotaScheduleResponse, self).to_map()
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
            temp_model = GetQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleAclResponseBodyDataFunction(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleAclResponseBodyDataFunction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRoleAclResponseBodyDataInstance(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleAclResponseBodyDataInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRoleAclResponseBodyDataPackage(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleAclResponseBodyDataPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRoleAclResponseBodyDataProject(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleAclResponseBodyDataProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRoleAclResponseBodyDataResource(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleAclResponseBodyDataResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRoleAclResponseBodyDataTable(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleAclResponseBodyDataTable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRoleAclResponseBodyData(TeaModel):
    def __init__(self, function=None, instance=None, package=None, project=None, resource=None, table=None):
        self.function = function  # type: list[GetRoleAclResponseBodyDataFunction]
        self.instance = instance  # type: list[GetRoleAclResponseBodyDataInstance]
        # Package
        self.package = package  # type: list[GetRoleAclResponseBodyDataPackage]
        self.project = project  # type: list[GetRoleAclResponseBodyDataProject]
        self.resource = resource  # type: list[GetRoleAclResponseBodyDataResource]
        self.table = table  # type: list[GetRoleAclResponseBodyDataTable]

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()
        if self.package:
            for k in self.package:
                if k:
                    k.validate()
        if self.project:
            for k in self.project:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRoleAclResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['instance'].append(k.to_map() if k else None)
        result['package'] = []
        if self.package is not None:
            for k in self.package:
                result['package'].append(k.to_map() if k else None)
        result['project'] = []
        if self.project is not None:
            for k in self.project:
                result['project'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = GetRoleAclResponseBodyDataFunction()
                self.function.append(temp_model.from_map(k))
        self.instance = []
        if m.get('instance') is not None:
            for k in m.get('instance'):
                temp_model = GetRoleAclResponseBodyDataInstance()
                self.instance.append(temp_model.from_map(k))
        self.package = []
        if m.get('package') is not None:
            for k in m.get('package'):
                temp_model = GetRoleAclResponseBodyDataPackage()
                self.package.append(temp_model.from_map(k))
        self.project = []
        if m.get('project') is not None:
            for k in m.get('project'):
                temp_model = GetRoleAclResponseBodyDataProject()
                self.project.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = GetRoleAclResponseBodyDataResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = GetRoleAclResponseBodyDataTable()
                self.table.append(temp_model.from_map(k))
        return self


class GetRoleAclResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetRoleAclResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRoleAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRoleAclResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRoleAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRoleAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRoleAclResponse, self).to_map()
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
            temp_model = GetRoleAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleAclOnObjectRequest(TeaModel):
    def __init__(self, object_name=None, object_type=None):
        self.object_name = object_name  # type: str
        self.object_type = object_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleAclOnObjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_name is not None:
            result['objectName'] = self.object_name
        if self.object_type is not None:
            result['objectType'] = self.object_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        return self


class GetRoleAclOnObjectResponseBodyData(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleAclOnObjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRoleAclOnObjectResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetRoleAclOnObjectResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRoleAclOnObjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRoleAclOnObjectResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRoleAclOnObjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRoleAclOnObjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRoleAclOnObjectResponse, self).to_map()
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
            temp_model = GetRoleAclOnObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRolePolicyResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRolePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRolePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRolePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRolePolicyResponse, self).to_map()
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
            temp_model = GetRolePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrustedProjectsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrustedProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetTrustedProjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTrustedProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTrustedProjectsResponse, self).to_map()
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
            temp_model = GetTrustedProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(self, marker=None, max_item=None, prefix=None):
        self.marker = marker  # type: str
        self.max_item = max_item  # type: int
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListFunctionsResponseBodyDataFunctions(TeaModel):
    def __init__(self, class_=None, creation_time=None, name=None, owner=None, resources=None, schema=None):
        self.class_ = class_  # type: str
        self.creation_time = creation_time  # type: long
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.resources = resources  # type: str
        self.schema = schema  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionsResponseBodyDataFunctions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['class'] = self.class_
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.resources is not None:
            result['resources'] = self.resources
        if self.schema is not None:
            result['schema'] = self.schema
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        return self


class ListFunctionsResponseBodyData(TeaModel):
    def __init__(self, functions=None, marker=None, max_item=None):
        self.functions = functions  # type: list[ListFunctionsResponseBodyDataFunctions]
        self.marker = marker  # type: str
        self.max_item = max_item  # type: int

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['functions'].append(k.to_map() if k else None)
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k in m.get('functions'):
                temp_model = ListFunctionsResponseBodyDataFunctions()
                self.functions.append(temp_model.from_map(k))
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        return self


class ListFunctionsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListFunctionsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListFunctionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListFunctionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionsResponse, self).to_map()
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
            temp_model = ListFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPackagesResponseBodyDataCreatedPackages(TeaModel):
    def __init__(self, create_time=None, name=None):
        self.create_time = create_time  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPackagesResponseBodyDataCreatedPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListPackagesResponseBodyDataInstalledPackages(TeaModel):
    def __init__(self, install_time=None, name=None, source_project=None, status=None):
        self.install_time = install_time  # type: long
        self.name = name  # type: str
        self.source_project = source_project  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPackagesResponseBodyDataInstalledPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.install_time is not None:
            result['installTime'] = self.install_time
        if self.name is not None:
            result['name'] = self.name
        if self.source_project is not None:
            result['sourceProject'] = self.source_project
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('installTime') is not None:
            self.install_time = m.get('installTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceProject') is not None:
            self.source_project = m.get('sourceProject')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListPackagesResponseBodyData(TeaModel):
    def __init__(self, created_packages=None, installed_packages=None):
        self.created_packages = created_packages  # type: list[ListPackagesResponseBodyDataCreatedPackages]
        self.installed_packages = installed_packages  # type: list[ListPackagesResponseBodyDataInstalledPackages]

    def validate(self):
        if self.created_packages:
            for k in self.created_packages:
                if k:
                    k.validate()
        if self.installed_packages:
            for k in self.installed_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPackagesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['createdPackages'] = []
        if self.created_packages is not None:
            for k in self.created_packages:
                result['createdPackages'].append(k.to_map() if k else None)
        result['installedPackages'] = []
        if self.installed_packages is not None:
            for k in self.installed_packages:
                result['installedPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.created_packages = []
        if m.get('createdPackages') is not None:
            for k in m.get('createdPackages'):
                temp_model = ListPackagesResponseBodyDataCreatedPackages()
                self.created_packages.append(temp_model.from_map(k))
        self.installed_packages = []
        if m.get('installedPackages') is not None:
            for k in m.get('installedPackages'):
                temp_model = ListPackagesResponseBodyDataInstalledPackages()
                self.installed_packages.append(temp_model.from_map(k))
        return self


class ListPackagesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListPackagesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListPackagesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListPackagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPackagesResponse, self).to_map()
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
            temp_model = ListPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectUsersResponseBodyDataUsers(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectUsersResponseBodyDataUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListProjectUsersResponseBodyData(TeaModel):
    def __init__(self, users=None):
        self.users = users  # type: list[ListProjectUsersResponseBodyDataUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectUsersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListProjectUsersResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListProjectUsersResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListProjectUsersResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProjectUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProjectUsersResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectUsersResponse, self).to_map()
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
            temp_model = ListProjectUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, marker=None, max_item=None, prefix=None, quota_name=None, quota_nick_name=None, region=None,
                 sale_tags=None, tenant_id=None):
        self.marker = marker  # type: str
        self.max_item = max_item  # type: int
        self.prefix = prefix  # type: str
        self.quota_name = quota_name  # type: str
        self.quota_nick_name = quota_nick_name  # type: str
        self.region = region  # type: str
        self.sale_tags = sale_tags  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.quota_name is not None:
            result['quotaName'] = self.quota_name
        if self.quota_nick_name is not None:
            result['quotaNickName'] = self.quota_nick_name
        if self.region is not None:
            result['region'] = self.region
        if self.sale_tags is not None:
            result['saleTags'] = self.sale_tags
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('quotaName') is not None:
            self.quota_name = m.get('quotaName')
        if m.get('quotaNickName') is not None:
            self.quota_nick_name = m.get('quotaNickName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('saleTags') is not None:
            self.sale_tags = m.get('saleTags')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListProjectsResponseBodyDataProjectsTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjectsTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListProjectsResponseBodyDataProjectsIpWhiteList(TeaModel):
    def __init__(self, ip_list=None, vpc_ip_list=None):
        self.ip_list = ip_list  # type: str
        self.vpc_ip_list = vpc_ip_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjectsIpWhiteList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.vpc_ip_list is not None:
            result['vpcIpList'] = self.vpc_ip_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('vpcIpList') is not None:
            self.vpc_ip_list = m.get('vpcIpList')
        return self


class ListProjectsResponseBodyDataProjectsPropertiesEncryption(TeaModel):
    def __init__(self, algorithm=None, enable=None, key=None):
        self.algorithm = algorithm  # type: str
        self.enable = enable  # type: bool
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjectsPropertiesEncryption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.enable is not None:
            result['enable'] = self.enable
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListProjectsResponseBodyDataProjectsProperties(TeaModel):
    def __init__(self, allow_full_scan=None, elder_tunnel_quota=None, enable_decimal_2=None,
                 enable_tunnel_quota_route=None, encryption=None, retention_days=None, sql_metering_max=None, table_lifecycle=None,
                 timezone=None, tunnel_quota=None, type_system=None):
        self.allow_full_scan = allow_full_scan  # type: bool
        self.elder_tunnel_quota = elder_tunnel_quota  # type: str
        self.enable_decimal_2 = enable_decimal_2  # type: bool
        self.enable_tunnel_quota_route = enable_tunnel_quota_route  # type: bool
        self.encryption = encryption  # type: ListProjectsResponseBodyDataProjectsPropertiesEncryption
        self.retention_days = retention_days  # type: long
        self.sql_metering_max = sql_metering_max  # type: str
        self.table_lifecycle = table_lifecycle  # type: ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle
        self.timezone = timezone  # type: str
        self.tunnel_quota = tunnel_quota  # type: str
        self.type_system = type_system  # type: str

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjectsProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan
        if self.elder_tunnel_quota is not None:
            result['elderTunnelQuota'] = self.elder_tunnel_quota
        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2
        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route
        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max
        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        if self.type_system is not None:
            result['typeSystem'] = self.type_system
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')
        if m.get('elderTunnelQuota') is not None:
            self.elder_tunnel_quota = m.get('elderTunnelQuota')
        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')
        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')
        if m.get('encryption') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsPropertiesEncryption()
            self.encryption = temp_model.from_map(m['encryption'])
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')
        if m.get('tableLifecycle') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m['tableLifecycle'])
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')
        return self


class ListProjectsResponseBodyDataProjectsSaleTag(TeaModel):
    def __init__(self, resource_id=None, resource_type=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjectsSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection(TeaModel):
    def __init__(self, exception_policy=None, protected=None):
        self.exception_policy = exception_policy  # type: str
        self.protected = protected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_policy is not None:
            result['exceptionPolicy'] = self.exception_policy
        if self.protected is not None:
            result['protected'] = self.protected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exceptionPolicy') is not None:
            self.exception_policy = m.get('exceptionPolicy')
        if m.get('protected') is not None:
            self.protected = m.get('protected')
        return self


class ListProjectsResponseBodyDataProjectsSecurityProperties(TeaModel):
    def __init__(self, enable_download_privilege=None, label_security=None,
                 object_creator_has_access_permission=None, object_creator_has_grant_permission=None, project_protection=None, using_acl=None,
                 using_policy=None):
        self.enable_download_privilege = enable_download_privilege  # type: bool
        self.label_security = label_security  # type: bool
        self.object_creator_has_access_permission = object_creator_has_access_permission  # type: bool
        self.object_creator_has_grant_permission = object_creator_has_grant_permission  # type: bool
        self.project_protection = project_protection  # type: ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection
        self.using_acl = using_acl  # type: bool
        self.using_policy = using_policy  # type: bool

    def validate(self):
        if self.project_protection:
            self.project_protection.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjectsSecurityProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_download_privilege is not None:
            result['enableDownloadPrivilege'] = self.enable_download_privilege
        if self.label_security is not None:
            result['labelSecurity'] = self.label_security
        if self.object_creator_has_access_permission is not None:
            result['objectCreatorHasAccessPermission'] = self.object_creator_has_access_permission
        if self.object_creator_has_grant_permission is not None:
            result['objectCreatorHasGrantPermission'] = self.object_creator_has_grant_permission
        if self.project_protection is not None:
            result['projectProtection'] = self.project_protection.to_map()
        if self.using_acl is not None:
            result['usingAcl'] = self.using_acl
        if self.using_policy is not None:
            result['usingPolicy'] = self.using_policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableDownloadPrivilege') is not None:
            self.enable_download_privilege = m.get('enableDownloadPrivilege')
        if m.get('labelSecurity') is not None:
            self.label_security = m.get('labelSecurity')
        if m.get('objectCreatorHasAccessPermission') is not None:
            self.object_creator_has_access_permission = m.get('objectCreatorHasAccessPermission')
        if m.get('objectCreatorHasGrantPermission') is not None:
            self.object_creator_has_grant_permission = m.get('objectCreatorHasGrantPermission')
        if m.get('projectProtection') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection()
            self.project_protection = temp_model.from_map(m['projectProtection'])
        if m.get('usingAcl') is not None:
            self.using_acl = m.get('usingAcl')
        if m.get('usingPolicy') is not None:
            self.using_policy = m.get('usingPolicy')
        return self


class ListProjectsResponseBodyDataProjects(TeaModel):
    def __init__(self, tags=None, comment=None, cost_storage=None, default_quota=None, ip_white_list=None, name=None,
                 owner=None, properties=None, sale_tag=None, security_properties=None, status=None, type=None):
        self.tags = tags  # type: list[ListProjectsResponseBodyDataProjectsTags]
        self.comment = comment  # type: str
        self.cost_storage = cost_storage  # type: str
        self.default_quota = default_quota  # type: str
        self.ip_white_list = ip_white_list  # type: ListProjectsResponseBodyDataProjectsIpWhiteList
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.properties = properties  # type: ListProjectsResponseBodyDataProjectsProperties
        self.sale_tag = sale_tag  # type: ListProjectsResponseBodyDataProjectsSaleTag
        self.security_properties = security_properties  # type: ListProjectsResponseBodyDataProjectsSecurityProperties
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ip_white_list:
            self.ip_white_list.validate()
        if self.properties:
            self.properties.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.security_properties:
            self.security_properties.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBodyDataProjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.comment is not None:
            result['comment'] = self.comment
        if self.cost_storage is not None:
            result['costStorage'] = self.cost_storage
        if self.default_quota is not None:
            result['defaultQuota'] = self.default_quota
        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.properties is not None:
            result['properties'] = self.properties.to_map()
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.security_properties is not None:
            result['securityProperties'] = self.security_properties.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListProjectsResponseBodyDataProjectsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('costStorage') is not None:
            self.cost_storage = m.get('costStorage')
        if m.get('defaultQuota') is not None:
            self.default_quota = m.get('defaultQuota')
        if m.get('ipWhiteList') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsIpWhiteList()
            self.ip_white_list = temp_model.from_map(m['ipWhiteList'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('properties') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsProperties()
            self.properties = temp_model.from_map(m['properties'])
        if m.get('saleTag') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('securityProperties') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSecurityProperties()
            self.security_properties = temp_model.from_map(m['securityProperties'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListProjectsResponseBodyData(TeaModel):
    def __init__(self, next_token=None, marker=None, max_item=None, projects=None):
        self.next_token = next_token  # type: str
        self.marker = marker  # type: str
        self.max_item = max_item  # type: int
        self.projects = projects  # type: list[ListProjectsResponseBodyDataProjects]

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = ListProjectsResponseBodyDataProjects()
                self.projects.append(temp_model.from_map(k))
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListProjectsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProjectsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectsResponse, self).to_map()
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasRequest(TeaModel):
    def __init__(self, billing_type=None, marker=None, max_item=None, product_id=None, region=None, sale_tags=None,
                 tenant_id=None):
        self.billing_type = billing_type  # type: str
        self.marker = marker  # type: str
        self.max_item = max_item  # type: long
        self.product_id = product_id  # type: str
        self.region = region  # type: str
        self.sale_tags = sale_tags  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_type is not None:
            result['billingType'] = self.billing_type
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.region is not None:
            result['region'] = self.region
        if self.sale_tags is not None:
            result['saleTags'] = self.sale_tags
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingType') is not None:
            self.billing_type = m.get('billingType')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('saleTags') is not None:
            self.sale_tags = m.get('saleTags')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoListTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListQuotasResponseBodyDataQuotaInfoListBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoListBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSaleTag(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None):
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoListSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyDataQuotaInfoListScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None):
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, group_name=None,
                 id=None, name=None, nick_name=None, parameter=None, parent_id=None, region_id=None, sale_tag=None,
                 schedule_info=None, status=None, tag=None, tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.group_name = group_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.sale_tag = sale_tag  # type: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag
        self.schedule_info = schedule_info  # type: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo
        self.status = status  # type: str
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyDataQuotaInfoList(TeaModel):
    def __init__(self, tags=None, billing_policy=None, cluster=None, create_time=None, creator_id=None,
                 group_name=None, id=None, name=None, nick_name=None, parameter=None, parent_id=None, region_id=None,
                 sale_tag=None, schedule_info=None, status=None, sub_quota_info_list=None, tag=None, tenant_id=None,
                 type=None, version=None):
        self.tags = tags  # type: list[ListQuotasResponseBodyDataQuotaInfoListTags]
        self.billing_policy = billing_policy  # type: ListQuotasResponseBodyDataQuotaInfoListBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.group_name = group_name  # type: str
        # quota id
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.sale_tag = sale_tag  # type: ListQuotasResponseBodyDataQuotaInfoListSaleTag
        self.schedule_info = schedule_info  # type: ListQuotasResponseBodyDataQuotaInfoListScheduleInfo
        self.status = status  # type: str
        self.sub_quota_info_list = sub_quota_info_list  # type: list[ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList]
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotasResponseBodyDataQuotaInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyData(TeaModel):
    def __init__(self, next_token=None, marker=None, max_item=None, quota_info_list=None):
        self.next_token = next_token  # type: str
        self.marker = marker  # type: str
        self.max_item = max_item  # type: long
        self.quota_info_list = quota_info_list  # type: list[ListQuotasResponseBodyDataQuotaInfoList]

    def validate(self):
        if self.quota_info_list:
            for k in self.quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotasResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['quotaInfoList'] = []
        if self.quota_info_list is not None:
            for k in self.quota_info_list:
                result['quotaInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.quota_info_list = []
        if m.get('quotaInfoList') is not None:
            for k in m.get('quotaInfoList'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoList()
                self.quota_info_list.append(temp_model.from_map(k))
        return self


class ListQuotasResponseBodyQuotaInfoListTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoListTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListQuotasResponseBodyQuotaInfoListBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoListBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyQuotaInfoListSaleTag(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None):
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoListSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyQuotaInfoListScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None):
        self.resource_ids = resource_ids  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, group_name=None,
                 id=None, name=None, nick_name=None, parameter=None, parent_id=None, region_id=None, sale_tag=None,
                 schedule_info=None, status=None, tag=None, tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.group_name = group_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.sale_tag = sale_tag  # type: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag
        self.schedule_info = schedule_info  # type: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo
        self.status = status  # type: str
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyQuotaInfoList(TeaModel):
    def __init__(self, tags=None, billing_policy=None, cluster=None, create_time=None, creator_id=None,
                 group_name=None, id=None, name=None, nick_name=None, parameter=None, parent_id=None, region_id=None,
                 sale_tag=None, schedule_info=None, status=None, sub_quota_info_list=None, tag=None, tenant_id=None,
                 type=None, version=None):
        self.tags = tags  # type: list[ListQuotasResponseBodyQuotaInfoListTags]
        self.billing_policy = billing_policy  # type: ListQuotasResponseBodyQuotaInfoListBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.group_name = group_name  # type: str
        # quota ID
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.sale_tag = sale_tag  # type: ListQuotasResponseBodyQuotaInfoListSaleTag
        self.schedule_info = schedule_info  # type: ListQuotasResponseBodyQuotaInfoListScheduleInfo
        self.status = status  # type: str
        self.sub_quota_info_list = sub_quota_info_list  # type: list[ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList]
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotasResponseBodyQuotaInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListQuotasResponseBodyQuotaInfoListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBody(TeaModel):
    def __init__(self, next_token=None, data=None, marker=None, max_item=None, quota_info_list=None, request_id=None):
        self.next_token = next_token  # type: str
        self.data = data  # type: ListQuotasResponseBodyData
        self.marker = marker  # type: str
        self.max_item = max_item  # type: long
        self.quota_info_list = quota_info_list  # type: list[ListQuotasResponseBodyQuotaInfoList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()
        if self.quota_info_list:
            for k in self.quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['quotaInfoList'] = []
        if self.quota_info_list is not None:
            for k in self.quota_info_list:
                result['quotaInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('data') is not None:
            temp_model = ListQuotasResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.quota_info_list = []
        if m.get('quotaInfoList') is not None:
            for k in m.get('quotaInfoList'):
                temp_model = ListQuotasResponseBodyQuotaInfoList()
                self.quota_info_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQuotasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQuotasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQuotasResponse, self).to_map()
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
            temp_model = ListQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasPlansRequest(TeaModel):
    def __init__(self, region=None, tenant_id=None):
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(self, billing_method=None, odps_spec_code=None, order_id=None):
        self.billing_method = billing_method  # type: str
        self.odps_spec_code = odps_spec_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(self, curr_plan=None, curr_time=None, next_plan=None, next_time=None, once_plan=None,
                 once_time=None, operator_name=None):
        self.curr_plan = curr_plan  # type: str
        self.curr_time = curr_time  # type: str
        self.next_plan = next_plan  # type: str
        self.next_time = next_time  # type: str
        self.once_plan = once_plan  # type: str
        self.once_time = once_time  # type: str
        self.operator_name = operator_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, id=None, name=None,
                 nick_name=None, parameter=None, parent_id=None, region_id=None, schedule_info=None, status=None, tag=None,
                 tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.schedule_info = schedule_info  # type: ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo
        self.status = status  # type: str
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super(ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuota(TeaModel):
    def __init__(self, billing_policy=None, cluster=None, create_time=None, creator_id=None, id=None, name=None,
                 nick_name=None, parameter=None, parent_id=None, region_id=None, schedule_info=None, status=None,
                 sub_quota_info_list=None, tag=None, tenant_id=None, type=None, version=None):
        self.billing_policy = billing_policy  # type: ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy
        self.cluster = cluster  # type: str
        self.create_time = create_time  # type: long
        self.creator_id = creator_id  # type: str
        # quota ID
        self.id = id  # type: str
        self.name = name  # type: str
        self.nick_name = nick_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.schedule_info = schedule_info  # type: ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo
        self.status = status  # type: str
        self.sub_quota_info_list = sub_quota_info_list  # type: list[ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList]
        self.tag = tag  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotasPlansResponseBodyDataPlanListQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasPlansResponseBodyDataPlanList(TeaModel):
    def __init__(self, create_time=None, name=None, quota=None):
        self.create_time = create_time  # type: str
        self.name = name  # type: str
        self.quota = quota  # type: ListQuotasPlansResponseBodyDataPlanListQuota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(ListQuotasPlansResponseBodyDataPlanList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class ListQuotasPlansResponseBodyData(TeaModel):
    def __init__(self, plan_list=None):
        self.plan_list = plan_list  # type: list[ListQuotasPlansResponseBodyDataPlanList]

    def validate(self):
        if self.plan_list:
            for k in self.plan_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotasPlansResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['planList'] = []
        if self.plan_list is not None:
            for k in self.plan_list:
                result['planList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.plan_list = []
        if m.get('planList') is not None:
            for k in m.get('planList'):
                temp_model = ListQuotasPlansResponseBodyDataPlanList()
                self.plan_list.append(temp_model.from_map(k))
        return self


class ListQuotasPlansResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListQuotasPlansResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListQuotasPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListQuotasPlansResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQuotasPlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQuotasPlansResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQuotasPlansResponse, self).to_map()
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
            temp_model = ListQuotasPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(self, marker=None, max_item=None, name=None):
        self.marker = marker  # type: str
        self.max_item = max_item  # type: int
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListResourcesResponseBodyDataResources(TeaModel):
    def __init__(self, creation_time=None, name=None, owner=None, schema=None, type=None):
        self.creation_time = creation_time  # type: long
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.schema = schema  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesResponseBodyDataResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.schema is not None:
            result['schema'] = self.schema
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListResourcesResponseBodyData(TeaModel):
    def __init__(self, marker=None, max_item=None, resources=None):
        self.marker = marker  # type: str
        self.max_item = max_item  # type: int
        self.resources = resources  # type: list[ListResourcesResponseBodyDataResources]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ListResourcesResponseBodyDataResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListResourcesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListResourcesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourcesResponse, self).to_map()
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
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesResponseBodyDataRolesAclFunction(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRolesAclFunction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclInstance(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRolesAclInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclPackage(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRolesAclPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclProject(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRolesAclProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclResource(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRolesAclResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclTable(TeaModel):
    def __init__(self, actions=None, name=None):
        self.actions = actions  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRolesAclTable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAcl(TeaModel):
    def __init__(self, function=None, instance=None, package=None, project=None, resource=None, table=None):
        self.function = function  # type: list[ListRolesResponseBodyDataRolesAclFunction]
        self.instance = instance  # type: list[ListRolesResponseBodyDataRolesAclInstance]
        # Package
        self.package = package  # type: list[ListRolesResponseBodyDataRolesAclPackage]
        self.project = project  # type: list[ListRolesResponseBodyDataRolesAclProject]
        self.resource = resource  # type: list[ListRolesResponseBodyDataRolesAclResource]
        self.table = table  # type: list[ListRolesResponseBodyDataRolesAclTable]

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()
        if self.package:
            for k in self.package:
                if k:
                    k.validate()
        if self.project:
            for k in self.project:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRolesAcl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['instance'].append(k.to_map() if k else None)
        result['package'] = []
        if self.package is not None:
            for k in self.package:
                result['package'].append(k.to_map() if k else None)
        result['project'] = []
        if self.project is not None:
            for k in self.project:
                result['project'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = ListRolesResponseBodyDataRolesAclFunction()
                self.function.append(temp_model.from_map(k))
        self.instance = []
        if m.get('instance') is not None:
            for k in m.get('instance'):
                temp_model = ListRolesResponseBodyDataRolesAclInstance()
                self.instance.append(temp_model.from_map(k))
        self.package = []
        if m.get('package') is not None:
            for k in m.get('package'):
                temp_model = ListRolesResponseBodyDataRolesAclPackage()
                self.package.append(temp_model.from_map(k))
        self.project = []
        if m.get('project') is not None:
            for k in m.get('project'):
                temp_model = ListRolesResponseBodyDataRolesAclProject()
                self.project.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = ListRolesResponseBodyDataRolesAclResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = ListRolesResponseBodyDataRolesAclTable()
                self.table.append(temp_model.from_map(k))
        return self


class ListRolesResponseBodyDataRoles(TeaModel):
    def __init__(self, acl=None, name=None, policy=None, type=None):
        self.acl = acl  # type: ListRolesResponseBodyDataRolesAcl
        self.name = name  # type: str
        self.policy = policy  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        _map = super(ListRolesResponseBodyDataRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.policy is not None:
            result['policy'] = self.policy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('acl') is not None:
            temp_model = ListRolesResponseBodyDataRolesAcl()
            self.acl = temp_model.from_map(m['acl'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListRolesResponseBodyData(TeaModel):
    def __init__(self, roles=None):
        self.roles = roles  # type: list[ListRolesResponseBodyDataRoles]

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRolesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = ListRolesResponseBodyDataRoles()
                self.roles.append(temp_model.from_map(k))
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListRolesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListRolesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListRolesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListRolesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRolesResponse, self).to_map()
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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablesRequest(TeaModel):
    def __init__(self, marker=None, max_item=None, prefix=None, type=None):
        self.marker = marker  # type: str
        self.max_item = max_item  # type: int
        self.prefix = prefix  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTablesResponseBodyDataTables(TeaModel):
    def __init__(self, creation_time=None, name=None, owner=None, schema=None, type=None):
        self.creation_time = creation_time  # type: long
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.schema = schema  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTablesResponseBodyDataTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.schema is not None:
            result['schema'] = self.schema
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTablesResponseBodyData(TeaModel):
    def __init__(self, marker=None, max_item=None, tables=None):
        self.marker = marker  # type: str
        self.max_item = max_item  # type: int
        self.tables = tables  # type: list[ListTablesResponseBodyDataTables]

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTablesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.tables = []
        if m.get('tables') is not None:
            for k in m.get('tables'):
                temp_model = ListTablesResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        return self


class ListTablesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListTablesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListTablesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListTablesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTablesResponse, self).to_map()
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
            temp_model = ListTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListUsersResponseBodyDataUsers(TeaModel):
    def __init__(self, account_id=None, account_name=None, account_type=None, display_name=None, tenant_id=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.account_type = account_type  # type: str
        self.display_name = display_name  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyDataUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, users=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.users = users  # type: list[ListUsersResponseBodyDataUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListUsersResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListUsersResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersResponse, self).to_map()
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersByRoleResponseBodyDataUsers(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersByRoleResponseBodyDataUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListUsersByRoleResponseBodyData(TeaModel):
    def __init__(self, users=None):
        self.users = users  # type: list[ListUsersByRoleResponseBodyDataUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersByRoleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListUsersByRoleResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersByRoleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListUsersByRoleResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListUsersByRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListUsersByRoleResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUsersByRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersByRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersByRoleResponse, self).to_map()
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
            temp_model = ListUsersByRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePackageRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdatePackageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePackageResponse, self).to_map()
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
            temp_model = UpdatePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectIpWhiteListRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectIpWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateProjectIpWhiteListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectIpWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProjectIpWhiteListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProjectIpWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProjectIpWhiteListResponse, self).to_map()
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
            temp_model = UpdateProjectIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaHeaders(TeaModel):
    def __init__(self, common_headers=None, ak_proven=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.ak_proven = ak_proven  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.ak_proven is not None:
            result['AkProven'] = self.ak_proven
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AkProven') is not None:
            self.ak_proven = m.get('AkProven')
        return self


class UpdateQuotaRequest(TeaModel):
    def __init__(self, body=None, region=None, tenant_id=None):
        self.body = body  # type: str
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateQuotaResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateQuotaResponse, self).to_map()
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
            temp_model = UpdateQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaPlanRequest(TeaModel):
    def __init__(self, body=None, region=None, tenant_id=None):
        self.body = body  # type: str
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateQuotaPlanResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQuotaPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateQuotaPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateQuotaPlanResponse, self).to_map()
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
            temp_model = UpdateQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaScheduleRequest(TeaModel):
    def __init__(self, body=None, region=None, tenant_id=None):
        self.body = body  # type: str
        self.region = region  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateQuotaScheduleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQuotaScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateQuotaScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateQuotaScheduleResponse, self).to_map()
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
            temp_model = UpdateQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


