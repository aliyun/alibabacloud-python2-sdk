# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class JobSettings(TeaModel):
    def __init__(self, business_user_id=None, caller=None, tags=None, pipeline_id=None):
        # 作业关联用户ID
        self.business_user_id = business_user_id  # type: str
        # 调用方
        self.caller = caller  # type: str
        # 自定义标签
        self.tags = tags  # type: dict[str, str]
        # 工作流ID
        self.pipeline_id = pipeline_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class QuotaDetail(TeaModel):
    def __init__(self, cpu=None, memory=None, gpu=None, gputype=None, gputype_full_name=None, gpudetails=None):
        # CPU核数
        self.cpu = cpu  # type: str
        # 内存容量
        self.memory = memory  # type: str
        # GPU卡数
        self.gpu = gpu  # type: str
        # GPU卡型
        self.gputype = gputype  # type: str
        # GPU卡型全名
        self.gputype_full_name = gputype_full_name  # type: str
        # GPU详情
        self.gpudetails = gpudetails  # type: list[GPUDetail]

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
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.gputype_full_name is not None:
            result['GPUTypeFullName'] = self.gputype_full_name
        result['GPUDetails'] = []
        if self.gpudetails is not None:
            for k in self.gpudetails:
                result['GPUDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('GPUTypeFullName') is not None:
            self.gputype_full_name = m.get('GPUTypeFullName')
        self.gpudetails = []
        if m.get('GPUDetails') is not None:
            for k in m.get('GPUDetails'):
                temp_model = GPUDetail()
                self.gpudetails.append(temp_model.from_map(k))
        return self


class GPUDetail(TeaModel):
    def __init__(self, gpu=None, gputype=None, gputype_full_name=None):
        # GPU卡数
        self.gpu = gpu  # type: str
        # GPU卡型
        self.gputype = gputype  # type: str
        # GPU卡型全名
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


class Tensorboard(TeaModel):
    def __init__(self, tensorboard_id=None, tensorboard_url=None, status=None, duration=None, gmt_create_time=None,
                 gmt_modify_time=None, request_id=None, display_name=None, data_source_id=None, summary_path=None, user_id=None,
                 reason_code=None, reason_message=None, job_id=None):
        # Tensorboard Id
        self.tensorboard_id = tensorboard_id  # type: str
        # Tensorboard URL
        self.tensorboard_url = tensorboard_url  # type: str
        # 状态
        self.status = status  # type: str
        # 运行时长
        self.duration = duration  # type: str
        # 创建时间（UTC）
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间（UTC）
        self.gmt_modify_time = gmt_modify_time  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 展示名称
        self.display_name = display_name  # type: str
        # 数据源Id
        self.data_source_id = data_source_id  # type: str
        # 文件路径
        self.summary_path = summary_path  # type: str
        # 创建者
        self.user_id = user_id  # type: str
        # 状态详情码
        self.reason_code = reason_code  # type: str
        # 状态详情
        self.reason_message = reason_message  # type: str
        # 任务Id
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Tensorboard, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.tensorboard_url is not None:
            result['TensorboardUrl'] = self.tensorboard_url
        if self.status is not None:
            result['Status'] = self.status
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('TensorboardUrl') is not None:
            self.tensorboard_url = m.get('TensorboardUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class AliyunAccounts(TeaModel):
    def __init__(self, aliyun_uid=None, employee_id=None, gmt_create_time=None, gmt_modify_time=None):
        # Aliyun账号的UID
        self.aliyun_uid = aliyun_uid  # type: str
        # 弹内用户的工号
        self.employee_id = employee_id  # type: str
        # 这条记录的创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 这条记录的上次修改时间
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


class ContainerSpec(TeaModel):
    def __init__(self, name=None, image=None, command=None, args=None, working_dir=None, env=None):
        # 容器名称
        self.name = name  # type: str
        # 容器镜像地址
        self.image = image  # type: str
        # 用户命令
        self.command = command  # type: list[str]
        # 命令参数
        self.args = args  # type: list[str]
        # 容器内工作目录
        self.working_dir = working_dir  # type: str
        # 环境变量
        self.env = env  # type: list[EnvVar]

    def validate(self):
        if self.env:
            for k in self.env:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ContainerSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.image is not None:
            result['Image'] = self.image
        if self.command is not None:
            result['Command'] = self.command
        if self.args is not None:
            result['Args'] = self.args
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        result['Env'] = []
        if self.env is not None:
            for k in self.env:
                result['Env'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        self.env = []
        if m.get('Env') is not None:
            for k in m.get('Env'):
                temp_model = EnvVar()
                self.env.append(temp_model.from_map(k))
        return self


class EcsSpec(TeaModel):
    def __init__(self, instance_type=None, cpu=None, gpu=None, gpu_type=None, memory=None):
        # 规格类型
        self.instance_type = instance_type  # type: str
        # cpu数量
        self.cpu = cpu  # type: int
        # gpu数量
        self.gpu = gpu  # type: int
        # gpu类型
        self.gpu_type = gpu_type  # type: str
        # Memory数量
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcsSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class PodMetric(TeaModel):
    def __init__(self, pod_id=None, metrics=None):
        # Pod编号
        self.pod_id = pod_id  # type: str
        # 监控指标样本序列
        self.metrics = metrics  # type: list[Metric]

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
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        return self


class JobItemDataSources(TeaModel):
    def __init__(self, data_source_id=None, mount_path=None):
        # 数据源Id
        self.data_source_id = data_source_id  # type: str
        # 本地挂载路径
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


class JobItemCodeSource(TeaModel):
    def __init__(self, code_source_id=None, branch=None, commit=None, mount_path=None):
        # 代码源Id
        self.code_source_id = code_source_id  # type: str
        # 代码分支
        self.branch = branch  # type: str
        # 代码Commit
        self.commit = commit  # type: str
        # 本地挂载路径
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobItemCodeSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class JobItem(TeaModel):
    def __init__(self, job_id=None, job_type=None, display_name=None, user_id=None, status=None, workspace_id=None,
                 workspace_name=None, resource_id=None, reason_code=None, reason_message=None, job_specs=None, user_command=None,
                 data_sources=None, code_source=None, thirdparty_libs=None, thirdparty_lib_dir=None, envs=None,
                 gmt_create_time=None, gmt_finish_time=None, duration=None, settings=None):
        # 作业Id
        self.job_id = job_id  # type: str
        # 作业类型
        self.job_type = job_type  # type: str
        # 作业显示名称
        self.display_name = display_name  # type: str
        # 作业提交人Id
        self.user_id = user_id  # type: str
        # 作业状态
        self.status = status  # type: str
        # 作业所属工作空间ID
        self.workspace_id = workspace_id  # type: str
        # 作业所属工作空间名称
        self.workspace_name = workspace_name  # type: str
        # 作业运行所在的资源组ID
        self.resource_id = resource_id  # type: str
        # 状态详情码
        self.reason_code = reason_code  # type: str
        # 状态详情
        self.reason_message = reason_message  # type: str
        # 作业规格配置
        self.job_specs = job_specs  # type: list[JobSpec]
        # 用户命令
        self.user_command = user_command  # type: str
        # 数据源配置列表
        self.data_sources = data_sources  # type: list[JobItemDataSources]
        # 代码源配置
        self.code_source = code_source  # type: JobItemCodeSource
        # 三方库配置列表
        self.thirdparty_libs = thirdparty_libs  # type: list[str]
        # 三方库(requirements.txt)文件路径
        self.thirdparty_lib_dir = thirdparty_lib_dir  # type: str
        # 环境变量配置
        self.envs = envs  # type: dict[str, str]
        # 作业创建时间（UTC）
        self.gmt_create_time = gmt_create_time  # type: str
        # 作业结束时间（UTC）
        self.gmt_finish_time = gmt_finish_time  # type: str
        # 作业运行时长，单位：秒
        self.duration = duration  # type: long
        # 作业额外参数
        self.settings = settings  # type: JobSettings

    def validate(self):
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.code_source:
            self.code_source.validate()
        if self.settings:
            self.settings.validate()

    def to_map(self):
        _map = super(JobItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.user_command is not None:
            result['UserCommand'] = self.user_command
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()
        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs
        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = JobItemDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('CodeSource') is not None:
            temp_model = JobItemCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')
        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Settings') is not None:
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        return self


class JobElasticSpec(TeaModel):
    def __init__(self, enable_elastic_training=None, min_parallelism=None, max_parallelism=None,
                 aimaster_type=None):
        # 打开弹性训练
        self.enable_elastic_training = enable_elastic_training  # type: bool
        # 最小并行度
        self.min_parallelism = min_parallelism  # type: int
        # 最大并行度
        self.max_parallelism = max_parallelism  # type: int
        # aimaster角色使用的资源规格
        self.aimaster_type = aimaster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobElasticSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_elastic_training is not None:
            result['EnableElasticTraining'] = self.enable_elastic_training
        if self.min_parallelism is not None:
            result['MinParallelism'] = self.min_parallelism
        if self.max_parallelism is not None:
            result['MaxParallelism'] = self.max_parallelism
        if self.aimaster_type is not None:
            result['AIMasterType'] = self.aimaster_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableElasticTraining') is not None:
            self.enable_elastic_training = m.get('EnableElasticTraining')
        if m.get('MinParallelism') is not None:
            self.min_parallelism = m.get('MinParallelism')
        if m.get('MaxParallelism') is not None:
            self.max_parallelism = m.get('MaxParallelism')
        if m.get('AIMasterType') is not None:
            self.aimaster_type = m.get('AIMasterType')
        return self


class NodeMetric(TeaModel):
    def __init__(self, node_name=None, metrics=None):
        # 节点名称
        self.node_name = node_name  # type: str
        # 监控指标样本序列
        self.metrics = metrics  # type: list[Metric]

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
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        return self


class CodeSourceItem(TeaModel):
    def __init__(self, code_source_id=None, display_name=None, description=None, code_repo=None, code_branch=None,
                 code_commit=None, code_repo_user_name=None, code_repo_access_token=None, user_id=None, gmt_create_time=None,
                 gmt_modify_time=None):
        # 代码源ID
        self.code_source_id = code_source_id  # type: str
        # 代码源配置的名字
        self.display_name = display_name  # type: str
        # 代码源详细描述
        self.description = description  # type: str
        # 代码仓库地址
        self.code_repo = code_repo  # type: str
        # 代码分支
        self.code_branch = code_branch  # type: str
        # 代码Commit ID
        self.code_commit = code_commit  # type: str
        # 访问代码仓库的用户名
        self.code_repo_user_name = code_repo_user_name  # type: str
        # 访问代码仓库所用的AccessToken
        self.code_repo_access_token = code_repo_access_token  # type: str
        # 代码源配置的用户ID
        self.user_id = user_id  # type: str
        # 创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间
        self.gmt_modify_time = gmt_modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CodeSourceItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.code_repo is not None:
            result['CodeRepo'] = self.code_repo
        if self.code_branch is not None:
            result['CodeBranch'] = self.code_branch
        if self.code_commit is not None:
            result['CodeCommit'] = self.code_commit
        if self.code_repo_user_name is not None:
            result['CodeRepoUserName'] = self.code_repo_user_name
        if self.code_repo_access_token is not None:
            result['CodeRepoAccessToken'] = self.code_repo_access_token
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CodeRepo') is not None:
            self.code_repo = m.get('CodeRepo')
        if m.get('CodeBranch') is not None:
            self.code_branch = m.get('CodeBranch')
        if m.get('CodeCommit') is not None:
            self.code_commit = m.get('CodeCommit')
        if m.get('CodeRepoUserName') is not None:
            self.code_repo_user_name = m.get('CodeRepoUserName')
        if m.get('CodeRepoAccessToken') is not None:
            self.code_repo_access_token = m.get('CodeRepoAccessToken')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        return self


class Quota(TeaModel):
    def __init__(self, quota_id=None, quota_name=None, quota_type=None, used_quota=None, total_quota=None,
                 cluster_id=None, cluster_name=None, is_exclusive_quota=None):
        # 资源配额id
        self.quota_id = quota_id  # type: str
        # 资源配额名称
        self.quota_name = quota_name  # type: str
        # 资源配额类型
        self.quota_type = quota_type  # type: str
        # 资源用量
        self.used_quota = used_quota  # type: QuotaDetail
        # 资源总量
        self.total_quota = total_quota  # type: QuotaDetail
        # 集群id
        self.cluster_id = cluster_id  # type: str
        # 集群名称
        self.cluster_name = cluster_name  # type: str
        # 是否是独占Quota组
        self.is_exclusive_quota = is_exclusive_quota  # type: bool

    def validate(self):
        if self.used_quota:
            self.used_quota.validate()
        if self.total_quota:
            self.total_quota.validate()

    def to_map(self):
        _map = super(Quota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.is_exclusive_quota is not None:
            result['IsExclusiveQuota'] = self.is_exclusive_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('UsedQuota') is not None:
            temp_model = QuotaDetail()
            self.used_quota = temp_model.from_map(m['UsedQuota'])
        if m.get('TotalQuota') is not None:
            temp_model = QuotaDetail()
            self.total_quota = temp_model.from_map(m['TotalQuota'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('IsExclusiveQuota') is not None:
            self.is_exclusive_quota = m.get('IsExclusiveQuota')
        return self


class EnvVar(TeaModel):
    def __init__(self, name=None, value=None):
        # 环境变量名称
        self.name = name  # type: str
        # 环境变量值
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


class Metric(TeaModel):
    def __init__(self, time=None, value=None):
        # 时间戳（毫秒）
        self.time = time  # type: long
        # 样本值
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


class JobSpec(TeaModel):
    def __init__(self, type=None, image=None, pod_count=None, ecs_spec=None, extra_pod_spec=None,
                 resource_config=None):
        # 类型
        self.type = type  # type: str
        # 镜像
        self.image = image  # type: str
        # 实例数量
        self.pod_count = pod_count  # type: long
        # Ecs实例规格
        self.ecs_spec = ecs_spec  # type: str
        # 额外的Pod配置
        self.extra_pod_spec = extra_pod_spec  # type: ExtraPodSpec
        # 资源配置
        self.resource_config = resource_config  # type: ResourceConfig

    def validate(self):
        if self.extra_pod_spec:
            self.extra_pod_spec.validate()
        if self.resource_config:
            self.resource_config.validate()

    def to_map(self):
        _map = super(JobSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.image is not None:
            result['Image'] = self.image
        if self.pod_count is not None:
            result['PodCount'] = self.pod_count
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.extra_pod_spec is not None:
            result['ExtraPodSpec'] = self.extra_pod_spec.to_map()
        if self.resource_config is not None:
            result['ResourceConfig'] = self.resource_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('ExtraPodSpec') is not None:
            temp_model = ExtraPodSpec()
            self.extra_pod_spec = temp_model.from_map(m['ExtraPodSpec'])
        if m.get('ResourceConfig') is not None:
            temp_model = ResourceConfig()
            self.resource_config = temp_model.from_map(m['ResourceConfig'])
        return self


class DataSourceItem(TeaModel):
    def __init__(self, data_source_type=None, data_source_id=None, display_name=None, description=None,
                 file_system_id=None, path=None, endpoint=None, options=None, mount_path=None, user_id=None, gmt_create_time=None,
                 gmt_modify_time=None):
        # 数据源类型
        self.data_source_type = data_source_type  # type: str
        # 数据源Id
        self.data_source_id = data_source_id  # type: str
        # 数据源显示名称
        self.display_name = display_name  # type: str
        # 数据源描述
        self.description = description  # type: str
        # 阿里云NAS文件系统Id
        self.file_system_id = file_system_id  # type: str
        # 阿里云OSS文件系统路径
        self.path = path  # type: str
        # 阿里云OSS文件系统服务端点
        self.endpoint = endpoint  # type: str
        # 阿里云OSS文件系统配置选项
        self.options = options  # type: str
        # 本地挂载目录
        self.mount_path = mount_path  # type: str
        # 创建人Id
        self.user_id = user_id  # type: str
        # 创建时间（UTC）
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间（UTC）
        self.gmt_modify_time = gmt_modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSourceItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.options is not None:
            result['Options'] = self.options
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        return self


class ImageItem(TeaModel):
    def __init__(self, image_tag=None, image_url=None, image_url_vpc=None, image_provider_type=None,
                 accelerator_type=None, framework=None):
        # 镜像Tag
        self.image_tag = image_tag  # type: str
        # 镜像地址
        self.image_url = image_url  # type: str
        # 镜像vpc地址
        self.image_url_vpc = image_url_vpc  # type: str
        # 镜像类型
        self.image_provider_type = image_provider_type  # type: str
        # 加速器类型
        self.accelerator_type = accelerator_type  # type: str
        # 镜像包含的框架类型
        self.framework = framework  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.image_url_vpc is not None:
            result['ImageUrlVpc'] = self.image_url_vpc
        if self.image_provider_type is not None:
            result['ImageProviderType'] = self.image_provider_type
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.framework is not None:
            result['Framework'] = self.framework
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ImageUrlVpc') is not None:
            self.image_url_vpc = m.get('ImageUrlVpc')
        if m.get('ImageProviderType') is not None:
            self.image_provider_type = m.get('ImageProviderType')
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Framework') is not None:
            self.framework = m.get('Framework')
        return self


class ResourceConfig(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None, shared_memory=None, gputype=None):
        # CPU核心数
        self.cpu = cpu  # type: str
        # GPU核心数
        self.gpu = gpu  # type: str
        # 内存容量
        self.memory = memory  # type: str
        # 共享内存容量
        self.shared_memory = shared_memory  # type: str
        # 显卡类型
        self.gputype = gputype  # type: str

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
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        return self


class Resources(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None):
        # CPU核心数
        self.cpu = cpu  # type: str
        # GPU卡数
        self.gpu = gpu  # type: str
        # 内存大小
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


class ExtraPodSpec(TeaModel):
    def __init__(self, side_car_containers=None, init_containers=None, pod_labels=None, pod_annotations=None,
                 shared_volume_mount_paths=None):
        # 伴随容器
        self.side_car_containers = side_car_containers  # type: list[ContainerSpec]
        # 初始化容器
        self.init_containers = init_containers  # type: list[ContainerSpec]
        # Pod标签
        self.pod_labels = pod_labels  # type: dict[str, str]
        # Pod注解
        self.pod_annotations = pod_annotations  # type: dict[str, str]
        # 容器间共享的本地目录
        self.shared_volume_mount_paths = shared_volume_mount_paths  # type: list[str]

    def validate(self):
        if self.side_car_containers:
            for k in self.side_car_containers:
                if k:
                    k.validate()
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ExtraPodSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SideCarContainers'] = []
        if self.side_car_containers is not None:
            for k in self.side_car_containers:
                result['SideCarContainers'].append(k.to_map() if k else None)
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.pod_labels is not None:
            result['PodLabels'] = self.pod_labels
        if self.pod_annotations is not None:
            result['PodAnnotations'] = self.pod_annotations
        if self.shared_volume_mount_paths is not None:
            result['SharedVolumeMountPaths'] = self.shared_volume_mount_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.side_car_containers = []
        if m.get('SideCarContainers') is not None:
            for k in m.get('SideCarContainers'):
                temp_model = ContainerSpec()
                self.side_car_containers.append(temp_model.from_map(k))
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = ContainerSpec()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('PodLabels') is not None:
            self.pod_labels = m.get('PodLabels')
        if m.get('PodAnnotations') is not None:
            self.pod_annotations = m.get('PodAnnotations')
        if m.get('SharedVolumeMountPaths') is not None:
            self.shared_volume_mount_paths = m.get('SharedVolumeMountPaths')
        return self


class Member(TeaModel):
    def __init__(self, member_id=None, member_type=None):
        # 成员id
        self.member_id = member_id  # type: str
        # 成员角色
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


class Workspace(TeaModel):
    def __init__(self, workspace_id=None, workspace_name=None, creator=None, gmt_create_time=None,
                 gmt_modify_time=None, quotas=None, total_resources=None, members=None, workspace_admins=None):
        # 工作空间id
        self.workspace_id = workspace_id  # type: str
        # 工作空间名称
        self.workspace_name = workspace_name  # type: str
        # 创建者
        self.creator = creator  # type: str
        # 创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 最近修改时间
        self.gmt_modify_time = gmt_modify_time  # type: str
        # 资源配额列表
        self.quotas = quotas  # type: list[Quota]
        # 资源总量
        self.total_resources = total_resources  # type: Resources
        # 成员列表
        self.members = members  # type: list[Member]
        # 管理员列表
        self.workspace_admins = workspace_admins  # type: list[Member]

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.workspace_admins:
            for k in self.workspace_admins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Workspace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        result['WorkspaceAdmins'] = []
        if self.workspace_admins is not None:
            for k in self.workspace_admins:
                result['WorkspaceAdmins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = Quota()
                self.quotas.append(temp_model.from_map(k))
        if m.get('TotalResources') is not None:
            temp_model = Resources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = Member()
                self.members.append(temp_model.from_map(k))
        self.workspace_admins = []
        if m.get('WorkspaceAdmins') is not None:
            for k in m.get('WorkspaceAdmins'):
                temp_model = Member()
                self.workspace_admins.append(temp_model.from_map(k))
        return self


class ListDataSourcesRequest(TeaModel):
    def __init__(self, data_source_type=None, display_name=None, page_number=None, page_size=None, sort_by=None,
                 order=None):
        # 数据源类型
        self.data_source_type = data_source_type  # type: str
        # 数据源显示名称，支持模糊查询
        self.display_name = display_name  # type: str
        # 查询第几页数据
        self.page_number = page_number  # type: int
        # 设置查询的分页大写
        self.page_size = page_size  # type: int
        # 按返回字段排序
        self.sort_by = sort_by  # type: str
        # 排序顺序
        self.order = order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(self, data_sources=None, total_count=None, request_id=None):
        # 数据源配置列表
        self.data_sources = data_sources  # type: list[DataSourceItem]
        # 符合条件的数据源总数量
        self.total_count = total_count  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = DataSourceItem()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponse, self).to_map()
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
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobsStatisticsRequest(TeaModel):
    def __init__(self, workspace_id=None):
        # 工作空间id
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobsStatisticsRequest, self).to_map()
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


class GetJobsStatisticsResponseBody(TeaModel):
    def __init__(self, statistics=None, request_id=None):
        # 当前的Workspace ID下面的JOB统计数据
        self.statistics = statistics  # type: dict[str, any]
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobsStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobsStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetJobsStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobsStatisticsResponse, self).to_map()
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
            temp_model = GetJobsStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceResponseBody(TeaModel):
    def __init__(self, data_source_type=None, data_source_id=None, display_name=None, description=None,
                 file_system_id=None, path=None, endpoint=None, options=None, mount_path=None, user_id=None, gmt_create_time=None,
                 gmt_modify_time=None, request_id=None):
        # 数据源类型
        self.data_source_type = data_source_type  # type: str
        # 数据源Id
        self.data_source_id = data_source_id  # type: str
        # 数据源显示名称
        self.display_name = display_name  # type: str
        # 数据源描述
        self.description = description  # type: str
        # 阿里云NAS文件系统Id
        self.file_system_id = file_system_id  # type: str
        # 阿里云OSS文件系统路径
        self.path = path  # type: str
        # 阿里云OSS文件系统服务端点
        self.endpoint = endpoint  # type: str
        # 阿里云OSS文件系统配置选项
        self.options = options  # type: str
        # 本地挂载目录
        self.mount_path = mount_path  # type: str
        # 创建人Id
        self.user_id = user_id  # type: str
        # 创建时间（UTC）
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间（UTC）
        self.gmt_modify_time = gmt_modify_time  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.options is not None:
            result['Options'] = self.options
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDataSourceResponse, self).to_map()
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
            temp_model = GetDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaRequest(TeaModel):
    def __init__(self, quota_name=None, quota_type=None, quota_detail=None):
        # 资源配额名称
        self.quota_name = quota_name  # type: str
        # 资源配额类型
        self.quota_type = quota_type  # type: str
        # 资源配额参数
        self.quota_detail = quota_detail  # type: QuotaDetail

    def validate(self):
        if self.quota_detail:
            self.quota_detail.validate()

    def to_map(self):
        _map = super(CreateQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.quota_detail is not None:
            result['QuotaDetail'] = self.quota_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('QuotaDetail') is not None:
            temp_model = QuotaDetail()
            self.quota_detail = temp_model.from_map(m['QuotaDetail'])
        return self


class CreateQuotaResponseBody(TeaModel):
    def __init__(self, quota_id=None, request_id=None):
        # 资源配额id
        self.quota_id = quota_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQuotaResponse, self).to_map()
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
            temp_model = CreateQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaResponseBody(TeaModel):
    def __init__(self, quota_id=None, quota_name=None, quota_type=None, used_quota=None, total_quota=None,
                 cluster_id=None, cluster_name=None, request_id=None):
        # 资源配额id
        self.quota_id = quota_id  # type: str
        # 资源配额名称
        self.quota_name = quota_name  # type: str
        # 资源配额类型
        self.quota_type = quota_type  # type: str
        # 资源用量
        self.used_quota = used_quota  # type: QuotaDetail
        # 资源总量
        self.total_quota = total_quota  # type: QuotaDetail
        # 集群id
        self.cluster_id = cluster_id  # type: str
        # 集群名称
        self.cluster_name = cluster_name  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.used_quota:
            self.used_quota.validate()
        if self.total_quota:
            self.total_quota.validate()

    def to_map(self):
        _map = super(GetQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('UsedQuota') is not None:
            temp_model = QuotaDetail()
            self.used_quota = temp_model.from_map(m['UsedQuota'])
        if m.get('TotalQuota') is not None:
            temp_model = QuotaDetail()
            self.total_quota = temp_model.from_map(m['TotalQuota'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeSourceResponseBody(TeaModel):
    def __init__(self, code_source_id=None, display_name=None, description=None, code_repo=None, code_branch=None,
                 code_commit=None, code_repo_user_name=None, code_repo_access_token=None, mount_path=None, user_id=None,
                 gmt_create_time=None, gmt_modify_time=None, request_id=None):
        # 代码源配置ID
        self.code_source_id = code_source_id  # type: str
        # 代码源配置名字
        self.display_name = display_name  # type: str
        # 详细描述
        self.description = description  # type: str
        # 代码仓库地址
        self.code_repo = code_repo  # type: str
        # 代码仓库分支
        self.code_branch = code_branch  # type: str
        # 代码Commit
        self.code_commit = code_commit  # type: str
        # 代码仓库的用户名
        self.code_repo_user_name = code_repo_user_name  # type: str
        # 访问代码仓库的token
        self.code_repo_access_token = code_repo_access_token  # type: str
        # 代码本地挂载目录，默认挂载到/root/code/下
        self.mount_path = mount_path  # type: str
        # 代码配置源的创建者ID
        self.user_id = user_id  # type: str
        # 创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间
        self.gmt_modify_time = gmt_modify_time  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.code_repo is not None:
            result['CodeRepo'] = self.code_repo
        if self.code_branch is not None:
            result['CodeBranch'] = self.code_branch
        if self.code_commit is not None:
            result['CodeCommit'] = self.code_commit
        if self.code_repo_user_name is not None:
            result['CodeRepoUserName'] = self.code_repo_user_name
        if self.code_repo_access_token is not None:
            result['CodeRepoAccessToken'] = self.code_repo_access_token
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CodeRepo') is not None:
            self.code_repo = m.get('CodeRepo')
        if m.get('CodeBranch') is not None:
            self.code_branch = m.get('CodeBranch')
        if m.get('CodeCommit') is not None:
            self.code_commit = m.get('CodeCommit')
        if m.get('CodeRepoUserName') is not None:
            self.code_repo_user_name = m.get('CodeRepoUserName')
        if m.get('CodeRepoAccessToken') is not None:
            self.code_repo_access_token = m.get('CodeRepoAccessToken')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCodeSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCodeSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCodeSourceResponse, self).to_map()
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
            temp_model = GetCodeSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None, vpc_id=None, v_switch_id=None, v_switch_name=None, cidr_block=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 所属VPC的id
        self.vpc_id = vpc_id  # type: str
        # 交换机的id
        self.v_switch_id = v_switch_id  # type: str
        # 交换机的名称
        self.v_switch_name = v_switch_name  # type: str
        # 网段
        self.cidr_block = cidr_block  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSwitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        return self


class GetSwitchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSwitchResponse, self).to_map()
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
            temp_model = GetSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPodEventsRequest(TeaModel):
    def __init__(self, max_events_num=None, start_time=None, end_time=None):
        # 返回的事件最大数量
        self.max_events_num = max_events_num  # type: int
        # 起始时间
        self.start_time = start_time  # type: str
        # 截止时间
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPodEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class GetPodEventsResponseBody(TeaModel):
    def __init__(self, job_id=None, pod_id=None, events=None, request_id=None):
        # 作业ID
        self.job_id = job_id  # type: str
        # 运行示例ID
        self.pod_id = pod_id  # type: str
        # 事件列表
        self.events = events  # type: list[str]
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPodEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.events is not None:
            result['Events'] = self.events
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPodEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPodEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPodEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSwitchesRequest(TeaModel):
    def __init__(self, vpc_id=None, page_number=None, page_size=None):
        # 所属VPC id
        self.vpc_id = vpc_id  # type: str
        # 取第几页的数据
        self.page_number = page_number  # type: int
        # 分页大小
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSwitchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSwitchesResponseBodySwitches(TeaModel):
    def __init__(self, v_switch_id=None, v_switch_name=None, vpc_id=None, description=None, cidr_block=None):
        # 交换机id
        self.v_switch_id = v_switch_id  # type: str
        # 交换机名称
        self.v_switch_name = v_switch_name  # type: str
        # 所属VPCid
        self.vpc_id = vpc_id  # type: str
        # 描述
        self.description = description  # type: str
        # 网段
        self.cidr_block = cidr_block  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSwitchesResponseBodySwitches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        return self


class ListSwitchesResponseBody(TeaModel):
    def __init__(self, switches=None, total_count=None, request_id=None):
        # 代码源配置列表
        self.switches = switches  # type: list[ListSwitchesResponseBodySwitches]
        # 符合过滤条件的代码源配置的总数量
        self.total_count = total_count  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.switches:
            for k in self.switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSwitchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Switches'] = []
        if self.switches is not None:
            for k in self.switches:
                result['Switches'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.switches = []
        if m.get('Switches') is not None:
            for k in m.get('Switches'):
                temp_model = ListSwitchesResponseBodySwitches()
                self.switches.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSwitchesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSwitchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSwitchesResponse, self).to_map()
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
            temp_model = ListSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTensorboardsRequest(TeaModel):
    def __init__(self, verbose=None, workspace_id=None, display_name=None, status=None, start_time=None,
                 end_time=None, page_number=None, page_size=None, sort_by=None, order=None, job_id=None, tensorboard_id=None):
        # 是否显示详情
        self.verbose = verbose  # type: bool
        # 工作空间ID
        self.workspace_id = workspace_id  # type: str
        # 展示名称
        self.display_name = display_name  # type: str
        # 根据状态过滤
        self.status = status  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 截止时间
        self.end_time = end_time  # type: str
        # 当前页
        self.page_number = page_number  # type: int
        # 每页返回的作业数
        self.page_size = page_size  # type: int
        # 按返回字段排序
        self.sort_by = sort_by  # type: str
        # 排序顺序
        self.order = order  # type: str
        # JobId
        self.job_id = job_id  # type: str
        # TensorboardId
        self.tensorboard_id = tensorboard_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTensorboardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class ListTensorboardsResponseBody(TeaModel):
    def __init__(self, tensorboards=None, total_count=None, request_id=None):
        # Tensorboard 列表
        self.tensorboards = tensorboards  # type: list[Tensorboard]
        # 符合条件的数据源总数量
        self.total_count = total_count  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

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
        result['Tensorboards'] = []
        if self.tensorboards is not None:
            for k in self.tensorboards:
                result['Tensorboards'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tensorboards = []
        if m.get('Tensorboards') is not None:
            for k in m.get('Tensorboards'):
                temp_model = Tensorboard()
                self.tensorboards.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTensorboardsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTensorboardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTensorboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityGroupsRequest(TeaModel):
    def __init__(self, vpc_id=None, page_number=None, page_size=None):
        # 所属Vpc
        self.vpc_id = vpc_id  # type: str
        # 取第几页的数据
        self.page_number = page_number  # type: int
        # 分页大小
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSecurityGroupsResponseBodySecurityGroups(TeaModel):
    def __init__(self, security_group_id=None, security_group_name=None, vpc_id=None, description=None):
        # 安全组Id
        self.security_group_id = security_group_id  # type: str
        # 安全组名称
        self.security_group_name = security_group_name  # type: str
        # 所属VPC ID
        self.vpc_id = vpc_id  # type: str
        # 描述
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityGroupsResponseBodySecurityGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ListSecurityGroupsResponseBody(TeaModel):
    def __init__(self, security_groups=None, total_count=None, request_id=None):
        # 代码源配置列表
        self.security_groups = security_groups  # type: list[ListSecurityGroupsResponseBodySecurityGroups]
        # 符合过滤条件的代码源配置的总数量
        self.total_count = total_count  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.security_groups:
            for k in self.security_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecurityGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k in self.security_groups:
                result['SecurityGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k in m.get('SecurityGroups'):
                temp_model = ListSecurityGroupsResponseBodySecurityGroups()
                self.security_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecurityGroupsResponse, self).to_map()
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
            temp_model = ListSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPodLogsRequest(TeaModel):
    def __init__(self, max_lines=None, start_time=None, end_time=None, download_to_file=None):
        # 返回的日志的最大行数，默认值：2000。
        self.max_lines = max_lines  # type: int
        # 查询的起始时间，默认值：7天前。
        self.start_time = start_time  # type: str
        # 查询的截止时间，默认值：当前。
        self.end_time = end_time  # type: str
        # 是否下载日志文件，默认：false。
        self.download_to_file = download_to_file  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPodLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_lines is not None:
            result['MaxLines'] = self.max_lines
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.download_to_file is not None:
            result['DownloadToFile'] = self.download_to_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxLines') is not None:
            self.max_lines = m.get('MaxLines')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DownloadToFile') is not None:
            self.download_to_file = m.get('DownloadToFile')
        return self


class GetPodLogsResponseBody(TeaModel):
    def __init__(self, job_id=None, pod_id=None, logs=None, request_id=None):
        # 作业ID
        self.job_id = job_id  # type: str
        # 实例ID
        self.pod_id = pod_id  # type: str
        # 日志列表
        self.logs = logs  # type: list[str]
        # 请求ID
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
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPodLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPodLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPodLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 取第几页的数据
        self.page_number = page_number  # type: int
        # 分页大小
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListVpcsResponseBodyVpcs(TeaModel):
    def __init__(self, vpc_id=None, vpc_name=None):
        # vpc的id
        self.vpc_id = vpc_id  # type: str
        # VPC的名称。
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcsResponseBodyVpcs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class ListVpcsResponseBody(TeaModel):
    def __init__(self, vpcs=None, total_count=None, request_id=None):
        # 代码源配置列表
        self.vpcs = vpcs  # type: list[ListVpcsResponseBodyVpcs]
        # 符合过滤条件的代码源配置的总数量
        self.total_count = total_count  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.vpcs:
            for k in self.vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = ListVpcsResponseBodyVpcs()
                self.vpcs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVpcsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVpcsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcsResponse, self).to_map()
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
            temp_model = ListVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None):
        # 工作空间ID
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
    def __init__(self, tensorboard_id=None, request_id=None):
        # Tensorboad Id
        self.tensorboard_id = tensorboard_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopTensorboardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequestDataSources(TeaModel):
    def __init__(self, data_source_id=None, mount_path=None):
        # 数据源Id
        self.data_source_id = data_source_id  # type: str
        # 本地挂载路径
        self.mount_path = mount_path  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class CreateJobRequestCodeSource(TeaModel):
    def __init__(self, code_source_id=None, branch=None, commit=None, mount_path=None):
        # 代码源Id
        self.code_source_id = code_source_id  # type: str
        # 代码分支
        self.branch = branch  # type: str
        # 代码Commit
        self.commit = commit  # type: str
        # 本地挂载路径
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestCodeSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class CreateJobRequestUserVpc(TeaModel):
    def __init__(self, vpc_id=None, switch_id=None, security_group_id=None, extended_cidrs=None):
        # 用户VPC的id
        self.vpc_id = vpc_id  # type: str
        # 用户交换机的id
        self.switch_id = switch_id  # type: str
        # 用户安全组的id
        self.security_group_id = security_group_id  # type: str
        # 扩展网段
        self.extended_cidrs = extended_cidrs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        return self


class CreateJobRequest(TeaModel):
    def __init__(self, display_name=None, job_type=None, job_specs=None, user_command=None, data_sources=None,
                 code_source=None, user_vpc=None, thirdparty_libs=None, thirdparty_lib_dir=None, envs=None,
                 job_max_running_time_minutes=None, workspace_id=None, resource_id=None, priority=None, settings=None, elastic_spec=None):
        # 作业显示名称
        self.display_name = display_name  # type: str
        # 作业类型
        self.job_type = job_type  # type: str
        # 作业规格配置
        self.job_specs = job_specs  # type: list[JobSpec]
        # 作业命令
        self.user_command = user_command  # type: str
        # 数据源配置列表
        self.data_sources = data_sources  # type: list[CreateJobRequestDataSources]
        # 代码源配置
        self.code_source = code_source  # type: CreateJobRequestCodeSource
        # 用户VPC
        self.user_vpc = user_vpc  # type: CreateJobRequestUserVpc
        # 三方库配置列表
        self.thirdparty_libs = thirdparty_libs  # type: list[str]
        # 三方库(requirements.txt)文件路径
        self.thirdparty_lib_dir = thirdparty_lib_dir  # type: str
        # 环境变量配置
        self.envs = envs  # type: dict[str, str]
        # 作业最大运行时间
        self.job_max_running_time_minutes = job_max_running_time_minutes  # type: long
        # 工作空间编号
        self.workspace_id = workspace_id  # type: str
        # 资源组编号
        self.resource_id = resource_id  # type: str
        # 作业优先级
        self.priority = priority  # type: int
        self.settings = settings  # type: JobSettings
        self.elastic_spec = elastic_spec  # type: JobElasticSpec

    def validate(self):
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.code_source:
            self.code_source.validate()
        if self.user_vpc:
            self.user_vpc.validate()
        if self.settings:
            self.settings.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()

    def to_map(self):
        _map = super(CreateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.job_type is not None:
            result['JobType'] = self.job_type
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.user_command is not None:
            result['UserCommand'] = self.user_command
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs
        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.job_max_running_time_minutes is not None:
            result['JobMaxRunningTimeMinutes'] = self.job_max_running_time_minutes
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.elastic_spec is not None:
            result['ElasticSpec'] = self.elastic_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = CreateJobRequestDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('CodeSource') is not None:
            temp_model = CreateJobRequestCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        if m.get('UserVpc') is not None:
            temp_model = CreateJobRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')
        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('JobMaxRunningTimeMinutes') is not None:
            self.job_max_running_time_minutes = m.get('JobMaxRunningTimeMinutes')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Settings') is not None:
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('ElasticSpec') is not None:
            temp_model = JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m['ElasticSpec'])
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # 作业Id
        self.job_id = job_id  # type: str
        # 请求Id
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


class ListCodeSourcesRequest(TeaModel):
    def __init__(self, display_name=None, page_number=None, page_size=None, sort_by=None, order=None):
        # 代码源显示名称，支持模糊匹配
        self.display_name = display_name  # type: str
        # 取第几页的数据
        self.page_number = page_number  # type: int
        # 分页大小
        self.page_size = page_size  # type: int
        # 用于排序的字段名，可选字段名：'DisplayName' 'GmtCreateTime' 'GmtModifyTime'
        self.sort_by = sort_by  # type: str
        # 排序顺序, 枚举值 desc 或者 asc
        self.order = order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCodeSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListCodeSourcesResponseBody(TeaModel):
    def __init__(self, code_sources=None, total_count=None, request_id=None):
        # 代码源配置列表
        self.code_sources = code_sources  # type: list[CodeSourceItem]
        # 符合过滤条件的代码源配置的总数量
        self.total_count = total_count  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.code_sources:
            for k in self.code_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCodeSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CodeSources'] = []
        if self.code_sources is not None:
            for k in self.code_sources:
                result['CodeSources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.code_sources = []
        if m.get('CodeSources') is not None:
            for k in m.get('CodeSources'):
                temp_model = CodeSourceItem()
                self.code_sources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCodeSourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCodeSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCodeSourcesResponse, self).to_map()
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
            temp_model = ListCodeSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JobDispatchSubmitRequest(TeaModel):
    def __init__(self, algo_name=None, project_name=None, properties=None, settings=None):
        # PAI-Xflow名称
        self.algo_name = algo_name  # type: str
        # PAI-project名称
        self.project_name = project_name  # type: str
        # properties of pai command
        self.properties = properties  # type: dict[str, str]
        # odps settings
        self.settings = settings  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobDispatchSubmitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.settings is not None:
            result['Settings'] = self.settings
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Settings') is not None:
            self.settings = m.get('Settings')
        return self


class JobDispatchSubmitResponseBody(TeaModel):
    def __init__(self, job_url=None):
        # 作业Url
        self.job_url = job_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobDispatchSubmitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_url is not None:
            result['JobUrl'] = self.job_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobUrl') is not None:
            self.job_url = m.get('JobUrl')
        return self


class JobDispatchSubmitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: JobDispatchSubmitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(JobDispatchSubmitResponse, self).to_map()
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
            temp_model = JobDispatchSubmitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsRequest(TeaModel):
    def __init__(self, sort_by=None, order=None, page_number=None, page_size=None):
        # 按返回字段排序
        self.sort_by = sort_by  # type: str
        # 排序顺序
        self.order = order  # type: str
        # 查询第几页数据
        self.page_number = page_number  # type: int
        # 设置查询的分页大写
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsSpecsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListEcsSpecsResponseBody(TeaModel):
    def __init__(self, request_id=None, ecs_specs=None, total_count=None):
        # 请求Id
        self.request_id = request_id  # type: str
        # ECS规格列表
        self.ecs_specs = ecs_specs  # type: list[EcsSpec]
        # 符合过滤条件的总数量
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k in self.ecs_specs:
                result['EcsSpecs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k in m.get('EcsSpecs'):
                temp_model = EcsSpec()
                self.ecs_specs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEcsSpecsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEcsSpecsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEcsSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuotaResponseBody(TeaModel):
    def __init__(self, quota_id=None, request_id=None):
        # 资源配额id
        self.quota_id = quota_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQuotaResponse, self).to_map()
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
            temp_model = DeleteQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None):
        # 工作空间ID
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
    def __init__(self, tensorboard_id=None, request_id=None):
        # Tensorboad Id
        self.tensorboard_id = tensorboard_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartTensorboardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None, jod_id=None):
        # 工作空间ID
        self.workspace_id = workspace_id  # type: str
        # JodId
        self.jod_id = jod_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTensorboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.jod_id is not None:
            result['JodId'] = self.jod_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('JodId') is not None:
            self.jod_id = m.get('JodId')
        return self


class GetTensorboardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: Tensorboard

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = Tensorboard()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkspaceResponseBody(TeaModel):
    def __init__(self, workspace=None, is_workspace_admin=None, request_id=None):
        # 工作空间
        self.workspace = workspace  # type: Workspace
        # 是否是当前工作空间的管理员
        self.is_workspace_admin = is_workspace_admin  # type: bool
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.workspace:
            self.workspace.validate()

    def to_map(self):
        _map = super(GetWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace.to_map()
        if self.is_workspace_admin is not None:
            result['IsWorkspaceAdmin'] = self.is_workspace_admin
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Workspace') is not None:
            temp_model = Workspace()
            self.workspace = temp_model.from_map(m['Workspace'])
        if m.get('IsWorkspaceAdmin') is not None:
            self.is_workspace_admin = m.get('IsWorkspaceAdmin')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkspaceResponse, self).to_map()
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
            temp_model = GetWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JobDispatchQueryRequest(TeaModel):
    def __init__(self, algo_name=None, project_name=None, properties=None, settings=None):
        # PAI-Xflow名称
        self.algo_name = algo_name  # type: str
        # PAI-project名称
        self.project_name = project_name  # type: str
        # properties of pai command
        self.properties = properties  # type: dict[str, str]
        # odps settings
        self.settings = settings  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobDispatchQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.settings is not None:
            result['Settings'] = self.settings
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Settings') is not None:
            self.settings = m.get('Settings')
        return self


class JobDispatchQueryShrinkRequest(TeaModel):
    def __init__(self, algo_name=None, project_name=None, properties_shrink=None, settings_shrink=None):
        # PAI-Xflow名称
        self.algo_name = algo_name  # type: str
        # PAI-project名称
        self.project_name = project_name  # type: str
        # properties of pai command
        self.properties_shrink = properties_shrink  # type: str
        # odps settings
        self.settings_shrink = settings_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobDispatchQueryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink
        if self.settings_shrink is not None:
            result['Settings'] = self.settings_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')
        if m.get('Settings') is not None:
            self.settings_shrink = m.get('Settings')
        return self


class JobDispatchQueryResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # 作业Id
        self.job_id = job_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobDispatchQueryResponseBody, self).to_map()
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


class JobDispatchQueryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: JobDispatchQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(JobDispatchQueryResponse, self).to_map()
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
            temp_model = JobDispatchQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, display_name=None, job_type=None, status=None, start_time=None, end_time=None,
                 page_number=None, page_size=None, sort_by=None, order=None, show_own=None, workspace_id=None, resource_id=None,
                 business_user_id=None, caller=None, tags=None, pipeline_id=None):
        # 作业显示名称，支持模糊查询
        self.display_name = display_name  # type: str
        # 作业类型
        self.job_type = job_type  # type: str
        # 作业状态
        self.status = status  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 截止时间
        self.end_time = end_time  # type: str
        # 当前页
        self.page_number = page_number  # type: int
        # 每页返回的作业数
        self.page_size = page_size  # type: int
        # 按返回字段排序
        self.sort_by = sort_by  # type: str
        # 排序顺序
        self.order = order  # type: str
        # 是否只返回当前登录者所提交的作业
        self.show_own = show_own  # type: bool
        # 工作空间ID
        self.workspace_id = workspace_id  # type: str
        # 资源组ID
        self.resource_id = resource_id  # type: str
        # 作业关联用户ID
        self.business_user_id = business_user_id  # type: str
        # 调用方
        self.caller = caller  # type: str
        # 自定义标签
        self.tags = tags  # type: dict[str, str]
        # 工作流ID
        self.pipeline_id = pipeline_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        if self.show_own is not None:
            result['ShowOwn'] = self.show_own
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class ListJobsShrinkRequest(TeaModel):
    def __init__(self, display_name=None, job_type=None, status=None, start_time=None, end_time=None,
                 page_number=None, page_size=None, sort_by=None, order=None, show_own=None, workspace_id=None, resource_id=None,
                 business_user_id=None, caller=None, tags_shrink=None, pipeline_id=None):
        # 作业显示名称，支持模糊查询
        self.display_name = display_name  # type: str
        # 作业类型
        self.job_type = job_type  # type: str
        # 作业状态
        self.status = status  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 截止时间
        self.end_time = end_time  # type: str
        # 当前页
        self.page_number = page_number  # type: int
        # 每页返回的作业数
        self.page_size = page_size  # type: int
        # 按返回字段排序
        self.sort_by = sort_by  # type: str
        # 排序顺序
        self.order = order  # type: str
        # 是否只返回当前登录者所提交的作业
        self.show_own = show_own  # type: bool
        # 工作空间ID
        self.workspace_id = workspace_id  # type: str
        # 资源组ID
        self.resource_id = resource_id  # type: str
        # 作业关联用户ID
        self.business_user_id = business_user_id  # type: str
        # 调用方
        self.caller = caller  # type: str
        # 自定义标签
        self.tags_shrink = tags_shrink  # type: str
        # 工作流ID
        self.pipeline_id = pipeline_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        if self.show_own is not None:
            result['ShowOwn'] = self.show_own
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, jobs=None, total_count=None, request_id=None):
        # 作业列表
        self.jobs = jobs  # type: list[JobItem]
        # 符合过滤条件的总作业数
        self.total_count = total_count  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = JobItem()
                self.jobs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetVpcResponseBody(TeaModel):
    def __init__(self, vpc_id=None, vpc_name=None, request_id=None):
        # Vpc的ID
        self.vpc_id = vpc_id  # type: int
        # Vpc名称
        self.vpc_name = vpc_name  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVpcResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVpcResponse, self).to_map()
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
            temp_model = GetVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCodeSourceRequest(TeaModel):
    def __init__(self, display_name=None, description=None, code_repo=None, code_branch=None, mount_path=None,
                 code_repo_user_name=None, code_repo_access_token=None):
        # 代码源配置名称
        self.display_name = display_name  # type: str
        # 代码源详细描述
        self.description = description  # type: str
        # 代码仓库地址
        self.code_repo = code_repo  # type: str
        # 代码分支
        self.code_branch = code_branch  # type: str
        # 代码本地挂载目录，默认挂载到/root/code/下
        self.mount_path = mount_path  # type: str
        # 用户名
        self.code_repo_user_name = code_repo_user_name  # type: str
        # 密码
        self.code_repo_access_token = code_repo_access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCodeSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.code_repo is not None:
            result['CodeRepo'] = self.code_repo
        if self.code_branch is not None:
            result['CodeBranch'] = self.code_branch
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.code_repo_user_name is not None:
            result['CodeRepoUserName'] = self.code_repo_user_name
        if self.code_repo_access_token is not None:
            result['CodeRepoAccessToken'] = self.code_repo_access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CodeRepo') is not None:
            self.code_repo = m.get('CodeRepo')
        if m.get('CodeBranch') is not None:
            self.code_branch = m.get('CodeBranch')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('CodeRepoUserName') is not None:
            self.code_repo_user_name = m.get('CodeRepoUserName')
        if m.get('CodeRepoAccessToken') is not None:
            self.code_repo_access_token = m.get('CodeRepoAccessToken')
        return self


class CreateCodeSourceResponseBody(TeaModel):
    def __init__(self, code_source_id=None, request_id=None):
        # 创建的代码源配置的ID
        self.code_source_id = code_source_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCodeSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCodeSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCodeSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCodeSourceResponse, self).to_map()
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
            temp_model = CreateCodeSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobMetricsRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, time_step=None, metric_type=None, token=None):
        # 起始时间
        self.start_time = start_time  # type: str
        # 截止时间
        self.end_time = end_time  # type: str
        # 时间间隔
        self.time_step = time_step  # type: str
        # 指标类型
        self.metric_type = metric_type  # type: str
        # Token
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetJobMetricsResponseBody(TeaModel):
    def __init__(self, job_id=None, pod_metrics=None, request_id=None):
        # 作业ID
        self.job_id = job_id  # type: str
        # 任务监控指标序列集合
        self.pod_metrics = pod_metrics  # type: list[PodMetric]
        # 请求ID
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetJobMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetJobMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobResponseBodyDataSources(TeaModel):
    def __init__(self, data_source_id=None, mount_path=None):
        # 数据源Id
        self.data_source_id = data_source_id  # type: str
        # 本地挂载路径
        self.mount_path = mount_path  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class GetJobResponseBodyCodeSource(TeaModel):
    def __init__(self, code_source_id=None, branch=None, commit=None, mount_path=None):
        # 代码源Id
        self.code_source_id = code_source_id  # type: str
        # 代码分支
        self.branch = branch  # type: str
        # 代码Commit
        self.commit = commit  # type: str
        # 本地挂载路径
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyCodeSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class GetJobResponseBodyPods(TeaModel):
    def __init__(self, type=None, pod_id=None, status=None, ip=None, gmt_create_time=None, gmt_start_time=None,
                 gmt_finish_time=None):
        # Pod类型
        self.type = type  # type: str
        # Pod Id
        self.pod_id = pod_id  # type: str
        # Pod状态
        self.status = status  # type: str
        # Pod Ip
        self.ip = ip  # type: str
        # Pod创建时间（UTC）
        self.gmt_create_time = gmt_create_time  # type: str
        # Pod启动时间（UTC）
        self.gmt_start_time = gmt_start_time  # type: str
        # Pod结束时间（UTC）
        self.gmt_finish_time = gmt_finish_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyPods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.status is not None:
            result['Status'] = self.status
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(self, job_id=None, job_type=None, display_name=None, user_id=None, status=None, workspace_id=None,
                 workspace_name=None, resource_id=None, reason_code=None, reason_message=None, job_specs=None, user_command=None,
                 data_sources=None, code_source=None, thirdparty_libs=None, thirdparty_lib_dir=None, envs=None,
                 gmt_create_time=None, gmt_submitted_time=None, gmt_running_time=None, gmt_successed_time=None,
                 gmt_stopped_time=None, gmt_failed_time=None, gmt_finish_time=None, duration=None, pods=None, request_id=None,
                 settings=None, cluster_id=None, elastic_spec=None):
        # 作业Id
        self.job_id = job_id  # type: str
        # 作业类型
        self.job_type = job_type  # type: str
        # 作业显示名称
        self.display_name = display_name  # type: str
        # 作业提交人Id
        self.user_id = user_id  # type: str
        # 作业状态
        self.status = status  # type: str
        # 作业所属工作空间ID
        self.workspace_id = workspace_id  # type: str
        # 作业所属工作空间名称
        self.workspace_name = workspace_name  # type: str
        # 作业运行所在的资源组ID
        self.resource_id = resource_id  # type: str
        # 状态详情码
        self.reason_code = reason_code  # type: str
        # 状态详情
        self.reason_message = reason_message  # type: str
        # 作业规格配置
        self.job_specs = job_specs  # type: list[JobSpec]
        # 用户命令
        self.user_command = user_command  # type: str
        # 数据源配置列表
        self.data_sources = data_sources  # type: list[GetJobResponseBodyDataSources]
        # 代码源配置
        self.code_source = code_source  # type: GetJobResponseBodyCodeSource
        # 三方库配置列表
        self.thirdparty_libs = thirdparty_libs  # type: list[str]
        # 三方库(requirements.txt)文件路径
        self.thirdparty_lib_dir = thirdparty_lib_dir  # type: str
        # 环境变量配置
        self.envs = envs  # type: dict[str, str]
        # 作业创建时间（UTC）
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_submitted_time = gmt_submitted_time  # type: str
        self.gmt_running_time = gmt_running_time  # type: str
        self.gmt_successed_time = gmt_successed_time  # type: str
        self.gmt_stopped_time = gmt_stopped_time  # type: str
        self.gmt_failed_time = gmt_failed_time  # type: str
        # 作业结束时间（UTC）
        self.gmt_finish_time = gmt_finish_time  # type: str
        # 作业运行时长（s）
        self.duration = duration  # type: long
        # 作业所以运行Pod列表
        self.pods = pods  # type: list[GetJobResponseBodyPods]
        # 请求Id
        self.request_id = request_id  # type: str
        # 作业额外参数配置
        self.settings = settings  # type: JobSettings
        # 集群ID
        self.cluster_id = cluster_id  # type: str
        # 弹性任务参数
        self.elastic_spec = elastic_spec  # type: JobElasticSpec

    def validate(self):
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.code_source:
            self.code_source.validate()
        if self.pods:
            for k in self.pods:
                if k:
                    k.validate()
        if self.settings:
            self.settings.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()

    def to_map(self):
        _map = super(GetJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.user_command is not None:
            result['UserCommand'] = self.user_command
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()
        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs
        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_submitted_time is not None:
            result['GmtSubmittedTime'] = self.gmt_submitted_time
        if self.gmt_running_time is not None:
            result['GmtRunningTime'] = self.gmt_running_time
        if self.gmt_successed_time is not None:
            result['GmtSuccessedTime'] = self.gmt_successed_time
        if self.gmt_stopped_time is not None:
            result['GmtStoppedTime'] = self.gmt_stopped_time
        if self.gmt_failed_time is not None:
            result['GmtFailedTime'] = self.gmt_failed_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.duration is not None:
            result['Duration'] = self.duration
        result['Pods'] = []
        if self.pods is not None:
            for k in self.pods:
                result['Pods'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.elastic_spec is not None:
            result['ElasticSpec'] = self.elastic_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = GetJobResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('CodeSource') is not None:
            temp_model = GetJobResponseBodyCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')
        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtSubmittedTime') is not None:
            self.gmt_submitted_time = m.get('GmtSubmittedTime')
        if m.get('GmtRunningTime') is not None:
            self.gmt_running_time = m.get('GmtRunningTime')
        if m.get('GmtSuccessedTime') is not None:
            self.gmt_successed_time = m.get('GmtSuccessedTime')
        if m.get('GmtStoppedTime') is not None:
            self.gmt_stopped_time = m.get('GmtStoppedTime')
        if m.get('GmtFailedTime') is not None:
            self.gmt_failed_time = m.get('GmtFailedTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.pods = []
        if m.get('Pods') is not None:
            for k in m.get('Pods'):
                temp_model = GetJobResponseBodyPods()
                self.pods.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Settings') is not None:
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ElasticSpec') is not None:
            temp_model = JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m['ElasticSpec'])
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


class BatchGetJobsStatisticsRequest(TeaModel):
    def __init__(self, workspace_ids=None):
        # 工作空间id列表
        self.workspace_ids = workspace_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetJobsStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        return self


class BatchGetJobsStatisticsResponseBody(TeaModel):
    def __init__(self, statistics=None, request_id=None):
        # 每一个工作空间id下面的Job按照状态的分类统计信息
        self.statistics = statistics  # type: dict[str, any]
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetJobsStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetJobsStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchGetJobsStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchGetJobsStatisticsResponse, self).to_map()
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
            temp_model = BatchGetJobsStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceRequest(TeaModel):
    def __init__(self, data_source_type=None, display_name=None, description=None, file_system_id=None, path=None,
                 endpoint=None, options=None, mount_path=None):
        # 数据源类型
        self.data_source_type = data_source_type  # type: str
        # 数据源显示名称
        self.display_name = display_name  # type: str
        # 数据源描述
        self.description = description  # type: str
        # 阿里云NAS文件系统Id
        self.file_system_id = file_system_id  # type: str
        # 阿里云OSS文件系统路径
        self.path = path  # type: str
        # 阿里云OSS文件系统服务端点
        self.endpoint = endpoint  # type: str
        # 阿里云OSS文件系统配置选项
        self.options = options  # type: str
        # 本地挂载目录
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.options is not None:
            result['Options'] = self.options
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class CreateDataSourceResponseBody(TeaModel):
    def __init__(self, data_source_id=None, request_id=None):
        # 数据源Id
        self.data_source_id = data_source_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataSourceResponse, self).to_map()
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
            temp_model = CreateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(self, image_provider_type=None, accelerator_type=None, framework=None, sort_by=None, order=None):
        # 镜像类型
        self.image_provider_type = image_provider_type  # type: str
        # 加速器类型
        self.accelerator_type = accelerator_type  # type: str
        # 镜像包含的框架类型
        self.framework = framework  # type: str
        # 按返回字段排序
        self.sort_by = sort_by  # type: str
        # 排序顺序
        self.order = order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_provider_type is not None:
            result['ImageProviderType'] = self.image_provider_type
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.framework is not None:
            result['Framework'] = self.framework
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageProviderType') is not None:
            self.image_provider_type = m.get('ImageProviderType')
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Framework') is not None:
            self.framework = m.get('Framework')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(self, images=None, total_count=None, request_id=None):
        # 镜像详情列表
        self.images = images  # type: list[ImageItem]
        # 2
        self.total_count = total_count  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

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
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ImageItem()
                self.images.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetSecurityGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, vpc_id=None, security_group_id=None, security_group_name=None):
        # 请求id
        self.request_id = request_id  # type: str
        # 所属vpc的id
        self.vpc_id = vpc_id  # type: str
        # 安全组id
        self.security_group_id = security_group_id  # type: str
        # 安全组名称
        self.security_group_name = security_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecurityGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class GetSecurityGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSecurityGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSecurityGroupResponse, self).to_map()
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
            temp_model = GetSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserAuthorizationResponseBody(TeaModel):
    def __init__(self, is_passed=None, request_id=None):
        # 是否通过鉴权
        self.is_passed = is_passed  # type: bool
        # 请求ID
        self.request_id = request_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_passed is not None:
            result['IsPassed'] = self.is_passed
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsPassed') is not None:
            self.is_passed = m.get('IsPassed')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserAuthorizationResponse, self).to_map()
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
            temp_model = GetUserAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None):
        # 工作空间ID
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
    def __init__(self, tensorboard_id=None, request_id=None):
        # Tensorboad Id
        self.tensorboard_id = tensorboard_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTensorboardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # 作业Id
        self.job_id = job_id  # type: str
        # 请求Id
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


class GetJobEventsRequest(TeaModel):
    def __init__(self, max_events_num=None, start_time=None, end_time=None):
        # 获取事件的最大数目，默认值：2000
        self.max_events_num = max_events_num  # type: int
        # 查询事件的时间区间的起始时间，默认值是7天前。
        self.start_time = start_time  # type: str
        # 查询事件的时间区间的截止时间，默认值是当前。
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class GetJobEventsResponseBody(TeaModel):
    def __init__(self, job_id=None, events=None, request_id=None):
        # 作业ID
        self.job_id = job_id  # type: str
        # 事件
        self.events = events  # type: list[str]
        # 请求ID
        self.request_id = request_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.events is not None:
            result['Events'] = self.events
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetJobEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetJobEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # 作业Id
        self.job_id = job_id  # type: str
        # 请求Id
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCodeSourceResponseBody(TeaModel):
    def __init__(self, code_source_id=None, request_id=None):
        # 被删除的代码源配置ID
        self.code_source_id = code_source_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCodeSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCodeSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCodeSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCodeSourceResponse, self).to_map()
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
            temp_model = DeleteCodeSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(self, data_source_id=None, request_id=None):
        # 数据源Id
        self.data_source_id = data_source_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataSourceResponse, self).to_map()
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
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspacesRequest(TeaModel):
    def __init__(self, need_detail=None, page_number=None, page_size=None, sort_by=None, order=None):
        # 是否返回详情(Quotas, Members)
        self.need_detail = need_detail  # type: bool
        # 查询第几页数据,最小值为1
        self.page_number = page_number  # type: int
        # 设置查询的分页大小,最小值为1
        self.page_size = page_size  # type: int
        # 返回结果的排序字段名，枚举值
        self.sort_by = sort_by  # type: str
        # 排列顺序: desc 或者 asc
        self.order = order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkspacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_detail is not None:
            result['NeedDetail'] = self.need_detail
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedDetail') is not None:
            self.need_detail = m.get('NeedDetail')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(self, workspaces=None, total_count=None, request_id=None):
        # 工作空间列表
        self.workspaces = workspaces  # type: list[Workspace]
        # 结果数
        self.total_count = total_count  # type: long
        # 请求id
        self.request_id = request_id  # type: str

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
        result['Workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['Workspaces'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k in m.get('Workspaces'):
                temp_model = Workspace()
                self.workspaces.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListWorkspacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListWorkspacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkspacesResponse, self).to_map()
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(self, target_type=None, target_id=None, expire_time=None):
        # TargetType
        self.target_type = target_type  # type: str
        # TargetId
        self.target_id = target_id  # type: str
        # ExpireTime
        self.expire_time = expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None):
        # RequestId
        self.request_id = request_id  # type: str
        # Token
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationResponseBody(TeaModel):
    def __init__(self, authorized=None, authorization_failed_code=None, authorization_failed_message=None,
                 request_id=None):
        # 是否授权
        self.authorized = authorized  # type: bool
        # 授权失败码
        self.authorization_failed_code = authorization_failed_code  # type: str
        # 授权失败消息
        self.authorization_failed_message = authorization_failed_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        if self.authorization_failed_code is not None:
            result['AuthorizationFailedCode'] = self.authorization_failed_code
        if self.authorization_failed_message is not None:
            result['AuthorizationFailedMessage'] = self.authorization_failed_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        if m.get('AuthorizationFailedCode') is not None:
            self.authorization_failed_code = m.get('AuthorizationFailedCode')
        if m.get('AuthorizationFailedMessage') is not None:
            self.authorization_failed_message = m.get('AuthorizationFailedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuthorizationResponse, self).to_map()
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
            temp_model = GetAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, sort_by=None, order=None):
        # 当前页
        self.page_number = page_number  # type: int
        # 每页返回的作业数
        self.page_size = page_size  # type: int
        # 按返回字段排序
        self.sort_by = sort_by  # type: str
        # 排序顺序
        self.order = order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListQuotasResponseBody(TeaModel):
    def __init__(self, quotas=None, request_id=None):
        # 资源配额列表
        self.quotas = quotas  # type: list[Quota]
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = Quota()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQuotasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListQuotasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None, job_id=None, data_source_id=None, display_name=None, summary_path=None,
                 data_sources=None):
        # 工作空间ID
        self.workspace_id = workspace_id  # type: str
        # 任务Id
        self.job_id = job_id  # type: str
        # DataSource Id
        self.data_source_id = data_source_id  # type: str
        # Tensorboard名称
        self.display_name = display_name  # type: str
        # Summary 目录
        self.summary_path = summary_path  # type: str
        self.data_sources = data_sources  # type: list[DataSourceItem]

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
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = DataSourceItem()
                self.data_sources.append(temp_model.from_map(k))
        return self


class CreateTensorboardResponseBody(TeaModel):
    def __init__(self, job_id=None, data_source_id=None, tensorboard_id=None, request_id=None):
        # 任务Id
        self.job_id = job_id  # type: str
        # DataSourceId
        self.data_source_id = data_source_id  # type: str
        # Tensorboard id
        self.tensorboard_id = tensorboard_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTensorboardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTensorboardRequest(TeaModel):
    def __init__(self, workspace_id=None, max_running_time_minutes=None):
        # 工作空间ID
        self.workspace_id = workspace_id  # type: str
        # MaxRunningTimeMinutes
        self.max_running_time_minutes = max_running_time_minutes  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTensorboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.max_running_time_minutes is not None:
            result['MaxRunningTimeMinutes'] = self.max_running_time_minutes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('MaxRunningTimeMinutes') is not None:
            self.max_running_time_minutes = m.get('MaxRunningTimeMinutes')
        return self


class UpdateTensorboardResponseBody(TeaModel):
    def __init__(self, tensorboard_id=None, request_id=None):
        # Tensorboad Id
        self.tensorboard_id = tensorboard_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTensorboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTensorboardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTensorboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaRequest(TeaModel):
    def __init__(self, quota_name=None, quota_type=None, quota_detail=None):
        # 资源配额名称
        self.quota_name = quota_name  # type: str
        # 资源配额类型
        self.quota_type = quota_type  # type: str
        # 资源配额参数
        self.quota_detail = quota_detail  # type: QuotaDetail

    def validate(self):
        if self.quota_detail:
            self.quota_detail.validate()

    def to_map(self):
        _map = super(UpdateQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.quota_detail is not None:
            result['QuotaDetail'] = self.quota_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('QuotaDetail') is not None:
            temp_model = QuotaDetail()
            self.quota_detail = temp_model.from_map(m['QuotaDetail'])
        return self


class UpdateQuotaResponseBody(TeaModel):
    def __init__(self, quota_id=None, request_id=None):
        # 资源配额id
        self.quota_id = quota_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


