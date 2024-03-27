# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeManualTaskRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManualTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeManualTaskResponseBody(TeaModel):
    def __init__(self, create_time=None, description=None, manual_task_id=None, manual_task_name=None,
                 parent_directory_id=None, project_id=None, resource_ids=None, task_params=None, task_type=None, update_time=None,
                 request_id=None):
        # 代表创建时间的资源属性字段
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 代表资源一级ID的资源属性字段
        self.manual_task_id = manual_task_id  # type: str
        # 代表资源名称的资源属性字段
        self.manual_task_name = manual_task_name  # type: str
        # 目录ID
        self.parent_directory_id = parent_directory_id  # type: str
        # 项目ID
        self.project_id = project_id  # type: str
        # 资源id列表
        self.resource_ids = resource_ids  # type: str
        # 任务参数
        self.task_params = task_params  # type: str
        # 任务类型
        self.task_type = task_type  # type: str
        # 更新时间
        self.update_time = update_time  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManualTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id
        if self.manual_task_name is not None:
            result['ManualTaskName'] = self.manual_task_name
        if self.parent_directory_id is not None:
            result['ParentDirectoryId'] = self.parent_directory_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')
        if m.get('ManualTaskName') is not None:
            self.manual_task_name = m.get('ManualTaskName')
        if m.get('ParentDirectoryId') is not None:
            self.parent_directory_id = m.get('ParentDirectoryId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeManualTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeManualTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeManualTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeManualTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeManualTaskInstanceRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManualTaskInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeManualTaskInstanceResponseBody(TeaModel):
    def __init__(self, emr_cluster_id=None, end_time=None, external_app_id=None, manual_task_instance_id=None,
                 manual_task_instance_name=None, resource_group_id=None, start_time=None, status=None, submit_time=None, task_params=None,
                 task_type=None, request_id=None):
        # EMR集群ID
        self.emr_cluster_id = emr_cluster_id  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 外部应用ID
        self.external_app_id = external_app_id  # type: str
        # 代表资源一级ID的资源属性字段
        self.manual_task_instance_id = manual_task_instance_id  # type: str
        # 代表资源名称的资源属性字段
        self.manual_task_instance_name = manual_task_instance_name  # type: str
        # 资源组ID
        self.resource_group_id = resource_group_id  # type: str
        # 开始时间
        self.start_time = start_time  # type: str
        # 状态
        self.status = status  # type: str
        # 提交时间
        self.submit_time = submit_time  # type: str
        # 任务参数
        self.task_params = task_params  # type: str
        # 任务类型
        self.task_type = task_type  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManualTaskInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_app_id is not None:
            result['ExternalAppId'] = self.external_app_id
        if self.manual_task_instance_id is not None:
            result['ManualTaskInstanceId'] = self.manual_task_instance_id
        if self.manual_task_instance_name is not None:
            result['ManualTaskInstanceName'] = self.manual_task_instance_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalAppId') is not None:
            self.external_app_id = m.get('ExternalAppId')
        if m.get('ManualTaskInstanceId') is not None:
            self.manual_task_instance_id = m.get('ManualTaskInstanceId')
        if m.get('ManualTaskInstanceName') is not None:
            self.manual_task_instance_name = m.get('ManualTaskInstanceName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeManualTaskInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeManualTaskInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeManualTaskInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeManualTaskInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeProjectResponseBody(TeaModel):
    def __init__(self, code=None, description=None, name=None, request_id=None):
        self.code = code  # type: long
        self.description = description  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeTaskResponseBody(TeaModel):
    def __init__(self, create_time=None, delay_time=None, description=None, fail_retry_interval=None,
                 fail_retry_times=None, flag=None, project_id=None, resource_ids=None, task_id=None, task_name=None, task_params=None,
                 task_priority=None, task_type=None, timeout=None, timeout_flag=None, timeout_notify_strategy=None,
                 update_time=None, version=None, request_id=None):
        # 代表创建时间的资源属性字段
        self.create_time = create_time  # type: str
        # 延时执行时间
        self.delay_time = delay_time  # type: int
        # 描述
        self.description = description  # type: str
        # 失败重试间隔
        self.fail_retry_interval = fail_retry_interval  # type: int
        # 失败重试次数
        self.fail_retry_times = fail_retry_times  # type: int
        # 运行标志
        self.flag = flag  # type: str
        # 项目ID
        self.project_id = project_id  # type: str
        # 资源ID列表
        self.resource_ids = resource_ids  # type: str
        # 代表资源一级ID的资源属性字段
        self.task_id = task_id  # type: str
        # 代表资源名称的资源属性字段
        self.task_name = task_name  # type: str
        # 任务参数
        self.task_params = task_params  # type: str
        # 任务优先级
        self.task_priority = task_priority  # type: str
        # 任务类型
        self.task_type = task_type  # type: str
        # 超时时长
        self.timeout = timeout  # type: int
        # 超时告警标志
        self.timeout_flag = timeout_flag  # type: str
        # 超时告警标志
        self.timeout_notify_strategy = timeout_notify_strategy  # type: str
        # 更新时间
        self.update_time = update_time  # type: str
        # 版本
        self.version = version  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.description is not None:
            result['Description'] = self.description
        if self.fail_retry_interval is not None:
            result['FailRetryInterval'] = self.fail_retry_interval
        if self.fail_retry_times is not None:
            result['FailRetryTimes'] = self.fail_retry_times
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_priority is not None:
            result['TaskPriority'] = self.task_priority
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_flag is not None:
            result['TimeoutFlag'] = self.timeout_flag
        if self.timeout_notify_strategy is not None:
            result['TimeoutNotifyStrategy'] = self.timeout_notify_strategy
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailRetryInterval') is not None:
            self.fail_retry_interval = m.get('FailRetryInterval')
        if m.get('FailRetryTimes') is not None:
            self.fail_retry_times = m.get('FailRetryTimes')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskPriority') is not None:
            self.task_priority = m.get('TaskPriority')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutFlag') is not None:
            self.timeout_flag = m.get('TimeoutFlag')
        if m.get('TimeoutNotifyStrategy') is not None:
            self.timeout_notify_strategy = m.get('TimeoutNotifyStrategy')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskInstanceRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeTaskInstanceResponseBody(TeaModel):
    def __init__(self, dry_run=None, emr_cluster_id=None, end_time=None, external_app_id=None,
                 resource_group_id=None, retry_times=None, start_time=None, status=None, submit_time=None, task_id=None,
                 task_instance_id=None, task_instance_name=None, task_params=None, task_type=None, task_version=None,
                 workflow_instance_id=None, request_id=None):
        # 空跑标识
        self.dry_run = dry_run  # type: str
        # EMR集群ID
        self.emr_cluster_id = emr_cluster_id  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 外部应用ID
        self.external_app_id = external_app_id  # type: str
        # 资源组ID
        self.resource_group_id = resource_group_id  # type: str
        # 重试次数
        self.retry_times = retry_times  # type: int
        # 开始时间
        self.start_time = start_time  # type: str
        # 状态
        self.status = status  # type: str
        # 提交时间
        self.submit_time = submit_time  # type: str
        # 任务ID
        self.task_id = task_id  # type: str
        # 任务实例ID
        self.task_instance_id = task_instance_id  # type: str
        # 任务实例名称
        self.task_instance_name = task_instance_name  # type: str
        # 任务参数
        self.task_params = task_params  # type: str
        # 任务类型
        self.task_type = task_type  # type: str
        # 任务版本
        self.task_version = task_version  # type: str
        # 工作流实例ID
        self.workflow_instance_id = workflow_instance_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_app_id is not None:
            result['ExternalAppId'] = self.external_app_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id
        if self.task_instance_name is not None:
            result['TaskInstanceName'] = self.task_instance_name
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalAppId') is not None:
            self.external_app_id = m.get('ExternalAppId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')
        if m.get('TaskInstanceName') is not None:
            self.task_instance_name = m.get('TaskInstanceName')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeTaskInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTaskInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTaskInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkflowRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeWorkflowResponseBodyTaskRelations(TeaModel):
    def __init__(self, name=None, post_task_id=None, post_task_version=None, pre_task_id=None,
                 pre_task_version=None):
        self.name = name  # type: str
        self.post_task_id = post_task_id  # type: long
        self.post_task_version = post_task_version  # type: int
        self.pre_task_id = pre_task_id  # type: long
        self.pre_task_version = pre_task_version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWorkflowResponseBodyTaskRelations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.post_task_id is not None:
            result['postTaskId'] = self.post_task_id
        if self.post_task_version is not None:
            result['postTaskVersion'] = self.post_task_version
        if self.pre_task_id is not None:
            result['preTaskId'] = self.pre_task_id
        if self.pre_task_version is not None:
            result['preTaskVersion'] = self.pre_task_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('postTaskId') is not None:
            self.post_task_id = m.get('postTaskId')
        if m.get('postTaskVersion') is not None:
            self.post_task_version = m.get('postTaskVersion')
        if m.get('preTaskId') is not None:
            self.pre_task_id = m.get('preTaskId')
        if m.get('preTaskVersion') is not None:
            self.pre_task_version = m.get('preTaskVersion')
        return self


class DescribeWorkflowResponseBodyTasks(TeaModel):
    def __init__(self, description=None, name=None, task_id=None, version=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.task_id = task_id  # type: long
        self.version = version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWorkflowResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeWorkflowResponseBody(TeaModel):
    def __init__(self, request_id=None, task_relations=None, tasks=None):
        self.request_id = request_id  # type: str
        self.task_relations = task_relations  # type: list[DescribeWorkflowResponseBodyTaskRelations]
        self.tasks = tasks  # type: list[DescribeWorkflowResponseBodyTasks]

    def validate(self):
        if self.task_relations:
            for k in self.task_relations:
                if k:
                    k.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWorkflowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['taskRelations'] = []
        if self.task_relations is not None:
            for k in self.task_relations:
                result['taskRelations'].append(k.to_map() if k else None)
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.task_relations = []
        if m.get('taskRelations') is not None:
            for k in m.get('taskRelations'):
                temp_model = DescribeWorkflowResponseBodyTaskRelations()
                self.task_relations.append(temp_model.from_map(k))
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = DescribeWorkflowResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DescribeWorkflowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWorkflowResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWorkflowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkflowInstanceRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWorkflowInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeWorkflowInstanceResponseBody(TeaModel):
    def __init__(self, emr_cluster_id=None, end_date=None, is_complement_data=None, name=None, request_id=None,
                 resource_group_id=None, run_times=None, schedule_time=None, start_date=None, state=None, timeout=None,
                 workflow_id=None, workflow_version=None):
        self.emr_cluster_id = emr_cluster_id  # type: str
        self.end_date = end_date  # type: str
        self.is_complement_data = is_complement_data  # type: bool
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.run_times = run_times  # type: int
        self.schedule_time = schedule_time  # type: str
        self.start_date = start_date  # type: str
        self.state = state  # type: str
        self.timeout = timeout  # type: int
        self.workflow_id = workflow_id  # type: long
        self.workflow_version = workflow_version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWorkflowInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emr_cluster_id is not None:
            result['emrClusterId'] = self.emr_cluster_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.is_complement_data is not None:
            result['isComplementData'] = self.is_complement_data
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.run_times is not None:
            result['runTimes'] = self.run_times
        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.state is not None:
            result['state'] = self.state
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workflow_version is not None:
            result['workflowVersion'] = self.workflow_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('emrClusterId') is not None:
            self.emr_cluster_id = m.get('emrClusterId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('isComplementData') is not None:
            self.is_complement_data = m.get('isComplementData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('runTimes') is not None:
            self.run_times = m.get('runTimes')
        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workflowVersion') is not None:
            self.workflow_version = m.get('workflowVersion')
        return self


class DescribeWorkflowInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWorkflowInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWorkflowInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWorkflowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListManualTaskInstancesRequest(TeaModel):
    def __init__(self, end_time=None, execution_status=None, max_results=None, next_token=None, search_val=None,
                 start_time=None, workspace_id=None):
        self.end_time = end_time  # type: str
        self.execution_status = execution_status  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.search_val = search_val  # type: str
        self.start_time = start_time  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListManualTaskInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_status is not None:
            result['executionStatus'] = self.execution_status
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionStatus') is not None:
            self.execution_status = m.get('executionStatus')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListManualTaskInstancesResponseBodyData(TeaModel):
    def __init__(self, emr_cluster_id=None, end_time=None, external_app_id=None, manual_task_instance_id=None,
                 manual_task_instance_name=None, resource_group_id=None, start_time=None, status=None, submit_time=None, task_params=None,
                 task_type=None):
        # EMR集群ID
        self.emr_cluster_id = emr_cluster_id  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 外部应用ID
        self.external_app_id = external_app_id  # type: str
        # 代表资源一级ID的资源属性字段
        self.manual_task_instance_id = manual_task_instance_id  # type: str
        # 代表资源名称的资源属性字段
        self.manual_task_instance_name = manual_task_instance_name  # type: str
        # 资源组ID
        self.resource_group_id = resource_group_id  # type: str
        # 开始时间
        self.start_time = start_time  # type: str
        # 状态
        self.status = status  # type: str
        # 提交时间
        self.submit_time = submit_time  # type: str
        # 任务参数
        self.task_params = task_params  # type: str
        # 任务类型
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListManualTaskInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_app_id is not None:
            result['ExternalAppId'] = self.external_app_id
        if self.manual_task_instance_id is not None:
            result['ManualTaskInstanceId'] = self.manual_task_instance_id
        if self.manual_task_instance_name is not None:
            result['ManualTaskInstanceName'] = self.manual_task_instance_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalAppId') is not None:
            self.external_app_id = m.get('ExternalAppId')
        if m.get('ManualTaskInstanceId') is not None:
            self.manual_task_instance_id = m.get('ManualTaskInstanceId')
        if m.get('ManualTaskInstanceName') is not None:
            self.manual_task_instance_name = m.get('ManualTaskInstanceName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListManualTaskInstancesResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None, total_size=None):
        self.data = data  # type: list[ListManualTaskInstancesResponseBodyData]
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListManualTaskInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListManualTaskInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListManualTaskInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListManualTaskInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListManualTaskInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListManualTaskInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListManualTasksRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, search_val=None, task_type=None, workspace_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.search_val = search_val  # type: str
        self.task_type = task_type  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListManualTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListManualTasksResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, manual_task_id=None, manual_task_name=None,
                 parent_directory_id=None, project_id=None, resource_ids=None, task_params=None, task_type=None, update_time=None):
        # 代表创建时间的资源属性字段
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 代表资源一级ID的资源属性字段
        self.manual_task_id = manual_task_id  # type: str
        # 代表资源名称的资源属性字段
        self.manual_task_name = manual_task_name  # type: str
        # 目录ID
        self.parent_directory_id = parent_directory_id  # type: str
        # 项目ID
        self.project_id = project_id  # type: str
        # 资源id列表
        self.resource_ids = resource_ids  # type: str
        # 任务参数
        self.task_params = task_params  # type: str
        # 任务类型
        self.task_type = task_type  # type: str
        # 更新时间
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListManualTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id
        if self.manual_task_name is not None:
            result['ManualTaskName'] = self.manual_task_name
        if self.parent_directory_id is not None:
            result['ParentDirectoryId'] = self.parent_directory_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')
        if m.get('ManualTaskName') is not None:
            self.manual_task_name = m.get('ManualTaskName')
        if m.get('ParentDirectoryId') is not None:
            self.parent_directory_id = m.get('ParentDirectoryId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListManualTasksResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None, total_size=None):
        self.data = data  # type: list[ListManualTasksResponseBodyData]
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListManualTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListManualTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListManualTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListManualTasksResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListManualTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListManualTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, search_val=None, workspace_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.search_val = search_val  # type: str
        self.workspace_id = workspace_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListProjectsResponseBodyData(TeaModel):
    def __init__(self, code=None, description=None, name=None, project_id=None):
        self.code = code  # type: long
        self.description = description  # type: str
        self.name = name  # type: str
        self.project_id = project_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None):
        self.data = data  # type: list[ListProjectsResponseBodyData]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectsResponseBody

    def validate(self):
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


class ListTaskInstancesRequest(TeaModel):
    def __init__(self, end_time=None, execution_status=None, max_results=None, next_token=None, search_val=None,
                 start_time=None, workflow_instance_id=None, workspace_id=None):
        self.end_time = end_time  # type: str
        self.execution_status = execution_status  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.search_val = search_val  # type: str
        self.start_time = start_time  # type: str
        self.workflow_instance_id = workflow_instance_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_status is not None:
            result['executionStatus'] = self.execution_status
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionStatus') is not None:
            self.execution_status = m.get('executionStatus')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('workflowInstanceId') is not None:
            self.workflow_instance_id = m.get('workflowInstanceId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListTaskInstancesResponseBodyData(TeaModel):
    def __init__(self, dry_run=None, emr_cluster_id=None, end_time=None, external_app_id=None,
                 resource_group_id=None, retry_times=None, start_time=None, status=None, submit_time=None, task_id=None,
                 task_instance_id=None, task_instance_name=None, task_params=None, task_type=None, task_version=None,
                 workflow_instance_id=None):
        # 空跑标识
        self.dry_run = dry_run  # type: str
        # EMR集群ID
        self.emr_cluster_id = emr_cluster_id  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 外部应用ID
        self.external_app_id = external_app_id  # type: str
        # 资源组ID
        self.resource_group_id = resource_group_id  # type: str
        # 重试次数
        self.retry_times = retry_times  # type: int
        # 开始时间
        self.start_time = start_time  # type: str
        # 状态
        self.status = status  # type: str
        # 提交时间
        self.submit_time = submit_time  # type: str
        # 任务ID
        self.task_id = task_id  # type: str
        # 任务实例ID
        self.task_instance_id = task_instance_id  # type: str
        # 任务实例名称
        self.task_instance_name = task_instance_name  # type: str
        # 任务参数
        self.task_params = task_params  # type: str
        # 任务类型
        self.task_type = task_type  # type: str
        # 任务版本
        self.task_version = task_version  # type: str
        # 工作流实例ID
        self.workflow_instance_id = workflow_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_app_id is not None:
            result['ExternalAppId'] = self.external_app_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id
        if self.task_instance_name is not None:
            result['TaskInstanceName'] = self.task_instance_name
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalAppId') is not None:
            self.external_app_id = m.get('ExternalAppId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')
        if m.get('TaskInstanceName') is not None:
            self.task_instance_name = m.get('TaskInstanceName')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        return self


class ListTaskInstancesResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None, total_size=None):
        self.data = data  # type: list[ListTaskInstancesResponseBodyData]
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListTaskInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListTaskInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTaskInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTaskInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTaskInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, search_val=None, task_type=None, workflow_id=None,
                 workspace_id=None):
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.search_val = search_val  # type: str
        self.task_type = task_type  # type: str
        self.workflow_id = workflow_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListTasksResponseBodyData(TeaModel):
    def __init__(self, create_time=None, delay_time=None, description=None, fail_retry_interval=None,
                 fail_retry_times=None, flag=None, project_id=None, resource_ids=None, task_id=None, task_name=None, task_params=None,
                 task_priority=None, task_type=None, timeout=None, timeout_flag=None, timeout_notify_strategy=None,
                 update_time=None, version=None):
        # 代表创建时间的资源属性字段
        self.create_time = create_time  # type: str
        # 延时执行时间
        self.delay_time = delay_time  # type: int
        # 描述
        self.description = description  # type: str
        # 失败重试间隔
        self.fail_retry_interval = fail_retry_interval  # type: int
        # 失败重试次数
        self.fail_retry_times = fail_retry_times  # type: int
        # 运行标志
        self.flag = flag  # type: str
        # 项目ID
        self.project_id = project_id  # type: str
        # 资源ID列表
        self.resource_ids = resource_ids  # type: str
        # 代表资源一级ID的资源属性字段
        self.task_id = task_id  # type: str
        # 代表资源名称的资源属性字段
        self.task_name = task_name  # type: str
        # 任务参数
        self.task_params = task_params  # type: str
        # 任务优先级
        self.task_priority = task_priority  # type: str
        # 任务类型
        self.task_type = task_type  # type: str
        # 超时时长
        self.timeout = timeout  # type: int
        # 超时告警标志
        self.timeout_flag = timeout_flag  # type: str
        # 超时告警标志
        self.timeout_notify_strategy = timeout_notify_strategy  # type: str
        # 更新时间
        self.update_time = update_time  # type: str
        # 版本
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.description is not None:
            result['Description'] = self.description
        if self.fail_retry_interval is not None:
            result['FailRetryInterval'] = self.fail_retry_interval
        if self.fail_retry_times is not None:
            result['FailRetryTimes'] = self.fail_retry_times
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_priority is not None:
            result['TaskPriority'] = self.task_priority
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_flag is not None:
            result['TimeoutFlag'] = self.timeout_flag
        if self.timeout_notify_strategy is not None:
            result['TimeoutNotifyStrategy'] = self.timeout_notify_strategy
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailRetryInterval') is not None:
            self.fail_retry_interval = m.get('FailRetryInterval')
        if m.get('FailRetryTimes') is not None:
            self.fail_retry_times = m.get('FailRetryTimes')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskPriority') is not None:
            self.task_priority = m.get('TaskPriority')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutFlag') is not None:
            self.timeout_flag = m.get('TimeoutFlag')
        if m.get('TimeoutNotifyStrategy') is not None:
            self.timeout_notify_strategy = m.get('TimeoutNotifyStrategy')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None, total_size=None):
        self.data = data  # type: list[ListTasksResponseBodyData]
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTasksResponseBody

    def validate(self):
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


class ListWorkflowInstancesRequest(TeaModel):
    def __init__(self, end_date=None, max_results=None, next_token=None, start_date=None, workflow_id=None,
                 workspace_id=None):
        self.end_date = end_date  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.start_date = start_date  # type: str
        self.workflow_id = workflow_id  # type: long
        self.workspace_id = workspace_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListWorkflowInstancesResponseBodyData(TeaModel):
    def __init__(self, end_date=None, name=None, run_times=None, schedule_time=None, start_date=None, state=None,
                 workflow_id=None, workflow_instance_id=None, workflow_version=None):
        self.end_date = end_date  # type: str
        self.name = name  # type: str
        self.run_times = run_times  # type: str
        self.schedule_time = schedule_time  # type: str
        self.start_date = start_date  # type: str
        self.state = state  # type: str
        self.workflow_id = workflow_id  # type: long
        self.workflow_instance_id = workflow_instance_id  # type: long
        self.workflow_version = workflow_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.name is not None:
            result['name'] = self.name
        if self.run_times is not None:
            result['runTimes'] = self.run_times
        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.state is not None:
            result['state'] = self.state
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id
        if self.workflow_version is not None:
            result['workflowVersion'] = self.workflow_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('runTimes') is not None:
            self.run_times = m.get('runTimes')
        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workflowInstanceId') is not None:
            self.workflow_instance_id = m.get('workflowInstanceId')
        if m.get('workflowVersion') is not None:
            self.workflow_version = m.get('workflowVersion')
        return self


class ListWorkflowInstancesResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None, total_size=None):
        self.data = data  # type: list[ListWorkflowInstancesResponseBodyData]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkflowInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListWorkflowInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListWorkflowInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListWorkflowInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkflowInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWorkflowInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkflowsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, search_val=None, workspace_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.search_val = search_val  # type: str
        self.workspace_id = workspace_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListWorkflowsResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, name=None, release_state=None, update_time=None,
                 workflow_id=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.release_state = release_state  # type: str
        self.update_time = update_time  # type: str
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.release_state is not None:
            result['releaseState'] = self.release_state
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('releaseState') is not None:
            self.release_state = m.get('releaseState')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        return self


class ListWorkflowsResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None, total_size=None):
        self.data = data  # type: list[ListWorkflowsResponseBodyData]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkflowsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListWorkflowsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListWorkflowsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListWorkflowsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkflowsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWorkflowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


