# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CheckCallbackRequest(TeaModel):
    def __init__(self, callback_result_string=None, region_id=None):
        self.callback_result_string = callback_result_string  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_result_string is not None:
            result['CallbackResultString'] = self.callback_result_string
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackResultString') is not None:
            self.callback_result_string = m.get('CallbackResultString')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None, return_code=None, return_value=None):
        self.request_id = request_id  # type: str
        self.return_code = return_code  # type: str
        self.return_value = return_value  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')
        return self


class CheckCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckCallbackResponse, self).to_map()
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
            temp_model = CheckCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateManualDagRequest(TeaModel):
    def __init__(self, bizdate=None, dag_para=None, flow_name=None, node_para=None, project_name=None,
                 region_id=None):
        self.bizdate = bizdate  # type: str
        self.dag_para = dag_para  # type: str
        self.flow_name = flow_name  # type: str
        self.node_para = node_para  # type: str
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateManualDagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate
        if self.dag_para is not None:
            result['DagPara'] = self.dag_para
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.node_para is not None:
            result['NodePara'] = self.node_para
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')
        if m.get('DagPara') is not None:
            self.dag_para = m.get('DagPara')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('NodePara') is not None:
            self.node_para = m.get('NodePara')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateManualDagResponseBody(TeaModel):
    def __init__(self, request_id=None, return_code=None, return_error_solution=None, return_message=None,
                 return_value=None):
        self.request_id = request_id  # type: str
        self.return_code = return_code  # type: str
        self.return_error_solution = return_error_solution  # type: str
        self.return_message = return_message  # type: str
        self.return_value = return_value  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateManualDagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.return_error_solution is not None:
            result['ReturnErrorSolution'] = self.return_error_solution
        if self.return_message is not None:
            result['ReturnMessage'] = self.return_message
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('ReturnErrorSolution') is not None:
            self.return_error_solution = m.get('ReturnErrorSolution')
        if m.get('ReturnMessage') is not None:
            self.return_message = m.get('ReturnMessage')
        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')
        return self


class CreateManualDagResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateManualDagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateManualDagResponse, self).to_map()
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
            temp_model = CreateManualDagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRealTimeProcessRequest(TeaModel):
    def __init__(self, action_type=None, create_res_group=None, data_source=None, dataworks_version=None,
                 file_id=None, job_config=None, project_id=None, region_id=None, resource_spec=None, table_rule=None,
                 tables=None):
        self.action_type = action_type  # type: str
        self.create_res_group = create_res_group  # type: bool
        self.data_source = data_source  # type: str
        self.dataworks_version = dataworks_version  # type: str
        self.file_id = file_id  # type: long
        self.job_config = job_config  # type: str
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_spec = resource_spec  # type: str
        self.table_rule = table_rule  # type: str
        self.tables = tables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRealTimeProcessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.create_res_group is not None:
            result['CreateResGroup'] = self.create_res_group
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.dataworks_version is not None:
            result['DataworksVersion'] = self.dataworks_version
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.job_config is not None:
            result['JobConfig'] = self.job_config
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec
        if self.table_rule is not None:
            result['TableRule'] = self.table_rule
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('CreateResGroup') is not None:
            self.create_res_group = m.get('CreateResGroup')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('DataworksVersion') is not None:
            self.dataworks_version = m.get('DataworksVersion')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('JobConfig') is not None:
            self.job_config = m.get('JobConfig')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceSpec') is not None:
            self.resource_spec = m.get('ResourceSpec')
        if m.get('TableRule') is not None:
            self.table_rule = m.get('TableRule')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class CreateRealTimeProcessResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRealTimeProcessResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateRealTimeProcessResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: CreateRealTimeProcessResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateRealTimeProcessResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateRealTimeProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRealTimeProcessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRealTimeProcessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRealTimeProcessResponse, self).to_map()
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
            temp_model = CreateRealTimeProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDISyncTaskRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, region_id=None, task_type=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDISyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DeleteDISyncTaskResponseBodyData(TeaModel):
    def __init__(self, message=None, status=None):
        self.message = message  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDISyncTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteDISyncTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DeleteDISyncTaskResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteDISyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDISyncTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDISyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDISyncTaskResponse, self).to_map()
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
            temp_model = DeleteDISyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, project_identifier=None, region_id=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.project_identifier = project_identifier  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployDISyncTaskRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, region_id=None, task_type=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployDISyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DeployDISyncTaskResponseBodyData(TeaModel):
    def __init__(self, message=None, status=None):
        self.message = message  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployDISyncTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeployDISyncTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DeployDISyncTaskResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeployDISyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeployDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeployDISyncTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeployDISyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployDISyncTaskResponse, self).to_map()
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
            temp_model = DeployDISyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEmrHiveTableRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, region_id=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.database_name = database_name  # type: str
        self.region_id = region_id  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEmrHiveTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeEmrHiveTableResponseBodyDataColumns(TeaModel):
    def __init__(self, column_comment=None, column_name=None, column_position=None, column_type=None, comment=None,
                 gmt_create=None, gmt_modified=None):
        self.column_comment = column_comment  # type: str
        self.column_name = column_name  # type: str
        self.column_position = column_position  # type: int
        self.column_type = column_type  # type: str
        self.comment = comment  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEmrHiveTableResponseBodyDataColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_comment is not None:
            result['ColumnComment'] = self.column_comment
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_position is not None:
            result['ColumnPosition'] = self.column_position
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ColumnComment') is not None:
            self.column_comment = m.get('ColumnComment')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnPosition') is not None:
            self.column_position = m.get('ColumnPosition')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeEmrHiveTableResponseBodyData(TeaModel):
    def __init__(self, cluster_biz_id=None, cluster_biz_name=None, columns=None, database_name=None,
                 gmt_create=None, gmt_modified=None, input_format=None, is_compressed=None, is_temporary=None,
                 last_access_time=None, last_modify_time=None, location=None, output_format=None, owner=None, owner_id=None,
                 owner_type=None, partition_keys=None, serialization_lib=None, table_comment=None, table_desc=None,
                 table_name=None, table_parameters=None, table_size=None, table_type=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.cluster_biz_name = cluster_biz_name  # type: str
        self.columns = columns  # type: list[DescribeEmrHiveTableResponseBodyDataColumns]
        self.database_name = database_name  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.input_format = input_format  # type: str
        self.is_compressed = is_compressed  # type: bool
        self.is_temporary = is_temporary  # type: bool
        self.last_access_time = last_access_time  # type: str
        self.last_modify_time = last_modify_time  # type: str
        self.location = location  # type: str
        self.output_format = output_format  # type: str
        self.owner = owner  # type: str
        self.owner_id = owner_id  # type: str
        self.owner_type = owner_type  # type: str
        self.partition_keys = partition_keys  # type: str
        self.serialization_lib = serialization_lib  # type: str
        self.table_comment = table_comment  # type: str
        self.table_desc = table_desc  # type: str
        self.table_name = table_name  # type: str
        self.table_parameters = table_parameters  # type: str
        self.table_size = table_size  # type: long
        self.table_type = table_type  # type: str

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEmrHiveTableResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_biz_name is not None:
            result['ClusterBizName'] = self.cluster_biz_name
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.is_compressed is not None:
            result['IsCompressed'] = self.is_compressed
        if self.is_temporary is not None:
            result['IsTemporary'] = self.is_temporary
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.partition_keys is not None:
            result['PartitionKeys'] = self.partition_keys
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        if self.table_comment is not None:
            result['TableComment'] = self.table_comment
        if self.table_desc is not None:
            result['TableDesc'] = self.table_desc
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_parameters is not None:
            result['TableParameters'] = self.table_parameters
        if self.table_size is not None:
            result['TableSize'] = self.table_size
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterBizName') is not None:
            self.cluster_biz_name = m.get('ClusterBizName')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = DescribeEmrHiveTableResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('IsCompressed') is not None:
            self.is_compressed = m.get('IsCompressed')
        if m.get('IsTemporary') is not None:
            self.is_temporary = m.get('IsTemporary')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('PartitionKeys') is not None:
            self.partition_keys = m.get('PartitionKeys')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        if m.get('TableComment') is not None:
            self.table_comment = m.get('TableComment')
        if m.get('TableDesc') is not None:
            self.table_desc = m.get('TableDesc')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableParameters') is not None:
            self.table_parameters = m.get('TableParameters')
        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class DescribeEmrHiveTableResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: DescribeEmrHiveTableResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEmrHiveTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeEmrHiveTableResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEmrHiveTableResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEmrHiveTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEmrHiveTableResponse, self).to_map()
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
            temp_model = DescribeEmrHiveTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDISyncInstanceInfoRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, region_id=None, task_type=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDISyncInstanceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetDISyncInstanceInfoResponseBodyData(TeaModel):
    def __init__(self, message=None, name=None, status=None):
        self.message = message  # type: str
        self.name = name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDISyncInstanceInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDISyncInstanceInfoResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: GetDISyncInstanceInfoResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDISyncInstanceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDISyncInstanceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDISyncInstanceInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDISyncInstanceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDISyncInstanceInfoResponse, self).to_map()
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
            temp_model = GetDISyncInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDISyncTaskRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, region_id=None, task_type=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDISyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetDISyncTaskResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, status=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDISyncTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDISyncTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: GetDISyncTaskResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDISyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDISyncTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDISyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDISyncTaskResponse, self).to_map()
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
            temp_model = GetDISyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSwitchValueRequest(TeaModel):
    def __init__(self, switch_name=None):
        self.switch_name = switch_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSwitchValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.switch_name is not None:
            result['SwitchName'] = self.switch_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SwitchName') is not None:
            self.switch_name = m.get('SwitchName')
        return self


class GetSwitchValueResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSwitchValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSwitchValueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSwitchValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSwitchValueResponse, self).to_map()
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
            temp_model = GetSwitchValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmrHiveAuditLogsRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, end_time=None, page_number=None, page_size=None,
                 region_id=None, start_time=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.database_name = database_name  # type: str
        self.end_time = end_time  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: int
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEmrHiveAuditLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListEmrHiveAuditLogsResponseBodyDataPagedData(TeaModel):
    def __init__(self, database=None, event_time=None, groups=None, operation=None, table=None, user=None):
        self.database = database  # type: str
        self.event_time = event_time  # type: long
        self.groups = groups  # type: list[str]
        self.operation = operation  # type: str
        self.table = table  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEmrHiveAuditLogsResponseBodyDataPagedData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.table is not None:
            result['Table'] = self.table
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class ListEmrHiveAuditLogsResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, paged_data=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.paged_data = paged_data  # type: list[ListEmrHiveAuditLogsResponseBodyDataPagedData]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.paged_data:
            for k in self.paged_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEmrHiveAuditLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListEmrHiveAuditLogsResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEmrHiveAuditLogsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListEmrHiveAuditLogsResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEmrHiveAuditLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListEmrHiveAuditLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEmrHiveAuditLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEmrHiveAuditLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEmrHiveAuditLogsResponse, self).to_map()
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
            temp_model = ListEmrHiveAuditLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmrHiveDatabasesRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEmrHiveDatabasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEmrHiveDatabasesResponseBodyData(TeaModel):
    def __init__(self, comment=None, gmt_create=None, gmt_modified=None, location=None, name=None, owner=None,
                 owner_id=None, owner_type=None, parameters=None, region=None, status=None, type=None):
        self.comment = comment  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.location = location  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.owner_id = owner_id  # type: str
        self.owner_type = owner_type  # type: str
        self.parameters = parameters  # type: str
        self.region = region  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEmrHiveDatabasesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListEmrHiveDatabasesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: list[ListEmrHiveDatabasesResponseBodyData]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEmrHiveDatabasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEmrHiveDatabasesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEmrHiveDatabasesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEmrHiveDatabasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEmrHiveDatabasesResponse, self).to_map()
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
            temp_model = ListEmrHiveDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmrHiveTablesRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, page_number=None, page_size=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.database_name = database_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEmrHiveTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEmrHiveTablesResponseBodyDataPagedData(TeaModel):
    def __init__(self, cluster_biz_id=None, cluster_biz_name=None, database_name=None, gmt_create=None,
                 gmt_modified=None, input_format=None, is_compressed=None, is_temporary=None, last_access_time=None,
                 last_modify_time=None, location=None, output_format=None, owner=None, owner_id=None, owner_type=None,
                 partition_keys=None, serialization_lib=None, table_comment=None, table_desc=None, table_name=None,
                 table_parameters=None, table_type=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.cluster_biz_name = cluster_biz_name  # type: str
        self.database_name = database_name  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.input_format = input_format  # type: str
        self.is_compressed = is_compressed  # type: bool
        self.is_temporary = is_temporary  # type: bool
        self.last_access_time = last_access_time  # type: str
        self.last_modify_time = last_modify_time  # type: str
        self.location = location  # type: str
        self.output_format = output_format  # type: str
        self.owner = owner  # type: str
        self.owner_id = owner_id  # type: str
        self.owner_type = owner_type  # type: str
        self.partition_keys = partition_keys  # type: str
        self.serialization_lib = serialization_lib  # type: str
        self.table_comment = table_comment  # type: str
        self.table_desc = table_desc  # type: str
        self.table_name = table_name  # type: str
        self.table_parameters = table_parameters  # type: str
        self.table_type = table_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEmrHiveTablesResponseBodyDataPagedData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_biz_name is not None:
            result['ClusterBizName'] = self.cluster_biz_name
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.is_compressed is not None:
            result['IsCompressed'] = self.is_compressed
        if self.is_temporary is not None:
            result['IsTemporary'] = self.is_temporary
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.partition_keys is not None:
            result['PartitionKeys'] = self.partition_keys
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        if self.table_comment is not None:
            result['TableComment'] = self.table_comment
        if self.table_desc is not None:
            result['TableDesc'] = self.table_desc
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_parameters is not None:
            result['TableParameters'] = self.table_parameters
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterBizName') is not None:
            self.cluster_biz_name = m.get('ClusterBizName')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('IsCompressed') is not None:
            self.is_compressed = m.get('IsCompressed')
        if m.get('IsTemporary') is not None:
            self.is_temporary = m.get('IsTemporary')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('PartitionKeys') is not None:
            self.partition_keys = m.get('PartitionKeys')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        if m.get('TableComment') is not None:
            self.table_comment = m.get('TableComment')
        if m.get('TableDesc') is not None:
            self.table_desc = m.get('TableDesc')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableParameters') is not None:
            self.table_parameters = m.get('TableParameters')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class ListEmrHiveTablesResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, paged_data=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.paged_data = paged_data  # type: list[ListEmrHiveTablesResponseBodyDataPagedData]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.paged_data:
            for k in self.paged_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEmrHiveTablesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListEmrHiveTablesResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEmrHiveTablesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListEmrHiveTablesResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEmrHiveTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListEmrHiveTablesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEmrHiveTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEmrHiveTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEmrHiveTablesResponse, self).to_map()
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
            temp_model = ListEmrHiveTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHiveColumnLineagesRequest(TeaModel):
    def __init__(self, cluster_id=None, column_name=None, database_name=None, region_id=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.column_name = column_name  # type: str
        self.database_name = database_name  # type: str
        self.region_id = region_id  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHiveColumnLineagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveColumnLineagesResponseBodyDataDownstreamLineages(TeaModel):
    def __init__(self, cluster_id=None, column_name=None, create_time=None, database_name=None,
                 direct_down_column_number=None, direct_down_table_number=None, direct_upper_column_number=None,
                 direct_upper_table_number=None, modified_time=None, source=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.column_name = column_name  # type: str
        self.create_time = create_time  # type: str
        self.database_name = database_name  # type: str
        self.direct_down_column_number = direct_down_column_number  # type: int
        self.direct_down_table_number = direct_down_table_number  # type: int
        self.direct_upper_column_number = direct_upper_column_number  # type: int
        self.direct_upper_table_number = direct_upper_table_number  # type: int
        self.modified_time = modified_time  # type: str
        self.source = source  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHiveColumnLineagesResponseBodyDataDownstreamLineages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.direct_down_column_number is not None:
            result['DirectDownColumnNumber'] = self.direct_down_column_number
        if self.direct_down_table_number is not None:
            result['DirectDownTableNumber'] = self.direct_down_table_number
        if self.direct_upper_column_number is not None:
            result['DirectUpperColumnNumber'] = self.direct_upper_column_number
        if self.direct_upper_table_number is not None:
            result['DirectUpperTableNumber'] = self.direct_upper_table_number
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DirectDownColumnNumber') is not None:
            self.direct_down_column_number = m.get('DirectDownColumnNumber')
        if m.get('DirectDownTableNumber') is not None:
            self.direct_down_table_number = m.get('DirectDownTableNumber')
        if m.get('DirectUpperColumnNumber') is not None:
            self.direct_upper_column_number = m.get('DirectUpperColumnNumber')
        if m.get('DirectUpperTableNumber') is not None:
            self.direct_upper_table_number = m.get('DirectUpperTableNumber')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveColumnLineagesResponseBodyDataUpstreamLineages(TeaModel):
    def __init__(self, cluster_id=None, column_name=None, create_time=None, database_name=None,
                 direct_down_column_number=None, direct_down_table_number=None, direct_upper_column_number=None,
                 direct_upper_table_number=None, modified_time=None, source=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.column_name = column_name  # type: str
        self.create_time = create_time  # type: str
        self.database_name = database_name  # type: str
        self.direct_down_column_number = direct_down_column_number  # type: int
        self.direct_down_table_number = direct_down_table_number  # type: int
        self.direct_upper_column_number = direct_upper_column_number  # type: int
        self.direct_upper_table_number = direct_upper_table_number  # type: int
        self.modified_time = modified_time  # type: str
        self.source = source  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHiveColumnLineagesResponseBodyDataUpstreamLineages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.direct_down_column_number is not None:
            result['DirectDownColumnNumber'] = self.direct_down_column_number
        if self.direct_down_table_number is not None:
            result['DirectDownTableNumber'] = self.direct_down_table_number
        if self.direct_upper_column_number is not None:
            result['DirectUpperColumnNumber'] = self.direct_upper_column_number
        if self.direct_upper_table_number is not None:
            result['DirectUpperTableNumber'] = self.direct_upper_table_number
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DirectDownColumnNumber') is not None:
            self.direct_down_column_number = m.get('DirectDownColumnNumber')
        if m.get('DirectDownTableNumber') is not None:
            self.direct_down_table_number = m.get('DirectDownTableNumber')
        if m.get('DirectUpperColumnNumber') is not None:
            self.direct_upper_column_number = m.get('DirectUpperColumnNumber')
        if m.get('DirectUpperTableNumber') is not None:
            self.direct_upper_table_number = m.get('DirectUpperTableNumber')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveColumnLineagesResponseBodyData(TeaModel):
    def __init__(self, downstream_lineages=None, downstream_number=None, upstream_lineages=None,
                 upstream_number=None):
        self.downstream_lineages = downstream_lineages  # type: list[ListHiveColumnLineagesResponseBodyDataDownstreamLineages]
        self.downstream_number = downstream_number  # type: int
        self.upstream_lineages = upstream_lineages  # type: list[ListHiveColumnLineagesResponseBodyDataUpstreamLineages]
        self.upstream_number = upstream_number  # type: int

    def validate(self):
        if self.downstream_lineages:
            for k in self.downstream_lineages:
                if k:
                    k.validate()
        if self.upstream_lineages:
            for k in self.upstream_lineages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHiveColumnLineagesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DownstreamLineages'] = []
        if self.downstream_lineages is not None:
            for k in self.downstream_lineages:
                result['DownstreamLineages'].append(k.to_map() if k else None)
        if self.downstream_number is not None:
            result['DownstreamNumber'] = self.downstream_number
        result['UpstreamLineages'] = []
        if self.upstream_lineages is not None:
            for k in self.upstream_lineages:
                result['UpstreamLineages'].append(k.to_map() if k else None)
        if self.upstream_number is not None:
            result['UpstreamNumber'] = self.upstream_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.downstream_lineages = []
        if m.get('DownstreamLineages') is not None:
            for k in m.get('DownstreamLineages'):
                temp_model = ListHiveColumnLineagesResponseBodyDataDownstreamLineages()
                self.downstream_lineages.append(temp_model.from_map(k))
        if m.get('DownstreamNumber') is not None:
            self.downstream_number = m.get('DownstreamNumber')
        self.upstream_lineages = []
        if m.get('UpstreamLineages') is not None:
            for k in m.get('UpstreamLineages'):
                temp_model = ListHiveColumnLineagesResponseBodyDataUpstreamLineages()
                self.upstream_lineages.append(temp_model.from_map(k))
        if m.get('UpstreamNumber') is not None:
            self.upstream_number = m.get('UpstreamNumber')
        return self


class ListHiveColumnLineagesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListHiveColumnLineagesResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListHiveColumnLineagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListHiveColumnLineagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHiveColumnLineagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHiveColumnLineagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHiveColumnLineagesResponse, self).to_map()
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
            temp_model = ListHiveColumnLineagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHiveTableLineagesRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, region_id=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.database_name = database_name  # type: str
        self.region_id = region_id  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHiveTableLineagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveTableLineagesResponseBodyDataDownstreamLineages(TeaModel):
    def __init__(self, cluster_id=None, create_time=None, database_name=None, engine=None, job_id=None,
                 modified_time=None, query_text=None, source=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.create_time = create_time  # type: str
        self.database_name = database_name  # type: str
        self.engine = engine  # type: str
        self.job_id = job_id  # type: str
        self.modified_time = modified_time  # type: str
        self.query_text = query_text  # type: str
        self.source = source  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHiveTableLineagesResponseBodyDataDownstreamLineages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.query_text is not None:
            result['QueryText'] = self.query_text
        if self.source is not None:
            result['Source'] = self.source
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveTableLineagesResponseBodyDataUpstreamLineages(TeaModel):
    def __init__(self, cluster_id=None, create_time=None, database_name=None, engine=None, job_id=None,
                 modified_time=None, query_text=None, source=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.create_time = create_time  # type: str
        self.database_name = database_name  # type: str
        self.engine = engine  # type: str
        self.job_id = job_id  # type: str
        self.modified_time = modified_time  # type: str
        self.query_text = query_text  # type: str
        self.source = source  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHiveTableLineagesResponseBodyDataUpstreamLineages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.query_text is not None:
            result['QueryText'] = self.query_text
        if self.source is not None:
            result['Source'] = self.source
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveTableLineagesResponseBodyData(TeaModel):
    def __init__(self, downstream_lineages=None, downstream_number=None, upstream_lineages=None,
                 upstream_number=None):
        self.downstream_lineages = downstream_lineages  # type: list[ListHiveTableLineagesResponseBodyDataDownstreamLineages]
        self.downstream_number = downstream_number  # type: int
        self.upstream_lineages = upstream_lineages  # type: list[ListHiveTableLineagesResponseBodyDataUpstreamLineages]
        self.upstream_number = upstream_number  # type: int

    def validate(self):
        if self.downstream_lineages:
            for k in self.downstream_lineages:
                if k:
                    k.validate()
        if self.upstream_lineages:
            for k in self.upstream_lineages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHiveTableLineagesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DownstreamLineages'] = []
        if self.downstream_lineages is not None:
            for k in self.downstream_lineages:
                result['DownstreamLineages'].append(k.to_map() if k else None)
        if self.downstream_number is not None:
            result['DownstreamNumber'] = self.downstream_number
        result['UpstreamLineages'] = []
        if self.upstream_lineages is not None:
            for k in self.upstream_lineages:
                result['UpstreamLineages'].append(k.to_map() if k else None)
        if self.upstream_number is not None:
            result['UpstreamNumber'] = self.upstream_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.downstream_lineages = []
        if m.get('DownstreamLineages') is not None:
            for k in m.get('DownstreamLineages'):
                temp_model = ListHiveTableLineagesResponseBodyDataDownstreamLineages()
                self.downstream_lineages.append(temp_model.from_map(k))
        if m.get('DownstreamNumber') is not None:
            self.downstream_number = m.get('DownstreamNumber')
        self.upstream_lineages = []
        if m.get('UpstreamLineages') is not None:
            for k in m.get('UpstreamLineages'):
                temp_model = ListHiveTableLineagesResponseBodyDataUpstreamLineages()
                self.upstream_lineages.append(temp_model.from_map(k))
        if m.get('UpstreamNumber') is not None:
            self.upstream_number = m.get('UpstreamNumber')
        return self


class ListHiveTableLineagesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListHiveTableLineagesResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListHiveTableLineagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListHiveTableLineagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHiveTableLineagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHiveTableLineagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHiveTableLineagesResponse, self).to_map()
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
            temp_model = ListHiveTableLineagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablePartitionsRequest(TeaModel):
    def __init__(self, cluster_id=None, database_name=None, order=None, page_number=None, page_size=None,
                 region_id=None, table_name=None):
        self.cluster_id = cluster_id  # type: str
        self.database_name = database_name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTablePartitionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListTablePartitionsResponseBodyDataPagedData(TeaModel):
    def __init__(self, gmt_create=None, gmt_modified=None, location=None, partition_comment=None,
                 partition_name=None, partition_path=None, partition_type=None):
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.location = location  # type: str
        self.partition_comment = partition_comment  # type: str
        self.partition_name = partition_name  # type: str
        self.partition_path = partition_path  # type: str
        self.partition_type = partition_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTablePartitionsResponseBodyDataPagedData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.location is not None:
            result['Location'] = self.location
        if self.partition_comment is not None:
            result['PartitionComment'] = self.partition_comment
        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name
        if self.partition_path is not None:
            result['PartitionPath'] = self.partition_path
        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('PartitionComment') is not None:
            self.partition_comment = m.get('PartitionComment')
        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')
        if m.get('PartitionPath') is not None:
            self.partition_path = m.get('PartitionPath')
        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')
        return self


class ListTablePartitionsResponseBodyData(TeaModel):
    def __init__(self, page_size=None, paged_data=None, total_count=None):
        self.page_size = page_size  # type: int
        self.paged_data = paged_data  # type: list[ListTablePartitionsResponseBodyDataPagedData]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.paged_data:
            for k in self.paged_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTablePartitionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListTablePartitionsResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTablePartitionsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListTablePartitionsResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTablePartitionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTablePartitionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTablePartitionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTablePartitionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTablePartitionsResponse, self).to_map()
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
            temp_model = ListTablePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDataWorksStandardServiceRequest(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDataWorksStandardServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class OpenDataWorksStandardServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDataWorksStandardServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenDataWorksStandardServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenDataWorksStandardServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenDataWorksStandardServiceResponse, self).to_map()
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
            temp_model = OpenDataWorksStandardServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataImportProcessRequest(TeaModel):
    def __init__(self, region_id=None, sub_uid=None):
        self.region_id = region_id  # type: str
        self.sub_uid = sub_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDataImportProcessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        return self


class QueryDataImportProcessResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDataImportProcessResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDataImportProcessResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: QueryDataImportProcessResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDataImportProcessResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryDataImportProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDataImportProcessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryDataImportProcessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDataImportProcessResponse, self).to_map()
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
            temp_model = QueryDataImportProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataImportProcessStatusRequest(TeaModel):
    def __init__(self, region_id=None, task_id=None):
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDataImportProcessStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDataImportProcessStatusResponseBodyDataProjectList(TeaModel):
    def __init__(self, project_id=None, project_identifier=None, project_name=None):
        self.project_id = project_id  # type: str
        self.project_identifier = project_identifier  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDataImportProcessStatusResponseBodyDataProjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class QueryDataImportProcessStatusResponseBodyData(TeaModel):
    def __init__(self, message=None, project_list=None, status=None):
        self.message = message  # type: str
        self.project_list = project_list  # type: list[QueryDataImportProcessStatusResponseBodyDataProjectList]
        self.status = status  # type: str

    def validate(self):
        if self.project_list:
            for k in self.project_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDataImportProcessStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        result['ProjectList'] = []
        if self.project_list is not None:
            for k in self.project_list:
                result['ProjectList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.project_list = []
        if m.get('ProjectList') is not None:
            for k in m.get('ProjectList'):
                temp_model = QueryDataImportProcessStatusResponseBodyDataProjectList()
                self.project_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDataImportProcessStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: QueryDataImportProcessStatusResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDataImportProcessStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryDataImportProcessStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDataImportProcessStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryDataImportProcessStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDataImportProcessStatusResponse, self).to_map()
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
            temp_model = QueryDataImportProcessStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRealTimeProcessStatusRequest(TeaModel):
    def __init__(self, region_id=None, task_id=None):
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRealTimeProcessStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryRealTimeProcessStatusResponseBodyData(TeaModel):
    def __init__(self, file_id=None, message=None, project_id=None, status=None, task_id=None, task_url=None):
        self.file_id = file_id  # type: long
        self.message = message  # type: str
        self.project_id = project_id  # type: long
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.task_url = task_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRealTimeProcessStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.message is not None:
            result['Message'] = self.message
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_url is not None:
            result['TaskUrl'] = self.task_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskUrl') is not None:
            self.task_url = m.get('TaskUrl')
        return self


class QueryRealTimeProcessStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: QueryRealTimeProcessStatusResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRealTimeProcessStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryRealTimeProcessStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRealTimeProcessStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRealTimeProcessStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRealTimeProcessStatusResponse, self).to_map()
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
            temp_model = QueryRealTimeProcessStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchManualDagNodeInstanceRequest(TeaModel):
    def __init__(self, dag_id=None, project_name=None, region_id=None):
        self.dag_id = dag_id  # type: long
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchManualDagNodeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchManualDagNodeInstanceResponseBodyDataNodeInsInfo(TeaModel):
    def __init__(self, begin_running_time=None, begin_wait_res_time=None, begin_wait_time_time=None, bizdate=None,
                 create_time=None, dag_id=None, dag_type=None, finish_time=None, instance_id=None, modify_time=None,
                 node_name=None, para_value=None, status=None):
        self.begin_running_time = begin_running_time  # type: str
        self.begin_wait_res_time = begin_wait_res_time  # type: str
        self.begin_wait_time_time = begin_wait_time_time  # type: str
        self.bizdate = bizdate  # type: str
        self.create_time = create_time  # type: str
        self.dag_id = dag_id  # type: long
        self.dag_type = dag_type  # type: int
        self.finish_time = finish_time  # type: str
        self.instance_id = instance_id  # type: long
        self.modify_time = modify_time  # type: str
        self.node_name = node_name  # type: str
        self.para_value = para_value  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchManualDagNodeInstanceResponseBodyDataNodeInsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_running_time is not None:
            result['BeginRunningTime'] = self.begin_running_time
        if self.begin_wait_res_time is not None:
            result['BeginWaitResTime'] = self.begin_wait_res_time
        if self.begin_wait_time_time is not None:
            result['BeginWaitTimeTime'] = self.begin_wait_time_time
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.dag_type is not None:
            result['DagType'] = self.dag_type
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.para_value is not None:
            result['ParaValue'] = self.para_value
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginRunningTime') is not None:
            self.begin_running_time = m.get('BeginRunningTime')
        if m.get('BeginWaitResTime') is not None:
            self.begin_wait_res_time = m.get('BeginWaitResTime')
        if m.get('BeginWaitTimeTime') is not None:
            self.begin_wait_time_time = m.get('BeginWaitTimeTime')
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('DagType') is not None:
            self.dag_type = m.get('DagType')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SearchManualDagNodeInstanceResponseBodyData(TeaModel):
    def __init__(self, node_ins_info=None):
        self.node_ins_info = node_ins_info  # type: list[SearchManualDagNodeInstanceResponseBodyDataNodeInsInfo]

    def validate(self):
        if self.node_ins_info:
            for k in self.node_ins_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchManualDagNodeInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInsInfo'] = []
        if self.node_ins_info is not None:
            for k in self.node_ins_info:
                result['NodeInsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_ins_info = []
        if m.get('NodeInsInfo') is not None:
            for k in m.get('NodeInsInfo'):
                temp_model = SearchManualDagNodeInstanceResponseBodyDataNodeInsInfo()
                self.node_ins_info.append(temp_model.from_map(k))
        return self


class SearchManualDagNodeInstanceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, request_id=None, success=None):
        self.data = data  # type: SearchManualDagNodeInstanceResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SearchManualDagNodeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SearchManualDagNodeInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchManualDagNodeInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SearchManualDagNodeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchManualDagNodeInstanceResponse, self).to_map()
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
            temp_model = SearchManualDagNodeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTaskMetaCallbackRequest(TeaModel):
    def __init__(self, code=None, connection_info=None, end_time=None, region_id=None, resources=None,
                 start_time=None, sub_type=None, task_env_param=None, tenant_id=None, type=None, user=None):
        self.code = code  # type: str
        self.connection_info = connection_info  # type: str
        self.end_time = end_time  # type: long
        self.region_id = region_id  # type: str
        self.resources = resources  # type: list[str]
        self.start_time = start_time  # type: long
        self.sub_type = sub_type  # type: str
        self.task_env_param = task_env_param  # type: str
        self.tenant_id = tenant_id  # type: long
        self.type = type  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTaskMetaCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.connection_info is not None:
            result['ConnectionInfo'] = self.connection_info
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.task_env_param is not None:
            result['TaskEnvParam'] = self.task_env_param
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConnectionInfo') is not None:
            self.connection_info = m.get('ConnectionInfo')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('TaskEnvParam') is not None:
            self.task_env_param = m.get('TaskEnvParam')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class SendTaskMetaCallbackResponseBody(TeaModel):
    def __init__(self, data=None, err_msg=None, error_code=None, request_id=None):
        self.data = data  # type: str
        self.err_msg = err_msg  # type: str
        self.error_code = error_code  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTaskMetaCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendTaskMetaCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendTaskMetaCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendTaskMetaCallbackResponse, self).to_map()
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
            temp_model = SendTaskMetaCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDISyncInstanceRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, region_id=None, start_param=None, task_type=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.start_param = start_param  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDISyncInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_param is not None:
            result['StartParam'] = self.start_param
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartParam') is not None:
            self.start_param = m.get('StartParam')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class StartDISyncInstanceResponseBodyData(TeaModel):
    def __init__(self, message=None, status=None):
        self.message = message  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDISyncInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class StartDISyncInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: StartDISyncInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StartDISyncInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StartDISyncInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartDISyncInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartDISyncInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDISyncInstanceResponse, self).to_map()
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
            temp_model = StartDISyncInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDISyncInstanceRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, region_id=None, task_type=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDISyncInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class StopDISyncInstanceResponseBodyData(TeaModel):
    def __init__(self, message=None, status=None):
        self.message = message  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDISyncInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class StopDISyncInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: StopDISyncInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StopDISyncInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StopDISyncInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopDISyncInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopDISyncInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDISyncInstanceResponse, self).to_map()
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
            temp_model = StopDISyncInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateDISyncInstanceRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, region_id=None, task_type=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TerminateDISyncInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class TerminateDISyncInstanceResponseBodyData(TeaModel):
    def __init__(self, message=None, status=None):
        self.message = message  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TerminateDISyncInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class TerminateDISyncInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: TerminateDISyncInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TerminateDISyncInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = TerminateDISyncInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TerminateDISyncInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TerminateDISyncInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TerminateDISyncInstanceResponse, self).to_map()
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
            temp_model = TerminateDISyncInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerDataLoaderResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerDataLoaderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TriggerDataLoaderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TriggerDataLoaderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerDataLoaderResponse, self).to_map()
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
            temp_model = TriggerDataLoaderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDISyncTaskRequest(TeaModel):
    def __init__(self, file_id=None, project_id=None, region_id=None, task_content=None, task_param=None,
                 task_type=None):
        self.file_id = file_id  # type: long
        self.project_id = project_id  # type: long
        self.region_id = region_id  # type: str
        self.task_content = task_content  # type: str
        self.task_param = task_param  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDISyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_content is not None:
            result['TaskContent'] = self.task_content
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskContent') is not None:
            self.task_content = m.get('TaskContent')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class UpdateDISyncTaskResponseBodyData(TeaModel):
    def __init__(self, message=None, status=None):
        self.message = message  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDISyncTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateDISyncTaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: UpdateDISyncTaskResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateDISyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDISyncTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDISyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDISyncTaskResponse, self).to_map()
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
            temp_model = UpdateDISyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


