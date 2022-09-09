# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class JobStatusDetailValue(TeaModel):
    def __init__(self, comment=None, time_stamps=None, job_result=None):
        self.comment = comment  # type: str
        self.time_stamps = time_stamps  # type: str
        self.job_result = job_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobStatusDetailValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.time_stamps is not None:
            result['timeStamps'] = self.time_stamps
        if self.job_result is not None:
            result['jobResult'] = self.job_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('timeStamps') is not None:
            self.time_stamps = m.get('timeStamps')
        if m.get('jobResult') is not None:
            self.job_result = m.get('jobResult')
        return self


class ProjectBuildConfigTaskPoliciesValue(TeaModel):
    def __init__(self, task_id=None, priority=None, destroy_after_execution=None):
        self.task_id = task_id  # type: str
        self.priority = priority  # type: long
        self.destroy_after_execution = destroy_after_execution  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProjectBuildConfigTaskPoliciesValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.priority is not None:
            result['priority'] = self.priority
        if self.destroy_after_execution is not None:
            result['destroyAfterExecution'] = self.destroy_after_execution
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('destroyAfterExecution') is not None:
            self.destroy_after_execution = m.get('destroyAfterExecution')
        return self


class JobsStatusDetailValue(TeaModel):
    def __init__(self, comment=None, time_stamps=None, job_result=None):
        self.comment = comment  # type: str
        self.time_stamps = time_stamps  # type: str
        self.job_result = job_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobsStatusDetailValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.time_stamps is not None:
            result['timeStamps'] = self.time_stamps
        if self.job_result is not None:
            result['jobResult'] = self.job_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('timeStamps') is not None:
            self.time_stamps = m.get('timeStamps')
        if m.get('jobResult') is not None:
            self.job_result = m.get('jobResult')
        return self


class AssociateParameterSetRequest(TeaModel):
    def __init__(self, parameter_set_ids=None, resource_id=None, resource_type=None):
        self.parameter_set_ids = parameter_set_ids  # type: list[str]
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateParameterSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_set_ids is not None:
            result['parameterSetIds'] = self.parameter_set_ids
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('parameterSetIds') is not None:
            self.parameter_set_ids = m.get('parameterSetIds')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class AssociateParameterSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateParameterSetResponseBody, self).to_map()
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


class AssociateParameterSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateParameterSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateParameterSetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateTaskGroupRequest(TeaModel):
    def __init__(self, task_ids=None):
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateTaskGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class AssociateTaskGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateTaskGroupResponseBody, self).to_map()
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


class AssociateTaskGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateTaskGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateTaskGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateTaskGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachRabbitmqPublisherRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachRabbitmqPublisherRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class AttachRabbitmqPublisherResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachRabbitmqPublisherResponseBody, self).to_map()
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


class AttachRabbitmqPublisherResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachRabbitmqPublisherResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachRabbitmqPublisherResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelResourceExportTaskRequest(TeaModel):
    def __init__(self, client_token=None, ram_role=None):
        self.client_token = client_token  # type: str
        self.ram_role = ram_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelResourceExportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        return self


class CancelResourceExportTaskResponseBody(TeaModel):
    def __init__(self, export_task_id=None, export_version=None, request_id=None):
        self.export_task_id = export_task_id  # type: str
        self.export_version = export_version  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelResourceExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelResourceExportTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelResourceExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelResourceExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneModuleRequest(TeaModel):
    def __init__(self, description=None, module_id=None, module_source=None, module_version=None, name=None):
        self.description = description  # type: str
        self.module_id = module_id  # type: str
        self.module_source = module_source  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneModuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_source is not None:
            result['moduleSource'] = self.module_source
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleSource') is not None:
            self.module_source = m.get('moduleSource')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CloneModuleResponseBody(TeaModel):
    def __init__(self, module_id=None, request_id=None):
        self.module_id = module_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneModuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CloneModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneModuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRequest(TeaModel):
    def __init__(self, client_token=None, due_time=None, module_id=None, module_version=None, name=None, uid=None):
        self.client_token = client_token  # type: str
        self.due_time = due_time  # type: str
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateAuthorizationResponseBody(TeaModel):
    def __init__(self, authorization_id=None, request_id=None):
        self.authorization_id = authorization_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_id is not None:
            result['authorizationId'] = self.authorization_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authorizationId') is not None:
            self.authorization_id = m.get('authorizationId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAuthorizationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None, project_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupResponseBody, self).to_map()
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


class CreateGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(self, client_token=None, description=None, sub_command=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.sub_command = sub_command  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.sub_command is not None:
            result['subCommand'] = self.sub_command
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None, source=None, source_path=None,
                 state_path=None, version_strategy=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str
        self.version_strategy = version_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class CreateModuleResponseBody(TeaModel):
    def __init__(self, module_id=None, request_id=None):
        self.module_id = module_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateModuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleMarketRequest(TeaModel):
    def __init__(self, client_token=None, code_url=None, description=None, module_detail=None, module_id=None,
                 module_version=None, name=None):
        self.client_token = client_token  # type: str
        self.code_url = code_url  # type: str
        self.description = description  # type: str
        self.module_detail = module_detail  # type: str
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModuleMarketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.code_url is not None:
            result['codeUrl'] = self.code_url
        if self.description is not None:
            result['description'] = self.description
        if self.module_detail is not None:
            result['moduleDetail'] = self.module_detail
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('codeUrl') is not None:
            self.code_url = m.get('codeUrl')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleDetail') is not None:
            self.module_detail = m.get('moduleDetail')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateModuleMarketResponseBody(TeaModel):
    def __init__(self, module_market_id=None, request_id=None):
        self.module_market_id = module_market_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModuleMarketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_market_id is not None:
            result['moduleMarketId'] = self.module_market_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('moduleMarketId') is not None:
            self.module_market_id = m.get('moduleMarketId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModuleMarketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateModuleMarketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModuleMarketResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleMarketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleVersionRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModuleVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateModuleVersionResponseBody(TeaModel):
    def __init__(self, module_version=None, request_id=None):
        self.module_version = module_version  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModuleVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModuleVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateModuleVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModuleVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParameterSetRequestParameters(TeaModel):
    def __init__(self, name=None, type=None, value=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParameterSetRequestParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateParameterSetRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None, parameters=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.parameters = parameters  # type: list[CreateParameterSetRequestParameters]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateParameterSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = CreateParameterSetRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class CreateParameterSetResponseBody(TeaModel):
    def __init__(self, parameter_set_id=None, request_id=None):
        self.parameter_set_id = parameter_set_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParameterSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateParameterSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateParameterSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateParameterSetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
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


class CreateProjectBuildRequestTaskPolicies(TeaModel):
    def __init__(self, destroy_after_execution=None, priority=None, task_id=None):
        self.destroy_after_execution = destroy_after_execution  # type: bool
        self.priority = priority  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectBuildRequestTaskPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destroy_after_execution is not None:
            result['destroyAfterExecution'] = self.destroy_after_execution
        if self.priority is not None:
            result['priority'] = self.priority
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('destroyAfterExecution') is not None:
            self.destroy_after_execution = m.get('destroyAfterExecution')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateProjectBuildRequest(TeaModel):
    def __init__(self, client_token=None, project_build_action=None, task_ids=None, task_policies=None):
        self.client_token = client_token  # type: str
        self.project_build_action = project_build_action  # type: str
        self.task_ids = task_ids  # type: list[str]
        self.task_policies = task_policies  # type: list[CreateProjectBuildRequestTaskPolicies]

    def validate(self):
        if self.task_policies:
            for k in self.task_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateProjectBuildRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.project_build_action is not None:
            result['projectBuildAction'] = self.project_build_action
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        result['taskPolicies'] = []
        if self.task_policies is not None:
            for k in self.task_policies:
                result['taskPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('projectBuildAction') is not None:
            self.project_build_action = m.get('projectBuildAction')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        self.task_policies = []
        if m.get('taskPolicies') is not None:
            for k in m.get('taskPolicies'):
                temp_model = CreateProjectBuildRequestTaskPolicies()
                self.task_policies.append(temp_model.from_map(k))
        return self


class CreateProjectBuildResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectBuildResponseBody, self).to_map()
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


class CreateProjectBuildResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProjectBuildResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectBuildResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProjectBuildResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRabbitmqPublisherRequest(TeaModel):
    def __init__(self, client_token=None, description=None, exchange_name=None, exchange_type=None, host_name=None,
                 name=None, password=None, port=None, user_name=None, virtual_host=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.exchange_name = exchange_name  # type: str
        self.exchange_type = exchange_type  # type: str
        self.host_name = host_name  # type: str
        self.name = name  # type: str
        self.password = password  # type: str
        self.port = port  # type: long
        self.user_name = user_name  # type: str
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRabbitmqPublisherRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.exchange_name is not None:
            result['exchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['exchangeType'] = self.exchange_type
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.name is not None:
            result['name'] = self.name
        if self.password is not None:
            result['password'] = self.password
        if self.port is not None:
            result['port'] = self.port
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.virtual_host is not None:
            result['virtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exchangeName') is not None:
            self.exchange_name = m.get('exchangeName')
        if m.get('exchangeType') is not None:
            self.exchange_type = m.get('exchangeType')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('virtualHost') is not None:
            self.virtual_host = m.get('virtualHost')
        return self


class CreateRabbitmqPublisherResponseBody(TeaModel):
    def __init__(self, publisher_id=None, request_id=None):
        self.publisher_id = publisher_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRabbitmqPublisherResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.publisher_id is not None:
            result['publisherId'] = self.publisher_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('publisherId') is not None:
            self.publisher_id = m.get('publisherId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRabbitmqPublisherResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRabbitmqPublisherResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRabbitmqPublisherResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceExportTaskRequestExcludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceExportTaskRequestExcludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateResourceExportTaskRequestExportToModule(TeaModel):
    def __init__(self, source=None, source_path=None, state_path=None):
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceExportTaskRequestExportToModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class CreateResourceExportTaskRequestIncludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceExportTaskRequestIncludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateResourceExportTaskRequestVariables(TeaModel):
    def __init__(self, properties=None, resource_type=None):
        self.properties = properties  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceExportTaskRequestVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class CreateResourceExportTaskRequest(TeaModel):
    def __init__(self, client_token=None, description=None, exclude_rules=None, export_to_module=None,
                 include_rules=None, name=None, ram_role=None, terraform_version=None, trigger_strategy=None, variables=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.exclude_rules = exclude_rules  # type: list[CreateResourceExportTaskRequestExcludeRules]
        self.export_to_module = export_to_module  # type: CreateResourceExportTaskRequestExportToModule
        self.include_rules = include_rules  # type: list[CreateResourceExportTaskRequestIncludeRules]
        self.name = name  # type: str
        self.ram_role = ram_role  # type: str
        self.terraform_version = terraform_version  # type: str
        self.trigger_strategy = trigger_strategy  # type: str
        self.variables = variables  # type: list[CreateResourceExportTaskRequestVariables]

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateResourceExportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = CreateResourceExportTaskRequestExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportToModule') is not None:
            temp_model = CreateResourceExportTaskRequestExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = CreateResourceExportTaskRequestIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = CreateResourceExportTaskRequestVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class CreateResourceExportTaskResponseBody(TeaModel):
    def __init__(self, export_task_id=None, export_version=None, request_id=None):
        self.export_task_id = export_task_id  # type: str
        self.export_version = export_version  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateResourceExportTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequestGroupInfo(TeaModel):
    def __init__(self, group_id=None, project_id=None):
        self.group_id = group_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskRequestGroupInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class CreateTaskRequest(TeaModel):
    def __init__(self, auto_apply=None, client_token=None, group_info=None, module_id=None, module_version=None,
                 name=None, parameters=None, protection_strategy=None, ram_role=None, terraform_version=None,
                 trigger_strategy=None):
        self.auto_apply = auto_apply  # type: bool
        self.client_token = client_token  # type: str
        self.group_info = group_info  # type: CreateTaskRequestGroupInfo
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.parameters = parameters  # type: dict[str, str]
        self.protection_strategy = protection_strategy  # type: list[str]
        self.ram_role = ram_role  # type: str
        self.terraform_version = terraform_version  # type: str
        self.trigger_strategy = trigger_strategy  # type: str

    def validate(self):
        if self.group_info:
            self.group_info.validate()

    def to_map(self):
        _map = super(CreateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('groupInfo') is not None:
            temp_model = CreateTaskRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class CreateTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthorizationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthorizationResponseBody, self).to_map()
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


class DeleteAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAuthorizationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupResponseBody, self).to_map()
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


class DeleteGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteModuleResponseBody, self).to_map()
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


class DeleteModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteModuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParameterSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParameterSetResponseBody, self).to_map()
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


class DeleteParameterSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteParameterSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteParameterSetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectResponseBody, self).to_map()
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


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRabbitmqPublisherResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRabbitmqPublisherResponseBody, self).to_map()
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


class DeleteRabbitmqPublisherResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRabbitmqPublisherResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRabbitmqPublisherResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceExportTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceExportTaskResponseBody, self).to_map()
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


class DeleteResourceExportTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceLinkRequest(TeaModel):
    def __init__(self, product_code=None, resource_type_code=None):
        self.product_code = product_code  # type: str
        self.resource_type_code = resource_type_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        return self


class DeleteResourceLinkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceLinkResponseBody, self).to_map()
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


class DeleteResourceLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceLinkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTaskResponseBody, self).to_map()
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


class DeleteTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachRabbitmqPublisherRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachRabbitmqPublisherRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DetachRabbitmqPublisherResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachRabbitmqPublisherResponseBody, self).to_map()
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


class DetachRabbitmqPublisherResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachRabbitmqPublisherResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachRabbitmqPublisherResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateParameterSetRequest(TeaModel):
    def __init__(self, parameter_set_ids=None, resource_id=None, resource_type=None):
        self.parameter_set_ids = parameter_set_ids  # type: list[str]
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateParameterSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_set_ids is not None:
            result['parameterSetIds'] = self.parameter_set_ids
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('parameterSetIds') is not None:
            self.parameter_set_ids = m.get('parameterSetIds')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class DissociateParameterSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateParameterSetResponseBody, self).to_map()
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


class DissociateParameterSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DissociateParameterSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateParameterSetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateTaskGroupRequest(TeaModel):
    def __init__(self, task_ids=None):
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateTaskGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class DissociateTaskGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateTaskGroupResponseBody, self).to_map()
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


class DissociateTaskGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DissociateTaskGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateTaskGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateTaskGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteResourceExportTaskRequest(TeaModel):
    def __init__(self, client_token=None, ram_role=None):
        self.client_token = client_token  # type: str
        self.ram_role = ram_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteResourceExportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        return self


class ExecuteResourceExportTaskResponseBody(TeaModel):
    def __init__(self, export_task_id=None, export_version=None, request_id=None):
        self.export_task_id = export_task_id  # type: str
        self.export_version = export_version  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteResourceExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExecuteResourceExportTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteResourceExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteResourceExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(self, create_time=None, description=None, id=None, name=None, project_id=None, task_cnt=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.project_id = project_id  # type: str
        self.task_cnt = task_cnt  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupResponseBodyGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(self, group=None, request_id=None):
        self.group = group  # type: GetGroupResponseBodyGroup
        self.request_id = request_id  # type: str

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super(GetGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('group') is not None:
            temp_model = GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['group'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobResponseBodyJobConfig(TeaModel):
    def __init__(self, auto_apply=None, is_destroy=None, module_version=None, resources_changed=None):
        self.auto_apply = auto_apply  # type: bool
        self.is_destroy = is_destroy  # type: bool
        self.module_version = module_version  # type: str
        self.resources_changed = resources_changed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyJobConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')
        return self


class GetJobResponseBodyJob(TeaModel):
    def __init__(self, config=None, create_time=None, description=None, job_id=None, output=None, parameters=None,
                 runtime_type=None, status=None, status_detail=None, task_id=None):
        self.config = config  # type: GetJobResponseBodyJobConfig
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.parameters = parameters  # type: dict[str, str]
        self.runtime_type = runtime_type  # type: str
        self.status = status  # type: str
        self.status_detail = status_detail  # type: dict[str, JobStatusDetailValue]
        self.task_id = task_id  # type: str

    def validate(self):
        if self.config:
            self.config.validate()
        if self.status_detail:
            for v in self.status_detail.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.output is not None:
            result['output'] = self.output
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.runtime_type is not None:
            result['runtimeType'] = self.runtime_type
        if self.status is not None:
            result['status'] = self.status
        result['statusDetail'] = {}
        if self.status_detail is not None:
            for k, v in self.status_detail.items():
                result['statusDetail'][k] = v.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = GetJobResponseBodyJobConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('runtimeType') is not None:
            self.runtime_type = m.get('runtimeType')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.status_detail = {}
        if m.get('statusDetail') is not None:
            for k, v in m.get('statusDetail').items():
                temp_model = JobStatusDetailValue()
                self.status_detail[k] = temp_model.from_map(v)
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(self, job=None, request_id=None):
        self.job = job  # type: GetJobResponseBodyJob
        self.request_id = request_id  # type: str

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super(GetJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['job'] = self.job.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('job') is not None:
            temp_model = GetJobResponseBodyJob()
            self.job = temp_model.from_map(m['job'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleResponseBodyModule(TeaModel):
    def __init__(self, create_time=None, description=None, latest_version=None, module_id=None, name=None,
                 output_path=None, source=None, source_path=None, state_path=None, status=None, version_strategy=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.latest_version = latest_version  # type: str
        self.module_id = module_id  # type: str
        self.name = name  # type: str
        self.output_path = output_path  # type: str
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str
        self.status = status  # type: str
        self.version_strategy = version_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModuleResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.name is not None:
            result['name'] = self.name
        if self.output_path is not None:
            result['outputPath'] = self.output_path
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.status is not None:
            result['status'] = self.status
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('outputPath') is not None:
            self.output_path = m.get('outputPath')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class GetModuleResponseBody(TeaModel):
    def __init__(self, module=None, request_id=None):
        self.module = module  # type: GetModuleResponseBodyModule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super(GetModuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = GetModuleResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetModuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetModuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleMarketResponseBodyModuleMarket(TeaModel):
    def __init__(self, description=None, message=None, module_detail=None, module_id=None, module_market_id=None,
                 module_version=None, name=None, status=None):
        self.description = description  # type: str
        self.message = message  # type: str
        self.module_detail = module_detail  # type: str
        self.module_id = module_id  # type: str
        self.module_market_id = module_market_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModuleMarketResponseBodyModuleMarket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.message is not None:
            result['message'] = self.message
        if self.module_detail is not None:
            result['moduleDetail'] = self.module_detail
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_market_id is not None:
            result['moduleMarketId'] = self.module_market_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('moduleDetail') is not None:
            self.module_detail = m.get('moduleDetail')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleMarketId') is not None:
            self.module_market_id = m.get('moduleMarketId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetModuleMarketResponseBody(TeaModel):
    def __init__(self, module_market=None, request_id=None):
        self.module_market = module_market  # type: GetModuleMarketResponseBodyModuleMarket
        self.request_id = request_id  # type: str

    def validate(self):
        if self.module_market:
            self.module_market.validate()

    def to_map(self):
        _map = super(GetModuleMarketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_market is not None:
            result['moduleMarket'] = self.module_market.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('moduleMarket') is not None:
            temp_model = GetModuleMarketResponseBodyModuleMarket()
            self.module_market = temp_model.from_map(m['moduleMarket'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetModuleMarketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetModuleMarketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModuleMarketResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleMarketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleVersionResponseBodyVersion(TeaModel):
    def __init__(self, create_time=None, description=None, module_id=None, module_version=None, name=None,
                 source=None, source_path=None, state_path=None, terraform_context=None, version_strategy=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str
        self.terraform_context = terraform_context  # type: dict[str, any]
        self.version_strategy = version_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModuleVersionResponseBodyVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.terraform_context is not None:
            result['terraformContext'] = self.terraform_context
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('terraformContext') is not None:
            self.terraform_context = m.get('terraformContext')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class GetModuleVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, version=None):
        self.request_id = request_id  # type: str
        self.version = version  # type: GetModuleVersionResponseBodyVersion

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super(GetModuleVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.version is not None:
            result['version'] = self.version.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('version') is not None:
            temp_model = GetModuleVersionResponseBodyVersion()
            self.version = temp_model.from_map(m['version'])
        return self


class GetModuleVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetModuleVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModuleVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParameterSetResponseBodyParameterSetParameters(TeaModel):
    def __init__(self, name=None, type=None, value=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.value = value  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParameterSetResponseBodyParameterSetParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetParameterSetResponseBodyParameterSetRelationList(TeaModel):
    def __init__(self, create_time=None, resource_id=None, resource_type=None):
        self.create_time = create_time  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetParameterSetResponseBodyParameterSetRelationList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetParameterSetResponseBodyParameterSet(TeaModel):
    def __init__(self, create_time=None, description=None, name=None, parameter_set_id=None, parameters=None,
                 relation_list=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.parameter_set_id = parameter_set_id  # type: str
        self.parameters = parameters  # type: list[GetParameterSetResponseBodyParameterSetParameters]
        self.relation_list = relation_list  # type: list[GetParameterSetResponseBodyParameterSetRelationList]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetParameterSetResponseBodyParameterSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        result['relationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['relationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = GetParameterSetResponseBodyParameterSetParameters()
                self.parameters.append(temp_model.from_map(k))
        self.relation_list = []
        if m.get('relationList') is not None:
            for k in m.get('relationList'):
                temp_model = GetParameterSetResponseBodyParameterSetRelationList()
                self.relation_list.append(temp_model.from_map(k))
        return self


class GetParameterSetResponseBody(TeaModel):
    def __init__(self, parameter_set=None, request_id=None):
        self.parameter_set = parameter_set  # type: GetParameterSetResponseBodyParameterSet
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameter_set:
            self.parameter_set.validate()

    def to_map(self):
        _map = super(GetParameterSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_set is not None:
            result['parameterSet'] = self.parameter_set.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('parameterSet') is not None:
            temp_model = GetParameterSetResponseBodyParameterSet()
            self.parameter_set = temp_model.from_map(m['parameterSet'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetParameterSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetParameterSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetParameterSetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponseBodyProject(TeaModel):
    def __init__(self, create_time=None, description=None, id=None, name=None, task_cnt=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.task_cnt = task_cnt  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: GetProjectResponseBodyProject
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(GetProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('project') is not None:
            temp_model = GetProjectResponseBodyProject()
            self.project = temp_model.from_map(m['project'])
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


class GetProjectBuildConfigRequest(TeaModel):
    def __init__(self, project_build_id=None):
        self.project_build_id = project_build_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectBuildConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_build_id is not None:
            result['projectBuildId'] = self.project_build_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('projectBuildId') is not None:
            self.project_build_id = m.get('projectBuildId')
        return self


class GetProjectBuildConfigResponseBodyProjectBuildConfig(TeaModel):
    def __init__(self, task_policies=None):
        self.task_policies = task_policies  # type: dict[str, ProjectBuildConfigTaskPoliciesValue]

    def validate(self):
        if self.task_policies:
            for v in self.task_policies.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(GetProjectBuildConfigResponseBodyProjectBuildConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['taskPolicies'] = {}
        if self.task_policies is not None:
            for k, v in self.task_policies.items():
                result['taskPolicies'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_policies = {}
        if m.get('taskPolicies') is not None:
            for k, v in m.get('taskPolicies').items():
                temp_model = ProjectBuildConfigTaskPoliciesValue()
                self.task_policies[k] = temp_model.from_map(v)
        return self


class GetProjectBuildConfigResponseBody(TeaModel):
    def __init__(self, project_build_config=None, request_id=None):
        self.project_build_config = project_build_config  # type: GetProjectBuildConfigResponseBodyProjectBuildConfig
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project_build_config:
            self.project_build_config.validate()

    def to_map(self):
        _map = super(GetProjectBuildConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_build_config is not None:
            result['projectBuildConfig'] = self.project_build_config.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('projectBuildConfig') is not None:
            temp_model = GetProjectBuildConfigResponseBodyProjectBuildConfig()
            self.project_build_config = temp_model.from_map(m['projectBuildConfig'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectBuildConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectBuildConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectBuildConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectBuildConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectBuildContextResponseBodyProjectBuildJobList(TeaModel):
    def __init__(self, is_deleted=None, job_id=None, module_id=None, module_version=None, name=None, status=None,
                 task_id=None):
        self.is_deleted = is_deleted  # type: long
        self.job_id = job_id  # type: str
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectBuildContextResponseBodyProjectBuildJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_deleted is not None:
            result['isDeleted'] = self.is_deleted
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isDeleted') is not None:
            self.is_deleted = m.get('isDeleted')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetProjectBuildContextResponseBodyProjectBuildResourceList(TeaModel):
    def __init__(self, info=None, resource_cnt=None, resource_type=None):
        self.info = info  # type: dict[str, str]
        self.resource_cnt = resource_cnt  # type: long
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectBuildContextResponseBodyProjectBuildResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['info'] = self.info
        if self.resource_cnt is not None:
            result['resourceCnt'] = self.resource_cnt
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('info') is not None:
            self.info = m.get('info')
        if m.get('resourceCnt') is not None:
            self.resource_cnt = m.get('resourceCnt')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetProjectBuildContextResponseBodyProjectBuild(TeaModel):
    def __init__(self, end_time=None, fail_cnt=None, job_list=None, job_total_cnt=None, project_build_id=None,
                 project_id=None, resource_cnt=None, resource_list=None, resource_type_cnt=None, status=None, success_cnt=None):
        self.end_time = end_time  # type: str
        self.fail_cnt = fail_cnt  # type: long
        self.job_list = job_list  # type: list[GetProjectBuildContextResponseBodyProjectBuildJobList]
        self.job_total_cnt = job_total_cnt  # type: long
        self.project_build_id = project_build_id  # type: str
        self.project_id = project_id  # type: str
        self.resource_cnt = resource_cnt  # type: long
        self.resource_list = resource_list  # type: list[GetProjectBuildContextResponseBodyProjectBuildResourceList]
        self.resource_type_cnt = resource_type_cnt  # type: long
        self.status = status  # type: str
        self.success_cnt = success_cnt  # type: long

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProjectBuildContextResponseBodyProjectBuild, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.fail_cnt is not None:
            result['failCnt'] = self.fail_cnt
        result['jobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['jobList'].append(k.to_map() if k else None)
        if self.job_total_cnt is not None:
            result['jobTotalCnt'] = self.job_total_cnt
        if self.project_build_id is not None:
            result['projectBuildId'] = self.project_build_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.resource_cnt is not None:
            result['resourceCnt'] = self.resource_cnt
        result['resourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['resourceList'].append(k.to_map() if k else None)
        if self.resource_type_cnt is not None:
            result['resourceTypeCnt'] = self.resource_type_cnt
        if self.status is not None:
            result['status'] = self.status
        if self.success_cnt is not None:
            result['successCnt'] = self.success_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('failCnt') is not None:
            self.fail_cnt = m.get('failCnt')
        self.job_list = []
        if m.get('jobList') is not None:
            for k in m.get('jobList'):
                temp_model = GetProjectBuildContextResponseBodyProjectBuildJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('jobTotalCnt') is not None:
            self.job_total_cnt = m.get('jobTotalCnt')
        if m.get('projectBuildId') is not None:
            self.project_build_id = m.get('projectBuildId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('resourceCnt') is not None:
            self.resource_cnt = m.get('resourceCnt')
        self.resource_list = []
        if m.get('resourceList') is not None:
            for k in m.get('resourceList'):
                temp_model = GetProjectBuildContextResponseBodyProjectBuildResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('resourceTypeCnt') is not None:
            self.resource_type_cnt = m.get('resourceTypeCnt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('successCnt') is not None:
            self.success_cnt = m.get('successCnt')
        return self


class GetProjectBuildContextResponseBody(TeaModel):
    def __init__(self, project_build=None, request_id=None):
        self.project_build = project_build  # type: GetProjectBuildContextResponseBodyProjectBuild
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project_build:
            self.project_build.validate()

    def to_map(self):
        _map = super(GetProjectBuildContextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_build is not None:
            result['ProjectBuild'] = self.project_build.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectBuild') is not None:
            temp_model = GetProjectBuildContextResponseBodyProjectBuild()
            self.project_build = temp_model.from_map(m['ProjectBuild'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectBuildContextResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectBuildContextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectBuildContextResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectBuildContextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectJobSummaryResponseBodyJobSummaryDetail(TeaModel):
    def __init__(self, fail_cnt=None, running_cnt=None, success_cnt=None, task_id=None, total=None):
        self.fail_cnt = fail_cnt  # type: long
        self.running_cnt = running_cnt  # type: long
        self.success_cnt = success_cnt  # type: long
        self.task_id = task_id  # type: str
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectJobSummaryResponseBodyJobSummaryDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_cnt is not None:
            result['failCnt'] = self.fail_cnt
        if self.running_cnt is not None:
            result['runningCnt'] = self.running_cnt
        if self.success_cnt is not None:
            result['successCnt'] = self.success_cnt
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('failCnt') is not None:
            self.fail_cnt = m.get('failCnt')
        if m.get('runningCnt') is not None:
            self.running_cnt = m.get('runningCnt')
        if m.get('successCnt') is not None:
            self.success_cnt = m.get('successCnt')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetProjectJobSummaryResponseBodyJobSummary(TeaModel):
    def __init__(self, detail=None, fail_cnt=None, running_cnt=None, success_cnt=None, total=None):
        self.detail = detail  # type: list[GetProjectJobSummaryResponseBodyJobSummaryDetail]
        self.fail_cnt = fail_cnt  # type: long
        self.running_cnt = running_cnt  # type: long
        self.success_cnt = success_cnt  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProjectJobSummaryResponseBodyJobSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        if self.fail_cnt is not None:
            result['failCnt'] = self.fail_cnt
        if self.running_cnt is not None:
            result['runningCnt'] = self.running_cnt
        if self.success_cnt is not None:
            result['successCnt'] = self.success_cnt
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = GetProjectJobSummaryResponseBodyJobSummaryDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('failCnt') is not None:
            self.fail_cnt = m.get('failCnt')
        if m.get('runningCnt') is not None:
            self.running_cnt = m.get('runningCnt')
        if m.get('successCnt') is not None:
            self.success_cnt = m.get('successCnt')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetProjectJobSummaryResponseBody(TeaModel):
    def __init__(self, job_summary=None, request_id=None):
        self.job_summary = job_summary  # type: GetProjectJobSummaryResponseBodyJobSummary
        self.request_id = request_id  # type: str

    def validate(self):
        if self.job_summary:
            self.job_summary.validate()

    def to_map(self):
        _map = super(GetProjectJobSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_summary is not None:
            result['jobSummary'] = self.job_summary.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('jobSummary') is not None:
            temp_model = GetProjectJobSummaryResponseBodyJobSummary()
            self.job_summary = temp_model.from_map(m['jobSummary'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectJobSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectJobSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectJobSummaryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectJobSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResourceSummaryResponseBodyResourceSummaryDetail(TeaModel):
    def __init__(self, resource_cnt=None, resource_type=None, task_ids=None):
        self.resource_cnt = resource_cnt  # type: long
        self.resource_type = resource_type  # type: str
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResourceSummaryResponseBodyResourceSummaryDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cnt is not None:
            result['resourceCnt'] = self.resource_cnt
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceCnt') is not None:
            self.resource_cnt = m.get('resourceCnt')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class GetProjectResourceSummaryResponseBodyResourceSummary(TeaModel):
    def __init__(self, detail=None, resource_cnt=None, resource_type_cnt=None):
        self.detail = detail  # type: list[GetProjectResourceSummaryResponseBodyResourceSummaryDetail]
        self.resource_cnt = resource_cnt  # type: long
        self.resource_type_cnt = resource_type_cnt  # type: long

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProjectResourceSummaryResponseBodyResourceSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        if self.resource_cnt is not None:
            result['resourceCnt'] = self.resource_cnt
        if self.resource_type_cnt is not None:
            result['resourceTypeCnt'] = self.resource_type_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = GetProjectResourceSummaryResponseBodyResourceSummaryDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('resourceCnt') is not None:
            self.resource_cnt = m.get('resourceCnt')
        if m.get('resourceTypeCnt') is not None:
            self.resource_type_cnt = m.get('resourceTypeCnt')
        return self


class GetProjectResourceSummaryResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_summary=None):
        self.request_id = request_id  # type: str
        self.resource_summary = resource_summary  # type: GetProjectResourceSummaryResponseBodyResourceSummary

    def validate(self):
        if self.resource_summary:
            self.resource_summary.validate()

    def to_map(self):
        _map = super(GetProjectResourceSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_summary is not None:
            result['resourceSummary'] = self.resource_summary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceSummary') is not None:
            temp_model = GetProjectResourceSummaryResponseBodyResourceSummary()
            self.resource_summary = temp_model.from_map(m['resourceSummary'])
        return self


class GetProjectResourceSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectResourceSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectResourceSummaryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectResourceSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRabbitmqPublisherResponseBodyPublisher(TeaModel):
    def __init__(self, create_time=None, description=None, exchange_name=None, exchange_type=None, host_name=None,
                 name=None, port=None, publisher_id=None, task_ids=None, user_name=None, virtual_host=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.exchange_name = exchange_name  # type: str
        self.exchange_type = exchange_type  # type: str
        self.host_name = host_name  # type: str
        self.name = name  # type: str
        self.port = port  # type: long
        self.publisher_id = publisher_id  # type: str
        self.task_ids = task_ids  # type: list[str]
        self.user_name = user_name  # type: str
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRabbitmqPublisherResponseBodyPublisher, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.exchange_name is not None:
            result['exchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['exchangeType'] = self.exchange_type
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.publisher_id is not None:
            result['publisherId'] = self.publisher_id
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.virtual_host is not None:
            result['virtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exchangeName') is not None:
            self.exchange_name = m.get('exchangeName')
        if m.get('exchangeType') is not None:
            self.exchange_type = m.get('exchangeType')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('publisherId') is not None:
            self.publisher_id = m.get('publisherId')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('virtualHost') is not None:
            self.virtual_host = m.get('virtualHost')
        return self


class GetRabbitmqPublisherResponseBody(TeaModel):
    def __init__(self, publisher=None, request_id=None):
        self.publisher = publisher  # type: GetRabbitmqPublisherResponseBodyPublisher
        self.request_id = request_id  # type: str

    def validate(self):
        if self.publisher:
            self.publisher.validate()

    def to_map(self):
        _map = super(GetRabbitmqPublisherResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.publisher is not None:
            result['publisher'] = self.publisher.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('publisher') is not None:
            temp_model = GetRabbitmqPublisherResponseBodyPublisher()
            self.publisher = temp_model.from_map(m['publisher'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRabbitmqPublisherResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRabbitmqPublisherResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRabbitmqPublisherResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceExportTaskRequest(TeaModel):
    def __init__(self, export_version=None):
        self.export_version = export_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceExportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        return self


class GetResourceExportTaskResponseBodyTaskExcludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceExportTaskResponseBodyTaskExcludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetResourceExportTaskResponseBodyTaskExportToModule(TeaModel):
    def __init__(self, source=None, source_path=None, state_path=None):
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceExportTaskResponseBodyTaskExportToModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class GetResourceExportTaskResponseBodyTaskIncludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceExportTaskResponseBodyTaskIncludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetResourceExportTaskResponseBodyTaskModules(TeaModel):
    def __init__(self, source=None, source_path=None, version=None):
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceExportTaskResponseBodyTaskModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetResourceExportTaskResponseBodyTaskVariables(TeaModel):
    def __init__(self, properties=None, resource_type=None):
        self.properties = properties  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceExportTaskResponseBodyTaskVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetResourceExportTaskResponseBodyTask(TeaModel):
    def __init__(self, create_time=None, description=None, exclude_rules=None, export_task_id=None,
                 export_to_module=None, export_version=None, failed_reason=None, include_rules=None, modules=None, name=None,
                 ram_role=None, status=None, task_output_path=None, terraform_version=None, trigger_strategy=None,
                 variables=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.exclude_rules = exclude_rules  # type: list[GetResourceExportTaskResponseBodyTaskExcludeRules]
        self.export_task_id = export_task_id  # type: str
        self.export_to_module = export_to_module  # type: GetResourceExportTaskResponseBodyTaskExportToModule
        self.export_version = export_version  # type: str
        self.failed_reason = failed_reason  # type: str
        self.include_rules = include_rules  # type: list[GetResourceExportTaskResponseBodyTaskIncludeRules]
        self.modules = modules  # type: list[GetResourceExportTaskResponseBodyTaskModules]
        self.name = name  # type: str
        self.ram_role = ram_role  # type: str
        self.status = status  # type: str
        self.task_output_path = task_output_path  # type: str
        self.terraform_version = terraform_version  # type: str
        self.trigger_strategy = trigger_strategy  # type: str
        self.variables = variables  # type: list[GetResourceExportTaskResponseBodyTaskVariables]

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceExportTaskResponseBodyTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.status is not None:
            result['status'] = self.status
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = GetResourceExportTaskResponseBodyTaskExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = GetResourceExportTaskResponseBodyTaskExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = GetResourceExportTaskResponseBodyTaskIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = GetResourceExportTaskResponseBodyTaskModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = GetResourceExportTaskResponseBodyTaskVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class GetResourceExportTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task=None):
        self.request_id = request_id  # type: str
        self.task = task  # type: GetResourceExportTaskResponseBodyTask

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super(GetResourceExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetResourceExportTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetResourceExportTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceLinkRequest(TeaModel):
    def __init__(self, product_code=None, resource_type_code=None):
        self.product_code = product_code  # type: str
        self.resource_type_code = resource_type_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        return self


class GetResourceLinkResponseBody(TeaModel):
    def __init__(self, link=None, request_id=None):
        self.link = link  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link is not None:
            result['link'] = self.link
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetResourceLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceLinkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBodyTaskGroupInfo(TeaModel):
    def __init__(self, group_id=None, group_name=None, project_id=None, project_name=None):
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskGroupInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class GetTaskResponseBodyTask(TeaModel):
    def __init__(self, auto_apply=None, create_time=None, current_job_id=None, group_info=None, meta=None,
                 module_id=None, module_version=None, name=None, parameters=None, protection_strategy=None, ram_role=None,
                 status=None, task_id=None, task_output_path=None, terraform_version=None, trigger_strategy=None):
        self.auto_apply = auto_apply  # type: bool
        self.create_time = create_time  # type: str
        self.current_job_id = current_job_id  # type: str
        self.group_info = group_info  # type: GetTaskResponseBodyTaskGroupInfo
        self.meta = meta  # type: dict[str, str]
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.parameters = parameters  # type: dict[str, str]
        self.protection_strategy = protection_strategy  # type: list[str]
        self.ram_role = ram_role  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.task_output_path = task_output_path  # type: str
        self.terraform_version = terraform_version  # type: str
        self.trigger_strategy = trigger_strategy  # type: str

    def validate(self):
        if self.group_info:
            self.group_info.validate()

    def to_map(self):
        _map = super(GetTaskResponseBodyTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.meta is not None:
            result['meta'] = self.meta
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')
        if m.get('groupInfo') is not None:
            temp_model = GetTaskResponseBodyTaskGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task=None):
        self.request_id = request_id  # type: str
        self.task = task  # type: GetTaskResponseBodyTask

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super(GetTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskContextResponseBodyTaskJobConfig(TeaModel):
    def __init__(self, is_destroy=None, job_module_version=None, resources_changed=None):
        self.is_destroy = is_destroy  # type: bool
        self.job_module_version = job_module_version  # type: str
        self.resources_changed = resources_changed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskContextResponseBodyTaskJobConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy
        if self.job_module_version is not None:
            result['jobModuleVersion'] = self.job_module_version
        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')
        if m.get('jobModuleVersion') is not None:
            self.job_module_version = m.get('jobModuleVersion')
        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')
        return self


class GetTaskContextResponseBodyTask(TeaModel):
    def __init__(self, auto_apply=None, job_config=None, job_description=None, job_gmt_create=None, job_id=None,
                 job_status=None, module_id=None, module_path=None, module_version=None, parameters=None, ram_role=None,
                 resource_count=None, task_gmt_create=None, task_id=None, task_name=None, task_output_path=None, task_status=None,
                 terraform_version=None, trigger_strategy=None):
        self.auto_apply = auto_apply  # type: bool
        self.job_config = job_config  # type: GetTaskContextResponseBodyTaskJobConfig
        self.job_description = job_description  # type: str
        self.job_gmt_create = job_gmt_create  # type: str
        self.job_id = job_id  # type: str
        self.job_status = job_status  # type: str
        self.module_id = module_id  # type: str
        self.module_path = module_path  # type: str
        self.module_version = module_version  # type: str
        self.parameters = parameters  # type: dict[str, str]
        self.ram_role = ram_role  # type: str
        self.resource_count = resource_count  # type: int
        self.task_gmt_create = task_gmt_create  # type: str
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.task_output_path = task_output_path  # type: str
        self.task_status = task_status  # type: str
        self.terraform_version = terraform_version  # type: str
        self.trigger_strategy = trigger_strategy  # type: str

    def validate(self):
        if self.job_config:
            self.job_config.validate()

    def to_map(self):
        _map = super(GetTaskContextResponseBodyTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.job_config is not None:
            result['jobConfig'] = self.job_config.to_map()
        if self.job_description is not None:
            result['jobDescription'] = self.job_description
        if self.job_gmt_create is not None:
            result['jobGmtCreate'] = self.job_gmt_create
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_path is not None:
            result['modulePath'] = self.module_path
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.resource_count is not None:
            result['resourceCount'] = self.resource_count
        if self.task_gmt_create is not None:
            result['taskGmtCreate'] = self.task_gmt_create
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_name is not None:
            result['taskName'] = self.task_name
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('jobConfig') is not None:
            temp_model = GetTaskContextResponseBodyTaskJobConfig()
            self.job_config = temp_model.from_map(m['jobConfig'])
        if m.get('jobDescription') is not None:
            self.job_description = m.get('jobDescription')
        if m.get('jobGmtCreate') is not None:
            self.job_gmt_create = m.get('jobGmtCreate')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('modulePath') is not None:
            self.module_path = m.get('modulePath')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('resourceCount') is not None:
            self.resource_count = m.get('resourceCount')
        if m.get('taskGmtCreate') is not None:
            self.task_gmt_create = m.get('taskGmtCreate')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class GetTaskContextResponseBody(TeaModel):
    def __init__(self, request_id=None, task=None):
        self.request_id = request_id  # type: str
        self.task = task  # type: GetTaskContextResponseBodyTask

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super(GetTaskContextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetTaskContextResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetTaskContextResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskContextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskContextResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskContextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizationsRequest(TeaModel):
    def __init__(self, authorization_id=None, authorization_type=None, keyword=None, page_number=None,
                 page_size=None):
        self.authorization_id = authorization_id  # type: str
        self.authorization_type = authorization_type  # type: str
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_id is not None:
            result['authorizationId'] = self.authorization_id
        if self.authorization_type is not None:
            result['authorizationType'] = self.authorization_type
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authorizationId') is not None:
            self.authorization_id = m.get('authorizationId')
        if m.get('authorizationType') is not None:
            self.authorization_type = m.get('authorizationType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAuthorizationsResponseBodyAuthorizations(TeaModel):
    def __init__(self, authorization_id=None, create_time=None, due_time=None, module_id=None, module_version=None,
                 name=None, owner_uid=None, uid=None):
        self.authorization_id = authorization_id  # type: str
        self.create_time = create_time  # type: str
        self.due_time = due_time  # type: str
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.owner_uid = owner_uid  # type: long
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizationsResponseBodyAuthorizations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_id is not None:
            result['authorizationId'] = self.authorization_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.owner_uid is not None:
            result['ownerUid'] = self.owner_uid
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authorizationId') is not None:
            self.authorization_id = m.get('authorizationId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ownerUid') is not None:
            self.owner_uid = m.get('ownerUid')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListAuthorizationsResponseBody(TeaModel):
    def __init__(self, authorizations=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.authorizations = authorizations  # type: list[ListAuthorizationsResponseBodyAuthorizations]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.authorizations:
            for k in self.authorizations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthorizationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['authorizations'] = []
        if self.authorizations is not None:
            for k in self.authorizations:
                result['authorizations'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.authorizations = []
        if m.get('authorizations') is not None:
            for k in m.get('authorizations'):
                temp_model = ListAuthorizationsResponseBodyAuthorizations()
                self.authorizations.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAuthorizationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAuthorizationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthorizationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAuthorizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None):
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class ListGroupResponseBodyGroups(TeaModel):
    def __init__(self, create_time=None, description=None, id=None, is_default=None, name=None, project_id=None,
                 task_cnt=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.is_default = is_default  # type: bool
        self.name = name  # type: str
        self.project_id = project_id  # type: str
        self.task_cnt = task_cnt  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class ListGroupResponseBody(TeaModel):
    def __init__(self, count=None, groups=None, page_number=None, page_size=None, request_id=None):
        self.count = count  # type: long
        self.groups = groups  # type: list[ListGroupResponseBodyGroups]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.groups = []
        if m.get('groups') is not None:
            for k in m.get('groups'):
                temp_model = ListGroupResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, status=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListJobsResponseBodyJobsConfig(TeaModel):
    def __init__(self, module_version=None, resources_changed=None):
        self.module_version = module_version  # type: str
        self.resources_changed = resources_changed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyJobsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(self, config=None, create_time=None, description=None, job_id=None, status=None, status_detail=None,
                 task_id=None):
        self.config = config  # type: ListJobsResponseBodyJobsConfig
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.job_id = job_id  # type: str
        self.status = status  # type: str
        self.status_detail = status_detail  # type: dict[str, JobsStatusDetailValue]
        self.task_id = task_id  # type: str

    def validate(self):
        if self.config:
            self.config.validate()
        if self.status_detail:
            for v in self.status_detail.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(ListJobsResponseBodyJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.status is not None:
            result['status'] = self.status
        result['statusDetail'] = {}
        if self.status_detail is not None:
            for k, v in self.status_detail.items():
                result['statusDetail'][k] = v.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = ListJobsResponseBodyJobsConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.status_detail = {}
        if m.get('statusDetail') is not None:
            for k, v in m.get('statusDetail').items():
                temp_model = JobsStatusDetailValue()
                self.status_detail[k] = temp_model.from_map(v)
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, jobs=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.jobs = jobs  # type: list[ListJobsResponseBodyJobs]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

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
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleMarketsRequest(TeaModel):
    def __init__(self, keyword=None, page_number=None, page_size=None, status=None, type=None):
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModuleMarketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListModuleMarketsResponseBodyModuleMarkets(TeaModel):
    def __init__(self, clone_count=None, code_url=None, config=None, description=None, message=None,
                 module_detail=None, module_id=None, module_market_id=None, module_version=None, name=None, related_id=None,
                 status=None):
        self.clone_count = clone_count  # type: int
        self.code_url = code_url  # type: str
        self.config = config  # type: dict[str, str]
        self.description = description  # type: str
        self.message = message  # type: str
        self.module_detail = module_detail  # type: str
        self.module_id = module_id  # type: str
        self.module_market_id = module_market_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.related_id = related_id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModuleMarketsResponseBodyModuleMarkets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clone_count is not None:
            result['cloneCount'] = self.clone_count
        if self.code_url is not None:
            result['codeUrl'] = self.code_url
        if self.config is not None:
            result['config'] = self.config
        if self.description is not None:
            result['description'] = self.description
        if self.message is not None:
            result['message'] = self.message
        if self.module_detail is not None:
            result['moduleDetail'] = self.module_detail
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_market_id is not None:
            result['moduleMarketId'] = self.module_market_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.related_id is not None:
            result['relatedId'] = self.related_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cloneCount') is not None:
            self.clone_count = m.get('cloneCount')
        if m.get('codeUrl') is not None:
            self.code_url = m.get('codeUrl')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('moduleDetail') is not None:
            self.module_detail = m.get('moduleDetail')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleMarketId') is not None:
            self.module_market_id = m.get('moduleMarketId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('relatedId') is not None:
            self.related_id = m.get('relatedId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListModuleMarketsResponseBody(TeaModel):
    def __init__(self, module_markets=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.module_markets = module_markets  # type: list[ListModuleMarketsResponseBodyModuleMarkets]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.module_markets:
            for k in self.module_markets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModuleMarketsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['moduleMarkets'] = []
        if self.module_markets is not None:
            for k in self.module_markets:
                result['moduleMarkets'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.module_markets = []
        if m.get('moduleMarkets') is not None:
            for k in m.get('moduleMarkets'):
                temp_model = ListModuleMarketsResponseBodyModuleMarkets()
                self.module_markets.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListModuleMarketsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModuleMarketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModuleMarketsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleMarketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleVersionRequest(TeaModel):
    def __init__(self, keyword=None, page_number=None, page_size=None):
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModuleVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListModuleVersionResponseBodyVersions(TeaModel):
    def __init__(self, create_time=None, description=None, module_id=None, module_version=None, name=None,
                 source_path=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.source_path = source_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModuleVersionResponseBodyVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        return self


class ListModuleVersionResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, versions=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.versions = versions  # type: list[ListModuleVersionResponseBodyVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModuleVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListModuleVersionResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListModuleVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModuleVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModuleVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulesRequest(TeaModel):
    def __init__(self, keyword=None, page_number=None, page_size=None):
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListModulesResponseBodyModules(TeaModel):
    def __init__(self, create_time=None, deletion_protection=None, description=None, latest_version=None, meta=None,
                 module_id=None, name=None, source=None, source_config=None, status=None):
        self.create_time = create_time  # type: str
        self.deletion_protection = deletion_protection  # type: bool
        self.description = description  # type: str
        self.latest_version = latest_version  # type: str
        self.meta = meta  # type: dict[str, any]
        self.module_id = module_id  # type: str
        self.name = name  # type: str
        self.source = source  # type: str
        self.source_config = source_config  # type: dict[str, any]
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModulesResponseBodyModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['description'] = self.description
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.meta is not None:
            result['meta'] = self.meta
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_config is not None:
            result['sourceConfig'] = self.source_config
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourceConfig') is not None:
            self.source_config = m.get('sourceConfig')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListModulesResponseBody(TeaModel):
    def __init__(self, modules=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.modules = modules  # type: list[ListModulesResponseBodyModules]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListModulesResponseBodyModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListModulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParameterSetRelationRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParameterSetRelationRequest, self).to_map()
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


class ListParameterSetRelationResponseBodyParameterSets(TeaModel):
    def __init__(self, create_time=None, description=None, name=None, parameter_set_id=None, parameters=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.parameter_set_id = parameter_set_id  # type: str
        self.parameters = parameters  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParameterSetRelationResponseBodyParameterSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class ListParameterSetRelationResponseBody(TeaModel):
    def __init__(self, parameter_sets=None, request_id=None, total_count=None):
        self.parameter_sets = parameter_sets  # type: list[ListParameterSetRelationResponseBodyParameterSets]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.parameter_sets:
            for k in self.parameter_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListParameterSetRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['parameterSets'] = []
        if self.parameter_sets is not None:
            for k in self.parameter_sets:
                result['parameterSets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameter_sets = []
        if m.get('parameterSets') is not None:
            for k in m.get('parameterSets'):
                temp_model = ListParameterSetRelationResponseBodyParameterSets()
                self.parameter_sets.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListParameterSetRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListParameterSetRelationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListParameterSetRelationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListParameterSetRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParameterSetsRequest(TeaModel):
    def __init__(self, keyword=None, page_number=None, page_size=None):
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParameterSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListParameterSetsResponseBodyParameterSetsParameters(TeaModel):
    def __init__(self, name=None, type=None, value=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.value = value  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParameterSetsResponseBodyParameterSetsParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListParameterSetsResponseBodyParameterSetsRelationList(TeaModel):
    def __init__(self, create_time=None, resource_id=None, resource_type=None):
        self.create_time = create_time  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParameterSetsResponseBodyParameterSetsRelationList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListParameterSetsResponseBodyParameterSets(TeaModel):
    def __init__(self, create_time=None, description=None, name=None, parameter_set_id=None, parameters=None,
                 relation_list=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.parameter_set_id = parameter_set_id  # type: str
        self.parameters = parameters  # type: list[ListParameterSetsResponseBodyParameterSetsParameters]
        self.relation_list = relation_list  # type: list[ListParameterSetsResponseBodyParameterSetsRelationList]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListParameterSetsResponseBodyParameterSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        result['relationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['relationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = ListParameterSetsResponseBodyParameterSetsParameters()
                self.parameters.append(temp_model.from_map(k))
        self.relation_list = []
        if m.get('relationList') is not None:
            for k in m.get('relationList'):
                temp_model = ListParameterSetsResponseBodyParameterSetsRelationList()
                self.relation_list.append(temp_model.from_map(k))
        return self


class ListParameterSetsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, parameter_sets=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.parameter_sets = parameter_sets  # type: list[ListParameterSetsResponseBodyParameterSets]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.parameter_sets:
            for k in self.parameter_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListParameterSetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['parameterSets'] = []
        if self.parameter_sets is not None:
            for k in self.parameter_sets:
                result['parameterSets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.parameter_sets = []
        if m.get('parameterSets') is not None:
            for k in m.get('parameterSets'):
                temp_model = ListParameterSetsResponseBodyParameterSets()
                self.parameter_sets.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListParameterSetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListParameterSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListParameterSetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListParameterSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectRequest, self).to_map()
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


class ListProjectResponseBodyProjects(TeaModel):
    def __init__(self, create_time=None, description=None, id=None, name=None, task_cnt=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.task_cnt = task_cnt  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectResponseBodyProjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(self, count=None, page_number=None, page_size=None, projects=None, request_id=None):
        self.count = count  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.projects = projects  # type: list[ListProjectResponseBodyProjects]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = ListProjectResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectBuildsResponseBodyProjectBuilds(TeaModel):
    def __init__(self, create_time=None, project_build_action=None, project_build_id=None,
                 project_build_index=None, project_id=None, status=None, timestamp=None):
        self.create_time = create_time  # type: str
        self.project_build_action = project_build_action  # type: str
        self.project_build_id = project_build_id  # type: str
        self.project_build_index = project_build_index  # type: long
        self.project_id = project_id  # type: str
        self.status = status  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectBuildsResponseBodyProjectBuilds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.project_build_action is not None:
            result['projectBuildAction'] = self.project_build_action
        if self.project_build_id is not None:
            result['projectBuildId'] = self.project_build_id
        if self.project_build_index is not None:
            result['projectBuildIndex'] = self.project_build_index
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status is not None:
            result['status'] = self.status
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('projectBuildAction') is not None:
            self.project_build_action = m.get('projectBuildAction')
        if m.get('projectBuildId') is not None:
            self.project_build_id = m.get('projectBuildId')
        if m.get('projectBuildIndex') is not None:
            self.project_build_index = m.get('projectBuildIndex')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class ListProjectBuildsResponseBody(TeaModel):
    def __init__(self, project_builds=None, request_id=None, total_count=None):
        self.project_builds = project_builds  # type: list[ListProjectBuildsResponseBodyProjectBuilds]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.project_builds:
            for k in self.project_builds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectBuildsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProjectBuilds'] = []
        if self.project_builds is not None:
            for k in self.project_builds:
                result['ProjectBuilds'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.project_builds = []
        if m.get('ProjectBuilds') is not None:
            for k in m.get('ProjectBuilds'):
                temp_model = ListProjectBuildsResponseBodyProjectBuilds()
                self.project_builds.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProjectBuildsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectBuildsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectBuildsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectBuildsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRabbitmqPublishersRequest(TeaModel):
    def __init__(self, keyword=None, page_number=None, page_size=None):
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRabbitmqPublishersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListRabbitmqPublishersResponseBodyAuthorizations(TeaModel):
    def __init__(self, create_time=None, description=None, exchange_name=None, exchange_type=None, host_name=None,
                 name=None, port=None, publisher_id=None, user_name=None, virtual_host=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.exchange_name = exchange_name  # type: str
        self.exchange_type = exchange_type  # type: str
        self.host_name = host_name  # type: str
        self.name = name  # type: str
        self.port = port  # type: long
        self.publisher_id = publisher_id  # type: str
        self.user_name = user_name  # type: str
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRabbitmqPublishersResponseBodyAuthorizations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.exchange_name is not None:
            result['exchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['exchangeType'] = self.exchange_type
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.publisher_id is not None:
            result['publisherId'] = self.publisher_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.virtual_host is not None:
            result['virtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exchangeName') is not None:
            self.exchange_name = m.get('exchangeName')
        if m.get('exchangeType') is not None:
            self.exchange_type = m.get('exchangeType')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('publisherId') is not None:
            self.publisher_id = m.get('publisherId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('virtualHost') is not None:
            self.virtual_host = m.get('virtualHost')
        return self


class ListRabbitmqPublishersResponseBody(TeaModel):
    def __init__(self, authorizations=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.authorizations = authorizations  # type: list[ListRabbitmqPublishersResponseBodyAuthorizations]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.authorizations:
            for k in self.authorizations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRabbitmqPublishersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['authorizations'] = []
        if self.authorizations is not None:
            for k in self.authorizations:
                result['authorizations'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.authorizations = []
        if m.get('authorizations') is not None:
            for k in m.get('authorizations'):
                temp_model = ListRabbitmqPublishersResponseBodyAuthorizations()
                self.authorizations.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListRabbitmqPublishersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRabbitmqPublishersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRabbitmqPublishersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRabbitmqPublishersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRelationModulesResponseBodyModules(TeaModel):
    def __init__(self, latest_version=None, module_id=None, name=None):
        self.latest_version = latest_version  # type: str
        self.module_id = module_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRelationModulesResponseBodyModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRelationModulesResponseBody(TeaModel):
    def __init__(self, modules=None, request_id=None, total_count=None):
        self.modules = modules  # type: list[ListRelationModulesResponseBodyModules]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRelationModulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListRelationModulesResponseBodyModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListRelationModulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRelationModulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRelationModulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRelationModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRelationTasksRequest(TeaModel):
    def __init__(self, keyword=None, module_id=None, page_number=None, page_size=None, project_id=None):
        self.keyword = keyword  # type: str
        self.module_id = module_id  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRelationTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class ListRelationTasksResponseBodyTasks(TeaModel):
    def __init__(self, create_time=None, module_id=None, module_version=None, name=None, status=None, task_id=None):
        self.create_time = create_time  # type: str
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRelationTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListRelationTasksResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, tasks=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[ListRelationTasksResponseBodyTasks]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRelationTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = ListRelationTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListRelationTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRelationTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRelationTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRelationTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExportTaskVersionsRequest(TeaModel):
    def __init__(self, export_version=None, keyword=None, page_number=None, page_size=None, status=None):
        self.export_version = export_version  # type: str
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksExcludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsResponseBodyExportTasksExcludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule(TeaModel):
    def __init__(self, source=None, source_path=None, state_path=None):
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksModules(TeaModel):
    def __init__(self, source=None, source_path=None, version=None):
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsResponseBodyExportTasksModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksVariables(TeaModel):
    def __init__(self, properties=None, resource_type=None):
        self.properties = properties  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsResponseBodyExportTasksVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasks(TeaModel):
    def __init__(self, create_time=None, description=None, exclude_rules=None, export_task_id=None,
                 export_to_module=None, export_version=None, failed_reason=None, has_destroy=None, include_rules=None, modules=None,
                 name=None, status=None, variables=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.exclude_rules = exclude_rules  # type: list[ListResourceExportTaskVersionsResponseBodyExportTasksExcludeRules]
        self.export_task_id = export_task_id  # type: str
        self.export_to_module = export_to_module  # type: ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule
        self.export_version = export_version  # type: str
        self.failed_reason = failed_reason  # type: str
        self.has_destroy = has_destroy  # type: bool
        self.include_rules = include_rules  # type: list[ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules]
        self.modules = modules  # type: list[ListResourceExportTaskVersionsResponseBodyExportTasksModules]
        self.name = name  # type: str
        self.status = status  # type: str
        self.variables = variables  # type: list[ListResourceExportTaskVersionsResponseBodyExportTasksVariables]

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsResponseBodyExportTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason
        if self.has_destroy is not None:
            result['hasDestroy'] = self.has_destroy
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')
        if m.get('hasDestroy') is not None:
            self.has_destroy = m.get('hasDestroy')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListResourceExportTaskVersionsResponseBody(TeaModel):
    def __init__(self, export_tasks=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.export_tasks = export_tasks  # type: list[ListResourceExportTaskVersionsResponseBodyExportTasks]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.export_tasks:
            for k in self.export_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['exportTasks'] = []
        if self.export_tasks is not None:
            for k in self.export_tasks:
                result['exportTasks'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.export_tasks = []
        if m.get('exportTasks') is not None:
            for k in m.get('exportTasks'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasks()
                self.export_tasks.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceExportTaskVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceExportTaskVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceExportTaskVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceExportTaskVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExportTasksRequest(TeaModel):
    def __init__(self, export_task_id=None, keyword=None, page_number=None, page_size=None):
        self.export_task_id = export_task_id  # type: str
        self.keyword = keyword  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListResourceExportTasksResponseBodyExportTasksExcludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTasksResponseBodyExportTasksExcludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTasksResponseBodyExportTasksExportToModule(TeaModel):
    def __init__(self, source=None, source_path=None, state_path=None):
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTasksResponseBodyExportTasksExportToModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class ListResourceExportTasksResponseBodyExportTasksIncludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTasksResponseBodyExportTasksIncludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTasksResponseBodyExportTasksModules(TeaModel):
    def __init__(self, source=None, source_path=None, version=None):
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTasksResponseBodyExportTasksModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListResourceExportTasksResponseBodyExportTasksVariables(TeaModel):
    def __init__(self, properties=None, resource_type=None):
        self.properties = properties  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceExportTasksResponseBodyExportTasksVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListResourceExportTasksResponseBodyExportTasks(TeaModel):
    def __init__(self, create_time=None, description=None, exclude_rules=None, export_task_id=None,
                 export_to_module=None, export_version=None, has_destroy=None, include_rules=None, modules=None, name=None,
                 status=None, variables=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.exclude_rules = exclude_rules  # type: list[ListResourceExportTasksResponseBodyExportTasksExcludeRules]
        self.export_task_id = export_task_id  # type: str
        self.export_to_module = export_to_module  # type: ListResourceExportTasksResponseBodyExportTasksExportToModule
        self.export_version = export_version  # type: str
        self.has_destroy = has_destroy  # type: bool
        self.include_rules = include_rules  # type: list[ListResourceExportTasksResponseBodyExportTasksIncludeRules]
        self.modules = modules  # type: list[ListResourceExportTasksResponseBodyExportTasksModules]
        self.name = name  # type: str
        self.status = status  # type: str
        self.variables = variables  # type: list[ListResourceExportTasksResponseBodyExportTasksVariables]

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceExportTasksResponseBodyExportTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.has_destroy is not None:
            result['hasDestroy'] = self.has_destroy
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = ListResourceExportTasksResponseBodyExportTasksExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('hasDestroy') is not None:
            self.has_destroy = m.get('hasDestroy')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListResourceExportTasksResponseBody(TeaModel):
    def __init__(self, export_tasks=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.export_tasks = export_tasks  # type: list[ListResourceExportTasksResponseBodyExportTasks]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.export_tasks:
            for k in self.export_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceExportTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['exportTasks'] = []
        if self.export_tasks is not None:
            for k in self.export_tasks:
                result['exportTasks'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.export_tasks = []
        if m.get('exportTasks') is not None:
            for k in m.get('exportTasks'):
                temp_model = ListResourceExportTasksResponseBodyExportTasks()
                self.export_tasks.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceExportTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceExportTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceExportTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceExportTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, source_type=None, source_value=None, spec_type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.source_type = source_type  # type: str
        self.source_value = source_value  # type: str
        self.spec_type = spec_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.source_value is not None:
            result['sourceValue'] = self.source_value
        if self.spec_type is not None:
            result['specType'] = self.spec_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('sourceValue') is not None:
            self.source_value = m.get('sourceValue')
        if m.get('specType') is not None:
            self.spec_type = m.get('specType')
        return self


class ListResourcesResponseBodyResourcesTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesResponseBodyResourcesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(self, account_id=None, create_time=None, depends_on_resource_ids=None, product_code=None,
                 properties=None, property_variables=None, region_id=None, resource_arn=None, resource_group_id=None,
                 resource_id=None, resource_name=None, resource_type=None, status=None, tags=None, terraform_arn=None,
                 terraform_code=None, zone_id=None):
        self.account_id = account_id  # type: str
        self.create_time = create_time  # type: str
        self.depends_on_resource_ids = depends_on_resource_ids  # type: list[str]
        self.product_code = product_code  # type: str
        self.properties = properties  # type: dict[str, any]
        self.property_variables = property_variables  # type: dict[str, any]
        self.region_id = region_id  # type: str
        self.resource_arn = resource_arn  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[ListResourcesResponseBodyResourcesTags]
        self.terraform_arn = terraform_arn  # type: str
        self.terraform_code = terraform_code  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.depends_on_resource_ids is not None:
            result['dependsOnResourceIds'] = self.depends_on_resource_ids
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.properties is not None:
            result['properties'] = self.properties
        if self.property_variables is not None:
            result['propertyVariables'] = self.property_variables
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.terraform_arn is not None:
            result['terraformArn'] = self.terraform_arn
        if self.terraform_code is not None:
            result['terraformCode'] = self.terraform_code
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dependsOnResourceIds') is not None:
            self.depends_on_resource_ids = m.get('dependsOnResourceIds')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('propertyVariables') is not None:
            self.property_variables = m.get('propertyVariables')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('terraformArn') is not None:
            self.terraform_arn = m.get('terraformArn')
        if m.get('terraformCode') is not None:
            self.terraform_code = m.get('terraformCode')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(self, resources=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.resources = resources  # type: list[ListResourcesResponseBodyResources]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
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


class ListTaskResourceRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskResourceRequest, self).to_map()
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


class ListTaskResourceResponseBodyResources(TeaModel):
    def __init__(self, instance_attribute=None, instance_id=None, job_id=None, name=None, type=None):
        self.instance_attribute = instance_attribute  # type: str
        self.instance_id = instance_id  # type: str
        self.job_id = job_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskResourceResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_attribute is not None:
            result['instanceAttribute'] = self.instance_attribute
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceAttribute') is not None:
            self.instance_attribute = m.get('instanceAttribute')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTaskResourceResponseBody(TeaModel):
    def __init__(self, count=None, page_number=None, page_size=None, request_id=None, resources=None):
        self.count = count  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[ListTaskResourceResponseBodyResources]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ListTaskResourceResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListTaskResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTaskResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTaskResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTaskResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, group_id=None, keyword=None, module_id=None, page_number=None, page_size=None,
                 project_id=None, task_id=None):
        self.group_id = group_id  # type: str
        self.keyword = keyword  # type: str
        self.module_id = module_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksResponseBodyTasksGroupInfo(TeaModel):
    def __init__(self, group_id=None, group_name=None, project_id=None, project_name=None):
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksResponseBodyTasksGroupInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(self, create_time=None, current_job_id=None, current_job_status=None, group_info=None,
                 has_destroy=None, module_id=None, module_version=None, name=None, status=None, task_id=None):
        self.create_time = create_time  # type: str
        self.current_job_id = current_job_id  # type: str
        self.current_job_status = current_job_status  # type: str
        self.group_info = group_info  # type: ListTasksResponseBodyTasksGroupInfo
        self.has_destroy = has_destroy  # type: bool
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.group_info:
            self.group_info.validate()

    def to_map(self):
        _map = super(ListTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.has_destroy is not None:
            result['hasDestroy'] = self.has_destroy
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')
        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')
        if m.get('groupInfo') is not None:
            temp_model = ListTasksResponseBodyTasksGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('hasDestroy') is not None:
            self.has_destroy = m.get('hasDestroy')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, tasks=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[ListTasksResponseBodyTasks]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateJobRequest(TeaModel):
    def __init__(self, comment=None):
        self.comment = comment  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self


class OperateJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateJobResponseBody, self).to_map()
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


class OperateJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OperateJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OperateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveResourceExportTaskVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveResourceExportTaskVersionResponseBody, self).to_map()
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


class RemoveResourceExportTaskVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveResourceExportTaskVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveResourceExportTaskVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveResourceExportTaskVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthorizationAttributeRequest(TeaModel):
    def __init__(self, due_time=None, name=None):
        self.due_time = due_time  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthorizationAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateAuthorizationAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthorizationAttributeResponseBody, self).to_map()
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


class UpdateAuthorizationAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAuthorizationAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAuthorizationAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAuthorizationAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateGroupResponseBodyGroup(TeaModel):
    def __init__(self, create_time=None, description=None, id=None, name=None, project_id=None, task_cnt=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.project_id = project_id  # type: str
        self.task_cnt = task_cnt  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupResponseBodyGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class UpdateGroupResponseBody(TeaModel):
    def __init__(self, group=None, request_id=None):
        self.group = group  # type: UpdateGroupResponseBodyGroup
        self.request_id = request_id  # type: str

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super(UpdateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('group') is not None:
            temp_model = UpdateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['group'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModuleAttributeRequest(TeaModel):
    def __init__(self, description=None, name=None, source=None, source_path=None, state_path=None,
                 version_strategy=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str
        self.version_strategy = version_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModuleAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class UpdateModuleAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModuleAttributeResponseBody, self).to_map()
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


class UpdateModuleAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateModuleAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateModuleAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateModuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModuleMarketAttributeRequest(TeaModel):
    def __init__(self, description=None, module_detail=None, name=None):
        self.description = description  # type: str
        self.module_detail = module_detail  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModuleMarketAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.module_detail is not None:
            result['moduleDetail'] = self.module_detail
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleDetail') is not None:
            self.module_detail = m.get('moduleDetail')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateModuleMarketAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModuleMarketAttributeResponseBody, self).to_map()
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


class UpdateModuleMarketAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateModuleMarketAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateModuleMarketAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateModuleMarketAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateParameterSetAttributeRequestParameters(TeaModel):
    def __init__(self, name=None, type=None, value=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateParameterSetAttributeRequestParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateParameterSetAttributeRequest(TeaModel):
    def __init__(self, description=None, name=None, parameters=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.parameters = parameters  # type: list[UpdateParameterSetAttributeRequestParameters]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateParameterSetAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = UpdateParameterSetAttributeRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class UpdateParameterSetAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateParameterSetAttributeResponseBody, self).to_map()
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


class UpdateParameterSetAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateParameterSetAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateParameterSetAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateParameterSetAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateProjectResponseBodyProject(TeaModel):
    def __init__(self, create_time=None, description=None, group_cnt=None, id=None, name=None, task_cnt=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.group_cnt = group_cnt  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.task_cnt = task_cnt  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.group_cnt is not None:
            result['groupCnt'] = self.group_cnt
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupCnt') is not None:
            self.group_cnt = m.get('groupCnt')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: UpdateProjectResponseBodyProject
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(UpdateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('project') is not None:
            temp_model = UpdateProjectResponseBodyProject()
            self.project = temp_model.from_map(m['project'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRabbitmqPublisherAttributeRequest(TeaModel):
    def __init__(self, description=None, exchange_name=None, exchange_type=None, name=None):
        self.description = description  # type: str
        self.exchange_name = exchange_name  # type: str
        self.exchange_type = exchange_type  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRabbitmqPublisherAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.exchange_name is not None:
            result['exchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['exchangeType'] = self.exchange_type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exchangeName') is not None:
            self.exchange_name = m.get('exchangeName')
        if m.get('exchangeType') is not None:
            self.exchange_type = m.get('exchangeType')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateRabbitmqPublisherAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRabbitmqPublisherAttributeResponseBody, self).to_map()
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


class UpdateRabbitmqPublisherAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRabbitmqPublisherAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRabbitmqPublisherAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRabbitmqPublisherAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceExportTaskAttributeRequestExcludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceExportTaskAttributeRequestExcludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdateResourceExportTaskAttributeRequestExportToModule(TeaModel):
    def __init__(self, source=None, source_path=None, state_path=None):
        self.source = source  # type: str
        self.source_path = source_path  # type: str
        self.state_path = state_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceExportTaskAttributeRequestExportToModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class UpdateResourceExportTaskAttributeRequestIncludeRules(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceExportTaskAttributeRequestIncludeRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdateResourceExportTaskAttributeRequestVariables(TeaModel):
    def __init__(self, properties=None, resource_type=None):
        self.properties = properties  # type: list[str]
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceExportTaskAttributeRequestVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class UpdateResourceExportTaskAttributeRequest(TeaModel):
    def __init__(self, client_token=None, description=None, exclude_rules=None, export_to_module=None,
                 include_rules=None, name=None, ram_role=None, terraform_version=None, trigger_strategy=None, variables=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.exclude_rules = exclude_rules  # type: list[UpdateResourceExportTaskAttributeRequestExcludeRules]
        self.export_to_module = export_to_module  # type: UpdateResourceExportTaskAttributeRequestExportToModule
        self.include_rules = include_rules  # type: list[UpdateResourceExportTaskAttributeRequestIncludeRules]
        self.name = name  # type: str
        self.ram_role = ram_role  # type: str
        self.terraform_version = terraform_version  # type: str
        self.trigger_strategy = trigger_strategy  # type: str
        self.variables = variables  # type: list[UpdateResourceExportTaskAttributeRequestVariables]

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateResourceExportTaskAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = UpdateResourceExportTaskAttributeRequestExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportToModule') is not None:
            temp_model = UpdateResourceExportTaskAttributeRequestExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = UpdateResourceExportTaskAttributeRequestIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = UpdateResourceExportTaskAttributeRequestVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class UpdateResourceExportTaskAttributeResponseBody(TeaModel):
    def __init__(self, export_task_id=None, export_version=None, request_id=None):
        self.export_task_id = export_task_id  # type: str
        self.export_version = export_version  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceExportTaskAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateResourceExportTaskAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceExportTaskAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceExportTaskAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceExportTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskAttributeRequestGroupInfo(TeaModel):
    def __init__(self, group_id=None, project_id=None):
        self.group_id = group_id  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskAttributeRequestGroupInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class UpdateTaskAttributeRequest(TeaModel):
    def __init__(self, auto_apply=None, group_info=None, module_id=None, module_version=None, name=None,
                 parameters=None, protection_strategy=None, ram_role=None, terraform_version=None, trigger_strategy=None):
        self.auto_apply = auto_apply  # type: bool
        self.group_info = group_info  # type: UpdateTaskAttributeRequestGroupInfo
        self.module_id = module_id  # type: str
        self.module_version = module_version  # type: str
        self.name = name  # type: str
        self.parameters = parameters  # type: dict[str, str]
        self.protection_strategy = protection_strategy  # type: list[str]
        self.ram_role = ram_role  # type: str
        self.terraform_version = terraform_version  # type: str
        self.trigger_strategy = trigger_strategy  # type: str

    def validate(self):
        if self.group_info:
            self.group_info.validate()

    def to_map(self):
        _map = super(UpdateTaskAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('groupInfo') is not None:
            temp_model = UpdateTaskAttributeRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class UpdateTaskAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskAttributeResponseBody, self).to_map()
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


class UpdateTaskAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTaskAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTaskAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


