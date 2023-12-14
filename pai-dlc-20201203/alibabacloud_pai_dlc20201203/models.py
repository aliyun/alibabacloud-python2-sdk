# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AliyunAccounts(TeaModel):
    def __init__(self, aliyun_uid=None, employee_id=None, gmt_create_time=None, gmt_modify_time=None):
        self.aliyun_uid = aliyun_uid  # type: str
        self.employee_id = employee_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AliyunAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.employee_id is not None:
            result['EmployeeId'] = self.employee_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('EmployeeId') is not None:
            self.employee_id = m.get('EmployeeId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        return self


class CodeSourceItem(TeaModel):
    def __init__(self, code_branch=None, code_commit=None, code_repo=None, code_repo_access_token=None,
                 code_repo_user_name=None, code_source_id=None, description=None, display_name=None, gmt_create_time=None,
                 gmt_modify_time=None, user_id=None):
        self.code_branch = code_branch  # type: str
        self.code_commit = code_commit  # type: str
        self.code_repo = code_repo  # type: str
        self.code_repo_access_token = code_repo_access_token  # type: str
        self.code_repo_user_name = code_repo_user_name  # type: str
        self.code_source_id = code_source_id  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CodeSourceItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_branch is not None:
            result['CodeBranch'] = self.code_branch
        if self.code_commit is not None:
            result['CodeCommit'] = self.code_commit
        if self.code_repo is not None:
            result['CodeRepo'] = self.code_repo
        if self.code_repo_access_token is not None:
            result['CodeRepoAccessToken'] = self.code_repo_access_token
        if self.code_repo_user_name is not None:
            result['CodeRepoUserName'] = self.code_repo_user_name
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeBranch') is not None:
            self.code_branch = m.get('CodeBranch')
        if m.get('CodeCommit') is not None:
            self.code_commit = m.get('CodeCommit')
        if m.get('CodeRepo') is not None:
            self.code_repo = m.get('CodeRepo')
        if m.get('CodeRepoAccessToken') is not None:
            self.code_repo_access_token = m.get('CodeRepoAccessToken')
        if m.get('CodeRepoUserName') is not None:
            self.code_repo_user_name = m.get('CodeRepoUserName')
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ContainerSpec(TeaModel):
    def __init__(self, args=None, command=None, env=None, image=None, name=None, resources=None, working_dir=None):
        self.args = args  # type: list[str]
        self.command = command  # type: list[str]
        self.env = env  # type: list[EnvVar]
        self.image = image  # type: str
        self.name = name  # type: str
        self.resources = resources  # type: ResourceRequirements
        self.working_dir = working_dir  # type: str

    def validate(self):
        if self.env:
            for k in self.env:
                if k:
                    k.validate()
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super(ContainerSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.command is not None:
            result['Command'] = self.command
        result['Env'] = []
        if self.env is not None:
            for k in self.env:
                result['Env'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        self.env = []
        if m.get('Env') is not None:
            for k in m.get('Env'):
                temp_model = EnvVar()
                self.env.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Resources') is not None:
            temp_model = ResourceRequirements()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DataSourceItem(TeaModel):
    def __init__(self, data_source_id=None, data_source_type=None, description=None, display_name=None,
                 endpoint=None, file_system_id=None, gmt_create_time=None, gmt_modify_time=None, mount_path=None,
                 options=None, path=None, user_id=None):
        self.data_source_id = data_source_id  # type: str
        self.data_source_type = data_source_type  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.endpoint = endpoint  # type: str
        self.file_system_id = file_system_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str
        self.mount_path = mount_path  # type: str
        self.options = options  # type: str
        self.path = path  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSourceItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.options is not None:
            result['Options'] = self.options
        if self.path is not None:
            result['Path'] = self.path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DebuggerConfig(TeaModel):
    def __init__(self, content=None, debugger_config_id=None, description=None, display_name=None,
                 gmt_create_time=None, gmt_modify_time=None):
        self.content = content  # type: str
        self.debugger_config_id = debugger_config_id  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DebuggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.debugger_config_id is not None:
            result['DebuggerConfigId'] = self.debugger_config_id
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DebuggerConfigId') is not None:
            self.debugger_config_id = m.get('DebuggerConfigId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        return self


class DebuggerJob(TeaModel):
    def __init__(self, debugger_job_id=None, display_name=None, duration=None, gmt_create_time=None,
                 gmt_failed_time=None, gmt_finish_time=None, gmt_running_time=None, gmt_stopped_time=None, gmt_submitted_time=None,
                 gmt_succeed_time=None, status=None, user_id=None, workspace_id=None, workspace_name=None):
        self.debugger_job_id = debugger_job_id  # type: str
        self.display_name = display_name  # type: str
        self.duration = duration  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_failed_time = gmt_failed_time  # type: str
        self.gmt_finish_time = gmt_finish_time  # type: str
        self.gmt_running_time = gmt_running_time  # type: str
        self.gmt_stopped_time = gmt_stopped_time  # type: str
        self.gmt_submitted_time = gmt_submitted_time  # type: str
        self.gmt_succeed_time = gmt_succeed_time  # type: str
        self.status = status  # type: str
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DebuggerJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debugger_job_id is not None:
            result['DebuggerJobId'] = self.debugger_job_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_failed_time is not None:
            result['GmtFailedTime'] = self.gmt_failed_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_running_time is not None:
            result['GmtRunningTime'] = self.gmt_running_time
        if self.gmt_stopped_time is not None:
            result['GmtStoppedTime'] = self.gmt_stopped_time
        if self.gmt_submitted_time is not None:
            result['GmtSubmittedTime'] = self.gmt_submitted_time
        if self.gmt_succeed_time is not None:
            result['GmtSucceedTime'] = self.gmt_succeed_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DebuggerJobId') is not None:
            self.debugger_job_id = m.get('DebuggerJobId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFailedTime') is not None:
            self.gmt_failed_time = m.get('GmtFailedTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtRunningTime') is not None:
            self.gmt_running_time = m.get('GmtRunningTime')
        if m.get('GmtStoppedTime') is not None:
            self.gmt_stopped_time = m.get('GmtStoppedTime')
        if m.get('GmtSubmittedTime') is not None:
            self.gmt_submitted_time = m.get('GmtSubmittedTime')
        if m.get('GmtSucceedTime') is not None:
            self.gmt_succeed_time = m.get('GmtSucceedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class DebuggerJobIssue(TeaModel):
    def __init__(self, debugger_job_issue=None, gmt_create_time=None, job_debugger_issue_id=None, job_id=None,
                 reason_code=None, reason_message=None, rule_name=None):
        self.debugger_job_issue = debugger_job_issue  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.job_debugger_issue_id = job_debugger_issue_id  # type: str
        self.job_id = job_id  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DebuggerJobIssue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debugger_job_issue is not None:
            result['DebuggerJobIssue'] = self.debugger_job_issue
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.job_debugger_issue_id is not None:
            result['JobDebuggerIssueId'] = self.job_debugger_issue_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DebuggerJobIssue') is not None:
            self.debugger_job_issue = m.get('DebuggerJobIssue')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JobDebuggerIssueId') is not None:
            self.job_debugger_issue_id = m.get('JobDebuggerIssueId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DebuggerResult(TeaModel):
    def __init__(self, debugger_config_content=None, debugger_job_issues=None, debugger_job_status=None,
                 debugger_report_url=None, job_display_name=None, job_id=None, job_user_id=None):
        self.debugger_config_content = debugger_config_content  # type: str
        self.debugger_job_issues = debugger_job_issues  # type: str
        self.debugger_job_status = debugger_job_status  # type: str
        self.debugger_report_url = debugger_report_url  # type: str
        self.job_display_name = job_display_name  # type: str
        self.job_id = job_id  # type: str
        self.job_user_id = job_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DebuggerResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content
        if self.debugger_job_issues is not None:
            result['DebuggerJobIssues'] = self.debugger_job_issues
        if self.debugger_job_status is not None:
            result['DebuggerJobStatus'] = self.debugger_job_status
        if self.debugger_report_url is not None:
            result['DebuggerReportURL'] = self.debugger_report_url
        if self.job_display_name is not None:
            result['JobDisplayName'] = self.job_display_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_user_id is not None:
            result['JobUserId'] = self.job_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')
        if m.get('DebuggerJobIssues') is not None:
            self.debugger_job_issues = m.get('DebuggerJobIssues')
        if m.get('DebuggerJobStatus') is not None:
            self.debugger_job_status = m.get('DebuggerJobStatus')
        if m.get('DebuggerReportURL') is not None:
            self.debugger_report_url = m.get('DebuggerReportURL')
        if m.get('JobDisplayName') is not None:
            self.job_display_name = m.get('JobDisplayName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobUserId') is not None:
            self.job_user_id = m.get('JobUserId')
        return self


class EcsSpec(TeaModel):
    def __init__(self, accelerator_type=None, cpu=None, gpu=None, gpu_type=None, instance_type=None,
                 is_available=None, memory=None):
        self.accelerator_type = accelerator_type  # type: str
        self.cpu = cpu  # type: int
        self.gpu = gpu  # type: int
        self.gpu_type = gpu_type  # type: str
        self.instance_type = instance_type  # type: str
        self.is_available = is_available  # type: bool
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcsSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_available is not None:
            result['IsAvailable'] = self.is_available
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class EnvVar(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnvVar, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class EventInfo(TeaModel):
    def __init__(self, content=None, id=None, pod_id=None, pod_uid=None, time=None):
        self.content = content  # type: str
        self.id = id  # type: str
        self.pod_id = pod_id  # type: str
        self.pod_uid = pod_uid  # type: str
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EventInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class ExtraPodSpec(TeaModel):
    def __init__(self, init_containers=None, pod_annotations=None, pod_labels=None, shared_volume_mount_paths=None,
                 side_car_containers=None):
        self.init_containers = init_containers  # type: list[ContainerSpec]
        self.pod_annotations = pod_annotations  # type: dict[str, str]
        self.pod_labels = pod_labels  # type: dict[str, str]
        self.shared_volume_mount_paths = shared_volume_mount_paths  # type: list[str]
        self.side_car_containers = side_car_containers  # type: list[ContainerSpec]

    def validate(self):
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()
        if self.side_car_containers:
            for k in self.side_car_containers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ExtraPodSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.pod_annotations is not None:
            result['PodAnnotations'] = self.pod_annotations
        if self.pod_labels is not None:
            result['PodLabels'] = self.pod_labels
        if self.shared_volume_mount_paths is not None:
            result['SharedVolumeMountPaths'] = self.shared_volume_mount_paths
        result['SideCarContainers'] = []
        if self.side_car_containers is not None:
            for k in self.side_car_containers:
                result['SideCarContainers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = ContainerSpec()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('PodAnnotations') is not None:
            self.pod_annotations = m.get('PodAnnotations')
        if m.get('PodLabels') is not None:
            self.pod_labels = m.get('PodLabels')
        if m.get('SharedVolumeMountPaths') is not None:
            self.shared_volume_mount_paths = m.get('SharedVolumeMountPaths')
        self.side_car_containers = []
        if m.get('SideCarContainers') is not None:
            for k in m.get('SideCarContainers'):
                temp_model = ContainerSpec()
                self.side_car_containers.append(temp_model.from_map(k))
        return self


class FreeResourceClusterControlItem(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, cross_clusters=None, enable_free_resource=None,
                 free_resource_cluster_control_id=None, gmt_create_time=None, gmt_modify_time=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cross_clusters = cross_clusters  # type: bool
        self.enable_free_resource = enable_free_resource  # type: bool
        self.free_resource_cluster_control_id = free_resource_cluster_control_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FreeResourceClusterControlItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cross_clusters is not None:
            result['CrossClusters'] = self.cross_clusters
        if self.enable_free_resource is not None:
            result['EnableFreeResource'] = self.enable_free_resource
        if self.free_resource_cluster_control_id is not None:
            result['FreeResourceClusterControlId'] = self.free_resource_cluster_control_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CrossClusters') is not None:
            self.cross_clusters = m.get('CrossClusters')
        if m.get('EnableFreeResource') is not None:
            self.enable_free_resource = m.get('EnableFreeResource')
        if m.get('FreeResourceClusterControlId') is not None:
            self.free_resource_cluster_control_id = m.get('FreeResourceClusterControlId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        return self


class FreeResourceDetail(TeaModel):
    def __init__(self, amount=None, resource_type=None):
        self.amount = amount  # type: int
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FreeResourceDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class FreeResourceItem(TeaModel):
    def __init__(self, available_number=None, cluster_id=None, cluster_name=None, free_resource_id=None,
                 gmt_create_time=None, gmt_modify_time=None, region_id=None, resource_type=None):
        self.available_number = available_number  # type: long
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.free_resource_id = free_resource_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FreeResourceItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_number is not None:
            result['AvailableNumber'] = self.available_number
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.free_resource_id is not None:
            result['FreeResourceId'] = self.free_resource_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableNumber') is not None:
            self.available_number = m.get('AvailableNumber')
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('FreeResourceId') is not None:
            self.free_resource_id = m.get('FreeResourceId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GPUDetail(TeaModel):
    def __init__(self, gpu=None, gputype=None, gputype_full_name=None):
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.gputype_full_name = gputype_full_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GPUDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.gputype_full_name is not None:
            result['GPUTypeFullName'] = self.gputype_full_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('GPUTypeFullName') is not None:
            self.gputype_full_name = m.get('GPUTypeFullName')
        return self


class ImageConfig(TeaModel):
    def __init__(self, auth=None, docker_registry=None, password=None, username=None):
        self.auth = auth  # type: str
        self.docker_registry = docker_registry  # type: str
        self.password = password  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.docker_registry is not None:
            result['DockerRegistry'] = self.docker_registry
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('DockerRegistry') is not None:
            self.docker_registry = m.get('DockerRegistry')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ImageItem(TeaModel):
    def __init__(self, accelerator_type=None, author_id=None, framework=None, image_provider_type=None,
                 image_tag=None, image_url=None, image_url_vpc=None):
        self.accelerator_type = accelerator_type  # type: str
        self.author_id = author_id  # type: str
        self.framework = framework  # type: str
        self.image_provider_type = image_provider_type  # type: str
        self.image_tag = image_tag  # type: str
        self.image_url = image_url  # type: str
        self.image_url_vpc = image_url_vpc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.author_id is not None:
            result['AuthorId'] = self.author_id
        if self.framework is not None:
            result['Framework'] = self.framework
        if self.image_provider_type is not None:
            result['ImageProviderType'] = self.image_provider_type
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.image_url_vpc is not None:
            result['ImageUrlVpc'] = self.image_url_vpc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('AuthorId') is not None:
            self.author_id = m.get('AuthorId')
        if m.get('Framework') is not None:
            self.framework = m.get('Framework')
        if m.get('ImageProviderType') is not None:
            self.image_provider_type = m.get('ImageProviderType')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ImageUrlVpc') is not None:
            self.image_url_vpc = m.get('ImageUrlVpc')
        return self


class JobDebuggerConfig(TeaModel):
    def __init__(self, debugger_config_content=None, debugger_config_id=None, gmt_create_time=None, job_id=None):
        self.debugger_config_content = debugger_config_content  # type: str
        self.debugger_config_id = debugger_config_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobDebuggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content
        if self.debugger_config_id is not None:
            result['DebuggerConfigId'] = self.debugger_config_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')
        if m.get('DebuggerConfigId') is not None:
            self.debugger_config_id = m.get('DebuggerConfigId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class JobElasticSpec(TeaModel):
    def __init__(self, aimaster_docker_image=None, aimaster_type=None, edpmax_parallelism=None,
                 edpmin_parallelism=None, elastic_strategy=None, enable_aimaster=None, enable_edp=None, enable_elastic_training=None,
                 enable_ps_job_elastic_ps=None, enable_ps_job_elastic_worker=None, enable_ps_resource_estimate=None, max_parallelism=None,
                 min_parallelism=None, psmax_parallelism=None, psmin_parallelism=None):
        self.aimaster_docker_image = aimaster_docker_image  # type: str
        self.aimaster_type = aimaster_type  # type: str
        self.edpmax_parallelism = edpmax_parallelism  # type: int
        self.edpmin_parallelism = edpmin_parallelism  # type: int
        self.elastic_strategy = elastic_strategy  # type: str
        self.enable_aimaster = enable_aimaster  # type: bool
        self.enable_edp = enable_edp  # type: bool
        self.enable_elastic_training = enable_elastic_training  # type: bool
        self.enable_ps_job_elastic_ps = enable_ps_job_elastic_ps  # type: bool
        self.enable_ps_job_elastic_worker = enable_ps_job_elastic_worker  # type: bool
        self.enable_ps_resource_estimate = enable_ps_resource_estimate  # type: bool
        self.max_parallelism = max_parallelism  # type: int
        self.min_parallelism = min_parallelism  # type: int
        self.psmax_parallelism = psmax_parallelism  # type: int
        self.psmin_parallelism = psmin_parallelism  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobElasticSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aimaster_docker_image is not None:
            result['AIMasterDockerImage'] = self.aimaster_docker_image
        if self.aimaster_type is not None:
            result['AIMasterType'] = self.aimaster_type
        if self.edpmax_parallelism is not None:
            result['EDPMaxParallelism'] = self.edpmax_parallelism
        if self.edpmin_parallelism is not None:
            result['EDPMinParallelism'] = self.edpmin_parallelism
        if self.elastic_strategy is not None:
            result['ElasticStrategy'] = self.elastic_strategy
        if self.enable_aimaster is not None:
            result['EnableAIMaster'] = self.enable_aimaster
        if self.enable_edp is not None:
            result['EnableEDP'] = self.enable_edp
        if self.enable_elastic_training is not None:
            result['EnableElasticTraining'] = self.enable_elastic_training
        if self.enable_ps_job_elastic_ps is not None:
            result['EnablePsJobElasticPS'] = self.enable_ps_job_elastic_ps
        if self.enable_ps_job_elastic_worker is not None:
            result['EnablePsJobElasticWorker'] = self.enable_ps_job_elastic_worker
        if self.enable_ps_resource_estimate is not None:
            result['EnablePsResourceEstimate'] = self.enable_ps_resource_estimate
        if self.max_parallelism is not None:
            result['MaxParallelism'] = self.max_parallelism
        if self.min_parallelism is not None:
            result['MinParallelism'] = self.min_parallelism
        if self.psmax_parallelism is not None:
            result['PSMaxParallelism'] = self.psmax_parallelism
        if self.psmin_parallelism is not None:
            result['PSMinParallelism'] = self.psmin_parallelism
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIMasterDockerImage') is not None:
            self.aimaster_docker_image = m.get('AIMasterDockerImage')
        if m.get('AIMasterType') is not None:
            self.aimaster_type = m.get('AIMasterType')
        if m.get('EDPMaxParallelism') is not None:
            self.edpmax_parallelism = m.get('EDPMaxParallelism')
        if m.get('EDPMinParallelism') is not None:
            self.edpmin_parallelism = m.get('EDPMinParallelism')
        if m.get('ElasticStrategy') is not None:
            self.elastic_strategy = m.get('ElasticStrategy')
        if m.get('EnableAIMaster') is not None:
            self.enable_aimaster = m.get('EnableAIMaster')
        if m.get('EnableEDP') is not None:
            self.enable_edp = m.get('EnableEDP')
        if m.get('EnableElasticTraining') is not None:
            self.enable_elastic_training = m.get('EnableElasticTraining')
        if m.get('EnablePsJobElasticPS') is not None:
            self.enable_ps_job_elastic_ps = m.get('EnablePsJobElasticPS')
        if m.get('EnablePsJobElasticWorker') is not None:
            self.enable_ps_job_elastic_worker = m.get('EnablePsJobElasticWorker')
        if m.get('EnablePsResourceEstimate') is not None:
            self.enable_ps_resource_estimate = m.get('EnablePsResourceEstimate')
        if m.get('MaxParallelism') is not None:
            self.max_parallelism = m.get('MaxParallelism')
        if m.get('MinParallelism') is not None:
            self.min_parallelism = m.get('MinParallelism')
        if m.get('PSMaxParallelism') is not None:
            self.psmax_parallelism = m.get('PSMaxParallelism')
        if m.get('PSMinParallelism') is not None:
            self.psmin_parallelism = m.get('PSMinParallelism')
        return self


class JobItemCodeSource(TeaModel):
    def __init__(self, branch=None, code_source_id=None, commit=None, mount_path=None):
        self.branch = branch  # type: str
        self.code_source_id = code_source_id  # type: str
        self.commit = commit  # type: str
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobItemCodeSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class JobItemDataSources(TeaModel):
    def __init__(self, data_source_id=None, mount_path=None):
        self.data_source_id = data_source_id  # type: str
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobItemDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class JobItem(TeaModel):
    def __init__(self, code_source=None, data_sources=None, display_name=None, duration=None, enabled_debugger=None,
                 envs=None, gmt_create_time=None, gmt_failed_time=None, gmt_finish_time=None, gmt_running_time=None,
                 gmt_stopped_time=None, gmt_submitted_time=None, gmt_successed_time=None, job_id=None, job_specs=None, job_type=None,
                 priority=None, reason_code=None, reason_message=None, resource_id=None, resource_level=None,
                 resource_name=None, settings=None, status=None, sub_status=None, thirdparty_lib_dir=None, thirdparty_libs=None,
                 user_command=None, user_id=None, workspace_id=None, workspace_name=None):
        self.code_source = code_source  # type: JobItemCodeSource
        self.data_sources = data_sources  # type: list[JobItemDataSources]
        self.display_name = display_name  # type: str
        self.duration = duration  # type: long
        self.enabled_debugger = enabled_debugger  # type: bool
        self.envs = envs  # type: dict[str, str]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_failed_time = gmt_failed_time  # type: str
        self.gmt_finish_time = gmt_finish_time  # type: str
        self.gmt_running_time = gmt_running_time  # type: str
        self.gmt_stopped_time = gmt_stopped_time  # type: str
        self.gmt_submitted_time = gmt_submitted_time  # type: str
        self.gmt_successed_time = gmt_successed_time  # type: str
        self.job_id = job_id  # type: str
        self.job_specs = job_specs  # type: list[JobSpec]
        self.job_type = job_type  # type: str
        self.priority = priority  # type: int
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_level = resource_level  # type: str
        self.resource_name = resource_name  # type: str
        self.settings = settings  # type: JobSettings
        self.status = status  # type: str
        self.sub_status = sub_status  # type: str
        self.thirdparty_lib_dir = thirdparty_lib_dir  # type: str
        self.thirdparty_libs = thirdparty_libs  # type: list[str]
        self.user_command = user_command  # type: str
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.settings:
            self.settings.validate()

    def to_map(self):
        _map = super(JobItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.enabled_debugger is not None:
            result['EnabledDebugger'] = self.enabled_debugger
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_failed_time is not None:
            result['GmtFailedTime'] = self.gmt_failed_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_running_time is not None:
            result['GmtRunningTime'] = self.gmt_running_time
        if self.gmt_stopped_time is not None:
            result['GmtStoppedTime'] = self.gmt_stopped_time
        if self.gmt_submitted_time is not None:
            result['GmtSubmittedTime'] = self.gmt_submitted_time
        if self.gmt_successed_time is not None:
            result['GmtSuccessedTime'] = self.gmt_successed_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir
        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs
        if self.user_command is not None:
            result['UserCommand'] = self.user_command
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSource') is not None:
            temp_model = JobItemCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = JobItemDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EnabledDebugger') is not None:
            self.enabled_debugger = m.get('EnabledDebugger')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFailedTime') is not None:
            self.gmt_failed_time = m.get('GmtFailedTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtRunningTime') is not None:
            self.gmt_running_time = m.get('GmtRunningTime')
        if m.get('GmtStoppedTime') is not None:
            self.gmt_stopped_time = m.get('GmtStoppedTime')
        if m.get('GmtSubmittedTime') is not None:
            self.gmt_submitted_time = m.get('GmtSubmittedTime')
        if m.get('GmtSuccessedTime') is not None:
            self.gmt_successed_time = m.get('GmtSuccessedTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Settings') is not None:
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')
        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')
        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class JobSettings(TeaModel):
    def __init__(self, advanced_settings=None, business_user_id=None, caller=None, driver=None,
                 enable_error_monitoring_in_aimaster=None, enable_oss_append=None, enable_rdma=None, enable_tide_resource=None,
                 error_monitoring_args=None, job_reserved_minutes=None, job_reserved_policy=None, oversold_type=None, pipeline_id=None,
                 tags=None):
        self.advanced_settings = advanced_settings  # type: dict[str, any]
        self.business_user_id = business_user_id  # type: str
        self.caller = caller  # type: str
        self.driver = driver  # type: str
        self.enable_error_monitoring_in_aimaster = enable_error_monitoring_in_aimaster  # type: bool
        self.enable_oss_append = enable_oss_append  # type: bool
        self.enable_rdma = enable_rdma  # type: bool
        self.enable_tide_resource = enable_tide_resource  # type: bool
        self.error_monitoring_args = error_monitoring_args  # type: str
        self.job_reserved_minutes = job_reserved_minutes  # type: int
        self.job_reserved_policy = job_reserved_policy  # type: str
        self.oversold_type = oversold_type  # type: str
        self.pipeline_id = pipeline_id  # type: str
        self.tags = tags  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_settings is not None:
            result['AdvancedSettings'] = self.advanced_settings
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.enable_error_monitoring_in_aimaster is not None:
            result['EnableErrorMonitoringInAIMaster'] = self.enable_error_monitoring_in_aimaster
        if self.enable_oss_append is not None:
            result['EnableOssAppend'] = self.enable_oss_append
        if self.enable_rdma is not None:
            result['EnableRDMA'] = self.enable_rdma
        if self.enable_tide_resource is not None:
            result['EnableTideResource'] = self.enable_tide_resource
        if self.error_monitoring_args is not None:
            result['ErrorMonitoringArgs'] = self.error_monitoring_args
        if self.job_reserved_minutes is not None:
            result['JobReservedMinutes'] = self.job_reserved_minutes
        if self.job_reserved_policy is not None:
            result['JobReservedPolicy'] = self.job_reserved_policy
        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedSettings') is not None:
            self.advanced_settings = m.get('AdvancedSettings')
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('EnableErrorMonitoringInAIMaster') is not None:
            self.enable_error_monitoring_in_aimaster = m.get('EnableErrorMonitoringInAIMaster')
        if m.get('EnableOssAppend') is not None:
            self.enable_oss_append = m.get('EnableOssAppend')
        if m.get('EnableRDMA') is not None:
            self.enable_rdma = m.get('EnableRDMA')
        if m.get('EnableTideResource') is not None:
            self.enable_tide_resource = m.get('EnableTideResource')
        if m.get('ErrorMonitoringArgs') is not None:
            self.error_monitoring_args = m.get('ErrorMonitoringArgs')
        if m.get('JobReservedMinutes') is not None:
            self.job_reserved_minutes = m.get('JobReservedMinutes')
        if m.get('JobReservedPolicy') is not None:
            self.job_reserved_policy = m.get('JobReservedPolicy')
        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class JobSpec(TeaModel):
    def __init__(self, ecs_spec=None, extra_pod_spec=None, image=None, image_config=None, pod_count=None,
                 resource_config=None, type=None, use_spot_instance=None):
        self.ecs_spec = ecs_spec  # type: str
        self.extra_pod_spec = extra_pod_spec  # type: ExtraPodSpec
        self.image = image  # type: str
        self.image_config = image_config  # type: ImageConfig
        self.pod_count = pod_count  # type: long
        self.resource_config = resource_config  # type: ResourceConfig
        self.type = type  # type: str
        self.use_spot_instance = use_spot_instance  # type: bool

    def validate(self):
        if self.extra_pod_spec:
            self.extra_pod_spec.validate()
        if self.image_config:
            self.image_config.validate()
        if self.resource_config:
            self.resource_config.validate()

    def to_map(self):
        _map = super(JobSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.extra_pod_spec is not None:
            result['ExtraPodSpec'] = self.extra_pod_spec.to_map()
        if self.image is not None:
            result['Image'] = self.image
        if self.image_config is not None:
            result['ImageConfig'] = self.image_config.to_map()
        if self.pod_count is not None:
            result['PodCount'] = self.pod_count
        if self.resource_config is not None:
            result['ResourceConfig'] = self.resource_config.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.use_spot_instance is not None:
            result['UseSpotInstance'] = self.use_spot_instance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('ExtraPodSpec') is not None:
            temp_model = ExtraPodSpec()
            self.extra_pod_spec = temp_model.from_map(m['ExtraPodSpec'])
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageConfig') is not None:
            temp_model = ImageConfig()
            self.image_config = temp_model.from_map(m['ImageConfig'])
        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')
        if m.get('ResourceConfig') is not None:
            temp_model = ResourceConfig()
            self.resource_config = temp_model.from_map(m['ResourceConfig'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UseSpotInstance') is not None:
            self.use_spot_instance = m.get('UseSpotInstance')
        return self


class LogInfo(TeaModel):
    def __init__(self, content=None, id=None, pod_id=None, pod_uid=None, source=None, time=None):
        self.content = content  # type: str
        self.id = id  # type: str
        self.pod_id = pod_id  # type: str
        self.pod_uid = pod_uid  # type: str
        self.source = source  # type: str
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.source is not None:
            result['Source'] = self.source
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class Member(TeaModel):
    def __init__(self, member_id=None, member_type=None):
        self.member_id = member_id  # type: str
        self.member_type = member_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Member, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        return self


class Metric(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: long
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(Metric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class NodeMetric(TeaModel):
    def __init__(self, metrics=None, node_name=None):
        self.metrics = metrics  # type: list[Metric]
        self.node_name = node_name  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(NodeMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class PodItem(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_finish_time=None, gmt_start_time=None, history_pods=None, ip=None,
                 pod_id=None, pod_uid=None, status=None, type=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_finish_time = gmt_finish_time  # type: str
        self.gmt_start_time = gmt_start_time  # type: str
        self.history_pods = history_pods  # type: list[PodItem]
        self.ip = ip  # type: str
        self.pod_id = pod_id  # type: str
        self.pod_uid = pod_uid  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.history_pods:
            for k in self.history_pods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PodItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        result['HistoryPods'] = []
        if self.history_pods is not None:
            for k in self.history_pods:
                result['HistoryPods'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        self.history_pods = []
        if m.get('HistoryPods') is not None:
            for k in m.get('HistoryPods'):
                temp_model = PodItem()
                self.history_pods.append(temp_model.from_map(k))
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PodMetric(TeaModel):
    def __init__(self, metrics=None, pod_id=None):
        self.metrics = metrics  # type: list[Metric]
        self.pod_id = pod_id  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PodMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        return self


class Quota(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, quota_config=None, quota_id=None, quota_name=None,
                 quota_type=None, total_quota=None, total_tide_quota=None, used_quota=None, used_tide_quota=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.quota_config = quota_config  # type: QuotaConfig
        self.quota_id = quota_id  # type: str
        self.quota_name = quota_name  # type: str
        self.quota_type = quota_type  # type: str
        self.total_quota = total_quota  # type: QuotaDetail
        self.total_tide_quota = total_tide_quota  # type: QuotaDetail
        self.used_quota = used_quota  # type: QuotaDetail
        self.used_tide_quota = used_tide_quota  # type: QuotaDetail

    def validate(self):
        if self.quota_config:
            self.quota_config.validate()
        if self.total_quota:
            self.total_quota.validate()
        if self.total_tide_quota:
            self.total_tide_quota.validate()
        if self.used_quota:
            self.used_quota.validate()
        if self.used_tide_quota:
            self.used_tide_quota.validate()

    def to_map(self):
        _map = super(Quota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota.to_map()
        if self.total_tide_quota is not None:
            result['TotalTideQuota'] = self.total_tide_quota.to_map()
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()
        if self.used_tide_quota is not None:
            result['UsedTideQuota'] = self.used_tide_quota.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('QuotaConfig') is not None:
            temp_model = QuotaConfig()
            self.quota_config = temp_model.from_map(m['QuotaConfig'])
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('TotalQuota') is not None:
            temp_model = QuotaDetail()
            self.total_quota = temp_model.from_map(m['TotalQuota'])
        if m.get('TotalTideQuota') is not None:
            temp_model = QuotaDetail()
            self.total_tide_quota = temp_model.from_map(m['TotalTideQuota'])
        if m.get('UsedQuota') is not None:
            temp_model = QuotaDetail()
            self.used_quota = temp_model.from_map(m['UsedQuota'])
        if m.get('UsedTideQuota') is not None:
            temp_model = QuotaDetail()
            self.used_tide_quota = temp_model.from_map(m['UsedTideQuota'])
        return self


class QuotaConfig(TeaModel):
    def __init__(self, allowed_max_priority=None, enable_dlc=None, enable_dsw=None, enable_tide_resource=None,
                 resource_level=None):
        self.allowed_max_priority = allowed_max_priority  # type: int
        self.enable_dlc = enable_dlc  # type: bool
        self.enable_dsw = enable_dsw  # type: bool
        self.enable_tide_resource = enable_tide_resource  # type: bool
        self.resource_level = resource_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuotaConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_max_priority is not None:
            result['AllowedMaxPriority'] = self.allowed_max_priority
        if self.enable_dlc is not None:
            result['EnableDLC'] = self.enable_dlc
        if self.enable_dsw is not None:
            result['EnableDSW'] = self.enable_dsw
        if self.enable_tide_resource is not None:
            result['EnableTideResource'] = self.enable_tide_resource
        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedMaxPriority') is not None:
            self.allowed_max_priority = m.get('AllowedMaxPriority')
        if m.get('EnableDLC') is not None:
            self.enable_dlc = m.get('EnableDLC')
        if m.get('EnableDSW') is not None:
            self.enable_dsw = m.get('EnableDSW')
        if m.get('EnableTideResource') is not None:
            self.enable_tide_resource = m.get('EnableTideResource')
        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')
        return self


class QuotaDetail(TeaModel):
    def __init__(self, cpu=None, gpu=None, gpudetails=None, gputype=None, gputype_full_name=None, memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gpudetails = gpudetails  # type: list[GPUDetail]
        self.gputype = gputype  # type: str
        self.gputype_full_name = gputype_full_name  # type: str
        self.memory = memory  # type: str

    def validate(self):
        if self.gpudetails:
            for k in self.gpudetails:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuotaDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        result['GPUDetails'] = []
        if self.gpudetails is not None:
            for k in self.gpudetails:
                result['GPUDetails'].append(k.to_map() if k else None)
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.gputype_full_name is not None:
            result['GPUTypeFullName'] = self.gputype_full_name
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        self.gpudetails = []
        if m.get('GPUDetails') is not None:
            for k in m.get('GPUDetails'):
                temp_model = GPUDetail()
                self.gpudetails.append(temp_model.from_map(k))
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('GPUTypeFullName') is not None:
            self.gputype_full_name = m.get('GPUTypeFullName')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ResourceConfig(TeaModel):
    def __init__(self, cpu=None, gpu=None, gputype=None, memory=None, shared_memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str
        self.shared_memory = shared_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        return self


class ResourceRequirements(TeaModel):
    def __init__(self, limits=None, requests=None):
        self.limits = limits  # type: dict[str, str]
        self.requests = requests  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceRequirements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['Limits'] = self.limits
        if self.requests is not None:
            result['Requests'] = self.requests
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limits') is not None:
            self.limits = m.get('Limits')
        if m.get('Requests') is not None:
            self.requests = m.get('Requests')
        return self


class Resources(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.memory = memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Resources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class SmartCache(TeaModel):
    def __init__(self, cache_worker_num=None, cache_worker_size=None, description=None, display_name=None,
                 duration=None, endpoint=None, file_system_id=None, gmt_create_time=None, gmt_modify_time=None,
                 mount_path=None, options=None, path=None, smart_cache_id=None, status=None, type=None, user_id=None):
        self.cache_worker_num = cache_worker_num  # type: long
        self.cache_worker_size = cache_worker_size  # type: long
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.duration = duration  # type: str
        self.endpoint = endpoint  # type: str
        self.file_system_id = file_system_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str
        self.mount_path = mount_path  # type: str
        self.options = options  # type: str
        self.path = path  # type: str
        self.smart_cache_id = smart_cache_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmartCache, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_worker_num is not None:
            result['CacheWorkerNum'] = self.cache_worker_num
        if self.cache_worker_size is not None:
            result['CacheWorkerSize'] = self.cache_worker_size
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.options is not None:
            result['Options'] = self.options
        if self.path is not None:
            result['Path'] = self.path
        if self.smart_cache_id is not None:
            result['SmartCacheId'] = self.smart_cache_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CacheWorkerNum') is not None:
            self.cache_worker_num = m.get('CacheWorkerNum')
        if m.get('CacheWorkerSize') is not None:
            self.cache_worker_size = m.get('CacheWorkerSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SmartCacheId') is not None:
            self.smart_cache_id = m.get('SmartCacheId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class Tensorboard(TeaModel):
    def __init__(self, data_source_id=None, display_name=None, duration=None, gmt_create_time=None,
                 gmt_modify_time=None, job_id=None, reason_code=None, reason_message=None, request_id=None, status=None,
                 summary_path=None, tensorboard_id=None, tensorboard_url=None, user_id=None):
        self.data_source_id = data_source_id  # type: str
        self.display_name = display_name  # type: str
        self.duration = duration  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str
        self.job_id = job_id  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.summary_path = summary_path  # type: str
        self.tensorboard_id = tensorboard_id  # type: str
        self.tensorboard_url = tensorboard_url  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Tensorboard, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.tensorboard_url is not None:
            result['TensorboardUrl'] = self.tensorboard_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('TensorboardUrl') is not None:
            self.tensorboard_url = m.get('TensorboardUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class Workspace(TeaModel):
    def __init__(self, creator=None, gmt_create_time=None, gmt_modify_time=None, members=None, quotas=None,
                 total_resources=None, workspace_admins=None, workspace_id=None, workspace_name=None):
        self.creator = creator  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modify_time = gmt_modify_time  # type: str
        self.members = members  # type: list[Member]
        self.quotas = quotas  # type: list[Quota]
        self.total_resources = total_resources  # type: Resources
        self.workspace_admins = workspace_admins  # type: list[Member]
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.workspace_admins:
            for k in self.workspace_admins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Workspace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        result['WorkspaceAdmins'] = []
        if self.workspace_admins is not None:
            for k in self.workspace_admins:
                result['WorkspaceAdmins'].append(k.to_map() if k else None)
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = Member()
                self.members.append(temp_model.from_map(k))
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = Quota()
                self.quotas.append(temp_model.from_map(k))
        if m.get('TotalResources') is not None:
            temp_model = Resources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        self.workspace_admins = []
        if m.get('WorkspaceAdmins') is not None:
            for k in m.get('WorkspaceAdmins'):
                temp_model = Member()
                self.workspace_admins.append(temp_model.from_map(k))
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class CreateJobRequestCodeSource(TeaModel):
    def __init__(self, branch=None, code_source_id=None, commit=None, mount_path=None):
        self.branch = branch  # type: str
        self.code_source_id = code_source_id  # type: str
        self.commit = commit  # type: str
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestCodeSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class CreateJobRequestDataSources(TeaModel):
    def __init__(self, data_source_id=None, mount_path=None, uri=None):
        self.data_source_id = data_source_id  # type: str
        self.mount_path = mount_path  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateJobRequestUserVpc(TeaModel):
    def __init__(self, default_route=None, extended_cidrs=None, security_group_id=None, switch_id=None, vpc_id=None):
        self.default_route = default_route  # type: str
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.security_group_id = security_group_id  # type: str
        self.switch_id = switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateJobRequest(TeaModel):
    def __init__(self, code_source=None, data_sources=None, debugger_config_content=None, display_name=None,
                 elastic_spec=None, envs=None, job_max_running_time_minutes=None, job_specs=None, job_type=None, options=None,
                 priority=None, resource_id=None, settings=None, success_policy=None, thirdparty_lib_dir=None,
                 thirdparty_libs=None, user_command=None, user_vpc=None, workspace_id=None):
        self.code_source = code_source  # type: CreateJobRequestCodeSource
        self.data_sources = data_sources  # type: list[CreateJobRequestDataSources]
        self.debugger_config_content = debugger_config_content  # type: str
        self.display_name = display_name  # type: str
        self.elastic_spec = elastic_spec  # type: JobElasticSpec
        self.envs = envs  # type: dict[str, str]
        self.job_max_running_time_minutes = job_max_running_time_minutes  # type: long
        self.job_specs = job_specs  # type: list[JobSpec]
        self.job_type = job_type  # type: str
        self.options = options  # type: str
        self.priority = priority  # type: int
        self.resource_id = resource_id  # type: str
        self.settings = settings  # type: JobSettings
        self.success_policy = success_policy  # type: str
        self.thirdparty_lib_dir = thirdparty_lib_dir  # type: str
        self.thirdparty_libs = thirdparty_libs  # type: list[str]
        self.user_command = user_command  # type: str
        self.user_vpc = user_vpc  # type: CreateJobRequestUserVpc
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.settings:
            self.settings.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(CreateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.elastic_spec is not None:
            result['ElasticSpec'] = self.elastic_spec.to_map()
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.job_max_running_time_minutes is not None:
            result['JobMaxRunningTimeMinutes'] = self.job_max_running_time_minutes
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.options is not None:
            result['Options'] = self.options
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.success_policy is not None:
            result['SuccessPolicy'] = self.success_policy
        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir
        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs
        if self.user_command is not None:
            result['UserCommand'] = self.user_command
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSource') is not None:
            temp_model = CreateJobRequestCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = CreateJobRequestDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ElasticSpec') is not None:
            temp_model = JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m['ElasticSpec'])
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('JobMaxRunningTimeMinutes') is not None:
            self.job_max_running_time_minutes = m.get('JobMaxRunningTimeMinutes')
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Settings') is not None:
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('SuccessPolicy') is not None:
            self.success_policy = m.get('SuccessPolicy')
        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')
        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')
        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')
        if m.get('UserVpc') is not None:
            temp_model = CreateJobRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
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
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CreateTensorboardRequest(TeaModel):
    def __init__(self, cpu=None, data_source_id=None, data_source_type=None, data_sources=None, display_name=None,
                 job_id=None, max_running_time_minutes=None, memory=None, options=None, source_id=None, source_type=None,
                 summary_path=None, summary_relative_path=None, uri=None, workspace_id=None):
        self.cpu = cpu  # type: long
        self.data_source_id = data_source_id  # type: str
        self.data_source_type = data_source_type  # type: str
        self.data_sources = data_sources  # type: list[DataSourceItem]
        self.display_name = display_name  # type: str
        self.job_id = job_id  # type: str
        self.max_running_time_minutes = max_running_time_minutes  # type: long
        self.memory = memory  # type: long
        self.options = options  # type: str
        self.source_id = source_id  # type: str
        self.source_type = source_type  # type: str
        self.summary_path = summary_path  # type: str
        self.summary_relative_path = summary_relative_path  # type: str
        self.uri = uri  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTensorboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.max_running_time_minutes is not None:
            result['MaxRunningTimeMinutes'] = self.max_running_time_minutes
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.options is not None:
            result['Options'] = self.options
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path
        if self.summary_relative_path is not None:
            result['SummaryRelativePath'] = self.summary_relative_path
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = DataSourceItem()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MaxRunningTimeMinutes') is not None:
            self.max_running_time_minutes = m.get('MaxRunningTimeMinutes')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')
        if m.get('SummaryRelativePath') is not None:
            self.summary_relative_path = m.get('SummaryRelativePath')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateTensorboardResponseBody(TeaModel):
    def __init__(self, data_source_id=None, job_id=None, request_id=None, tensorboard_id=None):
        self.data_source_id = data_source_id  # type: str
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str
        self.tensorboard_id = tensorboard_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class CreateTensorboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTensorboardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTensorboardRequest, self).to_map()
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


class DeleteTensorboardResponseBody(TeaModel):
    def __init__(self, request_id=None, tensorboard_id=None):
        self.request_id = request_id  # type: str
        self.tensorboard_id = tensorboard_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class DeleteTensorboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTensorboardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(self, need_detail=None):
        self.need_detail = need_detail  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_detail is not None:
            result['NeedDetail'] = self.need_detail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedDetail') is not None:
            self.need_detail = m.get('NeedDetail')
        return self


class GetJobResponseBodyCodeSource(TeaModel):
    def __init__(self, branch=None, code_source_id=None, commit=None, mount_path=None):
        self.branch = branch  # type: str
        self.code_source_id = code_source_id  # type: str
        self.commit = commit  # type: str
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyCodeSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class GetJobResponseBodyDataSources(TeaModel):
    def __init__(self, data_source_id=None, mount_path=None, uri=None):
        self.data_source_id = data_source_id  # type: str
        self.mount_path = mount_path  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class GetJobResponseBodyPodsHistoryPods(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_finish_time=None, gmt_start_time=None, ip=None, pod_id=None,
                 pod_uid=None, resource_type=None, status=None, sub_status=None, type=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_finish_time = gmt_finish_time  # type: str
        self.gmt_start_time = gmt_start_time  # type: str
        self.ip = ip  # type: str
        self.pod_id = pod_id  # type: str
        self.pod_uid = pod_uid  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.sub_status = sub_status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyPodsHistoryPods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetJobResponseBodyPods(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_finish_time=None, gmt_start_time=None, history_pods=None, ip=None,
                 pod_id=None, pod_uid=None, resource_type=None, status=None, sub_status=None, type=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_finish_time = gmt_finish_time  # type: str
        self.gmt_start_time = gmt_start_time  # type: str
        self.history_pods = history_pods  # type: list[GetJobResponseBodyPodsHistoryPods]
        self.ip = ip  # type: str
        self.pod_id = pod_id  # type: str
        self.pod_uid = pod_uid  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.sub_status = sub_status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.history_pods:
            for k in self.history_pods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyPods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        result['HistoryPods'] = []
        if self.history_pods is not None:
            for k in self.history_pods:
                result['HistoryPods'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        self.history_pods = []
        if m.get('HistoryPods') is not None:
            for k in m.get('HistoryPods'):
                temp_model = GetJobResponseBodyPodsHistoryPods()
                self.history_pods.append(temp_model.from_map(k))
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(self, cluster_id=None, code_source=None, data_sources=None, display_name=None, duration=None,
                 elastic_spec=None, enabled_debugger=None, envs=None, gmt_create_time=None, gmt_failed_time=None,
                 gmt_finish_time=None, gmt_running_time=None, gmt_stopped_time=None, gmt_submitted_time=None,
                 gmt_successed_time=None, job_id=None, job_specs=None, job_type=None, pods=None, priority=None, reason_code=None,
                 reason_message=None, request_id=None, resource_id=None, resource_level=None, restart_times=None, settings=None,
                 status=None, sub_status=None, thirdparty_lib_dir=None, thirdparty_libs=None, user_command=None,
                 user_id=None, workspace_id=None, workspace_name=None):
        self.cluster_id = cluster_id  # type: str
        self.code_source = code_source  # type: GetJobResponseBodyCodeSource
        self.data_sources = data_sources  # type: list[GetJobResponseBodyDataSources]
        self.display_name = display_name  # type: str
        self.duration = duration  # type: long
        self.elastic_spec = elastic_spec  # type: JobElasticSpec
        self.enabled_debugger = enabled_debugger  # type: bool
        self.envs = envs  # type: dict[str, str]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_failed_time = gmt_failed_time  # type: str
        self.gmt_finish_time = gmt_finish_time  # type: str
        self.gmt_running_time = gmt_running_time  # type: str
        self.gmt_stopped_time = gmt_stopped_time  # type: str
        self.gmt_submitted_time = gmt_submitted_time  # type: str
        self.gmt_successed_time = gmt_successed_time  # type: str
        self.job_id = job_id  # type: str
        self.job_specs = job_specs  # type: list[JobSpec]
        self.job_type = job_type  # type: str
        self.pods = pods  # type: list[GetJobResponseBodyPods]
        self.priority = priority  # type: int
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_level = resource_level  # type: str
        self.restart_times = restart_times  # type: str
        self.settings = settings  # type: JobSettings
        self.status = status  # type: str
        self.sub_status = sub_status  # type: str
        self.thirdparty_lib_dir = thirdparty_lib_dir  # type: str
        self.thirdparty_libs = thirdparty_libs  # type: list[str]
        self.user_command = user_command  # type: str
        self.user_id = user_id  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.pods:
            for k in self.pods:
                if k:
                    k.validate()
        if self.settings:
            self.settings.validate()

    def to_map(self):
        _map = super(GetJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.elastic_spec is not None:
            result['ElasticSpec'] = self.elastic_spec.to_map()
        if self.enabled_debugger is not None:
            result['EnabledDebugger'] = self.enabled_debugger
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_failed_time is not None:
            result['GmtFailedTime'] = self.gmt_failed_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_running_time is not None:
            result['GmtRunningTime'] = self.gmt_running_time
        if self.gmt_stopped_time is not None:
            result['GmtStoppedTime'] = self.gmt_stopped_time
        if self.gmt_submitted_time is not None:
            result['GmtSubmittedTime'] = self.gmt_submitted_time
        if self.gmt_successed_time is not None:
            result['GmtSuccessedTime'] = self.gmt_successed_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['JobType'] = self.job_type
        result['Pods'] = []
        if self.pods is not None:
            for k in self.pods:
                result['Pods'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level
        if self.restart_times is not None:
            result['RestartTimes'] = self.restart_times
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir
        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs
        if self.user_command is not None:
            result['UserCommand'] = self.user_command
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CodeSource') is not None:
            temp_model = GetJobResponseBodyCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = GetJobResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ElasticSpec') is not None:
            temp_model = JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m['ElasticSpec'])
        if m.get('EnabledDebugger') is not None:
            self.enabled_debugger = m.get('EnabledDebugger')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFailedTime') is not None:
            self.gmt_failed_time = m.get('GmtFailedTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtRunningTime') is not None:
            self.gmt_running_time = m.get('GmtRunningTime')
        if m.get('GmtStoppedTime') is not None:
            self.gmt_stopped_time = m.get('GmtStoppedTime')
        if m.get('GmtSubmittedTime') is not None:
            self.gmt_submitted_time = m.get('GmtSubmittedTime')
        if m.get('GmtSuccessedTime') is not None:
            self.gmt_successed_time = m.get('GmtSuccessedTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        self.pods = []
        if m.get('Pods') is not None:
            for k in m.get('Pods'):
                temp_model = GetJobResponseBodyPods()
                self.pods.append(temp_model.from_map(k))
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')
        if m.get('RestartTimes') is not None:
            self.restart_times = m.get('RestartTimes')
        if m.get('Settings') is not None:
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')
        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')
        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
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


class GetJobEventsRequest(TeaModel):
    def __init__(self, end_time=None, max_events_num=None, start_time=None):
        self.end_time = end_time  # type: str
        self.max_events_num = max_events_num  # type: int
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetJobEventsResponseBody(TeaModel):
    def __init__(self, events=None, job_id=None, request_id=None):
        self.events = events  # type: list[str]
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['Events'] = self.events
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobMetricsRequest(TeaModel):
    def __init__(self, end_time=None, metric_type=None, start_time=None, time_step=None, token=None):
        self.end_time = end_time  # type: str
        self.metric_type = metric_type  # type: str
        self.start_time = start_time  # type: str
        self.time_step = time_step  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetJobMetricsResponseBody(TeaModel):
    def __init__(self, job_id=None, pod_metrics=None, request_id=None):
        self.job_id = job_id  # type: str
        self.pod_metrics = pod_metrics  # type: list[PodMetric]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.pod_metrics:
            for k in self.pod_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetJobMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['PodMetrics'] = []
        if self.pod_metrics is not None:
            for k in self.pod_metrics:
                result['PodMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.pod_metrics = []
        if m.get('PodMetrics') is not None:
            for k in m.get('PodMetrics'):
                temp_model = PodMetric()
                self.pod_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPodEventsRequest(TeaModel):
    def __init__(self, end_time=None, max_events_num=None, pod_uid=None, start_time=None):
        self.end_time = end_time  # type: str
        self.max_events_num = max_events_num  # type: int
        self.pod_uid = pod_uid  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPodEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetPodEventsResponseBody(TeaModel):
    def __init__(self, events=None, job_id=None, pod_id=None, pod_uid=None, request_id=None):
        self.events = events  # type: list[str]
        self.job_id = job_id  # type: str
        self.pod_id = pod_id  # type: str
        self.pod_uid = pod_uid  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPodEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['Events'] = self.events
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPodEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPodEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPodEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPodEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPodLogsRequest(TeaModel):
    def __init__(self, download_to_file=None, end_time=None, max_lines=None, pod_uid=None, start_time=None):
        self.download_to_file = download_to_file  # type: bool
        self.end_time = end_time  # type: str
        self.max_lines = max_lines  # type: int
        self.pod_uid = pod_uid  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPodLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_to_file is not None:
            result['DownloadToFile'] = self.download_to_file
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_lines is not None:
            result['MaxLines'] = self.max_lines
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadToFile') is not None:
            self.download_to_file = m.get('DownloadToFile')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxLines') is not None:
            self.max_lines = m.get('MaxLines')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetPodLogsResponseBody(TeaModel):
    def __init__(self, job_id=None, logs=None, pod_id=None, pod_uid=None, request_id=None):
        self.job_id = job_id  # type: str
        self.logs = logs  # type: list[str]
        self.pod_id = pod_id  # type: str
        self.pod_uid = pod_uid  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPodLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPodLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPodLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPodLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPodLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTensorboardRequest(TeaModel):
    def __init__(self, jod_id=None, token=None, workspace_id=None):
        self.jod_id = jod_id  # type: str
        self.token = token  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTensorboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jod_id is not None:
            result['JodId'] = self.jod_id
        if self.token is not None:
            result['Token'] = self.token
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JodId') is not None:
            self.jod_id = m.get('JodId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetTensorboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Tensorboard

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTensorboardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Tensorboard()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTensorboardSharedUrlRequest(TeaModel):
    def __init__(self, expire_time_seconds=None):
        self.expire_time_seconds = expire_time_seconds  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTensorboardSharedUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time_seconds is not None:
            result['ExpireTimeSeconds'] = self.expire_time_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTimeSeconds') is not None:
            self.expire_time_seconds = m.get('ExpireTimeSeconds')
        return self


class GetTensorboardSharedUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, tensorboard_shared_url=None):
        self.request_id = request_id  # type: str
        self.tensorboard_shared_url = tensorboard_shared_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTensorboardSharedUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_shared_url is not None:
            result['TensorboardSharedUrl'] = self.tensorboard_shared_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardSharedUrl') is not None:
            self.tensorboard_shared_url = m.get('TensorboardSharedUrl')
        return self


class GetTensorboardSharedUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTensorboardSharedUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTensorboardSharedUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTensorboardSharedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(self, expire_time=None, target_id=None, target_type=None):
        self.expire_time = expire_time  # type: long
        self.target_id = target_id  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None):
        self.request_id = request_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebTerminalRequest(TeaModel):
    def __init__(self, is_shared=None, pod_uid=None):
        self.is_shared = is_shared  # type: bool
        # Pod UID。
        self.pod_uid = pod_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebTerminalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_shared is not None:
            result['IsShared'] = self.is_shared
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        return self


class GetWebTerminalResponseBody(TeaModel):
    def __init__(self, request_id=None, web_terminal_url=None):
        self.request_id = request_id  # type: str
        self.web_terminal_url = web_terminal_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebTerminalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.web_terminal_url is not None:
            result['WebTerminalUrl'] = self.web_terminal_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebTerminalUrl') is not None:
            self.web_terminal_url = m.get('WebTerminalUrl')
        return self


class GetWebTerminalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWebTerminalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWebTerminalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWebTerminalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsRequest(TeaModel):
    def __init__(self, accelerator_type=None, order=None, page_number=None, page_size=None, sort_by=None):
        self.accelerator_type = accelerator_type  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsSpecsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListEcsSpecsResponseBody(TeaModel):
    def __init__(self, ecs_specs=None, request_id=None, total_count=None):
        self.ecs_specs = ecs_specs  # type: list[EcsSpec]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.ecs_specs:
            for k in self.ecs_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEcsSpecsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k in self.ecs_specs:
                result['EcsSpecs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k in m.get('EcsSpecs'):
                temp_model = EcsSpec()
                self.ecs_specs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEcsSpecsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEcsSpecsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEcsSpecsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEcsSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, business_user_id=None, caller=None, display_name=None, end_time=None,
                 from_all_workspaces=None, job_id=None, job_type=None, order=None, page_number=None, page_size=None, pipeline_id=None,
                 resource_id=None, show_own=None, sort_by=None, start_time=None, status=None, tags=None, user_id_for_filter=None,
                 workspace_id=None):
        self.business_user_id = business_user_id  # type: str
        self.caller = caller  # type: str
        self.display_name = display_name  # type: str
        self.end_time = end_time  # type: str
        self.from_all_workspaces = from_all_workspaces  # type: bool
        self.job_id = job_id  # type: str
        self.job_type = job_type  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.pipeline_id = pipeline_id  # type: str
        self.resource_id = resource_id  # type: str
        self.show_own = show_own  # type: bool
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: dict[str, str]
        self.user_id_for_filter = user_id_for_filter  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.from_all_workspaces is not None:
            result['FromAllWorkspaces'] = self.from_all_workspaces
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.show_own is not None:
            result['ShowOwn'] = self.show_own
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_id_for_filter is not None:
            result['UserIdForFilter'] = self.user_id_for_filter
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FromAllWorkspaces') is not None:
            self.from_all_workspaces = m.get('FromAllWorkspaces')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserIdForFilter') is not None:
            self.user_id_for_filter = m.get('UserIdForFilter')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListJobsShrinkRequest(TeaModel):
    def __init__(self, business_user_id=None, caller=None, display_name=None, end_time=None,
                 from_all_workspaces=None, job_id=None, job_type=None, order=None, page_number=None, page_size=None, pipeline_id=None,
                 resource_id=None, show_own=None, sort_by=None, start_time=None, status=None, tags_shrink=None,
                 user_id_for_filter=None, workspace_id=None):
        self.business_user_id = business_user_id  # type: str
        self.caller = caller  # type: str
        self.display_name = display_name  # type: str
        self.end_time = end_time  # type: str
        self.from_all_workspaces = from_all_workspaces  # type: bool
        self.job_id = job_id  # type: str
        self.job_type = job_type  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.pipeline_id = pipeline_id  # type: str
        self.resource_id = resource_id  # type: str
        self.show_own = show_own  # type: bool
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.user_id_for_filter = user_id_for_filter  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.from_all_workspaces is not None:
            result['FromAllWorkspaces'] = self.from_all_workspaces
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.show_own is not None:
            result['ShowOwn'] = self.show_own
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_id_for_filter is not None:
            result['UserIdForFilter'] = self.user_id_for_filter
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FromAllWorkspaces') is not None:
            self.from_all_workspaces = m.get('FromAllWorkspaces')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserIdForFilter') is not None:
            self.user_id_for_filter = m.get('UserIdForFilter')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, jobs=None, request_id=None, total_count=None):
        self.jobs = jobs  # type: list[JobItem]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = JobItem()
                self.jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListTensorboardsRequest(TeaModel):
    def __init__(self, display_name=None, end_time=None, job_id=None, order=None, page_number=None, page_size=None,
                 show_own=None, sort_by=None, source_id=None, source_type=None, start_time=None, status=None,
                 tensorboard_id=None, verbose=None, workspace_id=None):
        self.display_name = display_name  # type: str
        self.end_time = end_time  # type: str
        self.job_id = job_id  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.show_own = show_own  # type: bool
        self.sort_by = sort_by  # type: str
        self.source_id = source_id  # type: str
        self.source_type = source_type  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.tensorboard_id = tensorboard_id  # type: str
        self.verbose = verbose  # type: bool
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTensorboardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.show_own is not None:
            result['ShowOwn'] = self.show_own
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTensorboardsResponseBody(TeaModel):
    def __init__(self, request_id=None, tensorboards=None, total_count=None):
        self.request_id = request_id  # type: str
        self.tensorboards = tensorboards  # type: list[Tensorboard]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.tensorboards:
            for k in self.tensorboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTensorboardsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tensorboards'] = []
        if self.tensorboards is not None:
            for k in self.tensorboards:
                result['Tensorboards'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tensorboards = []
        if m.get('Tensorboards') is not None:
            for k in m.get('Tensorboards'):
                temp_model = Tensorboard()
                self.tensorboards.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTensorboardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTensorboardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTensorboardsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTensorboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartTensorboardRequest, self).to_map()
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


class StartTensorboardResponseBody(TeaModel):
    def __init__(self, request_id=None, tensorboard_id=None):
        self.request_id = request_id  # type: str
        self.tensorboard_id = tensorboard_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class StartTensorboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartTensorboardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None):
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTensorboardRequest, self).to_map()
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


class StopTensorboardResponseBody(TeaModel):
    def __init__(self, request_id=None, tensorboard_id=None):
        self.request_id = request_id  # type: str
        self.tensorboard_id = tensorboard_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class StopTensorboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopTensorboardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateJobRequest(TeaModel):
    def __init__(self, priority=None):
        self.priority = priority  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class UpdateJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTensorboardRequest(TeaModel):
    def __init__(self, max_running_time_minutes=None, workspace_id=None):
        self.max_running_time_minutes = max_running_time_minutes  # type: long
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTensorboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_running_time_minutes is not None:
            result['MaxRunningTimeMinutes'] = self.max_running_time_minutes
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRunningTimeMinutes') is not None:
            self.max_running_time_minutes = m.get('MaxRunningTimeMinutes')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateTensorboardResponseBody(TeaModel):
    def __init__(self, request_id=None, tensorboard_id=None):
        self.request_id = request_id  # type: str
        self.tensorboard_id = tensorboard_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class UpdateTensorboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTensorboardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


