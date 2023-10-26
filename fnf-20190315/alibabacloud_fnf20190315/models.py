# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateFlowRequest(TeaModel):
    def __init__(self, definition=None, description=None, execution_mode=None, external_storage_location=None,
                 name=None, request_id=None, role_arn=None, type=None):
        # The definition of the flow. The definition must comply with the Flow Definition Language (FDL) syntax.
        self.definition = definition  # type: str
        # The description of the flow.
        self.description = description  # type: str
        # The execution mode or the enumeration type. Valid values: Express and Standard. The value Standard indicates an empty string.
        self.execution_mode = execution_mode  # type: str
        # The path of the external storage.
        self.external_storage_location = external_storage_location  # type: str
        # The name of the flow. The name is unique within the region and cannot be modified after the flow is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.name = name  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The Alibaba Cloud resource name (ARN) of the specified Resource Access Management (RAM) role that Serverless Workflow assumes to invoke resources when the task is executed.
        self.role_arn = role_arn  # type: str
        # The type of the flow. Valid value: **FDL**.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.external_storage_location is not None:
            result['ExternalStorageLocation'] = self.external_storage_location
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('ExternalStorageLocation') is not None:
            self.external_storage_location = m.get('ExternalStorageLocation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(self, created_time=None, definition=None, description=None, execution_mode=None, id=None,
                 last_modified_time=None, name=None, request_id=None, role_arn=None, type=None):
        # The time when the flow was created.
        self.created_time = created_time  # type: str
        # The definition of the flow.
        self.definition = definition  # type: str
        # The description of the flow.
        self.description = description  # type: str
        # The execution mode or the enumeration type. Valid values: Express and Standard. The value Standard indicates an empty string.
        self.execution_mode = execution_mode  # type: str
        # The unique ID of the flow.
        self.id = id  # type: str
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The name of the flow.
        self.name = name  # type: str
        # The request ID. Each time an `HTTP status code` is returned, Serverless Workflow returns a value for the parameter.
        self.request_id = request_id  # type: str
        # The ARN of the RAM role.
        self.role_arn = role_arn  # type: str
        # The type of the flow.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduleRequest(TeaModel):
    def __init__(self, cron_expression=None, description=None, enable=None, flow_name=None, payload=None,
                 request_id=None, schedule_name=None):
        # The CRON expression.
        self.cron_expression = cron_expression  # type: str
        # The description of the time-based schedule.
        self.description = description  # type: str
        # Specifies whether to enable the time-based schedule. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable  # type: bool
        # The name of the flow that is bound to the time-based schedule.
        self.flow_name = flow_name  # type: str
        # The trigger message of the time-based schedule. Specify the value in the JSON format.
        self.payload = payload  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The name of the time-based schedule. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.schedule_name = schedule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class CreateScheduleResponseBody(TeaModel):
    def __init__(self, created_time=None, cron_expression=None, description=None, enable=None,
                 last_modified_time=None, payload=None, request_id=None, schedule_id=None, schedule_name=None):
        # The time when the time-based schedule was created.
        self.created_time = created_time  # type: str
        # The CRON expression.
        self.cron_expression = cron_expression  # type: str
        # The description of the time-based schedule.
        self.description = description  # type: str
        # Indicates whether the time-based schedule is enabled.
        self.enable = enable  # type: bool
        # The time when the time-based schedule was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The trigger message of the time-based schedule.
        self.payload = payload  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id  # type: str
        # The name of the time-based schedule.
        self.schedule_name = schedule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class CreateScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateScheduleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(self, name=None, request_id=None):
        # The name of the flow. The name can contain letters, digits, underscores (\_), and hyphens (-) only. It cannot start with a digit or a hyphen (-). It must be 1 to 128 characters in length.
        self.name = name  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowResponseBody, self).to_map()
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


class DeleteFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduleRequest(TeaModel):
    def __init__(self, flow_name=None, request_id=None, schedule_name=None):
        # The name of the flow that is associated with the time-based schedule. The name is unique within the region and cannot be modified after the time-based schedule is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The name of the time-based schedule. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.schedule_name = schedule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class DeleteScheduleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleResponseBody, self).to_map()
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


class DeleteScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteScheduleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExecutionRequest(TeaModel):
    def __init__(self, execution_name=None, flow_name=None, request_id=None, wait_time_seconds=None):
        # The name of the execution, which is unique within a flow. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.execution_name = execution_name  # type: str
        # The name of the flow. The name is unique within the region and cannot be modified after the flow is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The maximum period of time for long polling waits. Valid values: 0 to 60. Unit: seconds. Configure this parameter based on the following rules:
        # 
        # *   If the value is 0, the system immediately returns the current execution status.
        # *   If the value is greater than 0, the long polling request waits until the execution ends or the specified period elapses.
        self.wait_time_seconds = wait_time_seconds  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.wait_time_seconds is not None:
            result['WaitTimeSeconds'] = self.wait_time_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WaitTimeSeconds') is not None:
            self.wait_time_seconds = m.get('WaitTimeSeconds')
        return self


class DescribeExecutionResponseBody(TeaModel):
    def __init__(self, flow_definition=None, flow_name=None, input=None, name=None, output=None, request_id=None,
                 started_time=None, status=None, stopped_time=None):
        # The definition of the flow.
        self.flow_definition = flow_definition  # type: str
        # The name of the flow.
        self.flow_name = flow_name  # type: str
        # The input of the execution, which is in the JSON format.
        self.input = input  # type: str
        # The name of the execution.
        self.name = name  # type: str
        # The execution result, which is in the JSON format.
        self.output = output  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The time when the execution started.
        self.started_time = started_time  # type: str
        # The execution state. Valid values:
        # 
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status  # type: str
        # The time when the execution stopped.
        self.stopped_time = stopped_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExecutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class DescribeExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExecutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowRequest(TeaModel):
    def __init__(self, name=None, request_id=None):
        # The name of the flow.
        self.name = name  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowResponseBody(TeaModel):
    def __init__(self, created_time=None, definition=None, description=None, execution_mode=None, id=None,
                 last_modified_time=None, name=None, request_id=None, role_arn=None, type=None):
        # The time when the flow was created.
        self.created_time = created_time  # type: str
        # The definition of the flow. The definition must comply with the Flow Definition Language (FDL) syntax.
        self.definition = definition  # type: str
        # The description of the flow.
        self.description = description  # type: str
        # The execution mode or the enumeration type. Valid values: Express and Standard. The value Standard indicates an empty string.
        self.execution_mode = execution_mode  # type: str
        # The unique ID of the flow.
        self.id = id  # type: str
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The name of the flow.
        self.name = name  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.role_arn = role_arn  # type: str
        # The type of the flow. Valid value: **FDL**.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduleRequest(TeaModel):
    def __init__(self, flow_name=None, request_id=None, schedule_name=None):
        # The name of the flow that is associated with the time-based schedule. The name is unique within the region and cannot be modified after the time-based schedule is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The name of the time-based schedule. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.schedule_name = schedule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class DescribeScheduleResponseBody(TeaModel):
    def __init__(self, created_time=None, cron_expression=None, description=None, enable=None,
                 last_modified_time=None, payload=None, request_id=None, schedule_id=None, schedule_name=None):
        # The time when the time-based schedule was created.
        self.created_time = created_time  # type: str
        # The CRON expression.
        self.cron_expression = cron_expression  # type: str
        # The description of the time-based schedule.
        self.description = description  # type: str
        # Indicates whether the time-based schedule is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable  # type: bool
        # The time when the time-based schedule was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The trigger message of the time-based schedule.
        self.payload = payload  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id  # type: str
        # The name of the time-based schedule.
        self.schedule_name = schedule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class DescribeScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeScheduleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecutionHistoryRequest(TeaModel):
    def __init__(self, execution_name=None, flow_name=None, limit=None, next_token=None, request_id=None):
        # The name of the execution, which is unique within a flow. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.execution_name = execution_name  # type: str
        # The name of the flow. The name is unique within the region and cannot be modified after the flow is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The maximum number of steps to be queried. Valid values: 1 to 1000.
        self.limit = limit  # type: int
        # The name of the event to start the query. You can obtain the value from the response data.
        self.next_token = next_token  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExecutionHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExecutionHistoryResponseBodyEvents(TeaModel):
    def __init__(self, event_detail=None, event_id=None, schedule_event_id=None, step_name=None, time=None,
                 type=None):
        # The details about the execution step.
        self.event_detail = event_detail  # type: str
        # The ID of the execution step.
        self.event_id = event_id  # type: long
        # The ID of the scheduling step.
        self.schedule_event_id = schedule_event_id  # type: long
        # The name of the execution step.
        self.step_name = step_name  # type: str
        # The time when the event was updated.
        self.time = time  # type: str
        # The type of the execution step. Valid values:
        # 
        # *   **StepEntered**\
        # *   **StepStarted**\
        # *   **StepSucceeded**\
        # *   **StepFailed**\
        # *   **StepExited**\
        # *   **BranchEntered**\
        # *   **BranchExited**\
        # *   **IterationEntered**\
        # *   **IterationExited**\
        # *   **TaskScheduled**\
        # *   **TaskStarted**\
        # *   **TaskSubmitted**\
        # *   **TaskSubmitFailed**\
        # *   **TaskSucceeded**\
        # *   **TaskFailed**\
        # *   **TaskTimedOut**\
        # *   **ExecutionStarted**\
        # *   **ExecutionStopped**\
        # *   **ExecutionSucceeded**\
        # *   **ExecutionFailed**\
        # *   **ExecutionTimedOut**\
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExecutionHistoryResponseBodyEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_detail is not None:
            result['EventDetail'] = self.event_detail
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.schedule_event_id is not None:
            result['ScheduleEventId'] = self.schedule_event_id
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventDetail') is not None:
            self.event_detail = m.get('EventDetail')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('ScheduleEventId') is not None:
            self.schedule_event_id = m.get('ScheduleEventId')
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExecutionHistoryResponseBody(TeaModel):
    def __init__(self, events=None, next_token=None, request_id=None):
        # The events.
        self.events = events  # type: list[GetExecutionHistoryResponseBodyEvents]
        # You do not need to specify this parameter for the first request. The returned value of **ScheduleEventId** is used as the token for the next query. No value is returned for the last query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetExecutionHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = GetExecutionHistoryResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExecutionHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetExecutionHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExecutionHistoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExecutionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionsRequest(TeaModel):
    def __init__(self, execution_name_prefix=None, flow_name=None, limit=None, next_token=None, request_id=None,
                 started_time_begin=None, started_time_end=None, status=None):
        # The name prefix of the execution.
        self.execution_name_prefix = execution_name_prefix  # type: str
        # The name of the flow. The name is unique within the region and cannot be modified after the flow is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The maximum number of executions to be queried. Valid values: 1 to 100.
        self.limit = limit  # type: int
        # The name of the execution to start the query. You can obtain the value from the response data. You do not need to specify this parameter for the first request.
        self.next_token = next_token  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The beginning of the time range to query executions. Specify the value in the UTC RFC3339 format.
        self.started_time_begin = started_time_begin  # type: str
        # The end of the time range to query executions. Specify the value in the UTC RFC3339 format.
        self.started_time_end = started_time_end  # type: str
        # The state of the execution that you want to filter. Valid values:
        # 
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name_prefix is not None:
            result['ExecutionNamePrefix'] = self.execution_name_prefix
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time_begin is not None:
            result['StartedTimeBegin'] = self.started_time_begin
        if self.started_time_end is not None:
            result['StartedTimeEnd'] = self.started_time_end
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionNamePrefix') is not None:
            self.execution_name_prefix = m.get('ExecutionNamePrefix')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTimeBegin') is not None:
            self.started_time_begin = m.get('StartedTimeBegin')
        if m.get('StartedTimeEnd') is not None:
            self.started_time_end = m.get('StartedTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExecutionsResponseBodyExecutions(TeaModel):
    def __init__(self, flow_definition=None, flow_name=None, input=None, name=None, output=None, started_time=None,
                 status=None, stopped_time=None):
        # The definition of the flow.
        self.flow_definition = flow_definition  # type: str
        # The name of the flow.
        self.flow_name = flow_name  # type: str
        # The input of the execution, which is in the JSON format.
        self.input = input  # type: str
        # The name of the execution.
        self.name = name  # type: str
        # The execution result, which is in the JSON format.
        self.output = output  # type: str
        # The time when the execution started.
        self.started_time = started_time  # type: str
        # The state of the execution.
        self.status = status  # type: str
        # The time when the execution stopped.
        self.stopped_time = stopped_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutionsResponseBodyExecutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class ListExecutionsResponseBody(TeaModel):
    def __init__(self, executions=None, next_token=None, request_id=None):
        # The queried executions.
        self.executions = executions  # type: list[ListExecutionsResponseBodyExecutions]
        # The start key for the next query. This parameter is not returned if all results have been returned.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.executions:
            for k in self.executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExecutionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executions'] = []
        if self.executions is not None:
            for k in self.executions:
                result['Executions'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.executions = []
        if m.get('Executions') is not None:
            for k in m.get('Executions'):
                temp_model = ListExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExecutionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExecutionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExecutionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, request_id=None):
        # The number of flows to be queried. Valid values: 1 to 1000.
        self.limit = limit  # type: int
        # The token to start the query.
        self.next_token = next_token  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowsResponseBodyFlows(TeaModel):
    def __init__(self, created_time=None, definition=None, description=None, execution_mode=None, id=None,
                 last_modified_time=None, name=None, role_arn=None, type=None):
        # The time when the flow was created.
        self.created_time = created_time  # type: str
        # The definition of the flow. The definition must comply with the Flow Definition Language (FDL) syntax.
        self.definition = definition  # type: str
        # The description of the flow.
        self.description = description  # type: str
        # The execution mode or the enumeration type. Valid values: Express and Standard. The value Standard indicates an empty string.
        self.execution_mode = execution_mode  # type: str
        # The unique ID of the flow.
        self.id = id  # type: str
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The name of the flow.
        self.name = name  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role.
        self.role_arn = role_arn  # type: str
        # The type of the flow.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowsResponseBodyFlows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowsResponseBody(TeaModel):
    def __init__(self, flows=None, next_token=None, request_id=None):
        # The details of flows.
        self.flows = flows  # type: list[ListFlowsResponseBodyFlows]
        # The start key for the next query. This parameter is not returned if all results have been returned.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListFlowsResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFlowsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchedulesRequest(TeaModel):
    def __init__(self, flow_name=None, limit=None, next_token=None, request_id=None):
        # The name of the flow that is associated with the time-based schedule. The name is unique within the region and cannot be modified after the time-based schedule is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The number of schedules to be queried. Valid values: 1 to 1000.
        self.limit = limit  # type: int
        # For the first query, you do not need to specify this parameter. The system uses the value of the **FlowName** parameter as the value of the **NextToken** parameter. When the query ends, no value is returned for this parameter.
        self.next_token = next_token  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSchedulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSchedulesResponseBodySchedules(TeaModel):
    def __init__(self, created_time=None, cron_expression=None, description=None, enable=None,
                 last_modified_time=None, payload=None, schedule_id=None, schedule_name=None):
        # The time when the time-based schedule was created.
        self.created_time = created_time  # type: str
        # The CRON expression of the scheduled task.
        self.cron_expression = cron_expression  # type: str
        # The description of the time-based schedule.
        self.description = description  # type: str
        # Indicates whether the time-based schedule is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable  # type: bool
        # The time when the time-based schedule was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The trigger message of the time-based schedule.
        self.payload = payload  # type: str
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id  # type: str
        # The name of the time-based schedule.
        self.schedule_name = schedule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSchedulesResponseBodySchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class ListSchedulesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, schedules=None):
        # The token for the next query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The time-based schedules that are queried.
        self.schedules = schedules  # type: list[ListSchedulesResponseBodySchedules]

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSchedulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = ListSchedulesResponseBodySchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class ListSchedulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSchedulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSchedulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportTaskFailedRequest(TeaModel):
    def __init__(self, cause=None, error=None, request_id=None, task_token=None):
        # The cause of the failure. The value must be 1 to 4,096 characters in length.
        self.cause = cause  # type: str
        # The error code for the failed task. The value must be 1 to 128 characters in length.
        self.error = error  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The token of the specified task that you want to report. If this parameter appears in **waitforCallback** mode, the parameter is passed to the called service, such as Message Service (MNS) or Function Compute. For MNS, the value of this parameter can be obtained from a message. For Function Compute, the value of this parameter can be obtained from an event.
        self.task_token = task_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportTaskFailedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.error is not None:
            result['Error'] = self.error
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_token is not None:
            result['TaskToken'] = self.task_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskToken') is not None:
            self.task_token = m.get('TaskToken')
        return self


class ReportTaskFailedResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None):
        # The ID of the event.
        self.event_id = event_id  # type: long
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportTaskFailedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportTaskFailedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportTaskFailedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportTaskFailedResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReportTaskFailedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportTaskSucceededRequest(TeaModel):
    def __init__(self, output=None, request_id=None, task_token=None):
        # The output information of the task whose execution success you want to report.
        self.output = output  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The token of the task whose execution success you want to report. If this parameter appears in **waitforCallback** mode, the parameter is passed to the called service, such as Message Service (MNS) or Function Compute. For MNS, the value of this parameter can be obtained from the message. For Function Compute, the value of this parameter can be obtained from the event.
        self.task_token = task_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportTaskSucceededRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_token is not None:
            result['TaskToken'] = self.task_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskToken') is not None:
            self.task_token = m.get('TaskToken')
        return self


class ReportTaskSucceededResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None):
        # The ID of the event.
        self.event_id = event_id  # type: long
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportTaskSucceededResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportTaskSucceededResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportTaskSucceededResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportTaskSucceededResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReportTaskSucceededResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartExecutionRequest(TeaModel):
    def __init__(self, callback_fn_ftask_token=None, execution_name=None, flow_name=None, input=None,
                 request_id=None):
        # Specifies that the **TaskToken**-related tasks are called back after the execution in the flow ends.
        self.callback_fn_ftask_token = callback_fn_ftask_token  # type: str
        # The name of the execution, which is unique within a flow. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.execution_name = execution_name  # type: str
        # The name of the flow you want to start to execute. The name is unique within the region and cannot be modified after the flow is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The input of the execution, which is in the JSON format.
        self.input = input  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_fn_ftask_token is not None:
            result['CallbackFnFTaskToken'] = self.callback_fn_ftask_token
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackFnFTaskToken') is not None:
            self.callback_fn_ftask_token = m.get('CallbackFnFTaskToken')
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartExecutionResponseBody(TeaModel):
    def __init__(self, flow_definition=None, flow_name=None, input=None, name=None, output=None, request_id=None,
                 started_time=None, status=None, stopped_time=None):
        # The definition of the flow.
        self.flow_definition = flow_definition  # type: str
        # The name of the flow.
        self.flow_name = flow_name  # type: str
        # The input of the execution, which is in the JSON format.
        self.input = input  # type: str
        # The name of the execution.
        self.name = name  # type: str
        # The execution result, which is in the JSON format.
        self.output = output  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The time when the execution started.
        self.started_time = started_time  # type: str
        # The execution state. Valid values:
        # 
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status  # type: str
        # The time when the execution stopped.
        self.stopped_time = stopped_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartExecutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class StartExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartExecutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSyncExecutionRequest(TeaModel):
    def __init__(self, execution_name=None, flow_name=None, input=None, request_id=None):
        self.execution_name = execution_name  # type: str
        self.flow_name = flow_name  # type: str
        self.input = input  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartSyncExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartSyncExecutionResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, flow_name=None, name=None, output=None, request_id=None,
                 started_time=None, status=None, stopped_time=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.flow_name = flow_name  # type: str
        self.name = name  # type: str
        self.output = output  # type: str
        self.request_id = request_id  # type: str
        self.started_time = started_time  # type: str
        self.status = status  # type: str
        self.stopped_time = stopped_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartSyncExecutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class StartSyncExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartSyncExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartSyncExecutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartSyncExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopExecutionRequest(TeaModel):
    def __init__(self, cause=None, error=None, execution_name=None, flow_name=None, request_id=None):
        # The reason for stopping the execution. The value must be 1 to 4,096 characters in length.
        self.cause = cause  # type: str
        # The error for stopping the execution. The value must be 1 to 128 characters in length.
        self.error = error  # type: str
        # The name of the execution that you want to stop. You can call the **ListExecutions** operation to obtain the value of this parameter. The name is unique in a flow. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.execution_name = execution_name  # type: str
        # The name of the flow that you want to stop. You can call the **ListFlows** operation to obtain the value of this parameter. The name is unique within the region and cannot be modified after the flow is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopExecutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.error is not None:
            result['Error'] = self.error
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopExecutionResponseBody(TeaModel):
    def __init__(self, flow_definition=None, flow_name=None, input=None, name=None, output=None, request_id=None,
                 started_time=None, status=None, stopped_time=None):
        # The definition of the flow.
        self.flow_definition = flow_definition  # type: str
        # The name of the flow.
        self.flow_name = flow_name  # type: str
        # The input of the execution, which is in the JSON format.
        self.input = input  # type: str
        # The name of the execution.
        self.name = name  # type: str
        # The execution result, which is in the JSON format.
        self.output = output  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The time when the execution started.
        self.started_time = started_time  # type: str
        # The execution state. Valid values:
        # 
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status  # type: str
        # The time when the execution stopped.
        self.stopped_time = stopped_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopExecutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class StopExecutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopExecutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopExecutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowRequest(TeaModel):
    def __init__(self, definition=None, description=None, name=None, request_id=None, role_arn=None, type=None):
        # The definition of the flow. The definition must comply with the Flow Definition Language (FDL) syntax.
        self.definition = definition  # type: str
        # The description of the flow.
        self.description = description  # type: str
        # The name of the flow. The name is unique within the region and cannot be modified after the time-based schedule is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.name = name  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The Alibaba Cloud resource name (ARN) of the specified Resource Access Management (RAM) role that Serverless Workflow assumes to invoke resources when the task is executed.
        self.role_arn = role_arn  # type: str
        # The type of the flow. Valid value: **FDL**.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateFlowResponseBody(TeaModel):
    def __init__(self, created_time=None, definition=None, description=None, external_storage_location=None,
                 id=None, last_modified_time=None, name=None, request_id=None, role_arn=None, type=None):
        # The time when the flow was created.
        self.created_time = created_time  # type: str
        # The definition of the flow.
        self.definition = definition  # type: str
        # The description of the flow.
        self.description = description  # type: str
        # The path of the external storage.
        self.external_storage_location = external_storage_location  # type: str
        # The unique ID of the flow.
        self.id = id  # type: str
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The name of the flow.
        self.name = name  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The ARN of the RAM role.
        self.role_arn = role_arn  # type: str
        # The type of the flow.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.external_storage_location is not None:
            result['ExternalStorageLocation'] = self.external_storage_location
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExternalStorageLocation') is not None:
            self.external_storage_location = m.get('ExternalStorageLocation')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateScheduleRequest(TeaModel):
    def __init__(self, cron_expression=None, description=None, enable=None, flow_name=None, payload=None,
                 request_id=None, schedule_name=None):
        # The CRON expression.
        self.cron_expression = cron_expression  # type: str
        # The description of the time-based schedule.
        self.description = description  # type: str
        # Specifies whether to enable the time-based schedule. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable  # type: bool
        # The name of the flow that is associated with the time-based schedule. The name is unique within the region and cannot be modified after the time-based schedule is created. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.flow_name = flow_name  # type: str
        # The trigger message of the time-based schedule. It must be in the JSON format.
        self.payload = payload  # type: str
        # The request ID. If you specify this parameter, the system uses this value as the ID of the request. If you do not specify this parameter, the system generates a value at random.
        self.request_id = request_id  # type: str
        # The name of the time-based schedule. Configure this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must start with a letter or an underscore (\_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.schedule_name = schedule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class UpdateScheduleResponseBody(TeaModel):
    def __init__(self, created_time=None, cron_expression=None, description=None, enable=None,
                 last_modified_time=None, payload=None, request_id=None, schedule_id=None, schedule_name=None):
        # The time when the time-based schedule was created.
        self.created_time = created_time  # type: str
        # The CRON expression.
        self.cron_expression = cron_expression  # type: str
        # The description of the time-based schedule.
        self.description = description  # type: str
        # Indicates whether the time-based schedule is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable  # type: bool
        # The time when the time-based schedule was last updated.
        self.last_modified_time = last_modified_time  # type: str
        # The trigger message of the time-based schedule.
        self.payload = payload  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id  # type: str
        # The name of the time-based schedule.
        self.schedule_name = schedule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class UpdateScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateScheduleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


