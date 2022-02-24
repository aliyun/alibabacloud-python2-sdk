# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Instance(TeaModel):
    def __init__(self, host_ip=None, host_name=None, inner_ip=None, instance_name=None, instance_port=None,
                 last_state=None, ready_processes=None, reason=None, restart_count=None, start_at=None, status=None,
                 total_processes=None):
        # 实例所在的宿主机IP
        self.host_ip = host_ip  # type: str
        # 实例所在的宿主机名字
        self.host_name = host_name  # type: str
        # 实例的内网IP
        self.inner_ip = inner_ip  # type: str
        # 实例的名字
        self.instance_name = instance_name  # type: str
        # 实例的网络端口
        self.instance_port = instance_port  # type: int
        # 实例上一次退出的状态
        self.last_state = last_state  # type: list[dict[str, any]]
        # 实例已经启动完成的进程数
        self.ready_processes = ready_processes  # type: int
        # 实例当前状态的标识
        self.reason = reason  # type: str
        # 实例重启次数
        self.restart_count = restart_count  # type: int
        # 实例的启动时间
        self.start_at = start_at  # type: str
        # 实例状态
        self.status = status  # type: str
        # 实例总的进程数
        self.total_processes = total_processes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(Instance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_ip is not None:
            result['HostIP'] = self.host_ip
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.last_state is not None:
            result['LastState'] = self.last_state
        if self.ready_processes is not None:
            result['ReadyProcesses'] = self.ready_processes
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.start_at is not None:
            result['StartAt'] = self.start_at
        if self.status is not None:
            result['Status'] = self.status
        if self.total_processes is not None:
            result['TotalProcesses'] = self.total_processes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostIP') is not None:
            self.host_ip = m.get('HostIP')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('LastState') is not None:
            self.last_state = m.get('LastState')
        if m.get('ReadyProcesses') is not None:
            self.ready_processes = m.get('ReadyProcesses')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('StartAt') is not None:
            self.start_at = m.get('StartAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalProcesses') is not None:
            self.total_processes = m.get('TotalProcesses')
        return self


class Resource(TeaModel):
    def __init__(self, cluster_id=None, cpu_count=None, create_time=None, extra_data=None, gpu_count=None,
                 instance_count=None, message=None, post_paid_instance_count=None, pre_paid_instance_count=None, resource_id=None,
                 resource_name=None, status=None, update_time=None):
        # 资源组所在的集群
        self.cluster_id = cluster_id  # type: str
        # 资源组CPU数量
        self.cpu_count = cpu_count  # type: int
        # 资源组创建时间
        self.create_time = create_time  # type: str
        # 资源组自定义数据
        self.extra_data = extra_data  # type: dict[str, any]
        # 资源组GPU个数
        self.gpu_count = gpu_count  # type: int
        # 资源组实例个数
        self.instance_count = instance_count  # type: int
        # 资源组摘要信息
        self.message = message  # type: str
        # 资源组按量付费实例个数
        self.post_paid_instance_count = post_paid_instance_count  # type: int
        # 资源组预付费实例个数
        self.pre_paid_instance_count = pre_paid_instance_count  # type: int
        # 资源组ID
        self.resource_id = resource_id  # type: str
        # 资源组名字
        self.resource_name = resource_name  # type: str
        # 资源组的状态
        self.status = status  # type: str
        # 资源组更新时间
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Resource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.message is not None:
            result['Message'] = self.message
        if self.post_paid_instance_count is not None:
            result['PostPaidInstanceCount'] = self.post_paid_instance_count
        if self.pre_paid_instance_count is not None:
            result['PrePaidInstanceCount'] = self.pre_paid_instance_count
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PostPaidInstanceCount') is not None:
            self.post_paid_instance_count = m.get('PostPaidInstanceCount')
        if m.get('PrePaidInstanceCount') is not None:
            self.pre_paid_instance_count = m.get('PrePaidInstanceCount')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ResourceInstance(TeaModel):
    def __init__(self, auto_renewal=None, charge_type=None, create_time=None, expired_time=None,
                 instance_cpu_count=None, instance_gpu_count=None, instance_id=None, instance_ip=None, instance_memory=None,
                 instance_name=None, instance_status=None, instance_type=None, instance_used_cpu=None, instance_used_gpu=None,
                 instance_used_memory=None):
        # 实例是否自动续费
        self.auto_renewal = auto_renewal  # type: bool
        # 实例的计费类型
        self.charge_type = charge_type  # type: str
        # 实例的创建时间
        self.create_time = create_time  # type: str
        # 实例过期时间
        self.expired_time = expired_time  # type: str
        # 实例的Cpu个数
        self.instance_cpu_count = instance_cpu_count  # type: int
        # 实例的Gpu个数
        self.instance_gpu_count = instance_gpu_count  # type: int
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 实例IP
        self.instance_ip = instance_ip  # type: str
        # 实例的内存大小
        self.instance_memory = instance_memory  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        # 实例状态
        self.instance_status = instance_status  # type: str
        # 实例的机型
        self.instance_type = instance_type  # type: str
        # 实例被使用的CPU数量
        self.instance_used_cpu = instance_used_cpu  # type: float
        # 实例被使用的GPU数量
        self.instance_used_gpu = instance_used_gpu  # type: int
        # 实例被使用的内存大小
        self.instance_used_memory = instance_used_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_cpu_count is not None:
            result['InstanceCpuCount'] = self.instance_cpu_count
        if self.instance_gpu_count is not None:
            result['InstanceGpuCount'] = self.instance_gpu_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_memory is not None:
            result['InstanceMemory'] = self.instance_memory
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_used_cpu is not None:
            result['InstanceUsedCpu'] = self.instance_used_cpu
        if self.instance_used_gpu is not None:
            result['InstanceUsedGpu'] = self.instance_used_gpu
        if self.instance_used_memory is not None:
            result['InstanceUsedMemory'] = self.instance_used_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceCpuCount') is not None:
            self.instance_cpu_count = m.get('InstanceCpuCount')
        if m.get('InstanceGpuCount') is not None:
            self.instance_gpu_count = m.get('InstanceGpuCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstanceMemory') is not None:
            self.instance_memory = m.get('InstanceMemory')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsedCpu') is not None:
            self.instance_used_cpu = m.get('InstanceUsedCpu')
        if m.get('InstanceUsedGpu') is not None:
            self.instance_used_gpu = m.get('InstanceUsedGpu')
        if m.get('InstanceUsedMemory') is not None:
            self.instance_used_memory = m.get('InstanceUsedMemory')
        return self


class ResourceInstanceWorker(TeaModel):
    def __init__(self, cpu_limit=None, cpu_request=None, gpu_limit=None, gpu_request=None, memory_limit=None,
                 memory_rquest=None, name=None, ready=None, restart_count=None, service_name=None, start_time=None, status=None):
        # CpuLimit
        self.cpu_limit = cpu_limit  # type: int
        # CpuRequest
        self.cpu_request = cpu_request  # type: int
        # GpuLimit
        self.gpu_limit = gpu_limit  # type: int
        # GpuRequest
        self.gpu_request = gpu_request  # type: int
        # MemoryLimit
        self.memory_limit = memory_limit  # type: int
        # MemoryRquest
        self.memory_rquest = memory_rquest  # type: int
        # pod名
        self.name = name  # type: str
        # 是否ready
        self.ready = ready  # type: bool
        # RestartCount
        self.restart_count = restart_count  # type: int
        # 服务名
        self.service_name = service_name  # type: str
        # StartTime
        self.start_time = start_time  # type: str
        # pod状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceInstanceWorker, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit
        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request
        if self.gpu_limit is not None:
            result['GpuLimit'] = self.gpu_limit
        if self.gpu_request is not None:
            result['GpuRequest'] = self.gpu_request
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.memory_rquest is not None:
            result['MemoryRquest'] = self.memory_rquest
        if self.name is not None:
            result['Name'] = self.name
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')
        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')
        if m.get('GpuLimit') is not None:
            self.gpu_limit = m.get('GpuLimit')
        if m.get('GpuRequest') is not None:
            self.gpu_request = m.get('GpuRequest')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('MemoryRquest') is not None:
            self.memory_rquest = m.get('MemoryRquest')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class Service(TeaModel):
    def __init__(self, access_token=None, caller_uid=None, cpu=None, create_time=None, current_version=None,
                 gpu=None, image=None, internet_endpoint=None, intranet_endpoint=None, latest_version=None, memory=None,
                 message=None, namespace=None, parent_uid=None, pending_instance=None, reason=None, region=None,
                 request_id=None, resource=None, running_instance=None, service_config=None, service_id=None,
                 service_name=None, status=None, total_instance=None, updatetime=None, weight=None):
        # 服务的请求Token
        self.access_token = access_token  # type: str
        # 服务创建账号的UID
        self.caller_uid = caller_uid  # type: str
        # 每个实例申请的cpu
        self.cpu = cpu  # type: int
        # 服务的创建时间
        self.create_time = create_time  # type: str
        # 当前运行的模型版本
        self.current_version = current_version  # type: int
        # 每个实例申请的gpu
        self.gpu = gpu  # type: int
        # 服务的数据镜像
        self.image = image  # type: str
        # 服务的公网endpoint
        self.internet_endpoint = internet_endpoint  # type: str
        # 服务内网endpoint
        self.intranet_endpoint = intranet_endpoint  # type: str
        # 服务最新版本号
        self.latest_version = latest_version  # type: int
        # 每个worker需要的内存大小，单位为M
        self.memory = memory  # type: int
        # 服务的摘要信息
        self.message = message  # type: str
        # 服务所在的命名空间
        self.namespace = namespace  # type: str
        # 服务创建账号的主账号UID
        self.parent_uid = parent_uid  # type: str
        # 被挂起的服务的实例个数
        self.pending_instance = pending_instance  # type: int
        # 服务的状态信息
        self.reason = reason  # type: str
        # 服务所在的区域
        self.region = region  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 服务所在的资源组
        self.resource = resource  # type: str
        # 正在运行的服务的实例个数
        self.running_instance = running_instance  # type: int
        # 服务的配置信息
        self.service_config = service_config  # type: str
        # 服务ID
        self.service_id = service_id  # type: str
        # 服务的名字
        self.service_name = service_name  # type: str
        # 服务的状态
        self.status = status  # type: str
        # 服务的所有实例总个数
        self.total_instance = total_instance  # type: int
        # 服务的更新时间
        self.updatetime = updatetime  # type: str
        # 服务灰度发布的权重值
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(Service, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid
        if self.pending_instance is not None:
            result['PendingInstance'] = self.pending_instance
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.running_instance is not None:
            result['RunningInstance'] = self.running_instance
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.total_instance is not None:
            result['TotalInstance'] = self.total_instance
        if self.updatetime is not None:
            result['Updatetime'] = self.updatetime
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')
        if m.get('PendingInstance') is not None:
            self.pending_instance = m.get('PendingInstance')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('RunningInstance') is not None:
            self.running_instance = m.get('RunningInstance')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalInstance') is not None:
            self.total_instance = m.get('TotalInstance')
        if m.get('Updatetime') is not None:
            self.updatetime = m.get('Updatetime')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateResourceRequest(TeaModel):
    def __init__(self, auto_renewal=None, charge_type=None, ecs_instance_count=None, ecs_instance_type=None):
        # 是否自动续费
        self.auto_renewal = auto_renewal  # type: bool
        # 付费类型，预付费PrePaid，后付费PostPaid
        self.charge_type = charge_type  # type: str
        # 实例数量
        self.ecs_instance_count = ecs_instance_count  # type: int
        # 实例机型，对应ecs机型
        self.ecs_instance_type = ecs_instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.ecs_instance_count is not None:
            result['EcsInstanceCount'] = self.ecs_instance_count
        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EcsInstanceCount') is not None:
            self.ecs_instance_count = m.get('EcsInstanceCount')
        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(self, cluster_id=None, owner_uid=None, request_id=None, resource_id=None, resource_name=None):
        # 资源组所在集群ID
        self.cluster_id = cluster_id  # type: str
        # 资源组的Owner UID
        self.owner_uid = owner_uid  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 资源组ID
        self.resource_id = resource_id  # type: str
        # 资源组名称
        self.resource_name = resource_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceID'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceID') is not None:
            self.resource_id = m.get('ResourceID')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceResponse, self).to_map()
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
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceInstancesRequest(TeaModel):
    def __init__(self, auto_renewal=None, charge_type=None, ecs_instance_count=None, ecs_instance_type=None,
                 user_data=None):
        # 是否自动续费
        self.auto_renewal = auto_renewal  # type: bool
        # 付费类型，预付费PrePaid，后付费PostPaid
        self.charge_type = charge_type  # type: str
        # 新创建的实例个数，(0, 100]
        self.ecs_instance_count = ecs_instance_count  # type: int
        # 实例机型，对应ecs机型
        self.ecs_instance_type = ecs_instance_type  # type: str
        # 用户自这义数据，小于 16KB
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.ecs_instance_count is not None:
            result['EcsInstanceCount'] = self.ecs_instance_count
        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EcsInstanceCount') is not None:
            self.ecs_instance_count = m.get('EcsInstanceCount')
        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateResourceInstancesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateResourceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceInstancesResponse, self).to_map()
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
            temp_model = CreateResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceLogRequest(TeaModel):
    def __init__(self, log_store=None, project_name=None):
        # sls日志库
        self.log_store = log_store  # type: str
        # 资源组对应的sls日志管理项目
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class CreateResourceLogResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateResourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceLogResponse, self).to_map()
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
            temp_model = CreateResourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceRequest, self).to_map()
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


class CreateServiceResponseBody(TeaModel):
    def __init__(self, internet_endpoint=None, intranet_endpoint=None, region=None, request_id=None,
                 service_id=None, service_name=None, status=None):
        self.internet_endpoint = internet_endpoint  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.region = region  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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


class CreateServiceAutoScalerRequestStrategies(TeaModel):
    def __init__(self, cpu=None, qps=None):
        # 最大 replica 数，需要大于MinReplica
        self.cpu = cpu  # type: float
        # 每个实例支持的最大qps数，超出即扩容
        self.qps = qps  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceAutoScalerRequestStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.qps is not None:
            result['Qps'] = self.qps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        return self


class CreateServiceAutoScalerRequest(TeaModel):
    def __init__(self, max=None, min=None, strategies=None):
        # 最大 replica 数，需要大于MinReplica
        self.max = max  # type: int
        # 最小 replica 数，需要大于0
        self.min = min  # type: int
        # map 类型的策略定义
        self.strategies = strategies  # type: CreateServiceAutoScalerRequestStrategies

    def validate(self):
        if self.strategies:
            self.strategies.validate()

    def to_map(self):
        _map = super(CreateServiceAutoScalerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.strategies is not None:
            result['Strategies'] = self.strategies.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Strategies') is not None:
            temp_model = CreateServiceAutoScalerRequestStrategies()
            self.strategies = temp_model.from_map(m['Strategies'])
        return self


class CreateServiceAutoScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceAutoScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceAutoScalerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceAutoScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceAutoScalerResponse, self).to_map()
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
            temp_model = CreateServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceCronScalerRequestScaleJobs(TeaModel):
    def __init__(self, name=None, schedule=None, target_size=None):
        self.name = name  # type: str
        # 要执行伸缩任务的cron表达式
        self.schedule = schedule  # type: str
        # 执行伸缩任务的目标replica
        self.target_size = target_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceCronScalerRequestScaleJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.target_size is not None:
            result['TargetSize'] = self.target_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')
        return self


class CreateServiceCronScalerRequest(TeaModel):
    def __init__(self, exclude_dates=None, scale_jobs=None):
        # 需要排除的时间点的cron表达式
        self.exclude_dates = exclude_dates  # type: list[str]
        # 定时伸缩任务描述
        self.scale_jobs = scale_jobs  # type: list[CreateServiceCronScalerRequestScaleJobs]

    def validate(self):
        if self.scale_jobs:
            for k in self.scale_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceCronScalerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_dates is not None:
            result['ExcludeDates'] = self.exclude_dates
        result['ScaleJobs'] = []
        if self.scale_jobs is not None:
            for k in self.scale_jobs:
                result['ScaleJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeDates') is not None:
            self.exclude_dates = m.get('ExcludeDates')
        self.scale_jobs = []
        if m.get('ScaleJobs') is not None:
            for k in m.get('ScaleJobs'):
                temp_model = CreateServiceCronScalerRequestScaleJobs()
                self.scale_jobs.append(temp_model.from_map(k))
        return self


class CreateServiceCronScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        # 操作成功消息
        self.message = message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceCronScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceCronScalerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceCronScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceCronScalerResponse, self).to_map()
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
            temp_model = CreateServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceMirrorRequest(TeaModel):
    def __init__(self, ratio=None, target=None):
        # 比例 [0, 100]
        self.ratio = ratio  # type: int
        # 服务实例列表
        self.target = target  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceMirrorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class CreateServiceMirrorResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceMirrorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceMirrorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceMirrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceMirrorResponse, self).to_map()
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
            temp_model = CreateServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceResponse, self).to_map()
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
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceDLinkResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceDLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceDLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteResourceDLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceDLinkResponse, self).to_map()
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
            temp_model = DeleteResourceDLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceInstancesRequest(TeaModel):
    def __init__(self, all_failed=None, instance_list=None):
        self.all_failed = all_failed  # type: bool
        self.instance_list = instance_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_failed is not None:
            result['AllFailed'] = self.all_failed
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllFailed') is not None:
            self.all_failed = m.get('AllFailed')
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        return self


class DeleteResourceInstancesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteResourceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceInstancesResponse, self).to_map()
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
            temp_model = DeleteResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceLogResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteResourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceLogResponse, self).to_map()
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
            temp_model = DeleteResourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
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


class DeleteServiceAutoScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceAutoScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceAutoScalerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceAutoScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceAutoScalerResponse, self).to_map()
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
            temp_model = DeleteServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceCronScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceCronScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceCronScalerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceCronScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceCronScalerResponse, self).to_map()
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
            temp_model = DeleteServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceInstancesRequest(TeaModel):
    def __init__(self, instance_list=None):
        # 删除的实例列表，多个实例名字之间逗号隔开
        self.instance_list = instance_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        return self


class DeleteServiceInstancesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceInstancesResponse, self).to_map()
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
            temp_model = DeleteServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceMirrorResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceMirrorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceMirrorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceMirrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceMirrorResponse, self).to_map()
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
            temp_model = DeleteServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cpu_count=None, create_time=None, extra_data=None, gpu_count=None,
                 instance_count=None, message=None, owner_uid=None, post_paid_instance_count=None, pre_paid_instance_count=None,
                 request_id=None, resource_id=None, resource_name=None, status=None, update_time=None):
        self.cluster_id = cluster_id  # type: str
        self.cpu_count = cpu_count  # type: int
        self.create_time = create_time  # type: str
        self.extra_data = extra_data  # type: str
        self.gpu_count = gpu_count  # type: int
        self.instance_count = instance_count  # type: int
        self.message = message  # type: str
        self.owner_uid = owner_uid  # type: str
        self.post_paid_instance_count = post_paid_instance_count  # type: int
        self.pre_paid_instance_count = pre_paid_instance_count  # type: int
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.status = status  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.message is not None:
            result['Message'] = self.message
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.post_paid_instance_count is not None:
            result['PostPaidInstanceCount'] = self.post_paid_instance_count
        if self.pre_paid_instance_count is not None:
            result['PrePaidInstanceCount'] = self.pre_paid_instance_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PostPaidInstanceCount') is not None:
            self.post_paid_instance_count = m.get('PostPaidInstanceCount')
        if m.get('PrePaidInstanceCount') is not None:
            self.pre_paid_instance_count = m.get('PrePaidInstanceCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResourceResponse, self).to_map()
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
            temp_model = DescribeResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceDLinkResponseBody(TeaModel):
    def __init__(self, aux_vswitch_list=None, destination_cidrs=None, request_id=None, security_group_id=None,
                 v_switch_id=None, vpc_id=None):
        # 已打通直连的副VSwitch ID
        self.aux_vswitch_list = aux_vswitch_list  # type: list[str]
        # 要打通的客户端的网段信息，会将该网段加入到服务端的回包路由中，与VSwitchIdList可二选一
        self.destination_cidrs = destination_cidrs  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 已打通直连的安全组
        self.security_group_id = security_group_id  # type: str
        # 已打通直连的主VSwitch ID
        self.v_switch_id = v_switch_id  # type: str
        # 已打通直接的Vpc ID
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceDLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aux_vswitch_list is not None:
            result['AuxVSwitchList'] = self.aux_vswitch_list
        if self.destination_cidrs is not None:
            result['DestinationCIDRs'] = self.destination_cidrs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuxVSwitchList') is not None:
            self.aux_vswitch_list = m.get('AuxVSwitchList')
        if m.get('DestinationCIDRs') is not None:
            self.destination_cidrs = m.get('DestinationCIDRs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeResourceDLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeResourceDLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResourceDLinkResponse, self).to_map()
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
            temp_model = DescribeResourceDLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceLogResponseBody(TeaModel):
    def __init__(self, log_store=None, message=None, project_name=None, request_id=None, status=None):
        # sls日志库
        self.log_store = log_store  # type: str
        # sls日志信息
        self.message = message  # type: str
        # 资源组对应的sls日志管理项目
        self.project_name = project_name  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 资源组状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.message is not None:
            result['Message'] = self.message
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeResourceLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeResourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResourceLogResponse, self).to_map()
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
            temp_model = DescribeResourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: Service

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceResponse, self).to_map()
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
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceAutoScalerResponseBody(TeaModel):
    def __init__(self, max_replica=None, min_replica=None, request_id=None, service_name=None, strategies=None):
        # 服务最大实例数
        self.max_replica = max_replica  # type: int
        # 服务最小实例数
        self.min_replica = min_replica  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        # 服务名字
        self.service_name = service_name  # type: str
        # 扩缩控制器控制策略
        self.strategies = strategies  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceAutoScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_replica is not None:
            result['MaxReplica'] = self.max_replica
        if self.min_replica is not None:
            result['MinReplica'] = self.min_replica
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.strategies is not None:
            result['Strategies'] = self.strategies
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxReplica') is not None:
            self.max_replica = m.get('MaxReplica')
        if m.get('MinReplica') is not None:
            self.min_replica = m.get('MinReplica')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Strategies') is not None:
            self.strategies = m.get('Strategies')
        return self


class DescribeServiceAutoScalerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeServiceAutoScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceAutoScalerResponse, self).to_map()
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
            temp_model = DescribeServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceCronScalerResponseBodyScaleJobs(TeaModel):
    def __init__(self, last_probe_time=None, message=None, name=None, schedule=None, state=None, target_size=None):
        self.last_probe_time = last_probe_time  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.schedule = schedule  # type: str
        self.state = state  # type: str
        self.target_size = target_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceCronScalerResponseBodyScaleJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_probe_time is not None:
            result['LastProbeTime'] = self.last_probe_time
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.state is not None:
            result['State'] = self.state
        if self.target_size is not None:
            result['TargetSize'] = self.target_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastProbeTime') is not None:
            self.last_probe_time = m.get('LastProbeTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')
        return self


class DescribeServiceCronScalerResponseBody(TeaModel):
    def __init__(self, exclude_dates=None, request_id=None, scale_jobs=None, service_name=None):
        self.exclude_dates = exclude_dates  # type: list[str]
        self.request_id = request_id  # type: str
        self.scale_jobs = scale_jobs  # type: list[DescribeServiceCronScalerResponseBodyScaleJobs]
        self.service_name = service_name  # type: str

    def validate(self):
        if self.scale_jobs:
            for k in self.scale_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeServiceCronScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_dates is not None:
            result['ExcludeDates'] = self.exclude_dates
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScaleJobs'] = []
        if self.scale_jobs is not None:
            for k in self.scale_jobs:
                result['ScaleJobs'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeDates') is not None:
            self.exclude_dates = m.get('ExcludeDates')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scale_jobs = []
        if m.get('ScaleJobs') is not None:
            for k in m.get('ScaleJobs'):
                temp_model = DescribeServiceCronScalerResponseBodyScaleJobs()
                self.scale_jobs.append(temp_model.from_map(k))
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeServiceCronScalerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeServiceCronScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceCronScalerResponse, self).to_map()
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
            temp_model = DescribeServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceLogRequest(TeaModel):
    def __init__(self, end_time=None, ip=None, keyword=None, page_num=None, page_size=None, start_time=None):
        # 查询的结束时间
        self.end_time = end_time  # type: str
        # 要查询的机器ip
        self.ip = ip  # type: str
        # 查询的关键字
        self.keyword = keyword  # type: str
        # 请求的页码（默认为1）
        self.page_num = page_num  # type: long
        # 每页的大小（默认为500）
        self.page_size = page_size  # type: long
        # 查询的开始时间
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeServiceLogResponseBody(TeaModel):
    def __init__(self, logs=None, page_num=None, request_id=None, total_count=None, total_page_num=None):
        # 返回的日志信息
        self.logs = logs  # type: list[str]
        # 当前页码
        self.page_num = page_num  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        # 总计数量
        self.total_count = total_count  # type: long
        # 总计页码
        self.total_page_num = total_page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class DescribeServiceLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeServiceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceLogResponse, self).to_map()
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
            temp_model = DescribeServiceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMirrorResponseBody(TeaModel):
    def __init__(self, ratio=None, request_id=None, service_name=None, target=None):
        # 比例[0,100]
        self.ratio = ratio  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 服务名字
        self.service_name = service_name  # type: str
        # 设置流量镜像对服务列表
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMirrorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class DescribeServiceMirrorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeServiceMirrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceMirrorResponse, self).to_map()
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
            temp_model = DescribeServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceInstanceWorkerRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceInstanceWorkerRequest, self).to_map()
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


class ListResourceInstanceWorkerResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, pods=None, request_id=None, total_count=None):
        # 当前页码
        self.page_number = page_number  # type: int
        # 每页大小
        self.page_size = page_size  # type: int
        # pod列表
        self.pods = pods  # type: list[ResourceInstanceWorker]
        # Id of the request
        self.request_id = request_id  # type: str
        # pod总数
        self.total_count = total_count  # type: int

    def validate(self):
        if self.pods:
            for k in self.pods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceInstanceWorkerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Pods'] = []
        if self.pods is not None:
            for k in self.pods:
                result['Pods'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.pods = []
        if m.get('Pods') is not None:
            for k in m.get('Pods'):
                temp_model = ResourceInstanceWorker()
                self.pods.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceInstanceWorkerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListResourceInstanceWorkerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceInstanceWorkerResponse, self).to_map()
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
            temp_model = ListResourceInstanceWorkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 请求的页码（默认为1）
        self.page_number = page_number  # type: int
        # 每页的大小（默认为100）
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceInstancesRequest, self).to_map()
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


class ListResourceInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.instances = instances  # type: list[ResourceInstance]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ResourceInstance()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListResourceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceInstancesResponse, self).to_map()
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
            temp_model = ListResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceServicesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 请求的页码（默认为1）
        self.page_number = page_number  # type: int
        # 每页的大小（默认为100）
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceServicesRequest, self).to_map()
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


class ListResourceServicesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, services=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.services = services  # type: list[Service]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = Service()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListResourceServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceServicesResponse, self).to_map()
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
            temp_model = ListResourceServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 请求的页码（默认为1）
        self.page_number = page_number  # type: int
        # 每页的大小（默认为100）
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesRequest, self).to_map()
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


class ListResourcesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, resources=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[Resource]
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = Resource()
                self.resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 请求的页码（默认为1）
        self.page_number = page_number  # type: int
        # 每页的大小（默认为100）
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesRequest, self).to_map()
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


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.instances = instances  # type: list[Instance]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = Instance()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponse, self).to_map()
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
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(self, filter=None, order=None, page_number=None, page_size=None, sort=None):
        # 模糊匹配字段（只支持按服务名字模糊匹配）
        self.filter = filter  # type: str
        # 排序方式（默认降序）
        self.order = order  # type: str
        # 请求的页码（默认为1）
        self.page_number = page_number  # type: int
        # 每页的大小（默认为100）
        self.page_size = page_size  # type: int
        # 排序字段 （时间戳类型默认倒序排序）
        self.sort = sort  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, services=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        self.services = services  # type: list[Service]
        self.total_count = total_count  # type: int

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = Service()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ReleaseServiceRequest(TeaModel):
    def __init__(self, weight=None):
        # 灰度权重，范围 [0, 100]
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ReleaseServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleaseServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseServiceResponse, self).to_map()
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
            temp_model = ReleaseServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartServiceResponse, self).to_map()
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
            temp_model = StartServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopServiceResponse, self).to_map()
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
            temp_model = StopServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(self, resource_name=None):
        # 新的资源组名称
        self.resource_name = resource_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_id=None, resource_name=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceResponse, self).to_map()
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
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceDLinkRequest(TeaModel):
    def __init__(self, destination_cidrs=None, security_group_id=None, v_switch_id=None, v_switch_id_list=None):
        # 要打通的客户端的网段信息，会将该网段加入到服务端的回包路由中，与VSwitchIdList可二选一
        self.destination_cidrs = destination_cidrs  # type: str
        # 客户端ECS归属的安全组
        self.security_group_id = security_group_id  # type: str
        # 对端的主VSwitchID，会在该vswitch中创建ENI
        self.v_switch_id = v_switch_id  # type: str
        # 要打通的客户端的vswitch列表，会将这些vswitch对应的网段加入到服务端的回包路由中
        self.v_switch_id_list = v_switch_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceDLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidrs is not None:
            result['DestinationCIDRs'] = self.destination_cidrs
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_id_list is not None:
            result['VSwitchIdList'] = self.v_switch_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCIDRs') is not None:
            self.destination_cidrs = m.get('DestinationCIDRs')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')
        return self


class UpdateResourceDLinkResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceDLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourceDLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateResourceDLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceDLinkResponse, self).to_map()
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
            temp_model = UpdateResourceDLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceRequest, self).to_map()
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


class UpdateServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        # 请求返回消息。
        self.message = message  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceResponse, self).to_map()
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
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceAutoScalerRequestStrategies(TeaModel):
    def __init__(self, cpu=None, qps=None):
        # 最大 replica 数，需要大于MinReplica
        self.cpu = cpu  # type: float
        # 每个实例支持的最大qps数，超出即扩容
        self.qps = qps  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceAutoScalerRequestStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.qps is not None:
            result['Qps'] = self.qps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        return self


class UpdateServiceAutoScalerRequest(TeaModel):
    def __init__(self, max=None, min=None, strategies=None):
        # 最大 replica 数，需要大于MinReplica
        self.max = max  # type: int
        # 最小 replica 数，需要大于0
        self.min = min  # type: int
        # map 类型的策略定义
        self.strategies = strategies  # type: UpdateServiceAutoScalerRequestStrategies

    def validate(self):
        if self.strategies:
            self.strategies.validate()

    def to_map(self):
        _map = super(UpdateServiceAutoScalerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.strategies is not None:
            result['Strategies'] = self.strategies.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Strategies') is not None:
            temp_model = UpdateServiceAutoScalerRequestStrategies()
            self.strategies = temp_model.from_map(m['Strategies'])
        return self


class UpdateServiceAutoScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceAutoScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceAutoScalerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceAutoScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceAutoScalerResponse, self).to_map()
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
            temp_model = UpdateServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceCronScalerRequestScaleJobs(TeaModel):
    def __init__(self, name=None, schedule=None, target_size=None):
        self.name = name  # type: str
        # 要执行伸缩任务的cron表达式
        self.schedule = schedule  # type: str
        # 执行伸缩任务的目标replica
        self.target_size = target_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceCronScalerRequestScaleJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.target_size is not None:
            result['TargetSize'] = self.target_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')
        return self


class UpdateServiceCronScalerRequest(TeaModel):
    def __init__(self, exclude_dates=None, scale_jobs=None):
        # 需要排除的时间点的cron表达式
        self.exclude_dates = exclude_dates  # type: list[str]
        # 定时伸缩任务描述
        self.scale_jobs = scale_jobs  # type: list[UpdateServiceCronScalerRequestScaleJobs]

    def validate(self):
        if self.scale_jobs:
            for k in self.scale_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateServiceCronScalerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_dates is not None:
            result['ExcludeDates'] = self.exclude_dates
        result['ScaleJobs'] = []
        if self.scale_jobs is not None:
            for k in self.scale_jobs:
                result['ScaleJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeDates') is not None:
            self.exclude_dates = m.get('ExcludeDates')
        self.scale_jobs = []
        if m.get('ScaleJobs') is not None:
            for k in m.get('ScaleJobs'):
                temp_model = UpdateServiceCronScalerRequestScaleJobs()
                self.scale_jobs.append(temp_model.from_map(k))
        return self


class UpdateServiceCronScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceCronScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceCronScalerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceCronScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceCronScalerResponse, self).to_map()
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
            temp_model = UpdateServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceMirrorRequest(TeaModel):
    def __init__(self, ratio=None, target=None):
        # 比例 [0, 100]
        self.ratio = ratio  # type: int
        # 服务实例列表
        self.target = target  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceMirrorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class UpdateServiceMirrorResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceMirrorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceMirrorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceMirrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceMirrorResponse, self).to_map()
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
            temp_model = UpdateServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceVersionRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateServiceVersionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceVersionResponse, self).to_map()
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
            temp_model = UpdateServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


