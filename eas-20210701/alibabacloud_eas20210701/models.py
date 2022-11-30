# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Group(TeaModel):
    def __init__(self, access_token=None, cluster_id=None, create_time=None, internet_endpoint=None,
                 intranet_endpoint=None, name=None, queue_service=None, update_time=None):
        self.access_token = access_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.create_time = create_time  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.name = name  # type: str
        self.queue_service = queue_service  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Group, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.name is not None:
            result['Name'] = self.name
        if self.queue_service is not None:
            result['QueueService'] = self.queue_service
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QueueService') is not None:
            self.queue_service = m.get('QueueService')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Instance(TeaModel):
    def __init__(self, host_ip=None, host_name=None, inner_ip=None, instance_name=None, instance_port=None,
                 last_state=None, namespace=None, ready_processes=None, reason=None, restart_count=None, start_at=None,
                 status=None, total_processes=None):
        self.host_ip = host_ip  # type: str
        self.host_name = host_name  # type: str
        self.inner_ip = inner_ip  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_port = instance_port  # type: int
        self.last_state = last_state  # type: list[dict[str, any]]
        self.namespace = namespace  # type: str
        self.ready_processes = ready_processes  # type: int
        self.reason = reason  # type: str
        self.restart_count = restart_count  # type: int
        self.start_at = start_at  # type: str
        self.status = status  # type: str
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
        if self.namespace is not None:
            result['Namespace'] = self.namespace
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
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
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
        self.cluster_id = cluster_id  # type: str
        self.cpu_count = cpu_count  # type: int
        self.create_time = create_time  # type: str
        self.extra_data = extra_data  # type: dict[str, any]
        self.gpu_count = gpu_count  # type: int
        self.instance_count = instance_count  # type: int
        self.message = message  # type: str
        self.post_paid_instance_count = post_paid_instance_count  # type: int
        self.pre_paid_instance_count = pre_paid_instance_count  # type: int
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.status = status  # type: str
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
    def __init__(self, arch=None, auto_renewal=None, charge_type=None, create_time=None, expired_time=None,
                 instance_cpu_count=None, instance_gpu_count=None, instance_gpu_memory=None, instance_id=None, instance_ip=None,
                 instance_memory=None, instance_name=None, instance_status=None, instance_type=None, instance_used_cpu=None,
                 instance_used_gpu=None, instance_used_memory=None, region=None, zone=None):
        self.arch = arch  # type: str
        self.auto_renewal = auto_renewal  # type: bool
        self.charge_type = charge_type  # type: str
        self.create_time = create_time  # type: str
        self.expired_time = expired_time  # type: str
        self.instance_cpu_count = instance_cpu_count  # type: int
        self.instance_gpu_count = instance_gpu_count  # type: int
        self.instance_gpu_memory = instance_gpu_memory  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_ip = instance_ip  # type: str
        self.instance_memory = instance_memory  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_status = instance_status  # type: str
        self.instance_type = instance_type  # type: str
        self.instance_used_cpu = instance_used_cpu  # type: float
        self.instance_used_gpu = instance_used_gpu  # type: int
        self.instance_used_memory = instance_used_memory  # type: str
        self.region = region  # type: str
        self.zone = zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arch is not None:
            result['Arch'] = self.arch
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
        if self.instance_gpu_memory is not None:
            result['InstanceGpuMemory'] = self.instance_gpu_memory
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
        if self.region is not None:
            result['Region'] = self.region
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arch') is not None:
            self.arch = m.get('Arch')
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
        if m.get('InstanceGpuMemory') is not None:
            self.instance_gpu_memory = m.get('InstanceGpuMemory')
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
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class ResourceInstanceWorker(TeaModel):
    def __init__(self, cpu_limit=None, cpu_request=None, gpu_limit=None, gpu_request=None, memory_limit=None,
                 memory_rquest=None, name=None, ready=None, restart_count=None, service_name=None, start_time=None, status=None):
        self.cpu_limit = cpu_limit  # type: int
        self.cpu_request = cpu_request  # type: int
        self.gpu_limit = gpu_limit  # type: int
        self.gpu_request = gpu_request  # type: int
        self.memory_limit = memory_limit  # type: int
        self.memory_rquest = memory_rquest  # type: int
        self.name = name  # type: str
        self.ready = ready  # type: bool
        self.restart_count = restart_count  # type: int
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: str
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
                 extra_data=None, gpu=None, image=None, internet_endpoint=None, intranet_endpoint=None, latest_version=None,
                 memory=None, message=None, namespace=None, parent_uid=None, pending_instance=None, reason=None,
                 region=None, request_id=None, resource=None, resource_alias=None, role=None, role_attrs=None,
                 running_instance=None, safety_lock=None, service_config=None, service_group=None, service_id=None,
                 service_name=None, service_uid=None, source=None, status=None, total_instance=None, update_time=None,
                 weight=None):
        self.access_token = access_token  # type: str
        self.caller_uid = caller_uid  # type: str
        self.cpu = cpu  # type: int
        self.create_time = create_time  # type: str
        self.current_version = current_version  # type: int
        self.extra_data = extra_data  # type: str
        self.gpu = gpu  # type: int
        self.image = image  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.latest_version = latest_version  # type: int
        self.memory = memory  # type: int
        self.message = message  # type: str
        self.namespace = namespace  # type: str
        self.parent_uid = parent_uid  # type: str
        self.pending_instance = pending_instance  # type: int
        self.reason = reason  # type: str
        self.region = region  # type: str
        self.request_id = request_id  # type: str
        self.resource = resource  # type: str
        self.resource_alias = resource_alias  # type: str
        self.role = role  # type: str
        self.role_attrs = role_attrs  # type: str
        self.running_instance = running_instance  # type: int
        self.safety_lock = safety_lock  # type: str
        self.service_config = service_config  # type: str
        self.service_group = service_group  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.service_uid = service_uid  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.total_instance = total_instance  # type: int
        self.update_time = update_time  # type: str
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
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
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
        if self.resource_alias is not None:
            result['ResourceAlias'] = self.resource_alias
        if self.role is not None:
            result['Role'] = self.role
        if self.role_attrs is not None:
            result['RoleAttrs'] = self.role_attrs
        if self.running_instance is not None:
            result['RunningInstance'] = self.running_instance
        if self.safety_lock is not None:
            result['SafetyLock'] = self.safety_lock
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_uid is not None:
            result['ServiceUid'] = self.service_uid
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.total_instance is not None:
            result['TotalInstance'] = self.total_instance
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
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
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
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
        if m.get('ResourceAlias') is not None:
            self.resource_alias = m.get('ResourceAlias')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleAttrs') is not None:
            self.role_attrs = m.get('RoleAttrs')
        if m.get('RunningInstance') is not None:
            self.running_instance = m.get('RunningInstance')
        if m.get('SafetyLock') is not None:
            self.safety_lock = m.get('SafetyLock')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceUid') is not None:
            self.service_uid = m.get('ServiceUid')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalInstance') is not None:
            self.total_instance = m.get('TotalInstance')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateBenchmarkTaskRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBenchmarkTaskRequest, self).to_map()
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


class CreateBenchmarkTaskResponseBody(TeaModel):
    def __init__(self, message=None, region=None, request_id=None, task_name=None):
        self.message = message  # type: str
        self.region = region  # type: str
        self.request_id = request_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBenchmarkTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateBenchmarkTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBenchmarkTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBenchmarkTaskResponse, self).to_map()
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
            temp_model = CreateBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRequest(TeaModel):
    def __init__(self, auto_renewal=None, charge_type=None, ecs_instance_count=None, ecs_instance_type=None):
        self.auto_renewal = auto_renewal  # type: bool
        self.charge_type = charge_type  # type: str
        self.ecs_instance_count = ecs_instance_count  # type: int
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
        self.cluster_id = cluster_id  # type: str
        self.owner_uid = owner_uid  # type: str
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str
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
            result['ResourceId'] = self.resource_id
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
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceInstancesRequest(TeaModel):
    def __init__(self, auto_renewal=None, charge_type=None, ecs_instance_count=None, ecs_instance_type=None,
                 user_data=None):
        self.auto_renewal = auto_renewal  # type: bool
        self.charge_type = charge_type  # type: str
        self.ecs_instance_count = ecs_instance_count  # type: int
        self.ecs_instance_type = ecs_instance_type  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceLogRequest(TeaModel):
    def __init__(self, log_store=None, project_name=None):
        self.log_store = log_store  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceAutoScalerRequestScaleStrategies(TeaModel):
    def __init__(self, metric_name=None, service=None, threshold=None):
        self.metric_name = metric_name  # type: str
        self.service = service  # type: str
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceAutoScalerRequestScaleStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.service is not None:
            result['service'] = self.service
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class CreateServiceAutoScalerRequest(TeaModel):
    def __init__(self, max=None, min=None, scale_strategies=None):
        self.max = max  # type: int
        self.min = min  # type: int
        self.scale_strategies = scale_strategies  # type: list[CreateServiceAutoScalerRequestScaleStrategies]

    def validate(self):
        if self.scale_strategies:
            for k in self.scale_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceAutoScalerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['max'] = self.max
        if self.min is not None:
            result['min'] = self.min
        result['scaleStrategies'] = []
        if self.scale_strategies is not None:
            for k in self.scale_strategies:
                result['scaleStrategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('max') is not None:
            self.max = m.get('max')
        if m.get('min') is not None:
            self.min = m.get('min')
        self.scale_strategies = []
        if m.get('scaleStrategies') is not None:
            for k in m.get('scaleStrategies'):
                temp_model = CreateServiceAutoScalerRequestScaleStrategies()
                self.scale_strategies.append(temp_model.from_map(k))
        return self


class CreateServiceAutoScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceAutoScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceCronScalerRequestScaleJobs(TeaModel):
    def __init__(self, name=None, schedule=None, target_size=None):
        self.name = name  # type: str
        self.schedule = schedule  # type: str
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
        self.exclude_dates = exclude_dates  # type: list[str]
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
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceCronScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceMirrorRequest(TeaModel):
    def __init__(self, ratio=None, target=None):
        self.ratio = ratio  # type: int
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceMirrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBenchmarkTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBenchmarkTaskResponseBody, self).to_map()
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


class DeleteBenchmarkTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBenchmarkTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBenchmarkTaskResponse, self).to_map()
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
            temp_model = DeleteBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceDLinkResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceDLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceLogResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteResourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceAutoScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceAutoScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceCronScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceCronScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceInstancesRequest(TeaModel):
    def __init__(self, instance_list=None):
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceMirrorResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceMirrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBenchmarkTaskResponseBody(TeaModel):
    def __init__(self, available_agent=None, caller_uid=None, desired_agent=None, endpoint=None, message=None,
                 parent_uid=None, reason=None, request_id=None, service_name=None, status=None, task_id=None, task_name=None,
                 token=None):
        self.available_agent = available_agent  # type: long
        self.caller_uid = caller_uid  # type: str
        self.desired_agent = desired_agent  # type: long
        self.endpoint = endpoint  # type: str
        self.message = message  # type: str
        self.parent_uid = parent_uid  # type: str
        self.reason = reason  # type: str
        self.request_id = request_id  # type: str
        self.service_name = service_name  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBenchmarkTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_agent is not None:
            result['AvailableAgent'] = self.available_agent
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.desired_agent is not None:
            result['DesiredAgent'] = self.desired_agent
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableAgent') is not None:
            self.available_agent = m.get('AvailableAgent')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('DesiredAgent') is not None:
            self.desired_agent = m.get('DesiredAgent')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeBenchmarkTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBenchmarkTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBenchmarkTaskResponse, self).to_map()
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
            temp_model = DescribeBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBenchmarkTaskReportRequest(TeaModel):
    def __init__(self, report_type=None):
        self.report_type = report_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBenchmarkTaskReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        return self


class DescribeBenchmarkTaskReportResponseBody(TeaModel):
    def __init__(self, data=None, report_url=None, request_id=None):
        self.data = data  # type: any
        self.report_url = report_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBenchmarkTaskReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBenchmarkTaskReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBenchmarkTaskReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBenchmarkTaskReportResponse, self).to_map()
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
            temp_model = DescribeBenchmarkTaskReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Group

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGroupResponse, self).to_map()
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
            temp_model = Group()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceDLinkResponseBody(TeaModel):
    def __init__(self, aux_vswitch_list=None, destination_cidrs=None, request_id=None, security_group_id=None,
                 v_switch_id=None, vpc_id=None):
        self.aux_vswitch_list = aux_vswitch_list  # type: list[str]
        self.destination_cidrs = destination_cidrs  # type: str
        self.request_id = request_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResourceDLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeResourceDLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceLogResponseBody(TeaModel):
    def __init__(self, log_store=None, message=None, project_name=None, request_id=None, status=None):
        self.log_store = log_store  # type: str
        self.message = message  # type: str
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeResourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Service

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceAutoScalerResponseBodyCurrentMetrics(TeaModel):
    def __init__(self, metric_name=None, service=None, value=None):
        self.metric_name = metric_name  # type: str
        self.service = service  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceAutoScalerResponseBodyCurrentMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.service is not None:
            result['service'] = self.service
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeServiceAutoScalerResponseBodyScaleStrategies(TeaModel):
    def __init__(self, metric_name=None, service=None, threshold=None):
        self.metric_name = metric_name  # type: str
        self.service = service  # type: str
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceAutoScalerResponseBodyScaleStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.service is not None:
            result['service'] = self.service
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class DescribeServiceAutoScalerResponseBody(TeaModel):
    def __init__(self, behavior=None, current_metrics=None, max_replica=None, min_replica=None, request_id=None,
                 scale_strategies=None, service_name=None):
        self.behavior = behavior  # type: dict[str, any]
        self.current_metrics = current_metrics  # type: list[DescribeServiceAutoScalerResponseBodyCurrentMetrics]
        self.max_replica = max_replica  # type: int
        self.min_replica = min_replica  # type: int
        self.request_id = request_id  # type: str
        self.scale_strategies = scale_strategies  # type: list[DescribeServiceAutoScalerResponseBodyScaleStrategies]
        self.service_name = service_name  # type: str

    def validate(self):
        if self.current_metrics:
            for k in self.current_metrics:
                if k:
                    k.validate()
        if self.scale_strategies:
            for k in self.scale_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeServiceAutoScalerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behavior is not None:
            result['Behavior'] = self.behavior
        result['CurrentMetrics'] = []
        if self.current_metrics is not None:
            for k in self.current_metrics:
                result['CurrentMetrics'].append(k.to_map() if k else None)
        if self.max_replica is not None:
            result['MaxReplica'] = self.max_replica
        if self.min_replica is not None:
            result['MinReplica'] = self.min_replica
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScaleStrategies'] = []
        if self.scale_strategies is not None:
            for k in self.scale_strategies:
                result['ScaleStrategies'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')
        self.current_metrics = []
        if m.get('CurrentMetrics') is not None:
            for k in m.get('CurrentMetrics'):
                temp_model = DescribeServiceAutoScalerResponseBodyCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k))
        if m.get('MaxReplica') is not None:
            self.max_replica = m.get('MaxReplica')
        if m.get('MinReplica') is not None:
            self.min_replica = m.get('MinReplica')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scale_strategies = []
        if m.get('ScaleStrategies') is not None:
            for k in m.get('ScaleStrategies'):
                temp_model = DescribeServiceAutoScalerResponseBodyScaleStrategies()
                self.scale_strategies.append(temp_model.from_map(k))
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeServiceAutoScalerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeServiceAutoScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceCronScalerResponseBodyScaleJobs(TeaModel):
    def __init__(self, create_time=None, last_probe_time=None, message=None, name=None, schedule=None, state=None,
                 target_size=None):
        self.create_time = create_time  # type: str
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeServiceCronScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceEventRequest(TeaModel):
    def __init__(self, end_time=None, page_num=None, page_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.page_num = page_num  # type: str
        self.page_size = page_size  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeServiceEventResponseBodyEvents(TeaModel):
    def __init__(self, message=None, reason=None, time=None, type=None):
        self.message = message  # type: str
        self.reason = reason  # type: str
        self.time = time  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceEventResponseBodyEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeServiceEventResponseBody(TeaModel):
    def __init__(self, events=None, page_num=None, request_id=None, total_count=None, total_page_num=None):
        self.events = events  # type: list[DescribeServiceEventResponseBodyEvents]
        self.page_num = page_num  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.total_page_num = total_page_num  # type: long

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeServiceEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
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
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeServiceEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class DescribeServiceEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeServiceEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceEventResponse, self).to_map()
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
            temp_model = DescribeServiceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceLogRequest(TeaModel):
    def __init__(self, end_time=None, ip=None, keyword=None, page_num=None, page_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.ip = ip  # type: str
        self.keyword = keyword  # type: str
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
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
        self.logs = logs  # type: list[str]
        self.page_num = page_num  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeServiceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeServiceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMirrorResponseBody(TeaModel):
    def __init__(self, ratio=None, request_id=None, service_name=None, target=None):
        self.ratio = ratio  # type: str
        self.request_id = request_id  # type: str
        self.service_name = service_name  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeServiceMirrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBenchmarkTaskRequest(TeaModel):
    def __init__(self, filter=None, page_number=None, page_size=None, service_name=None):
        self.filter = filter  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBenchmarkTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListBenchmarkTaskResponseBodyTasks(TeaModel):
    def __init__(self, available_agent=None, create_time=None, message=None, region=None, service_name=None,
                 status=None, task_id=None, task_name=None, update_time=None):
        self.available_agent = available_agent  # type: long
        self.create_time = create_time  # type: str
        self.message = message  # type: str
        self.region = region  # type: str
        self.service_name = service_name  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBenchmarkTaskResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_agent is not None:
            result['AvailableAgent'] = self.available_agent
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.message is not None:
            result['Message'] = self.message
        if self.region is not None:
            result['Region'] = self.region
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableAgent') is not None:
            self.available_agent = m.get('AvailableAgent')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListBenchmarkTaskResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, tasks=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[ListBenchmarkTaskResponseBodyTasks]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBenchmarkTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
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
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListBenchmarkTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBenchmarkTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBenchmarkTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBenchmarkTaskResponse, self).to_map()
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
            temp_model = ListBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(self, filter=None, page_number=None, page_size=None):
        self.filter = filter  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(self, groups=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.groups = groups  # type: list[Group]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
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
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = Group()
                self.groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupsResponse, self).to_map()
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
            temp_model = ListGroupsResponseBody()
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
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.pods = pods  # type: list[ResourceInstanceWorker]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceInstanceWorkerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListResourceInstanceWorkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceInstancesRequest(TeaModel):
    def __init__(self, charge_type=None, instance_id=None, instance_name=None, page_number=None, page_size=None):
        self.charge_type = charge_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceServicesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListResourceServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, resource_id=None, resource_name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str

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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, resources=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
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


class ListServiceInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceVersionsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceVersionsRequest, self).to_map()
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


class ListServiceVersionsResponseBodyVersions(TeaModel):
    def __init__(self, build_time=None, image_available=None, image_id=None, message=None, service_runnable=None):
        self.build_time = build_time  # type: str
        self.image_available = image_available  # type: str
        self.image_id = image_id  # type: int
        self.message = message  # type: str
        self.service_runnable = service_runnable  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceVersionsResponseBodyVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_time is not None:
            result['BuildTime'] = self.build_time
        if self.image_available is not None:
            result['ImageAvailable'] = self.image_available
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.message is not None:
            result['Message'] = self.message
        if self.service_runnable is not None:
            result['ServiceRunnable'] = self.service_runnable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildTime') is not None:
            self.build_time = m.get('BuildTime')
        if m.get('ImageAvailable') is not None:
            self.image_available = m.get('ImageAvailable')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ServiceRunnable') is not None:
            self.service_runnable = m.get('ServiceRunnable')
        return self


class ListServiceVersionsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, versions=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.versions = versions  # type: list[ListServiceVersionsResponseBodyVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListServiceVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListServiceVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceVersionsResponse, self).to_map()
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
            temp_model = ListServiceVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(self, filter=None, group_name=None, order=None, page_number=None, page_size=None, sort=None):
        self.filter = filter  # type: str
        self.group_name = group_name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
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
        if self.group_name is not None:
            result['GroupName'] = self.group_name
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
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseServiceRequest(TeaModel):
    def __init__(self, traffic_state=None, weight=None):
        self.traffic_state = traffic_state  # type: str
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.traffic_state is not None:
            result['TrafficState'] = self.traffic_state
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrafficState') is not None:
            self.traffic_state = m.get('TrafficState')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ReleaseServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ReleaseServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBenchmarkTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartBenchmarkTaskResponseBody, self).to_map()
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


class StartBenchmarkTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartBenchmarkTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartBenchmarkTaskResponse, self).to_map()
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
            temp_model = StartBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBenchmarkTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopBenchmarkTaskResponseBody, self).to_map()
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


class StopBenchmarkTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopBenchmarkTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopBenchmarkTaskResponse, self).to_map()
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
            temp_model = StopBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBenchmarkTaskRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBenchmarkTaskRequest, self).to_map()
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


class UpdateBenchmarkTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBenchmarkTaskResponseBody, self).to_map()
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


class UpdateBenchmarkTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBenchmarkTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBenchmarkTaskResponse, self).to_map()
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
            temp_model = UpdateBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(self, resource_name=None):
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceDLinkRequest(TeaModel):
    def __init__(self, destination_cidrs=None, security_group_id=None, v_switch_id=None, v_switch_id_list=None):
        self.destination_cidrs = destination_cidrs  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceDLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateResourceDLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceInstanceRequest(TeaModel):
    def __init__(self, action=None):
        self.action = action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class UpdateResourceInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None, resource_id=None):
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class UpdateResourceInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceInstanceResponse, self).to_map()
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
            temp_model = UpdateResourceInstanceResponseBody()
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
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceAutoScalerRequestScaleStrategies(TeaModel):
    def __init__(self, metric_name=None, service=None, threshold=None):
        self.metric_name = metric_name  # type: str
        self.service = service  # type: str
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceAutoScalerRequestScaleStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.service is not None:
            result['service'] = self.service
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class UpdateServiceAutoScalerRequest(TeaModel):
    def __init__(self, max=None, min=None, scale_strategies=None):
        self.max = max  # type: int
        self.min = min  # type: int
        self.scale_strategies = scale_strategies  # type: list[UpdateServiceAutoScalerRequestScaleStrategies]

    def validate(self):
        if self.scale_strategies:
            for k in self.scale_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateServiceAutoScalerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['max'] = self.max
        if self.min is not None:
            result['min'] = self.min
        result['scaleStrategies'] = []
        if self.scale_strategies is not None:
            for k in self.scale_strategies:
                result['scaleStrategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('max') is not None:
            self.max = m.get('max')
        if m.get('min') is not None:
            self.min = m.get('min')
        self.scale_strategies = []
        if m.get('scaleStrategies') is not None:
            for k in m.get('scaleStrategies'):
                temp_model = UpdateServiceAutoScalerRequestScaleStrategies()
                self.scale_strategies.append(temp_model.from_map(k))
        return self


class UpdateServiceAutoScalerResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceAutoScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceCronScalerRequestScaleJobs(TeaModel):
    def __init__(self, name=None, schedule=None, target_size=None):
        self.name = name  # type: str
        self.schedule = schedule  # type: str
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
        self.exclude_dates = exclude_dates  # type: list[str]
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceCronScalerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceMirrorRequest(TeaModel):
    def __init__(self, ratio=None, target=None):
        self.ratio = ratio  # type: int
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceMirrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceSafetyLockRequest(TeaModel):
    def __init__(self, lock=None):
        self.lock = lock  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceSafetyLockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock is not None:
            result['Lock'] = self.lock
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lock') is not None:
            self.lock = m.get('Lock')
        return self


class UpdateServiceSafetyLockResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceSafetyLockResponseBody, self).to_map()
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


class UpdateServiceSafetyLockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceSafetyLockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceSafetyLockResponse, self).to_map()
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
            temp_model = UpdateServiceSafetyLockResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


