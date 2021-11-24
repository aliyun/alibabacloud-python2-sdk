# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Addon(TeaModel):
    def __init__(self, config=None, disabled=None, name=None):
        # 插件配置参数。
        self.config = config  # type: str
        # 是否禁止默认安装。true | false。
        self.disabled = disabled  # type: bool
        # 插件名称。
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Addon, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DataDisk(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, category=None, encrypted=None, performance_level=None,
                 size=None):
        # 开启云盘备份时的自动备份策略。
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # 数据盘类型
        self.category = category  # type: str
        # 是否对数据盘加密。
        self.encrypted = encrypted  # type: str
        # 数据盘磁盘性能，只针对ESSD磁盘生效
        self.performance_level = performance_level  # type: str
        # 数据盘大小，取值范围：40～32767
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.performance_level is not None:
            result['performance_level'] = self.performance_level
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = m.get('auto_snapshot_policy_id')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('performance_level') is not None:
            self.performance_level = m.get('performance_level')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class MaintenanceWindow(TeaModel):
    def __init__(self, duration=None, enable=None, maintenance_time=None, weekly_period=None):
        # 维护时长。取值范围1～24，单位为小时。 默认值：3h。
        self.duration = duration  # type: str
        # 是否开启维护窗口。默认值false。
        self.enable = enable  # type: bool
        # 维护起始时间。Golang标准时间格式"15:04:05Z"。
        self.maintenance_time = maintenance_time  # type: str
        # 维护周期。取值范围为:Monday~Sunday，多个值用逗号分隔。 默认值：Thursday。
        self.weekly_period = weekly_period  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MaintenanceWindow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.enable is not None:
            result['enable'] = self.enable
        if self.maintenance_time is not None:
            result['maintenance_time'] = self.maintenance_time
        if self.weekly_period is not None:
            result['weekly_period'] = self.weekly_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('maintenance_time') is not None:
            self.maintenance_time = m.get('maintenance_time')
        if m.get('weekly_period') is not None:
            self.weekly_period = m.get('weekly_period')
        return self


class Runtime(TeaModel):
    def __init__(self, name=None, version=None):
        # 容器运行时名称
        self.name = name  # type: str
        # 容器运行时版本
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Runtime, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Tag(TeaModel):
    def __init__(self, key=None, value=None):
        # key值。
        self.key = key  # type: str
        # value值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Tag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class Taint(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # 污点生效策略。
        self.effect = effect  # type: str
        # key值。
        self.key = key  # type: str
        # value值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Taint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AttachInstancesRequest(TeaModel):
    def __init__(self, cpu_policy=None, format_disk=None, image_id=None, instances=None, is_edge_worker=None,
                 keep_instance_name=None, key_pair=None, nodepool_id=None, password=None, rds_instances=None, runtime=None, tags=None,
                 user_data=None):
        # CPU亲和策略。
        self.cpu_policy = cpu_policy  # type: str
        # 是否格式化数据盘。
        self.format_disk = format_disk  # type: bool
        # 自定义镜像ID。
        self.image_id = image_id  # type: str
        # 实例列表。
        self.instances = instances  # type: list[str]
        # 是否为边缘节点。
        self.is_edge_worker = is_edge_worker  # type: bool
        # 是否保留实例名称。
        self.keep_instance_name = keep_instance_name  # type: bool
        # key_pair名称，与login_password二选一
        self.key_pair = key_pair  # type: str
        # 节点池ID，欲将节点添加到哪个节点池中。。
        self.nodepool_id = nodepool_id  # type: str
        # password，与key_pair二选一。
        self.password = password  # type: str
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: list[str]
        self.runtime = runtime  # type: Runtime
        # 节点标签。
        self.tags = tags  # type: list[Tag]
        # 节点自定义数据。
        self.user_data = user_data  # type: str

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instances is not None:
            result['instances'] = self.instances
        if self.is_edge_worker is not None:
            result['is_edge_worker'] = self.is_edge_worker
        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.password is not None:
            result['password'] = self.password
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        if m.get('is_edge_worker') is not None:
            self.is_edge_worker = m.get('is_edge_worker')
        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('runtime') is not None:
            temp_model = Runtime()
            self.runtime = temp_model.from_map(m['runtime'])
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class AttachInstancesResponseBodyList(TeaModel):
    def __init__(self, code=None, instance_id=None, message=None):
        # 状态码。
        self.code = code  # type: str
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 添加结果描述。
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachInstancesResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class AttachInstancesResponseBody(TeaModel):
    def __init__(self, list=None, task_id=None):
        # 节点信息列表。
        self.list = list  # type: list[AttachInstancesResponseBodyList]
        # 任务ID。
        self.task_id = task_id  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = AttachInstancesResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class AttachInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachInstancesResponse, self).to_map()
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
            temp_model = AttachInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelClusterUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CancelClusterUpgradeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CancelComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CancelComponentUpgradeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CancelWorkflowRequest(TeaModel):
    def __init__(self, action=None):
        # 执行的操作，目前只支持cancel。
        self.action = action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class CancelWorkflowResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CancelWorkflowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateAutoscalingConfigRequest(TeaModel):
    def __init__(self, cool_down_duration=None, gpu_utilization_threshold=None, scan_interval=None,
                 unneeded_duration=None, utilization_threshold=None):
        # 静默时间，扩容出的节点，在静默时间过后，方可进入缩容判断
        self.cool_down_duration = cool_down_duration  # type: str
        # GPU缩容阈值，节点上 Request 的资源与总资源量的比值
        self.gpu_utilization_threshold = gpu_utilization_threshold  # type: str
        # 弹性灵敏度，判断伸缩的间隔时间
        self.scan_interval = scan_interval  # type: str
        # 缩容触发时延，节点缩容时需要连续满足触发时延所设定的时间，方可进行缩容
        self.unneeded_duration = unneeded_duration  # type: str
        # 缩容阈值，节点上 Request 的资源与总资源量的比值
        self.utilization_threshold = utilization_threshold  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAutoscalingConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cool_down_duration is not None:
            result['cool_down_duration'] = self.cool_down_duration
        if self.gpu_utilization_threshold is not None:
            result['gpu_utilization_threshold'] = self.gpu_utilization_threshold
        if self.scan_interval is not None:
            result['scan_interval'] = self.scan_interval
        if self.unneeded_duration is not None:
            result['unneeded_duration'] = self.unneeded_duration
        if self.utilization_threshold is not None:
            result['utilization_threshold'] = self.utilization_threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cool_down_duration') is not None:
            self.cool_down_duration = m.get('cool_down_duration')
        if m.get('gpu_utilization_threshold') is not None:
            self.gpu_utilization_threshold = m.get('gpu_utilization_threshold')
        if m.get('scan_interval') is not None:
            self.scan_interval = m.get('scan_interval')
        if m.get('unneeded_duration') is not None:
            self.unneeded_duration = m.get('unneeded_duration')
        if m.get('utilization_threshold') is not None:
            self.utilization_threshold = m.get('utilization_threshold')
        return self


class CreateAutoscalingConfigResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(CreateAutoscalingConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateClusterRequestWorkerDataDisks(TeaModel):
    def __init__(self, category=None, encrypted=None, performance_level=None, size=None):
        # 集群Worker节点数据盘类型
        self.category = category  # type: str
        # 集群Worker节点数据盘是否加密
        self.encrypted = encrypted  # type: str
        # 集群Worker节点数据盘磁盘性能等级，仅对ESSD磁盘生效
        self.performance_level = performance_level  # type: str
        # 集群Worker节点数据盘大小
        self.size = size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestWorkerDataDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.performance_level is not None:
            result['performance_level'] = self.performance_level
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('performance_level') is not None:
            self.performance_level = m.get('performance_level')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, addons=None, api_audiences=None, cis_enabled=None, cloud_monitor_flags=None,
                 cluster_domain=None, cluster_spec=None, cluster_type=None, container_cidr=None, controlplane_log_components=None,
                 controlplane_log_project=None, controlplane_log_ttl=None, cpu_policy=None, custom_san=None, deletion_protection=None,
                 disable_rollback=None, enable_rrsa=None, encryption_provider_key=None, endpoint_public_access=None,
                 format_disk=None, image_id=None, image_type=None, instances=None, is_enterprise_security_group=None,
                 keep_instance_name=None, key_pair=None, kubernetes_version=None, load_balancer_spec=None, logging_type=None,
                 login_password=None, master_auto_renew=None, master_auto_renew_period=None, master_count=None,
                 master_instance_charge_type=None, master_instance_types=None, master_period=None, master_period_unit=None,
                 master_system_disk_category=None, master_system_disk_performance_level=None, master_system_disk_size=None,
                 master_system_disk_snapshot_policy_id=None, master_vswitch_ids=None, name=None, nat_gateway=None, node_cidr_mask=None,
                 node_name_mode=None, node_port_range=None, num_of_nodes=None, os_type=None, platform=None, pod_vswitch_ids=None,
                 profile=None, proxy_mode=None, rds_instances=None, region_id=None, runtime=None, security_group_id=None,
                 service_account_issuer=None, service_cidr=None, service_discovery_types=None, snat_entry=None, soc_enabled=None,
                 ssh_flags=None, tags=None, taints=None, timeout_mins=None, timezone=None, user_ca=None, user_data=None,
                 vpcid=None, vswitch_ids=None, worker_auto_renew=None, worker_auto_renew_period=None,
                 worker_data_disks=None, worker_instance_charge_type=None, worker_instance_types=None, worker_period=None,
                 worker_period_unit=None, worker_system_disk_category=None, worker_system_disk_performance_level=None,
                 worker_system_disk_size=None, worker_system_disk_snapshot_policy_id=None, worker_vswitch_ids=None, zone_id=None):
        # 集群组件配置
        self.addons = addons  # type: list[Addon]
        # 合法的请求token身份，用于apiserver服务端认证请求token是否合法。
        self.api_audiences = api_audiences  # type: str
        # CIS安全加固
        self.cis_enabled = cis_enabled  # type: bool
        # 为ECS安装云监控
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 集群本地域名
        self.cluster_domain = cluster_domain  # type: str
        # 托管版集群类型
        self.cluster_spec = cluster_spec  # type: str
        # 集群类型
        self.cluster_type = cluster_type  # type: str
        # POD网络网段
        self.container_cidr = container_cidr  # type: str
        # 需要采集日志的组件
        self.controlplane_log_components = controlplane_log_components  # type: list[str]
        # 使用已有log project时，需要指定log project
        self.controlplane_log_project = controlplane_log_project  # type: str
        # 控制平面日志
        self.controlplane_log_ttl = controlplane_log_ttl  # type: str
        # CPU策略
        self.cpu_policy = cpu_policy  # type: str
        # 自定义证书SAN
        self.custom_san = custom_san  # type: str
        # 集群删除保护
        self.deletion_protection = deletion_protection  # type: bool
        # 失败回滚
        self.disable_rollback = disable_rollback  # type: bool
        # 启用 RRSA 功能
        self.enable_rrsa = enable_rrsa  # type: bool
        # Secret落盘加密
        self.encryption_provider_key = encryption_provider_key  # type: str
        # 使用EIP暴露apiServer
        self.endpoint_public_access = endpoint_public_access  # type: bool
        # 使用已有节点创建集群时，是否格式化已有实例的磁盘
        self.format_disk = format_disk  # type: bool
        # 自定义镜像
        self.image_id = image_id  # type: str
        # 操作系统镜像类型
        self.image_type = image_type  # type: str
        # 使用已有节点创建集群时，已有实例列表
        self.instances = instances  # type: list[str]
        # 自动创建企业安全组
        self.is_enterprise_security_group = is_enterprise_security_group  # type: bool
        # 使用已有节点创建集群时，是否保留实例名称。
        self.keep_instance_name = keep_instance_name  # type: bool
        # 密钥对名称，和login_password二选一。
        self.key_pair = key_pair  # type: str
        # 集群版本
        self.kubernetes_version = kubernetes_version  # type: str
        # 负载均衡规格
        self.load_balancer_spec = load_balancer_spec  # type: str
        # ASK 集群开启日志服务
        self.logging_type = logging_type  # type: str
        # SSH登录密码。密码规则为8~30 个字符，且至少同时包含三项（大小写字母、数字和特殊符号），和key_pair二选一。
        self.login_password = login_password  # type: str
        # 集群Master节点是否自动续费
        self.master_auto_renew = master_auto_renew  # type: bool
        # 集群Master节点自动续费时长
        self.master_auto_renew_period = master_auto_renew_period  # type: long
        # 集群Master节点数量
        self.master_count = master_count  # type: long
        # 集群Master节点付费类型
        self.master_instance_charge_type = master_instance_charge_type  # type: str
        # 集群Master节点类型
        self.master_instance_types = master_instance_types  # type: list[str]
        # 集群Master节点包年包月时长
        self.master_period = master_period  # type: long
        # 集群Master节点包年包月周期
        self.master_period_unit = master_period_unit  # type: str
        # 集群Master节点系统盘类型
        self.master_system_disk_category = master_system_disk_category  # type: str
        # Master节点系统盘磁盘性能，只针对ESSD磁盘生效
        self.master_system_disk_performance_level = master_system_disk_performance_level  # type: str
        # 集群Master节点系统盘大小，至少40
        self.master_system_disk_size = master_system_disk_size  # type: long
        # 集群Master节点自动快照备份策略
        self.master_system_disk_snapshot_policy_id = master_system_disk_snapshot_policy_id  # type: str
        # 集群Master节点使用的虚拟交换机
        self.master_vswitch_ids = master_vswitch_ids  # type: list[str]
        # 集群名称。
        self.name = name  # type: str
        # 使用自动创建专有网络创建ASK集群时，是否在vpc中创建Nat网关并配置SNAT规则。
        self.nat_gateway = nat_gateway  # type: bool
        # 节点IP数量
        self.node_cidr_mask = node_cidr_mask  # type: str
        # 自定义节点名称
        self.node_name_mode = node_name_mode  # type: str
        # 节点服务端口范围
        self.node_port_range = node_port_range  # type: str
        # 集群Worker节点数量
        self.num_of_nodes = num_of_nodes  # type: long
        # 操作系统平台类型
        self.os_type = os_type  # type: str
        # 操作系统发行版
        self.platform = platform  # type: str
        # 创建Terway网络类型的集群时，需要为pod指定单独的虚拟交换机
        self.pod_vswitch_ids = pod_vswitch_ids  # type: list[str]
        # 面向场景时的集群类型。  Default：非边缘场景集群。 Edge：边缘场景集群。
        self.profile = profile  # type: str
        # Proxy代理模式，ipvs|iptables
        self.proxy_mode = proxy_mode  # type: str
        # RDS白名单
        self.rds_instances = rds_instances  # type: list[str]
        # 地域ID
        self.region_id = region_id  # type: str
        self.runtime = runtime  # type: Runtime
        # 安全组ID，和is_enterprise_security_group二选一
        self.security_group_id = security_group_id  # type: str
        # serviceaccount token中的签发身份，即token payload中的iss字段。
        self.service_account_issuer = service_account_issuer  # type: str
        # 服务网络网段
        self.service_cidr = service_cidr  # type: str
        # 创建ASK集群时，服务发现类型
        self.service_discovery_types = service_discovery_types  # type: list[str]
        # 若您集群内的节点、应用等需要访问公网，勾选该项后我们将为您创建 NAT 网关并自动配置 SNAT 规则
        self.snat_entry = snat_entry  # type: bool
        # 等保安全加固
        self.soc_enabled = soc_enabled  # type: bool
        # 允许公网ssh登录
        self.ssh_flags = ssh_flags  # type: bool
        # 集群标签
        self.tags = tags  # type: list[Tag]
        # 节点污点信息
        self.taints = taints  # type: list[Taint]
        # 集群创建超时时间
        self.timeout_mins = timeout_mins  # type: long
        # 时区
        self.timezone = timezone  # type: str
        # 自定义集群CA
        self.user_ca = user_ca  # type: str
        # 节点自定义数据
        self.user_data = user_data  # type: str
        # 集群专有网络ID。
        self.vpcid = vpcid  # type: str
        # 集群节点所在虚拟交换机。
        self.vswitch_ids = vswitch_ids  # type: list[str]
        # 集群Worker节点到期是否自动续费
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # 集群Worker节点自动续费时长
        self.worker_auto_renew_period = worker_auto_renew_period  # type: long
        # 集群Worker节点数据盘配置
        self.worker_data_disks = worker_data_disks  # type: list[CreateClusterRequestWorkerDataDisks]
        # 集群Worker节点付费类型
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # 集群Worker节点类型
        self.worker_instance_types = worker_instance_types  # type: list[str]
        # 集群Worker节点包年包月时长
        self.worker_period = worker_period  # type: long
        # 集群Worker节点包年包月周期
        self.worker_period_unit = worker_period_unit  # type: str
        # 集群Worker节点系统盘类型
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # 集群Worker节点磁盘性能，只对ESSD类型磁盘生效
        self.worker_system_disk_performance_level = worker_system_disk_performance_level  # type: str
        # 集群Worker节点系统盘大小
        self.worker_system_disk_size = worker_system_disk_size  # type: long
        # 集群Worker节点系统盘快照备份策略
        self.worker_system_disk_snapshot_policy_id = worker_system_disk_snapshot_policy_id  # type: str
        # 集群Worker节点所在虚拟交换机
        self.worker_vswitch_ids = worker_vswitch_ids  # type: list[str]
        # 使用自动创建专有网络创建ASK集群时，需要指定专有网络的可用区
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['addons'].append(k.to_map() if k else None)
        if self.api_audiences is not None:
            result['api_audiences'] = self.api_audiences
        if self.cis_enabled is not None:
            result['cis_enabled'] = self.cis_enabled
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags
        if self.cluster_domain is not None:
            result['cluster_domain'] = self.cluster_domain
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.container_cidr is not None:
            result['container_cidr'] = self.container_cidr
        if self.controlplane_log_components is not None:
            result['controlplane_log_components'] = self.controlplane_log_components
        if self.controlplane_log_project is not None:
            result['controlplane_log_project'] = self.controlplane_log_project
        if self.controlplane_log_ttl is not None:
            result['controlplane_log_ttl'] = self.controlplane_log_ttl
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.custom_san is not None:
            result['custom_san'] = self.custom_san
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.disable_rollback is not None:
            result['disable_rollback'] = self.disable_rollback
        if self.enable_rrsa is not None:
            result['enable_rrsa'] = self.enable_rrsa
        if self.encryption_provider_key is not None:
            result['encryption_provider_key'] = self.encryption_provider_key
        if self.endpoint_public_access is not None:
            result['endpoint_public_access'] = self.endpoint_public_access
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.image_type is not None:
            result['image_type'] = self.image_type
        if self.instances is not None:
            result['instances'] = self.instances
        if self.is_enterprise_security_group is not None:
            result['is_enterprise_security_group'] = self.is_enterprise_security_group
        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.kubernetes_version is not None:
            result['kubernetes_version'] = self.kubernetes_version
        if self.load_balancer_spec is not None:
            result['load_balancer_spec'] = self.load_balancer_spec
        if self.logging_type is not None:
            result['logging_type'] = self.logging_type
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.master_auto_renew is not None:
            result['master_auto_renew'] = self.master_auto_renew
        if self.master_auto_renew_period is not None:
            result['master_auto_renew_period'] = self.master_auto_renew_period
        if self.master_count is not None:
            result['master_count'] = self.master_count
        if self.master_instance_charge_type is not None:
            result['master_instance_charge_type'] = self.master_instance_charge_type
        if self.master_instance_types is not None:
            result['master_instance_types'] = self.master_instance_types
        if self.master_period is not None:
            result['master_period'] = self.master_period
        if self.master_period_unit is not None:
            result['master_period_unit'] = self.master_period_unit
        if self.master_system_disk_category is not None:
            result['master_system_disk_category'] = self.master_system_disk_category
        if self.master_system_disk_performance_level is not None:
            result['master_system_disk_performance_level'] = self.master_system_disk_performance_level
        if self.master_system_disk_size is not None:
            result['master_system_disk_size'] = self.master_system_disk_size
        if self.master_system_disk_snapshot_policy_id is not None:
            result['master_system_disk_snapshot_policy_id'] = self.master_system_disk_snapshot_policy_id
        if self.master_vswitch_ids is not None:
            result['master_vswitch_ids'] = self.master_vswitch_ids
        if self.name is not None:
            result['name'] = self.name
        if self.nat_gateway is not None:
            result['nat_gateway'] = self.nat_gateway
        if self.node_cidr_mask is not None:
            result['node_cidr_mask'] = self.node_cidr_mask
        if self.node_name_mode is not None:
            result['node_name_mode'] = self.node_name_mode
        if self.node_port_range is not None:
            result['node_port_range'] = self.node_port_range
        if self.num_of_nodes is not None:
            result['num_of_nodes'] = self.num_of_nodes
        if self.os_type is not None:
            result['os_type'] = self.os_type
        if self.platform is not None:
            result['platform'] = self.platform
        if self.pod_vswitch_ids is not None:
            result['pod_vswitch_ids'] = self.pod_vswitch_ids
        if self.profile is not None:
            result['profile'] = self.profile
        if self.proxy_mode is not None:
            result['proxy_mode'] = self.proxy_mode
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.service_account_issuer is not None:
            result['service_account_issuer'] = self.service_account_issuer
        if self.service_cidr is not None:
            result['service_cidr'] = self.service_cidr
        if self.service_discovery_types is not None:
            result['service_discovery_types'] = self.service_discovery_types
        if self.snat_entry is not None:
            result['snat_entry'] = self.snat_entry
        if self.soc_enabled is not None:
            result['soc_enabled'] = self.soc_enabled
        if self.ssh_flags is not None:
            result['ssh_flags'] = self.ssh_flags
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.timeout_mins is not None:
            result['timeout_mins'] = self.timeout_mins
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.user_ca is not None:
            result['user_ca'] = self.user_ca
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.vpcid is not None:
            result['vpcid'] = self.vpcid
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        if self.worker_auto_renew is not None:
            result['worker_auto_renew'] = self.worker_auto_renew
        if self.worker_auto_renew_period is not None:
            result['worker_auto_renew_period'] = self.worker_auto_renew_period
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        if self.worker_instance_charge_type is not None:
            result['worker_instance_charge_type'] = self.worker_instance_charge_type
        if self.worker_instance_types is not None:
            result['worker_instance_types'] = self.worker_instance_types
        if self.worker_period is not None:
            result['worker_period'] = self.worker_period
        if self.worker_period_unit is not None:
            result['worker_period_unit'] = self.worker_period_unit
        if self.worker_system_disk_category is not None:
            result['worker_system_disk_category'] = self.worker_system_disk_category
        if self.worker_system_disk_performance_level is not None:
            result['worker_system_disk_performance_level'] = self.worker_system_disk_performance_level
        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size
        if self.worker_system_disk_snapshot_policy_id is not None:
            result['worker_system_disk_snapshot_policy_id'] = self.worker_system_disk_snapshot_policy_id
        if self.worker_vswitch_ids is not None:
            result['worker_vswitch_ids'] = self.worker_vswitch_ids
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.addons = []
        if m.get('addons') is not None:
            for k in m.get('addons'):
                temp_model = Addon()
                self.addons.append(temp_model.from_map(k))
        if m.get('api_audiences') is not None:
            self.api_audiences = m.get('api_audiences')
        if m.get('cis_enabled') is not None:
            self.cis_enabled = m.get('cis_enabled')
        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')
        if m.get('cluster_domain') is not None:
            self.cluster_domain = m.get('cluster_domain')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('container_cidr') is not None:
            self.container_cidr = m.get('container_cidr')
        if m.get('controlplane_log_components') is not None:
            self.controlplane_log_components = m.get('controlplane_log_components')
        if m.get('controlplane_log_project') is not None:
            self.controlplane_log_project = m.get('controlplane_log_project')
        if m.get('controlplane_log_ttl') is not None:
            self.controlplane_log_ttl = m.get('controlplane_log_ttl')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        if m.get('custom_san') is not None:
            self.custom_san = m.get('custom_san')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('disable_rollback') is not None:
            self.disable_rollback = m.get('disable_rollback')
        if m.get('enable_rrsa') is not None:
            self.enable_rrsa = m.get('enable_rrsa')
        if m.get('encryption_provider_key') is not None:
            self.encryption_provider_key = m.get('encryption_provider_key')
        if m.get('endpoint_public_access') is not None:
            self.endpoint_public_access = m.get('endpoint_public_access')
        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        if m.get('is_enterprise_security_group') is not None:
            self.is_enterprise_security_group = m.get('is_enterprise_security_group')
        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('kubernetes_version') is not None:
            self.kubernetes_version = m.get('kubernetes_version')
        if m.get('load_balancer_spec') is not None:
            self.load_balancer_spec = m.get('load_balancer_spec')
        if m.get('logging_type') is not None:
            self.logging_type = m.get('logging_type')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        if m.get('master_auto_renew') is not None:
            self.master_auto_renew = m.get('master_auto_renew')
        if m.get('master_auto_renew_period') is not None:
            self.master_auto_renew_period = m.get('master_auto_renew_period')
        if m.get('master_count') is not None:
            self.master_count = m.get('master_count')
        if m.get('master_instance_charge_type') is not None:
            self.master_instance_charge_type = m.get('master_instance_charge_type')
        if m.get('master_instance_types') is not None:
            self.master_instance_types = m.get('master_instance_types')
        if m.get('master_period') is not None:
            self.master_period = m.get('master_period')
        if m.get('master_period_unit') is not None:
            self.master_period_unit = m.get('master_period_unit')
        if m.get('master_system_disk_category') is not None:
            self.master_system_disk_category = m.get('master_system_disk_category')
        if m.get('master_system_disk_performance_level') is not None:
            self.master_system_disk_performance_level = m.get('master_system_disk_performance_level')
        if m.get('master_system_disk_size') is not None:
            self.master_system_disk_size = m.get('master_system_disk_size')
        if m.get('master_system_disk_snapshot_policy_id') is not None:
            self.master_system_disk_snapshot_policy_id = m.get('master_system_disk_snapshot_policy_id')
        if m.get('master_vswitch_ids') is not None:
            self.master_vswitch_ids = m.get('master_vswitch_ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nat_gateway') is not None:
            self.nat_gateway = m.get('nat_gateway')
        if m.get('node_cidr_mask') is not None:
            self.node_cidr_mask = m.get('node_cidr_mask')
        if m.get('node_name_mode') is not None:
            self.node_name_mode = m.get('node_name_mode')
        if m.get('node_port_range') is not None:
            self.node_port_range = m.get('node_port_range')
        if m.get('num_of_nodes') is not None:
            self.num_of_nodes = m.get('num_of_nodes')
        if m.get('os_type') is not None:
            self.os_type = m.get('os_type')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('pod_vswitch_ids') is not None:
            self.pod_vswitch_ids = m.get('pod_vswitch_ids')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('proxy_mode') is not None:
            self.proxy_mode = m.get('proxy_mode')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('runtime') is not None:
            temp_model = Runtime()
            self.runtime = temp_model.from_map(m['runtime'])
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('service_account_issuer') is not None:
            self.service_account_issuer = m.get('service_account_issuer')
        if m.get('service_cidr') is not None:
            self.service_cidr = m.get('service_cidr')
        if m.get('service_discovery_types') is not None:
            self.service_discovery_types = m.get('service_discovery_types')
        if m.get('snat_entry') is not None:
            self.snat_entry = m.get('snat_entry')
        if m.get('soc_enabled') is not None:
            self.soc_enabled = m.get('soc_enabled')
        if m.get('ssh_flags') is not None:
            self.ssh_flags = m.get('ssh_flags')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('timeout_mins') is not None:
            self.timeout_mins = m.get('timeout_mins')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('user_ca') is not None:
            self.user_ca = m.get('user_ca')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('vpcid') is not None:
            self.vpcid = m.get('vpcid')
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        if m.get('worker_auto_renew') is not None:
            self.worker_auto_renew = m.get('worker_auto_renew')
        if m.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = m.get('worker_auto_renew_period')
        self.worker_data_disks = []
        if m.get('worker_data_disks') is not None:
            for k in m.get('worker_data_disks'):
                temp_model = CreateClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if m.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = m.get('worker_instance_charge_type')
        if m.get('worker_instance_types') is not None:
            self.worker_instance_types = m.get('worker_instance_types')
        if m.get('worker_period') is not None:
            self.worker_period = m.get('worker_period')
        if m.get('worker_period_unit') is not None:
            self.worker_period_unit = m.get('worker_period_unit')
        if m.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = m.get('worker_system_disk_category')
        if m.get('worker_system_disk_performance_level') is not None:
            self.worker_system_disk_performance_level = m.get('worker_system_disk_performance_level')
        if m.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = m.get('worker_system_disk_size')
        if m.get('worker_system_disk_snapshot_policy_id') is not None:
            self.worker_system_disk_snapshot_policy_id = m.get('worker_system_disk_snapshot_policy_id')
        if m.get('worker_vswitch_ids') is not None:
            self.worker_vswitch_ids = m.get('worker_vswitch_ids')
        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str
        # 任务ID。
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterNodePoolRequestAutoScaling(TeaModel):
    def __init__(self, eip_bandwidth=None, eip_internet_charge_type=None, enable=None, is_bond_eip=None,
                 max_instances=None, min_instances=None, type=None):
        # 带宽峰值。
        self.eip_bandwidth = eip_bandwidth  # type: long
        # EIP实例规格。
        self.eip_internet_charge_type = eip_internet_charge_type  # type: str
        # 是否开启自动伸缩。
        self.enable = enable  # type: bool
        # 是否绑定EIP。
        self.is_bond_eip = is_bond_eip  # type: bool
        # 最大实例数。
        self.max_instances = max_instances  # type: long
        # 最小实例数。
        self.min_instances = min_instances  # type: long
        # 扩容节点类型。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestAutoScaling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_bandwidth is not None:
            result['eip_bandwidth'] = self.eip_bandwidth
        if self.eip_internet_charge_type is not None:
            result['eip_internet_charge_type'] = self.eip_internet_charge_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.is_bond_eip is not None:
            result['is_bond_eip'] = self.is_bond_eip
        if self.max_instances is not None:
            result['max_instances'] = self.max_instances
        if self.min_instances is not None:
            result['min_instances'] = self.min_instances
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eip_bandwidth') is not None:
            self.eip_bandwidth = m.get('eip_bandwidth')
        if m.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = m.get('eip_internet_charge_type')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('is_bond_eip') is not None:
            self.is_bond_eip = m.get('is_bond_eip')
        if m.get('max_instances') is not None:
            self.max_instances = m.get('max_instances')
        if m.get('min_instances') is not None:
            self.min_instances = m.get('min_instances')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateClusterNodePoolRequestInterconnectConfig(TeaModel):
    def __init__(self, bandwidth=None, ccn_id=None, ccn_region_id=None, cen_id=None, improved_period=None):
        # 边缘增强型节点池的网络带宽，单位M。
        self.bandwidth = bandwidth  # type: long
        # 边缘增强型节点池绑定的云连接网实例ID(CCNID)
        self.ccn_id = ccn_id  # type: str
        # 边缘增强型节点池绑定的云连接网实例所属的区域
        self.ccn_region_id = ccn_region_id  # type: str
        # 边缘增强型节点池绑定的云企业网实例ID(CENID)
        self.cen_id = cen_id  # type: str
        # 边缘增强型节点池的购买时长，单位月
        self.improved_period = improved_period  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestInterconnectConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.ccn_id is not None:
            result['ccn_id'] = self.ccn_id
        if self.ccn_region_id is not None:
            result['ccn_region_id'] = self.ccn_region_id
        if self.cen_id is not None:
            result['cen_id'] = self.cen_id
        if self.improved_period is not None:
            result['improved_period'] = self.improved_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('ccn_id') is not None:
            self.ccn_id = m.get('ccn_id')
        if m.get('ccn_region_id') is not None:
            self.ccn_region_id = m.get('ccn_region_id')
        if m.get('cen_id') is not None:
            self.cen_id = m.get('cen_id')
        if m.get('improved_period') is not None:
            self.improved_period = m.get('improved_period')
        return self


class CreateClusterNodePoolRequestKubernetesConfig(TeaModel):
    def __init__(self, cms_enabled=None, cpu_policy=None, labels=None, runtime=None, runtime_version=None,
                 taints=None, user_data=None):
        # 是否开启云监控。
        self.cms_enabled = cms_enabled  # type: bool
        # CPU管理策略。
        self.cpu_policy = cpu_policy  # type: str
        # 节点标签。
        self.labels = labels  # type: list[Tag]
        # 容器运行时。
        self.runtime = runtime  # type: str
        # 容器运行时版本。
        self.runtime_version = runtime_version  # type: str
        # 污点信息。
        self.taints = taints  # type: list[Taint]
        # 节点自定义数据。
        self.user_data = user_data  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestKubernetesConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = Tag()
                self.labels.append(temp_model.from_map(k))
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class CreateClusterNodePoolRequestManagementUpgradeConfig(TeaModel):
    def __init__(self, auto_upgrade=None, max_unavailable=None, surge=None, surge_percentage=None):
        # 是否启用自动升级
        self.auto_upgrade = auto_upgrade  # type: bool
        # 最大不可用节点数量。
        self.max_unavailable = max_unavailable  # type: long
        # 额外节点数量。
        self.surge = surge  # type: long
        # 额外节点比例。和surge二选一。
        self.surge_percentage = surge_percentage  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestManagementUpgradeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade
        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable
        if self.surge is not None:
            result['surge'] = self.surge
        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('max_unavailable') is not None:
            self.max_unavailable = m.get('max_unavailable')
        if m.get('surge') is not None:
            self.surge = m.get('surge')
        if m.get('surge_percentage') is not None:
            self.surge_percentage = m.get('surge_percentage')
        return self


class CreateClusterNodePoolRequestManagement(TeaModel):
    def __init__(self, auto_repair=None, enable=None, upgrade_config=None):
        # 是否启用自动修复。
        self.auto_repair = auto_repair  # type: bool
        # 是否启用托管节点池。
        self.enable = enable  # type: bool
        # 自动升级配置。
        self.upgrade_config = upgrade_config  # type: CreateClusterNodePoolRequestManagementUpgradeConfig

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestManagement, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.enable is not None:
            result['enable'] = self.enable
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = CreateClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class CreateClusterNodePoolRequestNodepoolInfo(TeaModel):
    def __init__(self, name=None, resource_group_id=None, type=None):
        # 节点池名称
        self.name = name  # type: str
        # 资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 节点池类型，对于边缘节点池来说，类型为"edge"
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestNodepoolInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateClusterNodePoolRequestScalingGroupSpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        # 抢占实例规格。
        self.instance_type = instance_type  # type: str
        # 抢占实例单价。
        self.price_limit = price_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestScalingGroupSpotPriceLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.price_limit is not None:
            result['price_limit'] = self.price_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')
        if m.get('price_limit') is not None:
            self.price_limit = m.get('price_limit')
        return self


class CreateClusterNodePoolRequestScalingGroupTags(TeaModel):
    def __init__(self, key=None, value=None):
        # key
        self.key = key  # type: str
        # value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestScalingGroupTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateClusterNodePoolRequestScalingGroup(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, compensate_with_on_demand=None, data_disks=None,
                 image_id=None, image_type=None, instance_charge_type=None, instance_types=None, internet_charge_type=None,
                 internet_max_bandwidth_out=None, key_pair=None, login_password=None, multi_az_policy=None, on_demand_base_capacity=None,
                 on_demand_percentage_above_base_capacity=None, period=None, period_unit=None, platform=None, rds_instances=None, scaling_policy=None,
                 security_group_id=None, security_group_ids=None, spot_instance_pools=None, spot_instance_remedy=None,
                 spot_price_limit=None, spot_strategy=None, system_disk_category=None, system_disk_performance_level=None,
                 system_disk_size=None, tags=None, vswitch_ids=None):
        # 节点是否开启自动续费
        self.auto_renew = auto_renew  # type: bool
        # 节点自动续费周期
        self.auto_renew_period = auto_renew_period  # type: long
        # 当MultiAZPolicy取值为COST_OPTIMIZED时，如果因价格、库存等原因无法创建足够的抢占式实例，是否允许自动尝试创建按量实例满足ECS实例数量要求。取值范围：true：允许。false：不允许。默认值：true
        self.compensate_with_on_demand = compensate_with_on_demand  # type: bool
        # 数据盘配置。
        self.data_disks = data_disks  # type: list[DataDisk]
        # 自定义镜像。
        self.image_id = image_id  # type: str
        # 操作系统镜像类型，和platform二选一
        self.image_type = image_type  # type: str
        # 节点付费类型
        self.instance_charge_type = instance_charge_type  # type: str
        # 实例规格。
        self.instance_types = instance_types  # type: list[str]
        # 节点公网IP网络计费类型
        self.internet_charge_type = internet_charge_type  # type: str
        # 节点公网IP出带宽最大值，单位为Mbps（Mega bit per second），取值范围：1~100
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: long
        # 密钥对名称，和login_password二选一。
        self.key_pair = key_pair  # type: str
        # SSH登录密码。
        self.login_password = login_password  # type: str
        # 多可用区伸缩组ECS实例扩缩容策略
        self.multi_az_policy = multi_az_policy  # type: str
        # 伸缩组所需要按量实例个数的最小值，取值范围：0~1000。当按量实例个数少于该值时，将优先创建按量实例。
        self.on_demand_base_capacity = on_demand_base_capacity  # type: long
        # 伸缩组满足最小按量实例数（OnDemandBaseCapacity）要求后，超出的实例中按量实例应占的比例，取值范围：0～100。
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity  # type: long
        # 节点包年包月时长。
        self.period = period  # type: long
        # 节点包年包月周期。
        self.period_unit = period_unit  # type: str
        # 操作系统发行版，和image_type二选一
        self.platform = platform  # type: str
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: list[str]
        # 自动伸缩。
        self.scaling_policy = scaling_policy  # type: str
        # 安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 多安全组ID
        self.security_group_ids = security_group_ids  # type: list[str]
        # 指定可用实例规格的个数，伸缩组将按成本最低的多个规格均衡创建抢占式实例。取值范围：1~10。
        self.spot_instance_pools = spot_instance_pools  # type: long
        # 是否开启补齐抢占式实例。开启后，当收到抢占式实例将被回收的系统消息时，伸缩组将尝试创建新的实例，替换掉将被回收的抢占式实例。
        self.spot_instance_remedy = spot_instance_remedy  # type: bool
        # 抢占实例价格上限配置。
        self.spot_price_limit = spot_price_limit  # type: list[CreateClusterNodePoolRequestScalingGroupSpotPriceLimit]
        # 抢占式实例类型
        self.spot_strategy = spot_strategy  # type: str
        # 节点系统盘类型。
        self.system_disk_category = system_disk_category  # type: str
        # 节点系统盘磁盘性能，只针对ESSD磁盘生效
        self.system_disk_performance_level = system_disk_performance_level  # type: str
        # 节点系统盘大小。
        self.system_disk_size = system_disk_size  # type: long
        # ECS标签
        self.tags = tags  # type: list[CreateClusterNodePoolRequestScalingGroupTags]
        # 虚拟交换机ID。
        self.vswitch_ids = vswitch_ids  # type: list[str]

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestScalingGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.image_type is not None:
            result['image_type'] = self.image_type
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_types is not None:
            result['instance_types'] = self.instance_types
        if self.internet_charge_type is not None:
            result['internet_charge_type'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['internet_max_bandwidth_out'] = self.internet_max_bandwidth_out
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.multi_az_policy is not None:
            result['multi_az_policy'] = self.multi_az_policy
        if self.on_demand_base_capacity is not None:
            result['on_demand_base_capacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['on_demand_percentage_above_base_capacity'] = self.on_demand_percentage_above_base_capacity
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.platform is not None:
            result['platform'] = self.platform
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.security_group_ids is not None:
            result['security_group_ids'] = self.security_group_ids
        if self.spot_instance_pools is not None:
            result['spot_instance_pools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['spot_instance_remedy'] = self.spot_instance_remedy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_renew') is not None:
            self.auto_renew = m.get('auto_renew')
        if m.get('auto_renew_period') is not None:
            self.auto_renew_period = m.get('auto_renew_period')
        if m.get('compensate_with_on_demand') is not None:
            self.compensate_with_on_demand = m.get('compensate_with_on_demand')
        self.data_disks = []
        if m.get('data_disks') is not None:
            for k in m.get('data_disks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
        if m.get('instance_types') is not None:
            self.instance_types = m.get('instance_types')
        if m.get('internet_charge_type') is not None:
            self.internet_charge_type = m.get('internet_charge_type')
        if m.get('internet_max_bandwidth_out') is not None:
            self.internet_max_bandwidth_out = m.get('internet_max_bandwidth_out')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        if m.get('multi_az_policy') is not None:
            self.multi_az_policy = m.get('multi_az_policy')
        if m.get('on_demand_base_capacity') is not None:
            self.on_demand_base_capacity = m.get('on_demand_base_capacity')
        if m.get('on_demand_percentage_above_base_capacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('on_demand_percentage_above_base_capacity')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('security_group_ids') is not None:
            self.security_group_ids = m.get('security_group_ids')
        if m.get('spot_instance_pools') is not None:
            self.spot_instance_pools = m.get('spot_instance_pools')
        if m.get('spot_instance_remedy') is not None:
            self.spot_instance_remedy = m.get('spot_instance_remedy')
        self.spot_price_limit = []
        if m.get('spot_price_limit') is not None:
            for k in m.get('spot_price_limit'):
                temp_model = CreateClusterNodePoolRequestScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')
        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')
        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = CreateClusterNodePoolRequestScalingGroupTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class CreateClusterNodePoolRequestTeeConfig(TeaModel):
    def __init__(self, tee_enable=None):
        # 是否为加密计算节点池。
        self.tee_enable = tee_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterNodePoolRequestTeeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')
        return self


class CreateClusterNodePoolRequest(TeaModel):
    def __init__(self, auto_scaling=None, count=None, interconnect_config=None, interconnect_mode=None,
                 kubernetes_config=None, management=None, max_nodes=None, nodepool_info=None, scaling_group=None, tee_config=None):
        # 自动伸缩节点池配置。
        self.auto_scaling = auto_scaling  # type: CreateClusterNodePoolRequestAutoScaling
        # 节点数量。
        self.count = count  # type: long
        # 边缘节点池网络相关的配置。该值只对edge类型的节点池有意义
        self.interconnect_config = interconnect_config  # type: CreateClusterNodePoolRequestInterconnectConfig
        # 边缘节点池的网络类型。basic：基础型；improved：增强型。该值只对edge类型的节点池有意义。
        self.interconnect_mode = interconnect_mode  # type: str
        # 集群配置
        self.kubernetes_config = kubernetes_config  # type: CreateClusterNodePoolRequestKubernetesConfig
        # 托管节点池配置。
        self.management = management  # type: CreateClusterNodePoolRequestManagement
        # 边缘节点池允许容纳的最大节点数量. 节点池内可以容纳的最大节点数量，该参数大于等于0。0表示无额外限制(仅受限于集群整体可以容纳的节点数，节点池本身无额外限制)。边缘节点池该参数值往往大于0；ess类型节点池和默认的edge类型节点池该参数值为0
        self.max_nodes = max_nodes  # type: long
        # 节点池配置
        self.nodepool_info = nodepool_info  # type: CreateClusterNodePoolRequestNodepoolInfo
        # 伸缩组配置
        self.scaling_group = scaling_group  # type: CreateClusterNodePoolRequestScalingGroup
        # 加密计算节点池配置。
        self.tee_config = tee_config  # type: CreateClusterNodePoolRequestTeeConfig

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.interconnect_config:
            self.interconnect_config.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.management:
            self.management.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.tee_config:
            self.tee_config.validate()

    def to_map(self):
        _map = super(CreateClusterNodePoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
        if self.count is not None:
            result['count'] = self.count
        if self.interconnect_config is not None:
            result['interconnect_config'] = self.interconnect_config.to_map()
        if self.interconnect_mode is not None:
            result['interconnect_mode'] = self.interconnect_mode
        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()
        if self.management is not None:
            result['management'] = self.management.to_map()
        if self.max_nodes is not None:
            result['max_nodes'] = self.max_nodes
        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()
        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()
        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_scaling') is not None:
            temp_model = CreateClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('interconnect_config') is not None:
            temp_model = CreateClusterNodePoolRequestInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m['interconnect_config'])
        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')
        if m.get('kubernetes_config') is not None:
            temp_model = CreateClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = CreateClusterNodePoolRequestManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')
        if m.get('nodepool_info') is not None:
            temp_model = CreateClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = CreateClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('tee_config') is not None:
            temp_model = CreateClusterNodePoolRequestTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
        return self


class CreateClusterNodePoolResponseBody(TeaModel):
    def __init__(self, nodepool_id=None):
        # 节点池ID
        self.nodepool_id = nodepool_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterNodePoolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        return self


class CreateClusterNodePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateClusterNodePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterNodePoolResponse, self).to_map()
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
            temp_model = CreateClusterNodePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEdgeMachineRequest(TeaModel):
    def __init__(self, hostname=None, model=None, sn=None):
        # hostname
        self.hostname = hostname  # type: str
        # model
        self.model = model  # type: str
        # sn
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEdgeMachineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.model is not None:
            result['model'] = self.model
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class CreateEdgeMachineResponseBody(TeaModel):
    def __init__(self, edge_machine_id=None, request_id=None):
        # edge machine id
        self.edge_machine_id = edge_machine_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEdgeMachineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_machine_id is not None:
            result['edge_machine_id'] = self.edge_machine_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('edge_machine_id') is not None:
            self.edge_machine_id = m.get('edge_machine_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class CreateEdgeMachineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEdgeMachineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEdgeMachineResponse, self).to_map()
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
            temp_model = CreateEdgeMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKubernetesTriggerRequest(TeaModel):
    def __init__(self, action=None, cluster_id=None, project_id=None, type=None):
        # 触发器行为
        self.action = action  # type: str
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 项目名称。
        self.project_id = project_id  # type: str
        # 触发器类型。默认deployment。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKubernetesTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateKubernetesTriggerResponseBody(TeaModel):
    def __init__(self, action=None, cluster_id=None, id=None, project_id=None, type=None):
        # 触发器行为。
        self.action = action  # type: str
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 触发器ID。
        self.id = id  # type: str
        # 触发器项目名称。
        self.project_id = project_id  # type: str
        # 触发器类型。默认值为 deployment 。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKubernetesTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.id is not None:
            result['id'] = self.id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateKubernetesTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateKubernetesTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateKubernetesTriggerResponse, self).to_map()
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
            temp_model = CreateKubernetesTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, description=None, name=None, tags=None, template=None, template_type=None):
        # 模板描述。
        self.description = description  # type: str
        # 模板名称。
        self.name = name  # type: str
        # 模板标签。
        self.tags = tags  # type: str
        # YAML格式的模板内容。
        self.template = template  # type: str
        # 模板类型。默认值：kubernetes
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template is not None:
            result['template'] = self.template
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, template_id=None):
        # 模板ID。
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateResponse, self).to_map()
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(self, action=None, cluster_id=None, project_id=None, type=None):
        # 触发器行为
        self.action = action  # type: str
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 项目名称。
        self.project_id = project_id  # type: str
        # 触发器类型。默认deployment。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateTriggerResponseBody(TeaModel):
    def __init__(self, action=None, cluster_id=None, id=None, project_id=None, type=None):
        # 触发器行为。
        self.action = action  # type: str
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 触发器ID。
        self.id = id  # type: str
        # 触发器项目名称。
        self.project_id = project_id  # type: str
        # 触发器类型。默认值为 deployment 。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.id is not None:
            result['id'] = self.id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTriggerResponse, self).to_map()
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
            temp_model = CreateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, keep_slb=None, retain_all_resources=None, retain_resources=None):
        # 是否保留SLB。  true：保留 false：不保留 默认值：false。
        self.keep_slb = keep_slb  # type: bool
        # 是否保留所有资源,如果设置了该值，将会忽略retain_resources。  true：保留 false：不保留 默认值：fase。
        self.retain_all_resources = retain_all_resources  # type: bool
        # 要保留的资源列表。
        self.retain_resources = retain_resources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_slb is not None:
            result['keep_slb'] = self.keep_slb
        if self.retain_all_resources is not None:
            result['retain_all_resources'] = self.retain_all_resources
        if self.retain_resources is not None:
            result['retain_resources'] = self.retain_resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keep_slb') is not None:
            self.keep_slb = m.get('keep_slb')
        if m.get('retain_all_resources') is not None:
            self.retain_all_resources = m.get('retain_all_resources')
        if m.get('retain_resources') is not None:
            self.retain_resources = m.get('retain_resources')
        return self


class DeleteClusterShrinkRequest(TeaModel):
    def __init__(self, keep_slb=None, retain_all_resources=None, retain_resources_shrink=None):
        # 是否保留SLB。  true：保留 false：不保留 默认值：false。
        self.keep_slb = keep_slb  # type: bool
        # 是否保留所有资源,如果设置了该值，将会忽略retain_resources。  true：保留 false：不保留 默认值：fase。
        self.retain_all_resources = retain_all_resources  # type: bool
        # 要保留的资源列表。
        self.retain_resources_shrink = retain_resources_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_slb is not None:
            result['keep_slb'] = self.keep_slb
        if self.retain_all_resources is not None:
            result['retain_all_resources'] = self.retain_all_resources
        if self.retain_resources_shrink is not None:
            result['retain_resources'] = self.retain_resources_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keep_slb') is not None:
            self.keep_slb = m.get('keep_slb')
        if m.get('retain_all_resources') is not None:
            self.retain_all_resources = m.get('retain_all_resources')
        if m.get('retain_resources') is not None:
            self.retain_resources_shrink = m.get('retain_resources')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteClusterNodepoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterNodepoolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class DeleteClusterNodepoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteClusterNodepoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClusterNodepoolResponse, self).to_map()
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
            temp_model = DeleteClusterNodepoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterNodesRequest(TeaModel):
    def __init__(self, drain_node=None, nodes=None, release_node=None):
        # 是否自动排空节点上的Pod。
        self.drain_node = drain_node  # type: bool
        # 移除节点列表。
        self.nodes = nodes  # type: list[str]
        # 是否同时释放 ECS
        self.release_node = release_node  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drain_node is not None:
            result['drain_node'] = self.drain_node
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.release_node is not None:
            result['release_node'] = self.release_node
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')
        return self


class DeleteClusterNodesResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID
        self.cluster_id = cluster_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 任务ID
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class DeleteClusterNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteClusterNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClusterNodesResponse, self).to_map()
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
            temp_model = DeleteClusterNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEdgeMachineRequest(TeaModel):
    def __init__(self, force=None):
        # whether force delete
        self.force = force  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEdgeMachineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class DeleteEdgeMachineResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteEdgeMachineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteKubernetesTriggerResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteKubernetesTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeletePolicyInstanceRequest(TeaModel):
    def __init__(self, instance_name=None):
        # 策略规则实例id
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        return self


class DeletePolicyInstanceResponseBody(TeaModel):
    def __init__(self, instances=None):
        # 策略实例列表
        self.instances = instances  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self


class DeletePolicyInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeletePolicyInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyInstanceResponse, self).to_map()
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
            temp_model = DeletePolicyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteTriggerResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(DeleteTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeployPolicyInstanceRequest(TeaModel):
    def __init__(self, action=None, namespace=None, parameters=None):
        # 规则治理动作
        self.action = action  # type: str
        # 策略实例实施范围
        self.namespace = namespace  # type: str
        # 当前规则实例的配置参数
        self.parameters = parameters  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployPolicyInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class DeployPolicyInstanceResponseBody(TeaModel):
    def __init__(self, instances=None):
        # 策略实例列表
        self.instances = instances  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployPolicyInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self


class DeployPolicyInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeployPolicyInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployPolicyInstanceResponse, self).to_map()
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
            temp_model = DeployPolicyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescirbeWorkflowResponseBody(TeaModel):
    def __init__(self, create_time=None, duration=None, finish_time=None, input_data_size=None, job_name=None,
                 job_namespace=None, output_data_size=None, status=None, total_bases=None, total_reads=None, user_input_data=None):
        # 工作流创建时间。
        self.create_time = create_time  # type: str
        # 工作流经过时长。
        self.duration = duration  # type: str
        # 任务结束时间。
        self.finish_time = finish_time  # type: str
        # 输入数据大小。
        self.input_data_size = input_data_size  # type: str
        # 工作流名称。
        self.job_name = job_name  # type: str
        # 工作流所在命名空间。
        self.job_namespace = job_namespace  # type: str
        # 输出数据大小。
        self.output_data_size = output_data_size  # type: str
        # 工作流当前状态。
        self.status = status  # type: str
        # 碱基对个数。
        self.total_bases = total_bases  # type: str
        # Reads个数。
        self.total_reads = total_reads  # type: str
        # 用户输入参数。
        self.user_input_data = user_input_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescirbeWorkflowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['create_time'] = self.create_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.finish_time is not None:
            result['finish_time'] = self.finish_time
        if self.input_data_size is not None:
            result['input_data_size'] = self.input_data_size
        if self.job_name is not None:
            result['job_name'] = self.job_name
        if self.job_namespace is not None:
            result['job_namespace'] = self.job_namespace
        if self.output_data_size is not None:
            result['output_data_size'] = self.output_data_size
        if self.status is not None:
            result['status'] = self.status
        if self.total_bases is not None:
            result['total_bases'] = self.total_bases
        if self.total_reads is not None:
            result['total_reads'] = self.total_reads
        if self.user_input_data is not None:
            result['user_input_data'] = self.user_input_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('create_time') is not None:
            self.create_time = m.get('create_time')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('finish_time') is not None:
            self.finish_time = m.get('finish_time')
        if m.get('input_data_size') is not None:
            self.input_data_size = m.get('input_data_size')
        if m.get('job_name') is not None:
            self.job_name = m.get('job_name')
        if m.get('job_namespace') is not None:
            self.job_namespace = m.get('job_namespace')
        if m.get('output_data_size') is not None:
            self.output_data_size = m.get('output_data_size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_bases') is not None:
            self.total_bases = m.get('total_bases')
        if m.get('total_reads') is not None:
            self.total_reads = m.get('total_reads')
        if m.get('user_input_data') is not None:
            self.user_input_data = m.get('user_input_data')
        return self


class DescirbeWorkflowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescirbeWorkflowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescirbeWorkflowResponse, self).to_map()
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
            temp_model = DescirbeWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddonsRequest(TeaModel):
    def __init__(self, cluster_type=None, region=None):
        # 集群类型。  - Kubernetes: 专有版集群。 - ManagedKubernetes：托管版集群。 - Ask：Serverless 集群。 - ExternalKubernetes：注册到ACK的外部集群。
        self.cluster_type = cluster_type  # type: str
        # 地域ID。
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAddonsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class DescribeAddonsResponseBodyComponentGroupsItems(TeaModel):
    def __init__(self, name=None):
        # 组件名称。
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAddonsResponseBodyComponentGroupsItems, self).to_map()
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


class DescribeAddonsResponseBodyComponentGroups(TeaModel):
    def __init__(self, group_name=None, items=None):
        # 组件组名称。
        self.group_name = group_name  # type: str
        # 组件列表
        self.items = items  # type: list[DescribeAddonsResponseBodyComponentGroupsItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAddonsResponseBodyComponentGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['group_name'] = self.group_name
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeAddonsResponseBodyComponentGroupsItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeAddonsResponseBody(TeaModel):
    def __init__(self, component_groups=None, standard_components=None):
        # 组件分组信息，例如：存储类组件，网络组件等。
        self.component_groups = component_groups  # type: list[DescribeAddonsResponseBodyComponentGroups]
        # 标准组件信息，包含各个组件的描述信息。
        self.standard_components = standard_components  # type: dict[str, StandardComponentsValue]

    def validate(self):
        if self.component_groups:
            for k in self.component_groups:
                if k:
                    k.validate()
        if self.standard_components:
            for v in self.standard_components.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(DescribeAddonsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentGroups'] = []
        if self.component_groups is not None:
            for k in self.component_groups:
                result['ComponentGroups'].append(k.to_map() if k else None)
        result['StandardComponents'] = {}
        if self.standard_components is not None:
            for k, v in self.standard_components.items():
                result['StandardComponents'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.component_groups = []
        if m.get('ComponentGroups') is not None:
            for k in m.get('ComponentGroups'):
                temp_model = DescribeAddonsResponseBodyComponentGroups()
                self.component_groups.append(temp_model.from_map(k))
        self.standard_components = {}
        if m.get('StandardComponents') is not None:
            for k, v in m.get('StandardComponents').items():
                temp_model = StandardComponentsValue()
                self.standard_components[k] = temp_model.from_map(v)
        return self


class DescribeAddonsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAddonsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAddonsResponse, self).to_map()
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
            temp_model = DescribeAddonsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterAddonMetadataResponseBody(TeaModel):
    def __init__(self, config_schema=None, name=None, version=None):
        # 组件参数Schema
        self.config_schema = config_schema  # type: str
        # 组件名称
        self.name = name  # type: str
        # 组件版本
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterAddonMetadataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_schema is not None:
            result['config_schema'] = self.config_schema
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config_schema') is not None:
            self.config_schema = m.get('config_schema')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeClusterAddonMetadataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterAddonMetadataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterAddonMetadataResponse, self).to_map()
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
            temp_model = DescribeClusterAddonMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterAddonUpgradeStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(DescribeClusterAddonUpgradeStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterAddonsUpgradeStatusRequest(TeaModel):
    def __init__(self, component_ids=None):
        # 组件名称列表。
        self.component_ids = component_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterAddonsUpgradeStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_ids is not None:
            result['componentIds'] = self.component_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentIds') is not None:
            self.component_ids = m.get('componentIds')
        return self


class DescribeClusterAddonsUpgradeStatusShrinkRequest(TeaModel):
    def __init__(self, component_ids_shrink=None):
        # 组件名称列表。
        self.component_ids_shrink = component_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterAddonsUpgradeStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_ids_shrink is not None:
            result['componentIds'] = self.component_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentIds') is not None:
            self.component_ids_shrink = m.get('componentIds')
        return self


class DescribeClusterAddonsUpgradeStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(DescribeClusterAddonsUpgradeStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterAddonsVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(DescribeClusterAddonsVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterAttachScriptsRequest(TeaModel):
    def __init__(self, arch=None, format_disk=None, keep_instance_name=None, nodepool_id=None, options=None,
                 rds_instances=None):
        # 节点CPU架构,支持amd64、arm、arm64。边缘托管集群专有字段。
        self.arch = arch  # type: str
        # 数据盘挂载
        self.format_disk = format_disk  # type: bool
        # 保留实例名称
        self.keep_instance_name = keep_instance_name  # type: bool
        # 节点池ID。将节点加入指定节点池。
        self.nodepool_id = nodepool_id  # type: str
        # 边缘托管版集群节点的接入配置。
        self.options = options  # type: str
        # RDS白名单
        self.rds_instances = rds_instances  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterAttachScriptsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arch is not None:
            result['arch'] = self.arch
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk
        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.options is not None:
            result['options'] = self.options
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arch') is not None:
            self.arch = m.get('arch')
        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')
        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        return self


class DescribeClusterAttachScriptsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(DescribeClusterAttachScriptsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterDetailResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, cluster_type=None, created=None, current_version=None,
                 deletion_protection=None, docker_version=None, external_loadbalancer_id=None, init_version=None,
                 maintenance_window=None, master_url=None, meta_data=None, name=None, network_mode=None, next_version=None,
                 private_zone=None, profile=None, region_id=None, resource_group_id=None, security_group_id=None, size=None,
                 state=None, subnet_cidr=None, tags=None, updated=None, vpc_id=None, vswitch_id=None,
                 worker_ram_role_name=None, zone_id=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 托管版集群类型，面向托管集群。  ack.pro.small：专业托管集群。 ack.standard ：标准托管集群。
        self.cluster_spec = cluster_spec  # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群创建时间。
        self.created = created  # type: str
        # 集群当前版本。
        self.current_version = current_version  # type: str
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 集群内Docker版本。
        self.docker_version = docker_version  # type: str
        # 集群Ingress LB实例ID。
        self.external_loadbalancer_id = external_loadbalancer_id  # type: str
        # 集群初始化版本。
        self.init_version = init_version  # type: str
        self.maintenance_window = maintenance_window  # type: MaintenanceWindow
        # 集群访问地址。
        self.master_url = master_url  # type: str
        # 集群元数据。
        self.meta_data = meta_data  # type: str
        # 集群名称。
        self.name = name  # type: str
        # 集群采用的网络类型，例如：VPC网络。
        self.network_mode = network_mode  # type: str
        # 集群可升级版本。
        self.next_version = next_version  # type: str
        # 集群是否启用用PrivateZone。  true：启用 false：不启用 默认值：false。
        self.private_zone = private_zone  # type: bool
        # 面向场景时的集群类型。  Default：非边缘场景集群。 Edge：边缘场景集群。
        self.profile = profile  # type: str
        # 集群所在地域ID。
        self.region_id = region_id  # type: str
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 集群安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 集群节点数量。
        self.size = size  # type: long
        # 集群运行状态。
        self.state = state  # type: str
        # Pod网络地址段，必须是有效的私有网段，即以下网段及其子网：10.0.0.0/8，172.16-31.0.0/12-16，192.168.0.0/16。不能与 VPC 及VPC 内已有 Kubernetes 集群使用的网段重复，创建成功后不能修改。  有关集群网络规划，请参见：[VPC下 Kubernetes 的网络地址段规划](https://help.aliyun.com/document_detail/～～86500～～)。
        self.subnet_cidr = subnet_cidr  # type: str
        # 集群标签。
        self.tags = tags  # type: list[Tag]
        # 集群更新时间。
        self.updated = updated  # type: str
        # 集群使用的VPC ID。
        self.vpc_id = vpc_id  # type: str
        # 集群节点使用的虚拟交换机列表。
        self.vswitch_id = vswitch_id  # type: str
        # Worker节点RAM角色名称。
        self.worker_ram_role_name = worker_ram_role_name  # type: str
        # 集群所在地域内的可用区ID。
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.docker_version is not None:
            result['docker_version'] = self.docker_version
        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id
        if self.init_version is not None:
            result['init_version'] = self.init_version
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        if self.name is not None:
            result['name'] = self.name
        if self.network_mode is not None:
            result['network_mode'] = self.network_mode
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.private_zone is not None:
            result['private_zone'] = self.private_zone
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.size is not None:
            result['size'] = self.size
        if self.state is not None:
            result['state'] = self.state
        if self.subnet_cidr is not None:
            result['subnet_cidr'] = self.subnet_cidr
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated is not None:
            result['updated'] = self.updated
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id
        if self.vswitch_id is not None:
            result['vswitch_id'] = self.vswitch_id
        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('docker_version') is not None:
            self.docker_version = m.get('docker_version')
        if m.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = m.get('external_loadbalancer_id')
        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')
        if m.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m['maintenance_window'])
        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')
        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('network_mode') is not None:
            self.network_mode = m.get('network_mode')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('private_zone') is not None:
            self.private_zone = m.get('private_zone')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('subnet_cidr') is not None:
            self.subnet_cidr = m.get('subnet_cidr')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')
        if m.get('vswitch_id') is not None:
            self.vswitch_id = m.get('vswitch_id')
        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')
        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')
        return self


class DescribeClusterDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterDetailResponse, self).to_map()
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
            temp_model = DescribeClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterLogsResponseBody(TeaModel):
    def __init__(self, id=None, cluster_id=None, cluster_log=None, log_level=None, created=None, updated=None):
        # 日志ID。
        self.id = id  # type: long
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 日志内容。
        self.cluster_log = cluster_log  # type: str
        # 日志等级。
        self.log_level = log_level  # type: str
        # 日志创建时间。
        self.created = created  # type: str
        # 日志更新时间。
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['ID'] = self.id
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_log is not None:
            result['cluster_log'] = self.cluster_log
        if self.log_level is not None:
            result['log_level'] = self.log_level
        if self.created is not None:
            result['created'] = self.created
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_log') is not None:
            self.cluster_log = m.get('cluster_log')
        if m.get('log_level') is not None:
            self.log_level = m.get('log_level')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeClusterLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[DescribeClusterLogsResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeClusterLogsResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeClusterNamespacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[str]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(DescribeClusterNamespacesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterNodePoolDetailResponseBodyAutoScaling(TeaModel):
    def __init__(self, eip_bandwidth=None, eip_internet_charge_type=None, enable=None, is_bond_eip=None,
                 max_instances=None, min_instances=None, type=None):
        # EIP带宽峰值。
        self.eip_bandwidth = eip_bandwidth  # type: long
        # EIP实例付费类型。
        self.eip_internet_charge_type = eip_internet_charge_type  # type: str
        # 是否启用自动伸缩。
        self.enable = enable  # type: bool
        # 是否绑定EIP。
        self.is_bond_eip = is_bond_eip  # type: bool
        # 最大实例数。
        self.max_instances = max_instances  # type: long
        # 最小实例数。
        self.min_instances = min_instances  # type: long
        # 扩容组类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyAutoScaling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_bandwidth is not None:
            result['eip_bandwidth'] = self.eip_bandwidth
        if self.eip_internet_charge_type is not None:
            result['eip_internet_charge_type'] = self.eip_internet_charge_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.is_bond_eip is not None:
            result['is_bond_eip'] = self.is_bond_eip
        if self.max_instances is not None:
            result['max_instances'] = self.max_instances
        if self.min_instances is not None:
            result['min_instances'] = self.min_instances
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eip_bandwidth') is not None:
            self.eip_bandwidth = m.get('eip_bandwidth')
        if m.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = m.get('eip_internet_charge_type')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('is_bond_eip') is not None:
            self.is_bond_eip = m.get('is_bond_eip')
        if m.get('max_instances') is not None:
            self.max_instances = m.get('max_instances')
        if m.get('min_instances') is not None:
            self.min_instances = m.get('min_instances')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeClusterNodePoolDetailResponseBodyInterconnectConfig(TeaModel):
    def __init__(self, bandwidth=None, ccn_id=None, ccn_region_id=None, cen_id=None, improved_period=None):
        # 边缘增强型节点池的网络带宽，单位M
        self.bandwidth = bandwidth  # type: long
        # 边缘增强型节点池绑定的云连接网实例ID(CCNID)
        self.ccn_id = ccn_id  # type: str
        # 边缘增强型节点池绑定的云连接网实例所属的区域
        self.ccn_region_id = ccn_region_id  # type: str
        # 边缘增强型节点池绑定的云企业网实例ID(CENID)
        self.cen_id = cen_id  # type: str
        # 边缘增强型节点池的购买时长，单位月
        self.improved_period = improved_period  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyInterconnectConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.ccn_id is not None:
            result['ccn_id'] = self.ccn_id
        if self.ccn_region_id is not None:
            result['ccn_region_id'] = self.ccn_region_id
        if self.cen_id is not None:
            result['cen_id'] = self.cen_id
        if self.improved_period is not None:
            result['improved_period'] = self.improved_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('ccn_id') is not None:
            self.ccn_id = m.get('ccn_id')
        if m.get('ccn_region_id') is not None:
            self.ccn_region_id = m.get('ccn_region_id')
        if m.get('cen_id') is not None:
            self.cen_id = m.get('cen_id')
        if m.get('improved_period') is not None:
            self.improved_period = m.get('improved_period')
        return self


class DescribeClusterNodePoolDetailResponseBodyKubernetesConfig(TeaModel):
    def __init__(self, cms_enabled=None, cpu_policy=None, labels=None, runtime=None, runtime_version=None,
                 taints=None, user_data=None):
        # 是否开启云监控
        self.cms_enabled = cms_enabled  # type: bool
        # CPU管理策略
        self.cpu_policy = cpu_policy  # type: str
        # 节点标签。
        self.labels = labels  # type: list[Tag]
        # 容器运行时
        self.runtime = runtime  # type: str
        # 容器运行时版本。
        self.runtime_version = runtime_version  # type: str
        # 污点配置。
        self.taints = taints  # type: list[Taint]
        # 节点自定义数据
        self.user_data = user_data  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyKubernetesConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = Tag()
                self.labels.append(temp_model.from_map(k))
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig(TeaModel):
    def __init__(self, auto_upgrade=None, max_unavailable=None, surge=None, surge_percentage=None):
        # 是否启用自动升级，自修复。
        self.auto_upgrade = auto_upgrade  # type: bool
        # 最大不可用节点数量。
        self.max_unavailable = max_unavailable  # type: long
        # 额外节点数量。
        self.surge = surge  # type: long
        # 额外节点比例， 和surge 二选一。
        self.surge_percentage = surge_percentage  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade
        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable
        if self.surge is not None:
            result['surge'] = self.surge
        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('max_unavailable') is not None:
            self.max_unavailable = m.get('max_unavailable')
        if m.get('surge') is not None:
            self.surge = m.get('surge')
        if m.get('surge_percentage') is not None:
            self.surge_percentage = m.get('surge_percentage')
        return self


class DescribeClusterNodePoolDetailResponseBodyManagement(TeaModel):
    def __init__(self, auto_repair=None, enable=None, upgrade_config=None):
        # 自动修复。
        self.auto_repair = auto_repair  # type: bool
        # 是否开启托管版节点池。
        self.enable = enable  # type: bool
        # 自动升级配置。
        self.upgrade_config = upgrade_config  # type: DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyManagement, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.enable is not None:
            result['enable'] = self.enable
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class DescribeClusterNodePoolDetailResponseBodyNodepoolInfo(TeaModel):
    def __init__(self, created=None, is_default=None, name=None, nodepool_id=None, region_id=None,
                 resource_group_id=None, type=None, updated=None):
        # 节点池创建时间。
        self.created = created  # type: str
        # 是否为默认节点池。
        self.is_default = is_default  # type: bool
        # 节点池名称。
        self.name = name  # type: str
        # 节点池ID。
        self.nodepool_id = nodepool_id  # type: str
        # 节点池所属地域ID。
        self.region_id = region_id  # type: str
        # 节点池所属资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 节点池类型。
        self.type = type  # type: str
        # 节点池更新时间。
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyNodepoolInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.is_default is not None:
            result['is_default'] = self.is_default
        if self.name is not None:
            result['name'] = self.name
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('is_default') is not None:
            self.is_default = m.get('is_default')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        # 抢占式实例规格。
        self.instance_type = instance_type  # type: str
        # 单台实例上限价格，单位：元/小时。
        self.price_limit = price_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.price_limit is not None:
            result['price_limit'] = self.price_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')
        if m.get('price_limit') is not None:
            self.price_limit = m.get('price_limit')
        return self


class DescribeClusterNodePoolDetailResponseBodyScalingGroup(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, compensate_with_on_demand=None, data_disks=None,
                 image_id=None, instance_charge_type=None, instance_types=None, internet_charge_type=None,
                 internet_max_bandwidth_out=None, key_pair=None, login_password=None, multi_az_policy=None, on_demand_base_capacity=None,
                 on_demand_percentage_above_base_capacity=None, period=None, period_unit=None, platform=None, ram_policy=None, rds_instances=None,
                 scaling_group_id=None, scaling_policy=None, security_group_id=None, security_group_ids=None,
                 spot_instance_pools=None, spot_instance_remedy=None, spot_price_limit=None, spot_strategy=None,
                 system_disk_category=None, system_disk_performance_level=None, system_disk_size=None, tags=None, vswitch_ids=None):
        # 节点是否开启自动续费。
        self.auto_renew = auto_renew  # type: bool
        # 节点自动续费周期。
        self.auto_renew_period = auto_renew_period  # type: long
        # 当MultiAZPolicy取值为COST_OPTIMIZED时，如果因价格、库存等原因无法创建足够的抢占式实例，是否允许自动尝试创建按量实例满足ECS实例数量要求。取值范围：true：允许。false：不允许。默认值：true
        self.compensate_with_on_demand = compensate_with_on_demand  # type: bool
        # 数据盘配置。
        self.data_disks = data_disks  # type: list[DataDisk]
        # 自定义镜像ID。
        self.image_id = image_id  # type: str
        # 节点付费类型。
        self.instance_charge_type = instance_charge_type  # type: str
        # 节点ECS规格类型。
        self.instance_types = instance_types  # type: list[str]
        # 节点公网IP网络计费类型
        self.internet_charge_type = internet_charge_type  # type: str
        # 节点公网IP出带宽最大值，单位为Mbps（Mega bit per second），取值范围：1~100
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: long
        # 密钥对名称
        self.key_pair = key_pair  # type: str
        # 登录密码
        self.login_password = login_password  # type: str
        # 多可用区伸缩组ECS实例扩缩容策略
        self.multi_az_policy = multi_az_policy  # type: str
        # 伸缩组所需要按量实例个数的最小值，取值范围：0~1000。当按量实例个数少于该值时，将优先创建按量实例。
        self.on_demand_base_capacity = on_demand_base_capacity  # type: long
        # 伸缩组满足最小按量实例数（OnDemandBaseCapacity）要求后，超出的实例中按量实例应占的比例，取值范围：0～100。
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity  # type: long
        # 节点包年包月时长。
        self.period = period  # type: long
        # 节点付费周期。
        self.period_unit = period_unit  # type: str
        # 操作系统发行版。取值： CentOS，AliyunLinux，Windows，WindowsCore。
        self.platform = platform  # type: str
        # 节点RAM 角色名称。
        self.ram_policy = ram_policy  # type: str
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: list[str]
        # 扩容组ID。
        self.scaling_group_id = scaling_group_id  # type: str
        # 扩容策略。
        self.scaling_policy = scaling_policy  # type: str
        # 节点所属安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 节点池所属安全组ID列表。
        self.security_group_ids = security_group_ids  # type: list[str]
        # 指定可用实例规格的个数，伸缩组将按成本最低的多个规格均衡创建抢占式实例。取值范围：1~10。
        self.spot_instance_pools = spot_instance_pools  # type: long
        # 是否开启补齐抢占式实例。开启后，当收到抢占式实例将被回收的系统消息时，伸缩组将尝试创建新的实例，替换掉将被回收的抢占式实例。
        self.spot_instance_remedy = spot_instance_remedy  # type: bool
        # 抢占式实例价格上限配置。
        self.spot_price_limit = spot_price_limit  # type: list[DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit]
        # 抢占式实例类型
        self.spot_strategy = spot_strategy  # type: str
        # 系统盘类型
        self.system_disk_category = system_disk_category  # type: str
        # 节点系统盘磁盘性能，只针对ESSD磁盘生效
        self.system_disk_performance_level = system_disk_performance_level  # type: str
        # 系统盘大小
        self.system_disk_size = system_disk_size  # type: long
        # ECS标签
        self.tags = tags  # type: list[Tag]
        # 虚拟交换机ID。
        self.vswitch_ids = vswitch_ids  # type: list[str]

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyScalingGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_types is not None:
            result['instance_types'] = self.instance_types
        if self.internet_charge_type is not None:
            result['internet_charge_type'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['internet_max_bandwidth_out'] = self.internet_max_bandwidth_out
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.multi_az_policy is not None:
            result['multi_az_policy'] = self.multi_az_policy
        if self.on_demand_base_capacity is not None:
            result['on_demand_base_capacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['on_demand_percentage_above_base_capacity'] = self.on_demand_percentage_above_base_capacity
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.platform is not None:
            result['platform'] = self.platform
        if self.ram_policy is not None:
            result['ram_policy'] = self.ram_policy
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_group_id is not None:
            result['scaling_group_id'] = self.scaling_group_id
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.security_group_ids is not None:
            result['security_group_ids'] = self.security_group_ids
        if self.spot_instance_pools is not None:
            result['spot_instance_pools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['spot_instance_remedy'] = self.spot_instance_remedy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_renew') is not None:
            self.auto_renew = m.get('auto_renew')
        if m.get('auto_renew_period') is not None:
            self.auto_renew_period = m.get('auto_renew_period')
        if m.get('compensate_with_on_demand') is not None:
            self.compensate_with_on_demand = m.get('compensate_with_on_demand')
        self.data_disks = []
        if m.get('data_disks') is not None:
            for k in m.get('data_disks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
        if m.get('instance_types') is not None:
            self.instance_types = m.get('instance_types')
        if m.get('internet_charge_type') is not None:
            self.internet_charge_type = m.get('internet_charge_type')
        if m.get('internet_max_bandwidth_out') is not None:
            self.internet_max_bandwidth_out = m.get('internet_max_bandwidth_out')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        if m.get('multi_az_policy') is not None:
            self.multi_az_policy = m.get('multi_az_policy')
        if m.get('on_demand_base_capacity') is not None:
            self.on_demand_base_capacity = m.get('on_demand_base_capacity')
        if m.get('on_demand_percentage_above_base_capacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('on_demand_percentage_above_base_capacity')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('ram_policy') is not None:
            self.ram_policy = m.get('ram_policy')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('scaling_group_id') is not None:
            self.scaling_group_id = m.get('scaling_group_id')
        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('security_group_ids') is not None:
            self.security_group_ids = m.get('security_group_ids')
        if m.get('spot_instance_pools') is not None:
            self.spot_instance_pools = m.get('spot_instance_pools')
        if m.get('spot_instance_remedy') is not None:
            self.spot_instance_remedy = m.get('spot_instance_remedy')
        self.spot_price_limit = []
        if m.get('spot_price_limit') is not None:
            for k in m.get('spot_price_limit'):
                temp_model = DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')
        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')
        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class DescribeClusterNodePoolDetailResponseBodyStatus(TeaModel):
    def __init__(self, failed_nodes=None, healthy_nodes=None, initial_nodes=None, offline_nodes=None,
                 removing_nodes=None, serving_nodes=None, state=None, total_nodes=None):
        # 失败节点数。
        self.failed_nodes = failed_nodes  # type: long
        # 处于健康状态节点数。
        self.healthy_nodes = healthy_nodes  # type: long
        # 正在初始化节点数。
        self.initial_nodes = initial_nodes  # type: long
        # 离线节点数量。
        self.offline_nodes = offline_nodes  # type: long
        # 正在被移除节点数。
        self.removing_nodes = removing_nodes  # type: long
        # 工作节点数量。
        self.serving_nodes = serving_nodes  # type: long
        # 节点池状态。
        self.state = state  # type: str
        # 总节点数。
        self.total_nodes = total_nodes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_nodes is not None:
            result['failed_nodes'] = self.failed_nodes
        if self.healthy_nodes is not None:
            result['healthy_nodes'] = self.healthy_nodes
        if self.initial_nodes is not None:
            result['initial_nodes'] = self.initial_nodes
        if self.offline_nodes is not None:
            result['offline_nodes'] = self.offline_nodes
        if self.removing_nodes is not None:
            result['removing_nodes'] = self.removing_nodes
        if self.serving_nodes is not None:
            result['serving_nodes'] = self.serving_nodes
        if self.state is not None:
            result['state'] = self.state
        if self.total_nodes is not None:
            result['total_nodes'] = self.total_nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('failed_nodes') is not None:
            self.failed_nodes = m.get('failed_nodes')
        if m.get('healthy_nodes') is not None:
            self.healthy_nodes = m.get('healthy_nodes')
        if m.get('initial_nodes') is not None:
            self.initial_nodes = m.get('initial_nodes')
        if m.get('offline_nodes') is not None:
            self.offline_nodes = m.get('offline_nodes')
        if m.get('removing_nodes') is not None:
            self.removing_nodes = m.get('removing_nodes')
        if m.get('serving_nodes') is not None:
            self.serving_nodes = m.get('serving_nodes')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('total_nodes') is not None:
            self.total_nodes = m.get('total_nodes')
        return self


class DescribeClusterNodePoolDetailResponseBodyTeeConfig(TeaModel):
    def __init__(self, tee_enable=None):
        # 是否为加密计算节点池。
        self.tee_enable = tee_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBodyTeeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')
        return self


class DescribeClusterNodePoolDetailResponseBody(TeaModel):
    def __init__(self, auto_scaling=None, interconnect_config=None, interconnect_mode=None, kubernetes_config=None,
                 management=None, max_nodes=None, nodepool_info=None, scaling_group=None, status=None, tee_config=None):
        # 节点池自动伸缩信息。
        self.auto_scaling = auto_scaling  # type: DescribeClusterNodePoolDetailResponseBodyAutoScaling
        # 边缘节点池网络相关的配置。该值只对edge类型的节点池有意义
        self.interconnect_config = interconnect_config  # type: DescribeClusterNodePoolDetailResponseBodyInterconnectConfig
        # 边缘节点池的网络类型。basic：基础型；improved：增强型。该值只对edge类型的节点池有意义
        self.interconnect_mode = interconnect_mode  # type: str
        # 节点池所属集群配置。
        self.kubernetes_config = kubernetes_config  # type: DescribeClusterNodePoolDetailResponseBodyKubernetesConfig
        # 托管版节点池配置。
        self.management = management  # type: DescribeClusterNodePoolDetailResponseBodyManagement
        # 边缘节点池允许容纳的最大节点数量. 节点池内可以容纳的最大节点数量，该参数大于等于0。0表示无额外限制(仅受限于集群整体可以容纳的节点数，节点池本身无额外限制)。边缘节点池该参数值往往大于0；ess类型节点池和默认的edge类型节点池该参数值为0
        self.max_nodes = max_nodes  # type: long
        # 节点池详情。
        self.nodepool_info = nodepool_info  # type: DescribeClusterNodePoolDetailResponseBodyNodepoolInfo
        # 节点池扩容组信息。
        self.scaling_group = scaling_group  # type: DescribeClusterNodePoolDetailResponseBodyScalingGroup
        # 节点池状态。
        self.status = status  # type: DescribeClusterNodePoolDetailResponseBodyStatus
        # 加密计算节点池信息。
        self.tee_config = tee_config  # type: DescribeClusterNodePoolDetailResponseBodyTeeConfig

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.interconnect_config:
            self.interconnect_config.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.management:
            self.management.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.status:
            self.status.validate()
        if self.tee_config:
            self.tee_config.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
        if self.interconnect_config is not None:
            result['interconnect_config'] = self.interconnect_config.to_map()
        if self.interconnect_mode is not None:
            result['interconnect_mode'] = self.interconnect_mode
        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()
        if self.management is not None:
            result['management'] = self.management.to_map()
        if self.max_nodes is not None:
            result['max_nodes'] = self.max_nodes
        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()
        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_scaling') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('interconnect_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m['interconnect_config'])
        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')
        if m.get('kubernetes_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')
        if m.get('nodepool_info') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('status') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('tee_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
        return self


class DescribeClusterNodePoolDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterNodePoolDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolDetailResponse, self).to_map()
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
            temp_model = DescribeClusterNodePoolDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling(TeaModel):
    def __init__(self, eip_bandwidth=None, eip_internet_charge_type=None, enable=None, is_bond_eip=None,
                 max_instances=None, min_instances=None, type=None):
        # EIP带宽峰值
        self.eip_bandwidth = eip_bandwidth  # type: long
        # EIP实例计费方式
        self.eip_internet_charge_type = eip_internet_charge_type  # type: str
        # 自动伸缩
        self.enable = enable  # type: bool
        # 是否绑定EIP
        self.is_bond_eip = is_bond_eip  # type: bool
        # 最大节点数	
        self.max_instances = max_instances  # type: long
        # 最小节点数	
        self.min_instances = min_instances  # type: long
        # 扩容组类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_bandwidth is not None:
            result['eip_bandwidth'] = self.eip_bandwidth
        if self.eip_internet_charge_type is not None:
            result['eip_internet_charge_type'] = self.eip_internet_charge_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.is_bond_eip is not None:
            result['is_bond_eip'] = self.is_bond_eip
        if self.max_instances is not None:
            result['max_instances'] = self.max_instances
        if self.min_instances is not None:
            result['min_instances'] = self.min_instances
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eip_bandwidth') is not None:
            self.eip_bandwidth = m.get('eip_bandwidth')
        if m.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = m.get('eip_internet_charge_type')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('is_bond_eip') is not None:
            self.is_bond_eip = m.get('is_bond_eip')
        if m.get('max_instances') is not None:
            self.max_instances = m.get('max_instances')
        if m.get('min_instances') is not None:
            self.min_instances = m.get('min_instances')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig(TeaModel):
    def __init__(self, bandwidth=None, ccn_id=None, ccn_region_id=None, cen_id=None, improved_period=None):
        # 边缘增强型节点池的网络带宽，单位M
        self.bandwidth = bandwidth  # type: long
        # 边缘增强型节点池绑定的云连接网实例ID(CCNID)
        self.ccn_id = ccn_id  # type: str
        # 边缘增强型节点池绑定的云连接网实例所属的区域
        self.ccn_region_id = ccn_region_id  # type: str
        # 边缘增强型节点池绑定的云企业网实例ID(CENID)
        self.cen_id = cen_id  # type: str
        # 边缘增强型节点池的购买时长，单位月
        self.improved_period = improved_period  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.ccn_id is not None:
            result['ccn_id'] = self.ccn_id
        if self.ccn_region_id is not None:
            result['ccn_region_id'] = self.ccn_region_id
        if self.cen_id is not None:
            result['cen_id'] = self.cen_id
        if self.improved_period is not None:
            result['improved_period'] = self.improved_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('ccn_id') is not None:
            self.ccn_id = m.get('ccn_id')
        if m.get('ccn_region_id') is not None:
            self.ccn_region_id = m.get('ccn_region_id')
        if m.get('cen_id') is not None:
            self.cen_id = m.get('cen_id')
        if m.get('improved_period') is not None:
            self.improved_period = m.get('improved_period')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig(TeaModel):
    def __init__(self, cms_enabled=None, cpu_policy=None, labels=None, runtime=None, runtime_version=None,
                 taints=None, user_data=None):
        # 是否开启云监控	
        self.cms_enabled = cms_enabled  # type: bool
        # CPU管理策略	
        self.cpu_policy = cpu_policy  # type: str
        # ECS标签
        self.labels = labels  # type: list[Tag]
        # 容器运行时	
        self.runtime = runtime  # type: str
        # 容器运行时版本	
        self.runtime_version = runtime_version  # type: str
        # 污点配置
        self.taints = taints  # type: list[Taint]
        # 节点自定义数据
        self.user_data = user_data  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = Tag()
                self.labels.append(temp_model.from_map(k))
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig(TeaModel):
    def __init__(self, auto_upgrade=None, max_unavailable=None, surge=None, surge_percentage=None):
        # 是否启用自动升级，自修复
        self.auto_upgrade = auto_upgrade  # type: bool
        # 最大不可用节点数量
        self.max_unavailable = max_unavailable  # type: long
        # 额外节点数量
        self.surge = surge  # type: long
        # 额外节点比例， 和surge 二选一
        self.surge_percentage = surge_percentage  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade
        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable
        if self.surge is not None:
            result['surge'] = self.surge
        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('max_unavailable') is not None:
            self.max_unavailable = m.get('max_unavailable')
        if m.get('surge') is not None:
            self.surge = m.get('surge')
        if m.get('surge_percentage') is not None:
            self.surge_percentage = m.get('surge_percentage')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsManagement(TeaModel):
    def __init__(self, auto_repair=None, enable=None, upgrade_config=None):
        # 是否启用自动修复
        self.auto_repair = auto_repair  # type: bool
        # 是否开启托管版节点池
        self.enable = enable  # type: bool
        # 是否启用自动修复
        self.upgrade_config = upgrade_config  # type: DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsManagement, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.enable is not None:
            result['enable'] = self.enable
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo(TeaModel):
    def __init__(self, created=None, is_default=None, name=None, nodepool_id=None, region_id=None,
                 resource_group_id=None, type=None, updated=None):
        # 节点池创建时间
        self.created = created  # type: str
        # 是否为默认节点池
        self.is_default = is_default  # type: bool
        # 节点池名称
        self.name = name  # type: str
        # 节点池ID
        self.nodepool_id = nodepool_id  # type: str
        # 节点池所在地域ID
        self.region_id = region_id  # type: str
        # 资源组ID
        self.resource_group_id = resource_group_id  # type: str
        # 节点池类型
        self.type = type  # type: str
        # 节点池更新时间
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.is_default is not None:
            result['is_default'] = self.is_default
        if self.name is not None:
            result['name'] = self.name
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('is_default') is not None:
            self.is_default = m.get('is_default')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        # 抢占式实例规格
        self.instance_type = instance_type  # type: str
        # 单台实例上限价格，单位：元/小时
        self.price_limit = price_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.price_limit is not None:
            result['price_limit'] = self.price_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')
        if m.get('price_limit') is not None:
            self.price_limit = m.get('price_limit')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, compensate_with_on_demand=None, data_disks=None,
                 image_id=None, instance_charge_type=None, instance_types=None, internet_charge_type=None,
                 internet_max_bandwidth_out=None, key_pair=None, login_password=None, multi_az_policy=None, on_demand_base_capacity=None,
                 on_demand_percentage_above_base_capacity=None, period=None, period_unit=None, platform=None, ram_policy=None, rds_instances=None,
                 scaling_group_id=None, scaling_policy=None, security_group_id=None, security_group_ids=None,
                 spot_instance_pools=None, spot_instance_remedy=None, spot_price_limit=None, spot_strategy=None,
                 system_disk_category=None, system_disk_performance_level=None, system_disk_size=None, tags=None, vswitch_ids=None):
        # 自动续费	
        self.auto_renew = auto_renew  # type: bool
        # 自动付费时长	
        self.auto_renew_period = auto_renew_period  # type: long
        # 当MultiAZPolicy取值为COST_OPTIMIZED时，如果因价格、库存等原因无法创建足够的抢占式实例，是否允许自动尝试创建按量实例满足ECS实例数量要求。取值范围：true：允许。false：不允许。默认值：true
        self.compensate_with_on_demand = compensate_with_on_demand  # type: bool
        # 数据盘配置	
        self.data_disks = data_disks  # type: list[DataDisk]
        # 镜像ID	
        self.image_id = image_id  # type: str
        # 节点付费类型	
        self.instance_charge_type = instance_charge_type  # type: str
        # 节点类型	
        self.instance_types = instance_types  # type: list[str]
        # 节点公网IP网络计费类型
        self.internet_charge_type = internet_charge_type  # type: str
        # 节点公网IP出带宽最大值，单位为Mbps（Mega bit per second），取值范围：1~100
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: long
        # 密钥对名称，和login_password二选一。
        self.key_pair = key_pair  # type: str
        # 登录密码，返回结果是加密的。
        self.login_password = login_password  # type: str
        # 多可用区伸缩组ECS实例扩缩容策略
        self.multi_az_policy = multi_az_policy  # type: str
        # 伸缩组所需要按量实例个数的最小值，取值范围：0~1000。当按量实例个数少于该值时，将优先创建按量实例
        self.on_demand_base_capacity = on_demand_base_capacity  # type: long
        # 伸缩组满足最小按量实例数（OnDemandBaseCapacity）要求后，超出的实例中按量实例应占的比例，取值范围：0～100
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity  # type: long
        # 包年包月时长	
        self.period = period  # type: long
        # 自动付费周期	
        self.period_unit = period_unit  # type: str
        # 操作系统发行版。取值： CentOS，AliyunLinux，Windows，WindowsCore
        self.platform = platform  # type: str
        # RAM 角色名称	
        self.ram_policy = ram_policy  # type: str
        # RDS列表	
        self.rds_instances = rds_instances  # type: list[str]
        # 扩容组ID	
        self.scaling_group_id = scaling_group_id  # type: str
        # 扩容节点策略	
        self.scaling_policy = scaling_policy  # type: str
        # 安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 安全组ID列表
        self.security_group_ids = security_group_ids  # type: list[str]
        # 指定可用实例规格的个数，伸缩组将按成本最低的多个规格均衡创建抢占式实例。取值范围：1~10
        self.spot_instance_pools = spot_instance_pools  # type: long
        # 是否开启补齐抢占式实例。开启后，当收到抢占式实例将被回收的系统消息时，伸缩组将尝试创建新的实例，替换掉将被回收的抢占式实例
        self.spot_instance_remedy = spot_instance_remedy  # type: bool
        # 抢占实例价格上限配置
        self.spot_price_limit = spot_price_limit  # type: list[DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit]
        # 抢占式实例类型
        self.spot_strategy = spot_strategy  # type: str
        # 系统盘类型。	
        self.system_disk_category = system_disk_category  # type: str
        # 节点系统盘磁盘性能，只针对ESSD磁盘生效
        self.system_disk_performance_level = system_disk_performance_level  # type: str
        # 系统盘大小	
        self.system_disk_size = system_disk_size  # type: long
        # 节点标签	
        self.tags = tags  # type: list[Tag]
        # 虚拟交换机ID
        self.vswitch_ids = vswitch_ids  # type: list[str]

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_types is not None:
            result['instance_types'] = self.instance_types
        if self.internet_charge_type is not None:
            result['internet_charge_type'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['internet_max_bandwidth_out'] = self.internet_max_bandwidth_out
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.multi_az_policy is not None:
            result['multi_az_policy'] = self.multi_az_policy
        if self.on_demand_base_capacity is not None:
            result['on_demand_base_capacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['on_demand_percentage_above_base_capacity'] = self.on_demand_percentage_above_base_capacity
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.platform is not None:
            result['platform'] = self.platform
        if self.ram_policy is not None:
            result['ram_policy'] = self.ram_policy
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_group_id is not None:
            result['scaling_group_id'] = self.scaling_group_id
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.security_group_ids is not None:
            result['security_group_ids'] = self.security_group_ids
        if self.spot_instance_pools is not None:
            result['spot_instance_pools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['spot_instance_remedy'] = self.spot_instance_remedy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_renew') is not None:
            self.auto_renew = m.get('auto_renew')
        if m.get('auto_renew_period') is not None:
            self.auto_renew_period = m.get('auto_renew_period')
        if m.get('compensate_with_on_demand') is not None:
            self.compensate_with_on_demand = m.get('compensate_with_on_demand')
        self.data_disks = []
        if m.get('data_disks') is not None:
            for k in m.get('data_disks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
        if m.get('instance_types') is not None:
            self.instance_types = m.get('instance_types')
        if m.get('internet_charge_type') is not None:
            self.internet_charge_type = m.get('internet_charge_type')
        if m.get('internet_max_bandwidth_out') is not None:
            self.internet_max_bandwidth_out = m.get('internet_max_bandwidth_out')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        if m.get('multi_az_policy') is not None:
            self.multi_az_policy = m.get('multi_az_policy')
        if m.get('on_demand_base_capacity') is not None:
            self.on_demand_base_capacity = m.get('on_demand_base_capacity')
        if m.get('on_demand_percentage_above_base_capacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('on_demand_percentage_above_base_capacity')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('ram_policy') is not None:
            self.ram_policy = m.get('ram_policy')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('scaling_group_id') is not None:
            self.scaling_group_id = m.get('scaling_group_id')
        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('security_group_ids') is not None:
            self.security_group_ids = m.get('security_group_ids')
        if m.get('spot_instance_pools') is not None:
            self.spot_instance_pools = m.get('spot_instance_pools')
        if m.get('spot_instance_remedy') is not None:
            self.spot_instance_remedy = m.get('spot_instance_remedy')
        self.spot_price_limit = []
        if m.get('spot_price_limit') is not None:
            for k in m.get('spot_price_limit'):
                temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')
        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')
        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsStatus(TeaModel):
    def __init__(self, failed_nodes=None, healthy_nodes=None, initial_nodes=None, offline_nodes=None,
                 removing_nodes=None, serving_nodes=None, state=None, total_nodes=None):
        # 失败的节点数	
        self.failed_nodes = failed_nodes  # type: long
        # 处于健康状态的节点数	
        self.healthy_nodes = healthy_nodes  # type: long
        # 正在创建的节点数	
        self.initial_nodes = initial_nodes  # type: long
        # 离线节点数	
        self.offline_nodes = offline_nodes  # type: long
        # 正在被移除的节点数
        self.removing_nodes = removing_nodes  # type: long
        # 正在工作节点数	
        self.serving_nodes = serving_nodes  # type: long
        # 节点池状态	
        self.state = state  # type: str
        # 节点总数	
        self.total_nodes = total_nodes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_nodes is not None:
            result['failed_nodes'] = self.failed_nodes
        if self.healthy_nodes is not None:
            result['healthy_nodes'] = self.healthy_nodes
        if self.initial_nodes is not None:
            result['initial_nodes'] = self.initial_nodes
        if self.offline_nodes is not None:
            result['offline_nodes'] = self.offline_nodes
        if self.removing_nodes is not None:
            result['removing_nodes'] = self.removing_nodes
        if self.serving_nodes is not None:
            result['serving_nodes'] = self.serving_nodes
        if self.state is not None:
            result['state'] = self.state
        if self.total_nodes is not None:
            result['total_nodes'] = self.total_nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('failed_nodes') is not None:
            self.failed_nodes = m.get('failed_nodes')
        if m.get('healthy_nodes') is not None:
            self.healthy_nodes = m.get('healthy_nodes')
        if m.get('initial_nodes') is not None:
            self.initial_nodes = m.get('initial_nodes')
        if m.get('offline_nodes') is not None:
            self.offline_nodes = m.get('offline_nodes')
        if m.get('removing_nodes') is not None:
            self.removing_nodes = m.get('removing_nodes')
        if m.get('serving_nodes') is not None:
            self.serving_nodes = m.get('serving_nodes')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('total_nodes') is not None:
            self.total_nodes = m.get('total_nodes')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig(TeaModel):
    def __init__(self, tee_enable=None):
        # 是否为加密计算节点池	
        self.tee_enable = tee_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')
        return self


class DescribeClusterNodePoolsResponseBodyNodepools(TeaModel):
    def __init__(self, auto_scaling=None, interconnect_config=None, interconnect_mode=None, kubernetes_config=None,
                 management=None, max_nodes=None, nodepool_info=None, scaling_group=None, status=None, tee_config=None):
        # 自动伸缩配置详情
        self.auto_scaling = auto_scaling  # type: DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling
        # 边缘节点池网络相关的配置。该值只对edge类型的节点池有意义
        self.interconnect_config = interconnect_config  # type: DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig
        # 边缘节点池的网络类型。basic：基础型；improved：增强型。该值只对edge类型的节点池有意义
        self.interconnect_mode = interconnect_mode  # type: str
        # 集群配置信息
        self.kubernetes_config = kubernetes_config  # type: DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig
        # 托管节点池配置
        self.management = management  # type: DescribeClusterNodePoolsResponseBodyNodepoolsManagement
        # 边缘节点池允许容纳的最大节点数量. 节点池内可以容纳的最大节点数量，该参数大于等于0。0表示无额外限制(仅受限于集群整体可以容纳的节点数，节点池本身无额外限制)。边缘节点池该参数值往往大于0；ess类型节点池和默认的edge类型节点池该参数值为0
        self.max_nodes = max_nodes  # type: long
        # 节点池配置详情
        self.nodepool_info = nodepool_info  # type: DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo
        # 扩容组配置详情
        self.scaling_group = scaling_group  # type: DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup
        # 节点池状态详情
        self.status = status  # type: DescribeClusterNodePoolsResponseBodyNodepoolsStatus
        # 加密计算配置详情
        self.tee_config = tee_config  # type: DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.interconnect_config:
            self.interconnect_config.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.management:
            self.management.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.status:
            self.status.validate()
        if self.tee_config:
            self.tee_config.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBodyNodepools, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
        if self.interconnect_config is not None:
            result['interconnect_config'] = self.interconnect_config.to_map()
        if self.interconnect_mode is not None:
            result['interconnect_mode'] = self.interconnect_mode
        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()
        if self.management is not None:
            result['management'] = self.management.to_map()
        if self.max_nodes is not None:
            result['max_nodes'] = self.max_nodes
        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()
        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_scaling') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('interconnect_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m['interconnect_config'])
        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')
        if m.get('kubernetes_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')
        if m.get('nodepool_info') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('status') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('tee_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
        return self


class DescribeClusterNodePoolsResponseBody(TeaModel):
    def __init__(self, nodepools=None):
        # 节点池列表
        self.nodepools = nodepools  # type: list[DescribeClusterNodePoolsResponseBodyNodepools]

    def validate(self):
        if self.nodepools:
            for k in self.nodepools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['nodepools'] = []
        if self.nodepools is not None:
            for k in self.nodepools:
                result['nodepools'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodepools = []
        if m.get('nodepools') is not None:
            for k in m.get('nodepools'):
                temp_model = DescribeClusterNodePoolsResponseBodyNodepools()
                self.nodepools.append(temp_model.from_map(k))
        return self


class DescribeClusterNodePoolsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterNodePoolsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterNodePoolsResponse, self).to_map()
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
            temp_model = DescribeClusterNodePoolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterNodesRequest(TeaModel):
    def __init__(self, instance_ids=None, nodepool_id=None, page_number=None, page_size=None, state=None):
        # 节点实例ID，按照实例ID进行过滤。  节点池ID不为空时会忽略此字段。多节点用逗号分割
        self.instance_ids = instance_ids  # type: str
        # 节点池ID。
        self.nodepool_id = nodepool_id  # type: str
        # 分页数量
        self.page_number = page_number  # type: str
        # 每页大小。
        self.page_size = page_size  # type: str
        # 节点状态。默认值：all。
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DescribeClusterNodesResponseBodyNodes(TeaModel):
    def __init__(self, creation_time=None, error_message=None, expired_time=None, host_name=None, image_id=None,
                 instance_charge_type=None, instance_id=None, instance_name=None, instance_role=None, instance_status=None,
                 instance_type=None, instance_type_family=None, ip_address=None, is_aliyun_node=None, node_name=None,
                 node_status=None, nodepool_id=None, source=None, spot_strategy=None, state=None):
        # 节点创建时间。
        self.creation_time = creation_time  # type: str
        # 错误信息说明。
        self.error_message = error_message  # type: str
        # 节点过期时间。
        self.expired_time = expired_time  # type: str
        # 节点主机名。
        self.host_name = host_name  # type: str
        # 节点使用的镜像ID。
        self.image_id = image_id  # type: str
        # 节点付费类型。
        self.instance_charge_type = instance_charge_type  # type: str
        # 节点实例ID。
        self.instance_id = instance_id  # type: str
        # 节点名称。
        self.instance_name = instance_name  # type: str
        # 节点实例角色类型，Master或Worker。
        self.instance_role = instance_role  # type: str
        # 节点实例状态，
        self.instance_status = instance_status  # type: str
        # 节点实例类型。
        self.instance_type = instance_type  # type: str
        # 节点实例所属ECS实例簇名称。
        self.instance_type_family = instance_type_family  # type: str
        # 节点IP地址。
        self.ip_address = ip_address  # type: list[str]
        # 节点是否为aliyun实例。
        self.is_aliyun_node = is_aliyun_node  # type: bool
        # 节点名称，该名称是k8s专用名称。
        self.node_name = node_name  # type: str
        # 节点状态，是否Ready。
        self.node_status = node_status  # type: str
        # 节点池ID。
        self.nodepool_id = nodepool_id  # type: str
        # 节点通过什么方式创建出来的，例如：ROS。
        self.source = source  # type: str
        # 抢占时实例类型
        self.spot_strategy = spot_strategy  # type: str
        # ECS运行状态，例如：Running。
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodesResponseBodyNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['creation_time'] = self.creation_time
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.expired_time is not None:
            result['expired_time'] = self.expired_time
        if self.host_name is not None:
            result['host_name'] = self.host_name
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.instance_role is not None:
            result['instance_role'] = self.instance_role
        if self.instance_status is not None:
            result['instance_status'] = self.instance_status
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.instance_type_family is not None:
            result['instance_type_family'] = self.instance_type_family
        if self.ip_address is not None:
            result['ip_address'] = self.ip_address
        if self.is_aliyun_node is not None:
            result['is_aliyun_node'] = self.is_aliyun_node
        if self.node_name is not None:
            result['node_name'] = self.node_name
        if self.node_status is not None:
            result['node_status'] = self.node_status
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.source is not None:
            result['source'] = self.source
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creation_time') is not None:
            self.creation_time = m.get('creation_time')
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('expired_time') is not None:
            self.expired_time = m.get('expired_time')
        if m.get('host_name') is not None:
            self.host_name = m.get('host_name')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('instance_role') is not None:
            self.instance_role = m.get('instance_role')
        if m.get('instance_status') is not None:
            self.instance_status = m.get('instance_status')
        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')
        if m.get('instance_type_family') is not None:
            self.instance_type_family = m.get('instance_type_family')
        if m.get('ip_address') is not None:
            self.ip_address = m.get('ip_address')
        if m.get('is_aliyun_node') is not None:
            self.is_aliyun_node = m.get('is_aliyun_node')
        if m.get('node_name') is not None:
            self.node_name = m.get('node_name')
        if m.get('node_status') is not None:
            self.node_status = m.get('node_status')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DescribeClusterNodesResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        # 总页数。
        self.page_number = page_number  # type: int
        # 单页展示结果数量。
        self.page_size = page_size  # type: int
        # 结果总条数。
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterNodesResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeClusterNodesResponseBody(TeaModel):
    def __init__(self, nodes=None, page=None):
        # 节点信息列表。
        self.nodes = nodes  # type: list[DescribeClusterNodesResponseBodyNodes]
        # 分页信息。
        self.page = page  # type: DescribeClusterNodesResponseBodyPage

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(DescribeClusterNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        if self.page is not None:
            result['page'] = self.page.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = DescribeClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('page') is not None:
            temp_model = DescribeClusterNodesResponseBodyPage()
            self.page = temp_model.from_map(m['page'])
        return self


class DescribeClusterNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterNodesResponse, self).to_map()
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
            temp_model = DescribeClusterNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterResourcesResponseBody(TeaModel):
    def __init__(self, cluster_id=None, created=None, instance_id=None, resource_info=None, resource_type=None,
                 state=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 资源创建时间。
        self.created = created  # type: str
        # 资源实例ID。
        self.instance_id = instance_id  # type: str
        # 资源元信息。
        self.resource_info = resource_info  # type: str
        # 资源类型。
        self.resource_type = resource_type  # type: str
        # 资源状态。
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.created is not None:
            result['created'] = self.created
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.resource_info is not None:
            result['resource_info'] = self.resource_info
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('resource_info') is not None:
            self.resource_info = m.get('resource_info')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DescribeClusterResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[DescribeClusterResourcesResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeClusterResourcesResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeClusterUserKubeconfigRequest(TeaModel):
    def __init__(self, private_ip_address=None, temporary_duration_minutes=None):
        # ApiServer是否为内网地址。
        self.private_ip_address = private_ip_address  # type: bool
        # 临时kubeconfig有效期，单位：分钟。  最小值：15（15分钟）  最大值：4320（3天）。
        self.temporary_duration_minutes = temporary_duration_minutes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterUserKubeconfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.temporary_duration_minutes is not None:
            result['TemporaryDurationMinutes'] = self.temporary_duration_minutes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('TemporaryDurationMinutes') is not None:
            self.temporary_duration_minutes = m.get('TemporaryDurationMinutes')
        return self


class DescribeClusterUserKubeconfigResponseBody(TeaModel):
    def __init__(self, config=None, expiration=None):
        # kubeconfig内容。
        self.config = config  # type: str
        # kubeconfig过期时间。格式：RFC3339 格式的 UTC 时间。
        self.expiration = expiration  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterUserKubeconfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.expiration is not None:
            result['expiration'] = self.expiration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        return self


class DescribeClusterUserKubeconfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterUserKubeconfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterUserKubeconfigResponse, self).to_map()
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
            temp_model = DescribeClusterUserKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterV2UserKubeconfigRequest(TeaModel):
    def __init__(self, private_ip_address=None):
        # 是否为内网访问。
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2UserKubeconfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeClusterV2UserKubeconfigResponseBody(TeaModel):
    def __init__(self, config=None):
        # kubeconfig内容。
        self.config = config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2UserKubeconfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class DescribeClusterV2UserKubeconfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterV2UserKubeconfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterV2UserKubeconfigResponse, self).to_map()
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
            temp_model = DescribeClusterV2UserKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(self, cluster_type=None, name=None):
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群名称。
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeClustersResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签名。
        self.key = key  # type: str
        # 标签值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeClustersResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, created=None, current_version=None,
                 data_disk_category=None, data_disk_size=None, deletion_protection=None, docker_version=None,
                 external_loadbalancer_id=None, init_version=None, master_url=None, meta_data=None, name=None, network_mode=None,
                 private_zone=None, profile=None, region_id=None, resource_group_id=None, security_group_id=None, size=None,
                 state=None, subnet_cidr=None, tags=None, updated=None, vpc_id=None, vswitch_cidr=None, vswitch_id=None,
                 worker_ram_role_name=None, zone_id=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群创建时间。
        self.created = created  # type: str
        # 集群当前版本。
        self.current_version = current_version  # type: str
        # 节点系统盘类型。
        self.data_disk_category = data_disk_category  # type: str
        # 节点系统盘大小。
        self.data_disk_size = data_disk_size  # type: long
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 容器运行时版本。
        self.docker_version = docker_version  # type: str
        # 集群Ingerss SLB实例的ID。
        self.external_loadbalancer_id = external_loadbalancer_id  # type: str
        # 集群创建时版本。
        self.init_version = init_version  # type: str
        # 集群的endpoint地址。
        self.master_url = master_url  # type: str
        # 集群元数据。
        self.meta_data = meta_data  # type: str
        # 集群名称。
        self.name = name  # type: str
        # 集群使用的网络类型。
        self.network_mode = network_mode  # type: str
        # 集群是否开启Private Zone，默认false。
        self.private_zone = private_zone  # type: bool
        # 集群标识，区分是否为边缘托管版。
        self.profile = profile  # type: str
        # 集群所在地域ID。
        self.region_id = region_id  # type: str
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 集群安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 集群内实例数量。
        self.size = size  # type: long
        # 集群运行状态。
        self.state = state  # type: str
        # POD网络。
        self.subnet_cidr = subnet_cidr  # type: str
        # 集群标签。
        self.tags = tags  # type: list[DescribeClustersResponseBodyTags]
        # 集群更新时间。
        self.updated = updated  # type: str
        # 集群使用的VPC ID。
        self.vpc_id = vpc_id  # type: str
        # 虚拟交换机网络ID。
        self.vswitch_cidr = vswitch_cidr  # type: str
        # 节点使用的Vswitch ID。
        self.vswitch_id = vswitch_id  # type: str
        # 集群Worker节点RAM角色名称。
        self.worker_ram_role_name = worker_ram_role_name  # type: str
        # 集群所在Region内的区域ID。
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.data_disk_category is not None:
            result['data_disk_category'] = self.data_disk_category
        if self.data_disk_size is not None:
            result['data_disk_size'] = self.data_disk_size
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.docker_version is not None:
            result['docker_version'] = self.docker_version
        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id
        if self.init_version is not None:
            result['init_version'] = self.init_version
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        if self.name is not None:
            result['name'] = self.name
        if self.network_mode is not None:
            result['network_mode'] = self.network_mode
        if self.private_zone is not None:
            result['private_zone'] = self.private_zone
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.size is not None:
            result['size'] = self.size
        if self.state is not None:
            result['state'] = self.state
        if self.subnet_cidr is not None:
            result['subnet_cidr'] = self.subnet_cidr
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated is not None:
            result['updated'] = self.updated
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id
        if self.vswitch_cidr is not None:
            result['vswitch_cidr'] = self.vswitch_cidr
        if self.vswitch_id is not None:
            result['vswitch_id'] = self.vswitch_id
        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')
        if m.get('data_disk_category') is not None:
            self.data_disk_category = m.get('data_disk_category')
        if m.get('data_disk_size') is not None:
            self.data_disk_size = m.get('data_disk_size')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('docker_version') is not None:
            self.docker_version = m.get('docker_version')
        if m.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = m.get('external_loadbalancer_id')
        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')
        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')
        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('network_mode') is not None:
            self.network_mode = m.get('network_mode')
        if m.get('private_zone') is not None:
            self.private_zone = m.get('private_zone')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('subnet_cidr') is not None:
            self.subnet_cidr = m.get('subnet_cidr')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = DescribeClustersResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')
        if m.get('vswitch_cidr') is not None:
            self.vswitch_cidr = m.get('vswitch_cidr')
        if m.get('vswitch_id') is not None:
            self.vswitch_id = m.get('vswitch_id')
        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')
        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[DescribeClustersResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeClustersResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeClustersV1Request(TeaModel):
    def __init__(self, cluster_spec=None, cluster_type=None, name=None, page_number=None, page_size=None,
                 profile=None):
        # 集群规格。
        self.cluster_spec = cluster_spec  # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 通过集群名称进行模糊查询。
        self.name = name  # type: str
        # 分页数。
        self.page_number = page_number  # type: long
        # 单页大小。
        self.page_size = page_size  # type: long
        # 集群标识。
        self.profile = profile  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersV1Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.profile is not None:
            result['profile'] = self.profile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        return self


class DescribeClustersV1ResponseBodyClusters(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, cluster_type=None, created=None, current_version=None,
                 deletion_protection=None, docker_version=None, external_loadbalancer_id=None, init_version=None,
                 maintenance_window=None, master_url=None, meta_data=None, name=None, network_mode=None, next_version=None,
                 private_zone=None, profile=None, region_id=None, resource_group_id=None, security_group_id=None, size=None,
                 state=None, subnet_cidr=None, tags=None, updated=None, vpc_id=None, vswitch_id=None,
                 worker_ram_role_name=None, zone_id=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 托管版集群类型，面向托管集群。 • ack.pro.small：专业托管集群。 • ack.standard ：标准托管集群。
        self.cluster_spec = cluster_spec  # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群初始化时间。
        self.created = created  # type: str
        # 集群当前版本。
        self.current_version = current_version  # type: str
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 集群使用的Docker版本。
        self.docker_version = docker_version  # type: str
        # 集群负载均衡服务的ID。
        self.external_loadbalancer_id = external_loadbalancer_id  # type: str
        # 集群初始化版本。
        self.init_version = init_version  # type: str
        self.maintenance_window = maintenance_window  # type: MaintenanceWindow
        # 集群访问地址列表。
        self.master_url = master_url  # type: str
        # 集群元数据信息。
        self.meta_data = meta_data  # type: str
        # 集群名称。
        self.name = name  # type: str
        # 集群使用的网络类型，例如：VPC网络。
        self.network_mode = network_mode  # type: str
        # 集群可升级版本。
        self.next_version = next_version  # type: str
        # 集群是否开启Private Zone。
        self.private_zone = private_zone  # type: bool
        # 边缘集群表示，用于区分边缘托管版集群。
        self.profile = profile  # type: str
        # 地域ID。
        self.region_id = region_id  # type: str
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 集群安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 集群节点数。
        self.size = size  # type: long
        # 集群运行状态。
        self.state = state  # type: str
        # POD网段地址。
        self.subnet_cidr = subnet_cidr  # type: str
        # 集群标签。
        self.tags = tags  # type: list[Tag]
        # 集群更新时间。
        self.updated = updated  # type: str
        # 集群所在的VPC ID。
        self.vpc_id = vpc_id  # type: str
        # 集群使用的虚拟交换ID。
        self.vswitch_id = vswitch_id  # type: str
        # 集群Worker RAM角色。
        self.worker_ram_role_name = worker_ram_role_name  # type: str
        # 可用区ID。
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersV1ResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.docker_version is not None:
            result['docker_version'] = self.docker_version
        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id
        if self.init_version is not None:
            result['init_version'] = self.init_version
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        if self.name is not None:
            result['name'] = self.name
        if self.network_mode is not None:
            result['network_mode'] = self.network_mode
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.private_zone is not None:
            result['private_zone'] = self.private_zone
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.size is not None:
            result['size'] = self.size
        if self.state is not None:
            result['state'] = self.state
        if self.subnet_cidr is not None:
            result['subnet_cidr'] = self.subnet_cidr
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated is not None:
            result['updated'] = self.updated
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id
        if self.vswitch_id is not None:
            result['vswitch_id'] = self.vswitch_id
        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('docker_version') is not None:
            self.docker_version = m.get('docker_version')
        if m.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = m.get('external_loadbalancer_id')
        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')
        if m.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m['maintenance_window'])
        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')
        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('network_mode') is not None:
            self.network_mode = m.get('network_mode')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('private_zone') is not None:
            self.private_zone = m.get('private_zone')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('subnet_cidr') is not None:
            self.subnet_cidr = m.get('subnet_cidr')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')
        if m.get('vswitch_id') is not None:
            self.vswitch_id = m.get('vswitch_id')
        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')
        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')
        return self


class DescribeClustersV1ResponseBodyPageInfo(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        # 分页数。
        self.page_number = page_number  # type: int
        # 单页大小。
        self.page_size = page_size  # type: int
        # 结果总数。
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersV1ResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeClustersV1ResponseBody(TeaModel):
    def __init__(self, clusters=None, page_info=None):
        # 集群详情列表。
        self.clusters = clusters  # type: list[DescribeClustersV1ResponseBodyClusters]
        # 分页信息。
        self.page_info = page_info  # type: DescribeClustersV1ResponseBodyPageInfo

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(DescribeClustersV1ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('clusters') is not None:
            for k in m.get('clusters'):
                temp_model = DescribeClustersV1ResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = DescribeClustersV1ResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        return self


class DescribeClustersV1Response(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClustersV1ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClustersV1Response, self).to_map()
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
            temp_model = DescribeClustersV1ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeMachineActiveProcessResponseBody(TeaModel):
    def __init__(self, logs=None, progress=None, request_id=None, state=None, step=None):
        # logs of activate
        self.logs = logs  # type: str
        # process of activate
        self.progress = progress  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        # state of activate
        self.state = state  # type: str
        # step of activate
        self.step = step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEdgeMachineActiveProcessResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['logs'] = self.logs
        if self.progress is not None:
            result['progress'] = self.progress
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.state is not None:
            result['state'] = self.state
        if self.step is not None:
            result['step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logs') is not None:
            self.logs = m.get('logs')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('step') is not None:
            self.step = m.get('step')
        return self


class DescribeEdgeMachineActiveProcessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEdgeMachineActiveProcessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEdgeMachineActiveProcessResponse, self).to_map()
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
            temp_model = DescribeEdgeMachineActiveProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeMachineModelsResponseBodyModels(TeaModel):
    def __init__(self, cpu=None, cpu_arch=None, created=None, description=None, manage_runtime=None, memory=None,
                 model=None, model_id=None):
        # cpu
        self.cpu = cpu  # type: int
        # cpu arch
        self.cpu_arch = cpu_arch  # type: str
        # created
        self.created = created  # type: str
        # description
        self.description = description  # type: str
        # manage runtime
        self.manage_runtime = manage_runtime  # type: int
        # memory
        self.memory = memory  # type: int
        # model
        self.model = model  # type: str
        # model id
        self.model_id = model_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEdgeMachineModelsResponseBodyModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.cpu_arch is not None:
            result['cpu_arch'] = self.cpu_arch
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.manage_runtime is not None:
            result['manage_runtime'] = self.manage_runtime
        if self.memory is not None:
            result['memory'] = self.memory
        if self.model is not None:
            result['model'] = self.model
        if self.model_id is not None:
            result['model_id'] = self.model_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('cpu_arch') is not None:
            self.cpu_arch = m.get('cpu_arch')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('manage_runtime') is not None:
            self.manage_runtime = m.get('manage_runtime')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('model_id') is not None:
            self.model_id = m.get('model_id')
        return self


class DescribeEdgeMachineModelsResponseBody(TeaModel):
    def __init__(self, models=None):
        # Id of the request
        self.models = models  # type: list[DescribeEdgeMachineModelsResponseBodyModels]

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEdgeMachineModelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['models'] = []
        if self.models is not None:
            for k in self.models:
                result['models'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.models = []
        if m.get('models') is not None:
            for k in m.get('models'):
                temp_model = DescribeEdgeMachineModelsResponseBodyModels()
                self.models.append(temp_model.from_map(k))
        return self


class DescribeEdgeMachineModelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEdgeMachineModelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEdgeMachineModelsResponse, self).to_map()
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
            temp_model = DescribeEdgeMachineModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeMachineTunnelConfigDetailResponseBody(TeaModel):
    def __init__(self, device_name=None, model=None, product_key=None, request_id=None, sn=None, token=None,
                 tunnel_endpoint=None):
        # device name
        self.device_name = device_name  # type: str
        # Id of the request
        self.model = model  # type: str
        # product key
        self.product_key = product_key  # type: str
        # request id
        self.request_id = request_id  # type: str
        # sn
        self.sn = sn  # type: str
        # token
        self.token = token  # type: str
        # tunnel endpoint
        self.tunnel_endpoint = tunnel_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEdgeMachineTunnelConfigDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['device_name'] = self.device_name
        if self.model is not None:
            result['model'] = self.model
        if self.product_key is not None:
            result['product_key'] = self.product_key
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.sn is not None:
            result['sn'] = self.sn
        if self.token is not None:
            result['token'] = self.token
        if self.tunnel_endpoint is not None:
            result['tunnel_endpoint'] = self.tunnel_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('device_name') is not None:
            self.device_name = m.get('device_name')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('product_key') is not None:
            self.product_key = m.get('product_key')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('tunnel_endpoint') is not None:
            self.tunnel_endpoint = m.get('tunnel_endpoint')
        return self


class DescribeEdgeMachineTunnelConfigDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEdgeMachineTunnelConfigDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEdgeMachineTunnelConfigDetailResponse, self).to_map()
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
            temp_model = DescribeEdgeMachineTunnelConfigDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeMachinesRequest(TeaModel):
    def __init__(self, hostname=None, life_state=None, model=None, online_state=None, page_number=None,
                 page_size=None):
        # host name
        self.hostname = hostname  # type: str
        # life state
        self.life_state = life_state  # type: str
        # model
        self.model = model  # type: str
        # online state
        self.online_state = online_state  # type: str
        # page number
        self.page_number = page_number  # type: long
        # page size
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEdgeMachinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.life_state is not None:
            result['life_state'] = self.life_state
        if self.model is not None:
            result['model'] = self.model
        if self.online_state is not None:
            result['online_state'] = self.online_state
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('life_state') is not None:
            self.life_state = m.get('life_state')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('online_state') is not None:
            self.online_state = m.get('online_state')
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        return self


class DescribeEdgeMachinesResponseBodyEdgeMachines(TeaModel):
    def __init__(self, active_time=None, created=None, edge_machine_id=None, hostname=None, life_state=None,
                 model=None, name=None, online_state=None, sn=None, updated=None):
        # actvite time
        self.active_time = active_time  # type: str
        # created time
        self.created = created  # type: str
        # edge machine id
        self.edge_machine_id = edge_machine_id  # type: str
        # hostname
        self.hostname = hostname  # type: str
        # life state
        self.life_state = life_state  # type: str
        # model
        self.model = model  # type: str
        # name of edgemachine
        self.name = name  # type: str
        # online state
        self.online_state = online_state  # type: str
        # sn
        self.sn = sn  # type: str
        # update time
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEdgeMachinesResponseBodyEdgeMachines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['active_time'] = self.active_time
        if self.created is not None:
            result['created'] = self.created
        if self.edge_machine_id is not None:
            result['edge_machine_id'] = self.edge_machine_id
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.life_state is not None:
            result['life_state'] = self.life_state
        if self.model is not None:
            result['model'] = self.model
        if self.name is not None:
            result['name'] = self.name
        if self.online_state is not None:
            result['online_state'] = self.online_state
        if self.sn is not None:
            result['sn'] = self.sn
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active_time') is not None:
            self.active_time = m.get('active_time')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('edge_machine_id') is not None:
            self.edge_machine_id = m.get('edge_machine_id')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('life_state') is not None:
            self.life_state = m.get('life_state')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online_state') is not None:
            self.online_state = m.get('online_state')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeEdgeMachinesResponseBodyPageInfo(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        # page number
        self.page_number = page_number  # type: int
        # page size
        self.page_size = page_size  # type: int
        # total count
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEdgeMachinesResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeEdgeMachinesResponseBody(TeaModel):
    def __init__(self, edge_machines=None, page_info=None):
        # Id of the request
        self.edge_machines = edge_machines  # type: list[DescribeEdgeMachinesResponseBodyEdgeMachines]
        # page info
        self.page_info = page_info  # type: DescribeEdgeMachinesResponseBodyPageInfo

    def validate(self):
        if self.edge_machines:
            for k in self.edge_machines:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(DescribeEdgeMachinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['edge_machines'] = []
        if self.edge_machines is not None:
            for k in self.edge_machines:
                result['edge_machines'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.edge_machines = []
        if m.get('edge_machines') is not None:
            for k in m.get('edge_machines'):
                temp_model = DescribeEdgeMachinesResponseBodyEdgeMachines()
                self.edge_machines.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = DescribeEdgeMachinesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        return self


class DescribeEdgeMachinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEdgeMachinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEdgeMachinesResponse, self).to_map()
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
            temp_model = DescribeEdgeMachinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventsRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None, type=None):
        # 集群ID
        self.cluster_id = cluster_id  # type: str
        # 没页记录数量
        self.page_number = page_number  # type: long
        # 页数
        self.page_size = page_size  # type: long
        # 事件类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeEventsResponseBodyEventsData(TeaModel):
    def __init__(self, level=None, message=None, reason=None):
        # 事件级别
        self.level = level  # type: str
        # 事件详情
        self.message = message  # type: str
        # 事件状态
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventsResponseBodyEventsData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['level'] = self.level
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class DescribeEventsResponseBodyEvents(TeaModel):
    def __init__(self, cluster_id=None, data=None, event_id=None, source=None, subject=None, time=None, type=None):
        # 集群ID
        self.cluster_id = cluster_id  # type: str
        # 事件描述
        self.data = data  # type: DescribeEventsResponseBodyEventsData
        # 事件ID
        self.event_id = event_id  # type: str
        # 事件源
        self.source = source  # type: str
        # 事件
        self.subject = subject  # type: str
        # 事件开始事件
        self.time = time  # type: str
        # 事件类型
        self.type = type  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEventsResponseBodyEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.event_id is not None:
            result['event_id'] = self.event_id
        if self.source is not None:
            result['source'] = self.source
        if self.subject is not None:
            result['subject'] = self.subject
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('data') is not None:
            temp_model = DescribeEventsResponseBodyEventsData()
            self.data = temp_model.from_map(m['data'])
        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeEventsResponseBodyPageInfo(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        # 每页记录数量
        self.page_number = page_number  # type: long
        # 页数
        self.page_size = page_size  # type: long
        # 结果总数
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventsResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeEventsResponseBody(TeaModel):
    def __init__(self, events=None, page_info=None):
        self.events = events  # type: list[DescribeEventsResponseBodyEvents]
        self.page_info = page_info  # type: DescribeEventsResponseBodyPageInfo

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(DescribeEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = DescribeEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = DescribeEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        return self


class DescribeEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventsResponse, self).to_map()
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
            temp_model = DescribeEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExternalAgentRequest(TeaModel):
    def __init__(self, private_ip_address=None):
        # 是否获取内网访问凭据。  true：获取内网连接凭据 false：获取公网连接凭据 默认值：false。
        self.private_ip_address = private_ip_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExternalAgentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeExternalAgentResponseBody(TeaModel):
    def __init__(self, config=None):
        # 代理配置。
        self.config = config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExternalAgentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class DescribeExternalAgentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeExternalAgentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExternalAgentResponse, self).to_map()
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
            temp_model = DescribeExternalAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKubernetesVersionMetadataRequest(TeaModel):
    def __init__(self, cluster_type=None, kubernetes_version=None, profile=None, region=None):
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 要查询的版本，如果为空则查所有版本。
        self.kubernetes_version = kubernetes_version  # type: str
        # 边缘集群标识，用于区分边缘集群，取值：Default或Edge。
        self.profile = profile  # type: str
        # 地域ID。
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKubernetesVersionMetadataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeKubernetesVersionMetadataResponseBodyImages(TeaModel):
    def __init__(self, image_id=None, image_name=None, platform=None, os_version=None, image_type=None, os_type=None,
                 image_category=None):
        # 镜像ID。	
        self.image_id = image_id  # type: str
        # 镜像名称。	
        self.image_name = image_name  # type: str
        # 操作系统发行版。取值范围： CentOS,AliyunLinux,Windows,WindowsCore。
        self.platform = platform  # type: str
        # 镜像版本。
        self.os_version = os_version  # type: str
        # 镜像类型。	
        self.image_type = image_type  # type: str
        # 操作系统发行版本号。
        self.os_type = os_type  # type: str
        # 镜像分类
        self.image_category = image_category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKubernetesVersionMetadataResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.image_name is not None:
            result['image_name'] = self.image_name
        if self.platform is not None:
            result['platform'] = self.platform
        if self.os_version is not None:
            result['os_version'] = self.os_version
        if self.image_type is not None:
            result['image_type'] = self.image_type
        if self.os_type is not None:
            result['os_type'] = self.os_type
        if self.image_category is not None:
            result['image_category'] = self.image_category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('image_name') is not None:
            self.image_name = m.get('image_name')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('os_version') is not None:
            self.os_version = m.get('os_version')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('os_type') is not None:
            self.os_type = m.get('os_type')
        if m.get('image_category') is not None:
            self.image_category = m.get('image_category')
        return self


class DescribeKubernetesVersionMetadataResponseBody(TeaModel):
    def __init__(self, capabilities=None, images=None, meta_data=None, runtimes=None, version=None, multi_az=None):
        # Kubernetes版本特性。	
        self.capabilities = capabilities  # type: dict[str, any]
        # ECS系统镜像列表。	
        self.images = images  # type: list[DescribeKubernetesVersionMetadataResponseBodyImages]
        # Kubernetes版本元数据信息。	
        self.meta_data = meta_data  # type: dict[str, any]
        # 容器运行时详情。	
        self.runtimes = runtimes  # type: list[Runtime]
        # Kubernetes版本。	
        self.version = version  # type: str
        # 是否为多可用区。
        self.multi_az = multi_az  # type: str

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.runtimes:
            for k in self.runtimes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeKubernetesVersionMetadataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capabilities is not None:
            result['capabilities'] = self.capabilities
        result['images'] = []
        if self.images is not None:
            for k in self.images:
                result['images'].append(k.to_map() if k else None)
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        result['runtimes'] = []
        if self.runtimes is not None:
            for k in self.runtimes:
                result['runtimes'].append(k.to_map() if k else None)
        if self.version is not None:
            result['version'] = self.version
        if self.multi_az is not None:
            result['multi_az'] = self.multi_az
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('capabilities') is not None:
            self.capabilities = m.get('capabilities')
        self.images = []
        if m.get('images') is not None:
            for k in m.get('images'):
                temp_model = DescribeKubernetesVersionMetadataResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')
        self.runtimes = []
        if m.get('runtimes') is not None:
            for k in m.get('runtimes'):
                temp_model = Runtime()
                self.runtimes.append(temp_model.from_map(k))
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('multi_az') is not None:
            self.multi_az = m.get('multi_az')
        return self


class DescribeKubernetesVersionMetadataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[DescribeKubernetesVersionMetadataResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeKubernetesVersionMetadataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeKubernetesVersionMetadataResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribePoliciesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: dict

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(DescribePoliciesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribePolicyDetailsResponseBody(TeaModel):
    def __init__(self, action=None, category=None, description=None, is_deleted=None, name=None, no_config=None,
                 severity=None, template=None):
        # 规则治理动作 ● enforce: 拦截违规部署 ● inform：告警
        self.action = action  # type: str
        # 规则模板类型
        self.category = category  # type: str
        # 规则模板描述
        self.description = description  # type: str
        # 软删除标志：0表示未删除 1表示删除
        self.is_deleted = is_deleted  # type: int
        # 策略治理规则名称
        self.name = name  # type: str
        # 是否需要配置策略： 0表示需要参数配置 1表示无需参数配置
        self.no_config = no_config  # type: int
        # 规则治理等级
        self.severity = severity  # type: str
        # 规则模板详情
        self.template = template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.is_deleted is not None:
            result['is_deleted'] = self.is_deleted
        if self.name is not None:
            result['name'] = self.name
        if self.no_config is not None:
            result['no_config'] = self.no_config
        if self.severity is not None:
            result['severity'] = self.severity
        if self.template is not None:
            result['template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('is_deleted') is not None:
            self.is_deleted = m.get('is_deleted')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('no_config') is not None:
            self.no_config = m.get('no_config')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('template') is not None:
            self.template = m.get('template')
        return self


class DescribePolicyDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePolicyDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyDetailsResponse, self).to_map()
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
            temp_model = DescribePolicyDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyGovernanceInClusterResponseBodyAdmitLogLog(TeaModel):
    def __init__(self, cluster_id=None, constraint_kind=None, msg=None, resource_kind=None, resource_name=None,
                 resource_namespace=None):
        # 目标集群ID
        self.cluster_id = cluster_id  # type: str
        # 策略类型名称
        self.constraint_kind = constraint_kind  # type: str
        # 策略治理审计日志信息
        self.msg = msg  # type: str
        # 目标资源类型
        self.resource_kind = resource_kind  # type: str
        # 目标资源名称
        self.resource_name = resource_name  # type: str
        # 目标资源命名空间
        self.resource_namespace = resource_namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyAdmitLogLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.constraint_kind is not None:
            result['constraint_kind'] = self.constraint_kind
        if self.msg is not None:
            result['msg'] = self.msg
        if self.resource_kind is not None:
            result['resource_kind'] = self.resource_kind
        if self.resource_name is not None:
            result['resource_name'] = self.resource_name
        if self.resource_namespace is not None:
            result['resource_namespace'] = self.resource_namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('constraint_kind') is not None:
            self.constraint_kind = m.get('constraint_kind')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('resource_kind') is not None:
            self.resource_kind = m.get('resource_kind')
        if m.get('resource_name') is not None:
            self.resource_name = m.get('resource_name')
        if m.get('resource_namespace') is not None:
            self.resource_namespace = m.get('resource_namespace')
        return self


class DescribePolicyGovernanceInClusterResponseBodyAdmitLog(TeaModel):
    def __init__(self, count=None, log=None, progress=None):
        # 当前查询到的日志总数
        self.count = count  # type: long
        # 策略治理审计日志内容
        self.log = log  # type: DescribePolicyGovernanceInClusterResponseBodyAdmitLogLog
        # 查询结果的状态
        self.progress = progress  # type: str

    def validate(self):
        if self.log:
            self.log.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyAdmitLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.log is not None:
            result['log'] = self.log.to_map()
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('log') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyAdmitLogLog()
            self.log = temp_model.from_map(m['log'])
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class DescribePolicyGovernanceInClusterResponseBodyOnState(TeaModel):
    def __init__(self, enabled_count=None, severity=None, total=None):
        # 当前开启的策略种类计数
        self.enabled_count = enabled_count  # type: int
        # 策略治理等级
        self.severity = severity  # type: str
        # 该等级下策略种类总数
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyOnState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_count is not None:
            result['enabled_count'] = self.enabled_count
        if self.severity is not None:
            result['severity'] = self.severity
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enabled_count') is not None:
            self.enabled_count = m.get('enabled_count')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class DescribePolicyGovernanceInClusterResponseBodyTotalViolationsDeny(TeaModel):
    def __init__(self, severity=None, violations=None):
        # 策略治理等级
        self.severity = severity  # type: str
        # 被拦截的事件计数
        self.violations = violations  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyTotalViolationsDeny, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.severity is not None:
            result['severity'] = self.severity
        if self.violations is not None:
            result['violations'] = self.violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('violations') is not None:
            self.violations = m.get('violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyTotalViolationsWarn(TeaModel):
    def __init__(self, severity=None, violations=None):
        # 策略治理等级
        self.severity = severity  # type: str
        # 告警的事件计数
        self.violations = violations  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyTotalViolationsWarn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.severity is not None:
            result['severity'] = self.severity
        if self.violations is not None:
            result['violations'] = self.violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('violations') is not None:
            self.violations = m.get('violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyTotalViolations(TeaModel):
    def __init__(self, deny=None, warn=None):
        # 被拦截的不同治理等级的违规计数统计
        self.deny = deny  # type: DescribePolicyGovernanceInClusterResponseBodyTotalViolationsDeny
        # 告警模式下不同治理等级的违规计数统计
        self.warn = warn  # type: DescribePolicyGovernanceInClusterResponseBodyTotalViolationsWarn

    def validate(self):
        if self.deny:
            self.deny.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyTotalViolations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deny is not None:
            result['deny'] = self.deny.to_map()
        if self.warn is not None:
            result['warn'] = self.warn.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deny') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyTotalViolationsDeny()
            self.deny = temp_model.from_map(m['deny'])
        if m.get('warn') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyTotalViolationsWarn()
            self.warn = temp_model.from_map(m['warn'])
        return self


class DescribePolicyGovernanceInClusterResponseBodyViolationsDeny(TeaModel):
    def __init__(self, policy_description=None, policy_name=None, severity=None, violations=None):
        # 策略描述
        self.policy_description = policy_description  # type: str
        # 策略名称
        self.policy_name = policy_name  # type: str
        # 策略治理等级
        self.severity = severity  # type: str
        # 对应规则的事件计数
        self.violations = violations  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyViolationsDeny, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['policyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.severity is not None:
            result['severity'] = self.severity
        if self.violations is not None:
            result['violations'] = self.violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('policyDescription') is not None:
            self.policy_description = m.get('policyDescription')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('violations') is not None:
            self.violations = m.get('violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyViolationsWarn(TeaModel):
    def __init__(self, policy_description=None, policy_name=None, severity=None, violations=None):
        # 策略描述
        self.policy_description = policy_description  # type: str
        # 策略名称
        self.policy_name = policy_name  # type: str
        # 策略治理等级
        self.severity = severity  # type: str
        # 对应规则的事件计数
        self.violations = violations  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyViolationsWarn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['policyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.severity is not None:
            result['severity'] = self.severity
        if self.violations is not None:
            result['violations'] = self.violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('policyDescription') is not None:
            self.policy_description = m.get('policyDescription')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('violations') is not None:
            self.violations = m.get('violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyViolations(TeaModel):
    def __init__(self, deny=None, warn=None):
        # 被拦截的不同策略类型的审计计数
        self.deny = deny  # type: DescribePolicyGovernanceInClusterResponseBodyViolationsDeny
        # 告警的不同策略类型审计计数
        self.warn = warn  # type: DescribePolicyGovernanceInClusterResponseBodyViolationsWarn

    def validate(self):
        if self.deny:
            self.deny.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyViolations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deny is not None:
            result['deny'] = self.deny.to_map()
        if self.warn is not None:
            result['warn'] = self.warn.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deny') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyViolationsDeny()
            self.deny = temp_model.from_map(m['deny'])
        if m.get('warn') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyViolationsWarn()
            self.warn = temp_model.from_map(m['warn'])
        return self


class DescribePolicyGovernanceInClusterResponseBody(TeaModel):
    def __init__(self, admit_log=None, on_state=None, total_violations=None, violations=None):
        # 集群当前策略治理审计日志
        self.admit_log = admit_log  # type: DescribePolicyGovernanceInClusterResponseBodyAdmitLog
        # 当前集群中开启的不同等级策略计数统计
        self.on_state = on_state  # type: list[DescribePolicyGovernanceInClusterResponseBodyOnState]
        # 集群中当前被拦截和告警两种处理类型下不同治理等级的违规计数。
        self.total_violations = total_violations  # type: DescribePolicyGovernanceInClusterResponseBodyTotalViolations
        # 集群中针对不同策略类型的拦截和告警的审计计数统计列表
        self.violations = violations  # type: DescribePolicyGovernanceInClusterResponseBodyViolations

    def validate(self):
        if self.admit_log:
            self.admit_log.validate()
        if self.on_state:
            for k in self.on_state:
                if k:
                    k.validate()
        if self.total_violations:
            self.total_violations.validate()
        if self.violations:
            self.violations.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admit_log is not None:
            result['admit_log'] = self.admit_log.to_map()
        result['on_state'] = []
        if self.on_state is not None:
            for k in self.on_state:
                result['on_state'].append(k.to_map() if k else None)
        if self.total_violations is not None:
            result['totalViolations'] = self.total_violations.to_map()
        if self.violations is not None:
            result['violations'] = self.violations.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('admit_log') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyAdmitLog()
            self.admit_log = temp_model.from_map(m['admit_log'])
        self.on_state = []
        if m.get('on_state') is not None:
            for k in m.get('on_state'):
                temp_model = DescribePolicyGovernanceInClusterResponseBodyOnState()
                self.on_state.append(temp_model.from_map(k))
        if m.get('totalViolations') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyTotalViolations()
            self.total_violations = temp_model.from_map(m['totalViolations'])
        if m.get('violations') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyViolations()
            self.violations = temp_model.from_map(m['violations'])
        return self


class DescribePolicyGovernanceInClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePolicyGovernanceInClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponse, self).to_map()
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
            temp_model = DescribePolicyGovernanceInClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyInstancesRequest(TeaModel):
    def __init__(self, instance_name=None, policy_name=None):
        # 策略实例名称
        self.instance_name = instance_name  # type: str
        # 策略类型
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.policy_name is not None:
            result['policy_name'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')
        return self


class DescribePolicyInstancesResponseBody(TeaModel):
    def __init__(self, ali_uid=None, cluster_id=None, instance_name=None, policy_name=None, policy_category=None,
                 policy_description=None, policy_parameters=None, policy_severity=None, policy_scope=None, policy_action=None):
        # 策略实例实施者UID
        self.ali_uid = ali_uid  # type: str
        # 目标集群ID
        self.cluster_id = cluster_id  # type: str
        # 规则实例名称
        self.instance_name = instance_name  # type: str
        # 策略治理规则名称
        self.policy_name = policy_name  # type: str
        # 策略类型名称
        self.policy_category = policy_category  # type: str
        # 规则模板描述
        self.policy_description = policy_description  # type: str
        # 当前规则实例的配置参数
        self.policy_parameters = policy_parameters  # type: str
        # 规则实例治理等级
        self.policy_severity = policy_severity  # type: str
        # 策略实例实施范围： 默认"*"代表集群所有ns 否则返回作用namespaces名称，多个namespaces以逗号分隔
        self.policy_scope = policy_scope  # type: str
        # 规则治理动作  deny: 拦截违规部署  warn：告警
        self.policy_action = policy_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['ali_uid'] = self.ali_uid
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.policy_name is not None:
            result['policy_name'] = self.policy_name
        if self.policy_category is not None:
            result['policy_category'] = self.policy_category
        if self.policy_description is not None:
            result['policy_description'] = self.policy_description
        if self.policy_parameters is not None:
            result['policy_parameters'] = self.policy_parameters
        if self.policy_severity is not None:
            result['policy_severity'] = self.policy_severity
        if self.policy_scope is not None:
            result['policy_scope'] = self.policy_scope
        if self.policy_action is not None:
            result['policy_action'] = self.policy_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ali_uid') is not None:
            self.ali_uid = m.get('ali_uid')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')
        if m.get('policy_category') is not None:
            self.policy_category = m.get('policy_category')
        if m.get('policy_description') is not None:
            self.policy_description = m.get('policy_description')
        if m.get('policy_parameters') is not None:
            self.policy_parameters = m.get('policy_parameters')
        if m.get('policy_severity') is not None:
            self.policy_severity = m.get('policy_severity')
        if m.get('policy_scope') is not None:
            self.policy_scope = m.get('policy_scope')
        if m.get('policy_action') is not None:
            self.policy_action = m.get('policy_action')
        return self


class DescribePolicyInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[DescribePolicyInstancesResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribePolicyInstancesResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribePolicyInstancesStatusResponseBodyPolicyInstances(TeaModel):
    def __init__(self, policy_category=None, policy_description=None, policy_instances_count=None,
                 policy_name=None, policy_severity=None):
        self.policy_category = policy_category  # type: str
        self.policy_description = policy_description  # type: str
        self.policy_instances_count = policy_instances_count  # type: long
        self.policy_name = policy_name  # type: str
        self.policy_severity = policy_severity  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponseBodyPolicyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_category is not None:
            result['policy_category'] = self.policy_category
        if self.policy_description is not None:
            result['policy_description'] = self.policy_description
        if self.policy_instances_count is not None:
            result['policy_instances_count'] = self.policy_instances_count
        if self.policy_name is not None:
            result['policy_name'] = self.policy_name
        if self.policy_severity is not None:
            result['policy_severity'] = self.policy_severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('policy_category') is not None:
            self.policy_category = m.get('policy_category')
        if m.get('policy_description') is not None:
            self.policy_description = m.get('policy_description')
        if m.get('policy_instances_count') is not None:
            self.policy_instances_count = m.get('policy_instances_count')
        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')
        if m.get('policy_severity') is not None:
            self.policy_severity = m.get('policy_severity')
        return self


class DescribePolicyInstancesStatusResponseBody(TeaModel):
    def __init__(self, instances_severity_count=None, policy_instances=None):
        self.instances_severity_count = instances_severity_count  # type: dict[str, any]
        # 不同策略类型下的策略实例计数列表
        self.policy_instances = policy_instances  # type: list[DescribePolicyInstancesStatusResponseBodyPolicyInstances]

    def validate(self):
        if self.policy_instances:
            for k in self.policy_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances_severity_count is not None:
            result['instances_severity_count'] = self.instances_severity_count
        result['policy_instances'] = []
        if self.policy_instances is not None:
            for k in self.policy_instances:
                result['policy_instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instances_severity_count') is not None:
            self.instances_severity_count = m.get('instances_severity_count')
        self.policy_instances = []
        if m.get('policy_instances') is not None:
            for k in m.get('policy_instances'):
                temp_model = DescribePolicyInstancesStatusResponseBodyPolicyInstances()
                self.policy_instances.append(temp_model.from_map(k))
        return self


class DescribePolicyInstancesStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePolicyInstancesStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponse, self).to_map()
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
            temp_model = DescribePolicyInstancesStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskInfoResponseBodyTaskResult(TeaModel):
    def __init__(self, data=None, status=None):
        # 操作的资源，例如：实例ID。
        self.data = data  # type: str
        # 资源的状态。
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskInfoResponseBodyTaskResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeTaskInfoResponseBody(TeaModel):
    def __init__(self, cluster_id=None, created=None, state=None, task_id=None, task_result=None, task_type=None,
                 updated=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 任务创建时间。
        self.created = created  # type: str
        # 任务当前状态。
        self.state = state  # type: str
        # 任务ID。
        self.task_id = task_id  # type: str
        # 任务执行详情。
        self.task_result = task_result  # type: list[DescribeTaskInfoResponseBodyTaskResult]
        # 当前任务类型。
        self.task_type = task_type  # type: str
        # 任务更新时间。
        self.updated = updated  # type: str

    def validate(self):
        if self.task_result:
            for k in self.task_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTaskInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.created is not None:
            result['created'] = self.created
        if self.state is not None:
            result['state'] = self.state
        if self.task_id is not None:
            result['task_id'] = self.task_id
        result['task_result'] = []
        if self.task_result is not None:
            for k in self.task_result:
                result['task_result'].append(k.to_map() if k else None)
        if self.task_type is not None:
            result['task_type'] = self.task_type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        self.task_result = []
        if m.get('task_result') is not None:
            for k in m.get('task_result'):
                temp_model = DescribeTaskInfoResponseBodyTaskResult()
                self.task_result.append(temp_model.from_map(k))
        if m.get('task_type') is not None:
            self.task_type = m.get('task_type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeTaskInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTaskInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTaskInfoResponse, self).to_map()
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
            temp_model = DescribeTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplateAttributeRequest(TeaModel):
    def __init__(self, template_type=None):
        # 模板类型，值为创建部署模板时指定的模板类型。
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        return self


class DescribeTemplateAttributeResponseBody(TeaModel):
    def __init__(self, id=None, acl=None, name=None, template=None, template_type=None, description=None, tags=None,
                 template_with_hist_id=None, created=None, updated=None):
        # 编排模板ID，模板每次修改，这个ID都会改变。	
        self.id = id  # type: str
        # 编排模板权限。取值：private，public，shared。
        self.acl = acl  # type: str
        # 编排模板名称。	
        self.name = name  # type: str
        # 编排模板内容。	
        self.template = template  # type: str
        # 编排模板类型
        self.template_type = template_type  # type: str
        # 编排模板描述。
        self.description = description  # type: str
        # 部署模板的标签。
        self.tags = tags  # type: str
        # 编排模板ID，该ID唯一不随更新而改变。	
        self.template_with_hist_id = template_with_hist_id  # type: str
        # 编排模板创建时间。
        self.created = created  # type: str
        # 编排模板修改时间。	
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.acl is not None:
            result['acl'] = self.acl
        if self.name is not None:
            result['name'] = self.name
        if self.template is not None:
            result['template'] = self.template
        if self.template_type is not None:
            result['template_type'] = self.template_type
        if self.description is not None:
            result['description'] = self.description
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template_with_hist_id is not None:
            result['template_with_hist_id'] = self.template_with_hist_id
        if self.created is not None:
            result['created'] = self.created
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('template_with_hist_id') is not None:
            self.template_with_hist_id = m.get('template_with_hist_id')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeTemplateAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[DescribeTemplateAttributeResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTemplateAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeTemplateAttributeResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeTemplatesRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, template_type=None):
        # 对查询结果进行分页处理，指定返回第几页的数据。  默认值为 1
        self.page_num = page_num  # type: long
        # 对查询结果进行分页处理，指定每页包含的数据条数。  默认值为 10
        self.page_size = page_size  # type: long
        # 模板类型，部署模板类型，目前一共有2种类型，取值为：kubernetes或compose。
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['page_num'] = self.page_num
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page_num') is not None:
            self.page_num = m.get('page_num')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        return self


class DescribeTemplatesResponseBodyPageInfo(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        # 当前页数。
        self.page_number = page_number  # type: long
        # 单页最大数据条数。
        self.page_size = page_size  # type: long
        # 结果总数。
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplatesResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, acl=None, created=None, description=None, id=None, name=None, tags=None, template=None,
                 template_type=None, template_with_hist_id=None, updated=None):
        # 模板访问权限，取值为：private、pubilc或shared。。
        self.acl = acl  # type: str
        # 模板创建时间。
        self.created = created  # type: str
        # 模板描述信息。
        self.description = description  # type: str
        # 模板ID。会模板随着更新而变化。
        self.id = id  # type: str
        # 模板名称。
        self.name = name  # type: str
        # 模板标签，如果不显式指定了，默认为模板名称。
        self.tags = tags  # type: str
        # 模板详情。
        self.template = template  # type: str
        # 部署模板类型。
        self.template_type = template_type  # type: str
        # 模板唯一ID。
        self.template_with_hist_id = template_with_hist_id  # type: str
        # 模板修改时间。
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template is not None:
            result['template'] = self.template
        if self.template_type is not None:
            result['template_type'] = self.template_type
        if self.template_with_hist_id is not None:
            result['template_with_hist_id'] = self.template_with_hist_id
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        if m.get('template_with_hist_id') is not None:
            self.template_with_hist_id = m.get('template_with_hist_id')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeTemplatesResponseBody(TeaModel):
    def __init__(self, page_info=None, templates=None):
        # 分页信息。
        self.page_info = page_info  # type: DescribeTemplatesResponseBodyPageInfo
        # 模板列表。
        self.templates = templates  # type: list[DescribeTemplatesResponseBodyTemplates]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        result['templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page_info') is not None:
            temp_model = DescribeTemplatesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        self.templates = []
        if m.get('templates') is not None:
            for k in m.get('templates'):
                temp_model = DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class DescribeTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTemplatesResponse, self).to_map()
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
            temp_model = DescribeTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTriggerRequest(TeaModel):
    def __init__(self, name=None, namespace=None, type=None, action=None):
        # 应用名称。
        self.name = name  # type: str
        # 应用所属命名空间。
        self.namespace = namespace  # type: str
        # 应用类型。
        self.type = type  # type: str
        # 触发器行为。
        self.action = action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class DescribeTriggerResponseBody(TeaModel):
    def __init__(self, id=None, name=None, cluster_id=None, project_id=None, type=None, action=None, token=None):
        # 触发器ID。
        self.id = id  # type: str
        # 触发器名称。
        self.name = name  # type: str
        # 集群ID
        self.cluster_id = cluster_id  # type: str
        # 触发器项目名称
        self.project_id = project_id  # type: str
        # 触发器类型。
        self.type = type  # type: str
        # 触发器行为
        self.action = action  # type: str
        # Token
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        if self.action is not None:
            result['action'] = self.action
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class DescribeTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[DescribeTriggerResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeTriggerResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeUserPermissionResponseBody(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, role_name=None, role_type=None, is_owner=None,
                 is_ram_role=None):
        # 集群访问配置
        self.resource_id = resource_id  # type: str
        # 授权类型
        self.resource_type = resource_type  # type: str
        # 自定义角色名称
        self.role_name = role_name  # type: str
        # 预置的角色类型
        self.role_type = role_type  # type: str
        # 是否为集群 owner 的授权
        self.is_owner = is_owner  # type: long
        # 是否为ram 角色授权
        self.is_ram_role = is_ram_role  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserPermissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resource_id'] = self.resource_id
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.role_name is not None:
            result['role_name'] = self.role_name
        if self.role_type is not None:
            result['role_type'] = self.role_type
        if self.is_owner is not None:
            result['is_owner'] = self.is_owner
        if self.is_ram_role is not None:
            result['is_ram_role'] = self.is_ram_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resource_id') is not None:
            self.resource_id = m.get('resource_id')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('role_name') is not None:
            self.role_name = m.get('role_name')
        if m.get('role_type') is not None:
            self.role_type = m.get('role_type')
        if m.get('is_owner') is not None:
            self.is_owner = m.get('is_owner')
        if m.get('is_ram_role') is not None:
            self.is_ram_role = m.get('is_ram_role')
        return self


class DescribeUserPermissionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[DescribeUserPermissionResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserPermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeUserPermissionResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeUserQuotaResponseBody(TeaModel):
    def __init__(self, amk_cluster_quota=None, ask_cluster_quota=None, cluster_nodepool_quota=None,
                 cluster_quota=None, node_quota=None):
        # 托管版集群配额。
        self.amk_cluster_quota = amk_cluster_quota  # type: long
        # Serverless集群配额。
        self.ask_cluster_quota = ask_cluster_quota  # type: long
        # 集群节点池配额。
        self.cluster_nodepool_quota = cluster_nodepool_quota  # type: long
        # 专有版集群托管版集群的总配额。
        self.cluster_quota = cluster_quota  # type: long
        # 单集群的节点配额。
        self.node_quota = node_quota  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amk_cluster_quota is not None:
            result['amk_cluster_quota'] = self.amk_cluster_quota
        if self.ask_cluster_quota is not None:
            result['ask_cluster_quota'] = self.ask_cluster_quota
        if self.cluster_nodepool_quota is not None:
            result['cluster_nodepool_quota'] = self.cluster_nodepool_quota
        if self.cluster_quota is not None:
            result['cluster_quota'] = self.cluster_quota
        if self.node_quota is not None:
            result['node_quota'] = self.node_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('amk_cluster_quota') is not None:
            self.amk_cluster_quota = m.get('amk_cluster_quota')
        if m.get('ask_cluster_quota') is not None:
            self.ask_cluster_quota = m.get('ask_cluster_quota')
        if m.get('cluster_nodepool_quota') is not None:
            self.cluster_nodepool_quota = m.get('cluster_nodepool_quota')
        if m.get('cluster_quota') is not None:
            self.cluster_quota = m.get('cluster_quota')
        if m.get('node_quota') is not None:
            self.node_quota = m.get('node_quota')
        return self


class DescribeUserQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserQuotaResponse, self).to_map()
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
            temp_model = DescribeUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkflowsResponseBodyJobs(TeaModel):
    def __init__(self, cluster_id=None, create_time=None, job_name=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 工作流创建时间。
        self.create_time = create_time  # type: str
        # 工作流名称。
        self.job_name = job_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWorkflowsResponseBodyJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.create_time is not None:
            result['create_time'] = self.create_time
        if self.job_name is not None:
            result['job_name'] = self.job_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('create_time') is not None:
            self.create_time = m.get('create_time')
        if m.get('job_name') is not None:
            self.job_name = m.get('job_name')
        return self


class DescribeWorkflowsResponseBody(TeaModel):
    def __init__(self, jobs=None):
        # job信息
        self.jobs = jobs  # type: list[DescribeWorkflowsResponseBodyJobs]

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWorkflowsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = DescribeWorkflowsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        return self


class DescribeWorkflowsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeWorkflowsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWorkflowsResponse, self).to_map()
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
            temp_model = DescribeWorkflowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EdgeClusterAddEdgeMachineRequest(TeaModel):
    def __init__(self, expired=None, nodepool_id=None, options=None):
        # expired
        self.expired = expired  # type: long
        # nodepool_id
        self.nodepool_id = nodepool_id  # type: str
        # options
        self.options = options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EdgeClusterAddEdgeMachineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired is not None:
            result['expired'] = self.expired
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.options is not None:
            result['options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('options') is not None:
            self.options = m.get('options')
        return self


class EdgeClusterAddEdgeMachineResponseBody(TeaModel):
    def __init__(self, edge_machine_id=None, request_id=None):
        # edge machine id
        self.edge_machine_id = edge_machine_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EdgeClusterAddEdgeMachineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_machine_id is not None:
            result['edge_machine_id'] = self.edge_machine_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('edge_machine_id') is not None:
            self.edge_machine_id = m.get('edge_machine_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class EdgeClusterAddEdgeMachineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EdgeClusterAddEdgeMachineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EdgeClusterAddEdgeMachineResponse, self).to_map()
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
            temp_model = EdgeClusterAddEdgeMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKubernetesTriggerRequest(TeaModel):
    def __init__(self, name=None, namespace=None, type=None, action=None):
        # 应用名称。
        self.name = name  # type: str
        # 应用所属命名空间。
        self.namespace = namespace  # type: str
        # 应用类型。
        self.type = type  # type: str
        # 触发器行为。
        self.action = action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKubernetesTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class GetKubernetesTriggerResponseBody(TeaModel):
    def __init__(self, id=None, name=None, cluster_id=None, project_id=None, type=None, action=None, token=None):
        # 触发器ID。
        self.id = id  # type: str
        # 触发器名称。
        self.name = name  # type: str
        # 集群ID
        self.cluster_id = cluster_id  # type: str
        # 触发器项目名称
        self.project_id = project_id  # type: str
        # 触发器类型。
        self.type = type  # type: str
        # 触发器行为
        self.action = action  # type: str
        # Token
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKubernetesTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        if self.action is not None:
            result['action'] = self.action
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetKubernetesTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: list[GetKubernetesTriggerResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetKubernetesTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = GetKubernetesTriggerResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class GetUpgradeStatusResponseBodyUpgradeTask(TeaModel):
    def __init__(self, message=None, status=None):
        # 任务描述信息。
        self.message = message  # type: str
        # 任务状态：  emptry、running、success、failed
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUpgradeStatusResponseBodyUpgradeTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetUpgradeStatusResponseBody(TeaModel):
    def __init__(self, error_message=None, precheck_report_id=None, status=None, upgrade_step=None,
                 upgrade_task=None):
        # 错误信息描述。
        self.error_message = error_message  # type: str
        # 预检查返回ID。
        self.precheck_report_id = precheck_report_id  # type: str
        # 升级状态。
        self.status = status  # type: str
        # 升级任务执行到哪一步了。
        self.upgrade_step = upgrade_step  # type: str
        # 升级任务详情。
        self.upgrade_task = upgrade_task  # type: GetUpgradeStatusResponseBodyUpgradeTask

    def validate(self):
        if self.upgrade_task:
            self.upgrade_task.validate()

    def to_map(self):
        _map = super(GetUpgradeStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.precheck_report_id is not None:
            result['precheck_report_id'] = self.precheck_report_id
        if self.status is not None:
            result['status'] = self.status
        if self.upgrade_step is not None:
            result['upgrade_step'] = self.upgrade_step
        if self.upgrade_task is not None:
            result['upgrade_task'] = self.upgrade_task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('precheck_report_id') is not None:
            self.precheck_report_id = m.get('precheck_report_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('upgrade_step') is not None:
            self.upgrade_step = m.get('upgrade_step')
        if m.get('upgrade_task') is not None:
            temp_model = GetUpgradeStatusResponseBodyUpgradeTask()
            self.upgrade_task = temp_model.from_map(m['upgrade_task'])
        return self


class GetUpgradeStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUpgradeStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUpgradeStatusResponse, self).to_map()
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
            temp_model = GetUpgradeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantPermissionsRequestBody(TeaModel):
    def __init__(self, cluster=None, is_custom=None, is_ram_role=None, namespace=None, role_name=None,
                 role_type=None):
        # 授权目标集群id
        self.cluster = cluster  # type: str
        # 该授权是否是自定义授权
        self.is_custom = is_custom  # type: bool
        # 是否是 RAM 角色授权
        self.is_ram_role = is_ram_role  # type: bool
        # 命名空间名称
        self.namespace = namespace  # type: str
        # 预置的角色名称
        self.role_name = role_name  # type: str
        # 授权类型
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantPermissionsRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.is_custom is not None:
            result['is_custom'] = self.is_custom
        if self.is_ram_role is not None:
            result['is_ram_role'] = self.is_ram_role
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.role_name is not None:
            result['role_name'] = self.role_name
        if self.role_type is not None:
            result['role_type'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('is_custom') is not None:
            self.is_custom = m.get('is_custom')
        if m.get('is_ram_role') is not None:
            self.is_ram_role = m.get('is_ram_role')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('role_name') is not None:
            self.role_name = m.get('role_name')
        if m.get('role_type') is not None:
            self.role_type = m.get('role_type')
        return self


class GrantPermissionsRequest(TeaModel):
    def __init__(self, body=None):
        # 请求体参数
        self.body = body  # type: list[GrantPermissionsRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GrantPermissionsRequest, self).to_map()
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
                temp_model = GrantPermissionsRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class GrantPermissionsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(GrantPermissionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class InstallClusterAddonsRequestBody(TeaModel):
    def __init__(self, config=None, name=None, version=None):
        # 组件配置信息。
        self.config = config  # type: str
        # 组件名称。
        self.name = name  # type: str
        # 组件版本号。
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallClusterAddonsRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class InstallClusterAddonsRequest(TeaModel):
    def __init__(self, body=None):
        # Addon列表。
        self.body = body  # type: list[InstallClusterAddonsRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InstallClusterAddonsRequest, self).to_map()
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
                temp_model = InstallClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class InstallClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(InstallClusterAddonsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, next_token=None, region_id=None, resource_ids=None, resource_type=None, tags=None):
        # 下一次查询Token。
        self.next_token = next_token  # type: str
        # 地域ID
        self.region_id = region_id  # type: str
        # 集群ID列表。
        self.resource_ids = resource_ids  # type: list[str]
        # 资源类型，只支持Cluster
        self.resource_type = resource_type  # type: str
        # 按标签查找。
        self.tags = tags  # type: list[Tag]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['next_token'] = self.next_token
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(self, next_token=None, region_id=None, resource_ids_shrink=None, resource_type=None,
                 tags_shrink=None):
        # 下一次查询Token。
        self.next_token = next_token  # type: str
        # 地域ID
        self.region_id = region_id  # type: str
        # 集群ID列表。
        self.resource_ids_shrink = resource_ids_shrink  # type: str
        # 资源类型，只支持Cluster
        self.resource_type = resource_type  # type: str
        # 按标签查找。
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['next_token'] = self.next_token
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['resource_ids'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids_shrink = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # 资源ID。
        self.resource_id = resource_id  # type: str
        # 资源类型。
        self.resource_type = resource_type  # type: str
        # 标签key。
        self.tag_key = tag_key  # type: str
        # 标签值。
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resource_id'] = self.resource_id
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.tag_key is not None:
            result['tag_key'] = self.tag_key
        if self.tag_value is not None:
            result['tag_value'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resource_id') is not None:
            self.resource_id = m.get('resource_id')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('tag_key') is not None:
            self.tag_key = m.get('tag_key')
        if m.get('tag_value') is not None:
            self.tag_value = m.get('tag_value')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        # 资源标签。
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tag_resource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['tag_resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('tag_resource') is not None:
            for k in m.get('tag_resource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        # 下一个查询开始Token，为空说明没有下一个
        self.next_token = next_token  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str
        # 资源标签列表。
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['next_token'] = self.next_token
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.tag_resources is not None:
            result['tag_resources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('tag_resources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['tag_resources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(MigrateClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ModifyClusterRequest(TeaModel):
    def __init__(self, api_server_eip=None, api_server_eip_id=None, deletion_protection=None, enable_rrsa=None,
                 ingress_domain_rebinding=None, ingress_loadbalancer_id=None, instance_deletion_protection=None, maintenance_window=None,
                 resource_group_id=None):
        # 集群是否绑定EIP，用于公网访问API Server。 true | false
        self.api_server_eip = api_server_eip  # type: bool
        # 集群API Server 公网连接端点。
        self.api_server_eip_id = api_server_eip_id  # type: str
        # 集群是否开启删除保护。默认值false。
        self.deletion_protection = deletion_protection  # type: bool
        # 启用或禁用 RRSA 功能。true: 启用，false: 禁用
        self.enable_rrsa = enable_rrsa  # type: bool
        # 域名是否重新绑定到Ingress的SLB地址。
        self.ingress_domain_rebinding = ingress_domain_rebinding  # type: str
        # 集群的Ingress SLB的ID。
        self.ingress_loadbalancer_id = ingress_loadbalancer_id  # type: str
        # 实例删除保护，防止通过控制台或API误删除释放节点。
        self.instance_deletion_protection = instance_deletion_protection  # type: bool
        self.maintenance_window = maintenance_window  # type: MaintenanceWindow
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()

    def to_map(self):
        _map = super(ModifyClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip is not None:
            result['api_server_eip'] = self.api_server_eip
        if self.api_server_eip_id is not None:
            result['api_server_eip_id'] = self.api_server_eip_id
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.enable_rrsa is not None:
            result['enable_rrsa'] = self.enable_rrsa
        if self.ingress_domain_rebinding is not None:
            result['ingress_domain_rebinding'] = self.ingress_domain_rebinding
        if self.ingress_loadbalancer_id is not None:
            result['ingress_loadbalancer_id'] = self.ingress_loadbalancer_id
        if self.instance_deletion_protection is not None:
            result['instance_deletion_protection'] = self.instance_deletion_protection
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('api_server_eip') is not None:
            self.api_server_eip = m.get('api_server_eip')
        if m.get('api_server_eip_id') is not None:
            self.api_server_eip_id = m.get('api_server_eip_id')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('enable_rrsa') is not None:
            self.enable_rrsa = m.get('enable_rrsa')
        if m.get('ingress_domain_rebinding') is not None:
            self.ingress_domain_rebinding = m.get('ingress_domain_rebinding')
        if m.get('ingress_loadbalancer_id') is not None:
            self.ingress_loadbalancer_id = m.get('ingress_loadbalancer_id')
        if m.get('instance_deletion_protection') is not None:
            self.instance_deletion_protection = m.get('instance_deletion_protection')
        if m.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m['maintenance_window'])
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        return self


class ModifyClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str
        # 任务ID。
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ModifyClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyClusterResponse, self).to_map()
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
            temp_model = ModifyClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterAddonRequest(TeaModel):
    def __init__(self, config=None):
        # 自定义参数设置
        self.config = config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterAddonRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class ModifyClusterAddonResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(ModifyClusterAddonResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ModifyClusterConfigurationRequestCustomizeConfigConfigs(TeaModel):
    def __init__(self, key=None, value=None):
        # key值。
        self.key = key  # type: str
        # value值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterConfigurationRequestCustomizeConfigConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ModifyClusterConfigurationRequestCustomizeConfig(TeaModel):
    def __init__(self, configs=None, name=None):
        # 组件配置。
        self.configs = configs  # type: list[ModifyClusterConfigurationRequestCustomizeConfigConfigs]
        # 组件名称。
        self.name = name  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyClusterConfigurationRequestCustomizeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = ModifyClusterConfigurationRequestCustomizeConfigConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ModifyClusterConfigurationRequest(TeaModel):
    def __init__(self, customize_config=None):
        # 自定义配置。
        self.customize_config = customize_config  # type: list[ModifyClusterConfigurationRequestCustomizeConfig]

    def validate(self):
        if self.customize_config:
            for k in self.customize_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyClusterConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['customize_config'] = []
        if self.customize_config is not None:
            for k in self.customize_config:
                result['customize_config'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.customize_config = []
        if m.get('customize_config') is not None:
            for k in m.get('customize_config'):
                temp_model = ModifyClusterConfigurationRequestCustomizeConfig()
                self.customize_config.append(temp_model.from_map(k))
        return self


class ModifyClusterConfigurationResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(ModifyClusterConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ModifyClusterNodePoolRequestAutoScaling(TeaModel):
    def __init__(self, eip_bandwidth=None, eip_internet_charge_type=None, enable=None, is_bond_eip=None,
                 max_instances=None, min_instances=None, type=None):
        # 带宽峰值。
        self.eip_bandwidth = eip_bandwidth  # type: long
        # EIP计费类型。
        self.eip_internet_charge_type = eip_internet_charge_type  # type: str
        # 是否开启自动伸缩。
        self.enable = enable  # type: bool
        # 是否绑定EIP。
        self.is_bond_eip = is_bond_eip  # type: bool
        # 最大实例数。
        self.max_instances = max_instances  # type: long
        # 最小实例数。
        self.min_instances = min_instances  # type: long
        # 自动伸缩节点类型。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequestAutoScaling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_bandwidth is not None:
            result['eip_bandwidth'] = self.eip_bandwidth
        if self.eip_internet_charge_type is not None:
            result['eip_internet_charge_type'] = self.eip_internet_charge_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.is_bond_eip is not None:
            result['is_bond_eip'] = self.is_bond_eip
        if self.max_instances is not None:
            result['max_instances'] = self.max_instances
        if self.min_instances is not None:
            result['min_instances'] = self.min_instances
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eip_bandwidth') is not None:
            self.eip_bandwidth = m.get('eip_bandwidth')
        if m.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = m.get('eip_internet_charge_type')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('is_bond_eip') is not None:
            self.is_bond_eip = m.get('is_bond_eip')
        if m.get('max_instances') is not None:
            self.max_instances = m.get('max_instances')
        if m.get('min_instances') is not None:
            self.min_instances = m.get('min_instances')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModifyClusterNodePoolRequestKubernetesConfig(TeaModel):
    def __init__(self, cms_enabled=None, cpu_policy=None, labels=None, runtime=None, runtime_version=None,
                 taints=None, user_data=None):
        # 是否开启云监控。
        self.cms_enabled = cms_enabled  # type: bool
        # CPU管理策略。
        self.cpu_policy = cpu_policy  # type: str
        # 节点标签。
        self.labels = labels  # type: list[Tag]
        # 容器运行时。
        self.runtime = runtime  # type: str
        # 容器运行时版本。
        self.runtime_version = runtime_version  # type: str
        # 污点配置。
        self.taints = taints  # type: list[Taint]
        # 实例自定义数据。
        self.user_data = user_data  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequestKubernetesConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = Tag()
                self.labels.append(temp_model.from_map(k))
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class ModifyClusterNodePoolRequestManagementUpgradeConfig(TeaModel):
    def __init__(self, auto_upgrade=None, max_unavailable=None, surge=None, surge_percentage=None):
        # 是否启用自动升级，自修复。
        self.auto_upgrade = auto_upgrade  # type: bool
        # 最大不可用节点数量。
        self.max_unavailable = max_unavailable  # type: long
        # 额外节点数量。
        self.surge = surge  # type: long
        # 额外节点比例， 和surge 二选一。
        self.surge_percentage = surge_percentage  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequestManagementUpgradeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade
        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable
        if self.surge is not None:
            result['surge'] = self.surge
        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('max_unavailable') is not None:
            self.max_unavailable = m.get('max_unavailable')
        if m.get('surge') is not None:
            self.surge = m.get('surge')
        if m.get('surge_percentage') is not None:
            self.surge_percentage = m.get('surge_percentage')
        return self


class ModifyClusterNodePoolRequestManagement(TeaModel):
    def __init__(self, auto_repair=None, enable=None, upgrade_config=None):
        # 是否开启自动修复。
        self.auto_repair = auto_repair  # type: bool
        # 是否启用托管节点池。
        self.enable = enable  # type: bool
        # 自动升级配置。
        self.upgrade_config = upgrade_config  # type: ModifyClusterNodePoolRequestManagementUpgradeConfig

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequestManagement, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.enable is not None:
            result['enable'] = self.enable
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = ModifyClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class ModifyClusterNodePoolRequestNodepoolInfo(TeaModel):
    def __init__(self, name=None, resource_group_id=None):
        # 节点池名称。
        self.name = name  # type: str
        # 资源组ID。
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequestNodepoolInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        return self


class ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        # 抢占式实例规格
        self.instance_type = instance_type  # type: str
        # 单台实例上限价格，单位：元/小时。
        self.price_limit = price_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.price_limit is not None:
            result['price_limit'] = self.price_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')
        if m.get('price_limit') is not None:
            self.price_limit = m.get('price_limit')
        return self


class ModifyClusterNodePoolRequestScalingGroup(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, compensate_with_on_demand=None, data_disks=None,
                 image_id=None, instance_charge_type=None, instance_types=None, internet_charge_type=None,
                 internet_max_bandwidth_out=None, key_pair=None, login_password=None, multi_az_policy=None, on_demand_base_capacity=None,
                 on_demand_percentage_above_base_capacity=None, period=None, period_unit=None, platform=None, rds_instances=None, scaling_policy=None,
                 spot_instance_pools=None, spot_instance_remedy=None, spot_price_limit=None, spot_strategy=None,
                 system_disk_category=None, system_disk_performance_level=None, system_disk_size=None, tags=None, vswitch_ids=None):
        # 节点池节点是启用自动续费
        self.auto_renew = auto_renew  # type: bool
        # 节点池节点自动续费周期
        self.auto_renew_period = auto_renew_period  # type: long
        # 当MultiAZPolicy取值为COST_OPTIMIZED时，如果因价格、库存等原因无法创建足够的抢占式实例，是否允许自动尝试创建按量实例满足ECS实例数量要求。取值范围：true：允许。false：不允许。默认值：true
        self.compensate_with_on_demand = compensate_with_on_demand  # type: bool
        # 数据盘配置。
        self.data_disks = data_disks  # type: list[DataDisk]
        # 自定义镜像
        self.image_id = image_id  # type: str
        # 节点付费类型。
        self.instance_charge_type = instance_charge_type  # type: str
        # 节点实例规格。
        self.instance_types = instance_types  # type: list[str]
        # 节点公网IP网络计费类型
        self.internet_charge_type = internet_charge_type  # type: str
        # 节点公网IP出带宽最大值，单位为Mbps（Mega bit per second），取值范围：1~100
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: long
        # 密钥对名称，和login_password二选一。
        self.key_pair = key_pair  # type: str
        # SSH登录密码，和key_pari二选一。
        self.login_password = login_password  # type: str
        # 多可用区伸缩组ECS实例扩缩容策略
        self.multi_az_policy = multi_az_policy  # type: str
        # 伸缩组所需要按量实例个数的最小值，取值范围：0~1000。当按量实例个数少于该值时，将优先创建按量实例。
        self.on_demand_base_capacity = on_demand_base_capacity  # type: long
        # 伸缩组满足最小按量实例数（OnDemandBaseCapacity）要求后，超出的实例中按量实例应占的比例，取值范围：0～100。
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity  # type: long
        # 包年包月时长
        self.period = period  # type: long
        # 付费周期
        self.period_unit = period_unit  # type: str
        # 操作系统发行版。
        self.platform = platform  # type: str
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: list[str]
        # 扩容策略。
        self.scaling_policy = scaling_policy  # type: str
        # 指定可用实例规格的个数，伸缩组将按成本最低的多个规格均衡创建抢占式实例。取值范围：1~10。
        self.spot_instance_pools = spot_instance_pools  # type: long
        # 是否开启补齐抢占式实例。开启后，当收到抢占式实例将被回收的系统消息时，伸缩组将尝试创建新的实例，替换掉将被回收的抢占式实例。
        self.spot_instance_remedy = spot_instance_remedy  # type: bool
        # 抢占实例价格上限配置
        self.spot_price_limit = spot_price_limit  # type: list[ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit]
        # 抢占式实例类型
        self.spot_strategy = spot_strategy  # type: str
        # 节点系统盘类型。
        self.system_disk_category = system_disk_category  # type: str
        # 节点系统盘磁盘性能，只针对ESSD磁盘生效
        self.system_disk_performance_level = system_disk_performance_level  # type: str
        # 节点系统盘大小。
        self.system_disk_size = system_disk_size  # type: long
        # ECS标签。
        self.tags = tags  # type: list[Tag]
        # 节点使用的虚拟交换机ID。
        self.vswitch_ids = vswitch_ids  # type: list[str]

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequestScalingGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_types is not None:
            result['instance_types'] = self.instance_types
        if self.internet_charge_type is not None:
            result['internet_charge_type'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['internet_max_bandwidth_out'] = self.internet_max_bandwidth_out
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.multi_az_policy is not None:
            result['multi_az_policy'] = self.multi_az_policy
        if self.on_demand_base_capacity is not None:
            result['on_demand_base_capacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['on_demand_percentage_above_base_capacity'] = self.on_demand_percentage_above_base_capacity
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.platform is not None:
            result['platform'] = self.platform
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.spot_instance_pools is not None:
            result['spot_instance_pools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['spot_instance_remedy'] = self.spot_instance_remedy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_renew') is not None:
            self.auto_renew = m.get('auto_renew')
        if m.get('auto_renew_period') is not None:
            self.auto_renew_period = m.get('auto_renew_period')
        if m.get('compensate_with_on_demand') is not None:
            self.compensate_with_on_demand = m.get('compensate_with_on_demand')
        self.data_disks = []
        if m.get('data_disks') is not None:
            for k in m.get('data_disks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
        if m.get('instance_types') is not None:
            self.instance_types = m.get('instance_types')
        if m.get('internet_charge_type') is not None:
            self.internet_charge_type = m.get('internet_charge_type')
        if m.get('internet_max_bandwidth_out') is not None:
            self.internet_max_bandwidth_out = m.get('internet_max_bandwidth_out')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        if m.get('multi_az_policy') is not None:
            self.multi_az_policy = m.get('multi_az_policy')
        if m.get('on_demand_base_capacity') is not None:
            self.on_demand_base_capacity = m.get('on_demand_base_capacity')
        if m.get('on_demand_percentage_above_base_capacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('on_demand_percentage_above_base_capacity')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')
        if m.get('spot_instance_pools') is not None:
            self.spot_instance_pools = m.get('spot_instance_pools')
        if m.get('spot_instance_remedy') is not None:
            self.spot_instance_remedy = m.get('spot_instance_remedy')
        self.spot_price_limit = []
        if m.get('spot_price_limit') is not None:
            for k in m.get('spot_price_limit'):
                temp_model = ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')
        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')
        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class ModifyClusterNodePoolRequestTeeConfig(TeaModel):
    def __init__(self, tee_enable=None):
        # 是否为加密计算节点池。
        self.tee_enable = tee_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequestTeeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')
        return self


class ModifyClusterNodePoolRequest(TeaModel):
    def __init__(self, auto_scaling=None, kubernetes_config=None, management=None, nodepool_info=None,
                 scaling_group=None, tee_config=None, update_nodes=None):
        # 自动伸缩节点池配置。
        self.auto_scaling = auto_scaling  # type: ModifyClusterNodePoolRequestAutoScaling
        # 集群配置。
        self.kubernetes_config = kubernetes_config  # type: ModifyClusterNodePoolRequestKubernetesConfig
        # 托管版节点池配置。
        self.management = management  # type: ModifyClusterNodePoolRequestManagement
        # 节点池配置。
        self.nodepool_info = nodepool_info  # type: ModifyClusterNodePoolRequestNodepoolInfo
        # 扩容组配置。
        self.scaling_group = scaling_group  # type: ModifyClusterNodePoolRequestScalingGroup
        # 加密计算配置。
        self.tee_config = tee_config  # type: ModifyClusterNodePoolRequestTeeConfig
        # 是否同步更新节点标签及污点。
        self.update_nodes = update_nodes  # type: bool

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.management:
            self.management.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.tee_config:
            self.tee_config.validate()

    def to_map(self):
        _map = super(ModifyClusterNodePoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()
        if self.management is not None:
            result['management'] = self.management.to_map()
        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()
        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()
        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()
        if self.update_nodes is not None:
            result['update_nodes'] = self.update_nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_scaling') is not None:
            temp_model = ModifyClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('kubernetes_config') is not None:
            temp_model = ModifyClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = ModifyClusterNodePoolRequestManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('nodepool_info') is not None:
            temp_model = ModifyClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = ModifyClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('tee_config') is not None:
            temp_model = ModifyClusterNodePoolRequestTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
        if m.get('update_nodes') is not None:
            self.update_nodes = m.get('update_nodes')
        return self


class ModifyClusterNodePoolResponseBody(TeaModel):
    def __init__(self, nodepool_id=None, task_id=None):
        # 节点池ID。
        self.nodepool_id = nodepool_id  # type: str
        # 任务ID。
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterNodePoolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ModifyClusterNodePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyClusterNodePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyClusterNodePoolResponse, self).to_map()
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
            temp_model = ModifyClusterNodePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterTagsRequest(TeaModel):
    def __init__(self, body=None):
        # 集群标签列表。
        self.body = body  # type: list[Tag]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyClusterTagsRequest, self).to_map()
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
                temp_model = Tag()
                self.body.append(temp_model.from_map(k))
        return self


class ModifyClusterTagsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(ModifyClusterTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ModifyPolicyInstanceRequest(TeaModel):
    def __init__(self, action=None, instance_name=None, namespace=None, parameters=None):
        # 规则治理动作
        self.action = action  # type: str
        # 策略规则实例id
        self.instance_name = instance_name  # type: str
        # 策略实例实施范围
        self.namespace = namespace  # type: str
        # 当前规则实例的配置参数
        self.parameters = parameters  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class ModifyPolicyInstanceResponseBody(TeaModel):
    def __init__(self, instances=None):
        self.instances = instances  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self


class ModifyPolicyInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyPolicyInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPolicyInstanceResponse, self).to_map()
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
            temp_model = ModifyPolicyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenAckServiceRequest(TeaModel):
    def __init__(self, type=None):
        # 要开通的服务类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenAckServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OpenAckServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # 开通服务的订单号。
        self.order_id = order_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenAckServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class OpenAckServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenAckServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenAckServiceResponse, self).to_map()
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
            temp_model = OpenAckServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseClusterUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(PauseClusterUpgradeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class PauseComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(PauseComponentUpgradeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class RemoveClusterNodesRequest(TeaModel):
    def __init__(self, drain_node=None, nodes=None, release_node=None):
        # 是否排空节点上的Pod。
        self.drain_node = drain_node  # type: bool
        # 要移除的Node列表。
        self.nodes = nodes  # type: list[str]
        # 是否同时释放ECS。
        self.release_node = release_node  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClusterNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drain_node is not None:
            result['drain_node'] = self.drain_node
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.release_node is not None:
            result['release_node'] = self.release_node
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')
        return self


class RemoveClusterNodesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(RemoveClusterNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class RemoveWorkflowResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(RemoveWorkflowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ResumeComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(ResumeComponentUpgradeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ResumeUpgradeClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(ResumeUpgradeClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ScaleClusterRequestTags(TeaModel):
    def __init__(self, key=None):
        # 标签值。
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleClusterRequestTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ScaleClusterRequestTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # 污点生效策略。
        self.effect = effect  # type: str
        # 污点键。
        self.key = key  # type: str
        # 污点值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleClusterRequestTaints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ScaleClusterRequestWorkerDataDisks(TeaModel):
    def __init__(self, category=None, encrypted=None, size=None):
        # 数据盘类型。
        self.category = category  # type: str
        # 是否对数据盘加密。
        self.encrypted = encrypted  # type: str
        # 数据盘大小。
        self.size = size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleClusterRequestWorkerDataDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ScaleClusterRequest(TeaModel):
    def __init__(self, cloud_monitor_flags=None, count=None, cpu_policy=None, disable_rollback=None, key_pair=None,
                 login_password=None, tags=None, taints=None, vswitch_ids=None, worker_auto_renew=None,
                 worker_auto_renew_period=None, worker_data_disk=None, worker_data_disks=None, worker_instance_charge_type=None,
                 worker_instance_types=None, worker_period=None, worker_period_unit=None, worker_system_disk_category=None,
                 worker_system_disk_size=None):
        # 节点是否安装云监控插件。
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 扩容节点数。
        self.count = count  # type: long
        # 节点CPU策略。
        self.cpu_policy = cpu_policy  # type: str
        # 失败是否回滚。
        self.disable_rollback = disable_rollback  # type: bool
        # keypair名称，和login_password二选一。
        self.key_pair = key_pair  # type: str
        # SSH登录密码。和keypair二选一。
        self.login_password = login_password  # type: str
        # 集群标签。
        self.tags = tags  # type: list[ScaleClusterRequestTags]
        # 节点污点标记。
        self.taints = taints  # type: list[ScaleClusterRequestTaints]
        # 节点交换机ID列表。
        self.vswitch_ids = vswitch_ids  # type: list[str]
        # 节点是否开启Worker节点自动续费。
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # 自动续费周期。
        self.worker_auto_renew_period = worker_auto_renew_period  # type: long
        # 是否挂载数据盘。
        self.worker_data_disk = worker_data_disk  # type: bool
        # Worker数据盘类型、大小等配置的组合。
        self.worker_data_disks = worker_data_disks  # type: list[ScaleClusterRequestWorkerDataDisks]
        # 节点付费类型。
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # Worker节点ECS规格类型。
        self.worker_instance_types = worker_instance_types  # type: list[str]
        # 节点包年包月时长。
        self.worker_period = worker_period  # type: long
        # 当指定为PrePaid的时候需要指定周期。
        self.worker_period_unit = worker_period_unit  # type: str
        # 节点系统盘类型。
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # 节点系统盘大小
        self.worker_system_disk_size = worker_system_disk_size  # type: long

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ScaleClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags
        if self.count is not None:
            result['count'] = self.count
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.disable_rollback is not None:
            result['disable_rollback'] = self.disable_rollback
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        if self.worker_auto_renew is not None:
            result['worker_auto_renew'] = self.worker_auto_renew
        if self.worker_auto_renew_period is not None:
            result['worker_auto_renew_period'] = self.worker_auto_renew_period
        if self.worker_data_disk is not None:
            result['worker_data_disk'] = self.worker_data_disk
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        if self.worker_instance_charge_type is not None:
            result['worker_instance_charge_type'] = self.worker_instance_charge_type
        if self.worker_instance_types is not None:
            result['worker_instance_types'] = self.worker_instance_types
        if self.worker_period is not None:
            result['worker_period'] = self.worker_period
        if self.worker_period_unit is not None:
            result['worker_period_unit'] = self.worker_period_unit
        if self.worker_system_disk_category is not None:
            result['worker_system_disk_category'] = self.worker_system_disk_category
        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        if m.get('disable_rollback') is not None:
            self.disable_rollback = m.get('disable_rollback')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ScaleClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = ScaleClusterRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        if m.get('worker_auto_renew') is not None:
            self.worker_auto_renew = m.get('worker_auto_renew')
        if m.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = m.get('worker_auto_renew_period')
        if m.get('worker_data_disk') is not None:
            self.worker_data_disk = m.get('worker_data_disk')
        self.worker_data_disks = []
        if m.get('worker_data_disks') is not None:
            for k in m.get('worker_data_disks'):
                temp_model = ScaleClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if m.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = m.get('worker_instance_charge_type')
        if m.get('worker_instance_types') is not None:
            self.worker_instance_types = m.get('worker_instance_types')
        if m.get('worker_period') is not None:
            self.worker_period = m.get('worker_period')
        if m.get('worker_period_unit') is not None:
            self.worker_period_unit = m.get('worker_period_unit')
        if m.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = m.get('worker_system_disk_category')
        if m.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = m.get('worker_system_disk_size')
        return self


class ScaleClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str
        # 任务ID。
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ScaleClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ScaleClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScaleClusterResponse, self).to_map()
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
            temp_model = ScaleClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleClusterNodePoolRequest(TeaModel):
    def __init__(self, count=None):
        # 扩容节点数量
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleClusterNodePoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class ScaleClusterNodePoolResponseBody(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID。
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleClusterNodePoolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ScaleClusterNodePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ScaleClusterNodePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScaleClusterNodePoolResponse, self).to_map()
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
            temp_model = ScaleClusterNodePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleOutClusterRequestWorkerDataDisks(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, category=None, encrypted=None, size=None):
        # 自动快照策略ID，云盘会按照快照策略自动备份。
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # 数据盘类型,默认值：cloud_efficiency
        self.category = category  # type: str
        # 是否对数据盘加密
        self.encrypted = encrypted  # type: str
        # 数据盘大小，单位为GiB。  取值范围：[40,32768]
        self.size = size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleOutClusterRequestWorkerDataDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = m.get('auto_snapshot_policy_id')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ScaleOutClusterRequest(TeaModel):
    def __init__(self, cloud_monitor_flags=None, count=None, cpu_policy=None, image_id=None, key_pair=None,
                 login_password=None, rds_instances=None, runtime=None, tags=None, taints=None, user_data=None, vswitch_ids=None,
                 worker_auto_renew=None, worker_auto_renew_period=None, worker_data_disks=None, worker_instance_charge_type=None,
                 worker_instance_types=None, worker_period=None, worker_period_unit=None, worker_system_disk_category=None,
                 worker_system_disk_size=None):
        # 在节点上安装云监控
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 扩容节点数
        self.count = count  # type: long
        # CPU亲和性策略
        self.cpu_policy = cpu_policy  # type: str
        # 自定义镜像
        self.image_id = image_id  # type: str
        # keypair名称，和login_password二选一。
        self.key_pair = key_pair  # type: str
        # SSH登录密码，和key_pair二选一。
        self.login_password = login_password  # type: str
        # RDS白名单
        self.rds_instances = rds_instances  # type: list[str]
        self.runtime = runtime  # type: Runtime
        # 节点标签
        self.tags = tags  # type: list[Tag]
        # 节点污点信息
        self.taints = taints  # type: list[Taint]
        # 节点自定义数据
        self.user_data = user_data  # type: str
        # 虚拟交换机
        self.vswitch_ids = vswitch_ids  # type: list[str]
        # Worker节点到期是否自动续费
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # Worker节点自动续费时长
        self.worker_auto_renew_period = worker_auto_renew_period  # type: long
        # Worker节点数据盘配置
        self.worker_data_disks = worker_data_disks  # type: list[ScaleOutClusterRequestWorkerDataDisks]
        # Worker节点付费类型
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # Worker节点实例规格
        self.worker_instance_types = worker_instance_types  # type: list[str]
        # Worker节点包年包月时长
        self.worker_period = worker_period  # type: long
        # Worker节点包年包月周期
        self.worker_period_unit = worker_period_unit  # type: str
        # Worker节点系统盘类型
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # Worker节点系统盘大小
        self.worker_system_disk_size = worker_system_disk_size  # type: long

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ScaleOutClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags
        if self.count is not None:
            result['count'] = self.count
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        if self.worker_auto_renew is not None:
            result['worker_auto_renew'] = self.worker_auto_renew
        if self.worker_auto_renew_period is not None:
            result['worker_auto_renew_period'] = self.worker_auto_renew_period
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        if self.worker_instance_charge_type is not None:
            result['worker_instance_charge_type'] = self.worker_instance_charge_type
        if self.worker_instance_types is not None:
            result['worker_instance_types'] = self.worker_instance_types
        if self.worker_period is not None:
            result['worker_period'] = self.worker_period
        if self.worker_period_unit is not None:
            result['worker_period_unit'] = self.worker_period_unit
        if self.worker_system_disk_category is not None:
            result['worker_system_disk_category'] = self.worker_system_disk_category
        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('runtime') is not None:
            temp_model = Runtime()
            self.runtime = temp_model.from_map(m['runtime'])
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        if m.get('worker_auto_renew') is not None:
            self.worker_auto_renew = m.get('worker_auto_renew')
        if m.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = m.get('worker_auto_renew_period')
        self.worker_data_disks = []
        if m.get('worker_data_disks') is not None:
            for k in m.get('worker_data_disks'):
                temp_model = ScaleOutClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if m.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = m.get('worker_instance_charge_type')
        if m.get('worker_instance_types') is not None:
            self.worker_instance_types = m.get('worker_instance_types')
        if m.get('worker_period') is not None:
            self.worker_period = m.get('worker_period')
        if m.get('worker_period_unit') is not None:
            self.worker_period_unit = m.get('worker_period_unit')
        if m.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = m.get('worker_system_disk_category')
        if m.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = m.get('worker_system_disk_size')
        return self


class ScaleOutClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str
        # 任务ID。
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleOutClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ScaleOutClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ScaleOutClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScaleOutClusterResponse, self).to_map()
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
            temp_model = ScaleOutClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartWorkflowRequest(TeaModel):
    def __init__(self, mapping_bam_out_filename=None, mapping_bam_out_path=None, mapping_bucket_name=None,
                 mapping_fastq_first_filename=None, mapping_fastq_path=None, mapping_fastq_second_filename=None, mapping_is_mark_dup=None,
                 mapping_oss_region=None, mapping_reference_path=None, service=None, wgs_bucket_name=None,
                 wgs_fastq_first_filename=None, wgs_fastq_path=None, wgs_fastq_second_filename=None, wgs_oss_region=None,
                 wgs_reference_path=None, wgs_vcf_out_filename=None, wgs_vcf_out_path=None, workflow_type=None):
        # bam文件输出名称。
        self.mapping_bam_out_filename = mapping_bam_out_filename  # type: str
        # bam文件输出路径。
        self.mapping_bam_out_path = mapping_bam_out_path  # type: str
        # 存放mapping的bucket名称。
        self.mapping_bucket_name = mapping_bucket_name  # type: str
        # mapping的第一个fastq文件名。
        self.mapping_fastq_first_filename = mapping_fastq_first_filename  # type: str
        # mapping的fastq文件路径。
        self.mapping_fastq_path = mapping_fastq_path  # type: str
        # mapping的第二个fastq文件名。
        self.mapping_fastq_second_filename = mapping_fastq_second_filename  # type: str
        # 是否进行dup。
        self.mapping_is_mark_dup = mapping_is_mark_dup  # type: str
        # mapping oss数据的存放region。
        self.mapping_oss_region = mapping_oss_region  # type: str
        # mapping的reference文件位置。
        self.mapping_reference_path = mapping_reference_path  # type: str
        # SLA类型，可选值：s、g、p。 白银级（s）：超过90 Gbp的部分，按1.5 Gbp/min计算增加的时间。 黄金级（g）：超过90 Gbp的部分，按2 Gbp/min计算增加的时间。 铂金级（p）：超过90 Gbp的部分，按3 Gbp/min计算增加的时间。
        self.service = service  # type: str
        # 存放wgs的bucket名称。
        self.wgs_bucket_name = wgs_bucket_name  # type: str
        # wgs的第一个fastq文件名。
        self.wgs_fastq_first_filename = wgs_fastq_first_filename  # type: str
        # wgs的fastq文件路径。
        self.wgs_fastq_path = wgs_fastq_path  # type: str
        # wgs的第二个fastq文件名。
        self.wgs_fastq_second_filename = wgs_fastq_second_filename  # type: str
        # wgs oss数据的存放region。
        self.wgs_oss_region = wgs_oss_region  # type: str
        # wgs的reference文件路径。
        self.wgs_reference_path = wgs_reference_path  # type: str
        # wgs的vcf输出文件名称。
        self.wgs_vcf_out_filename = wgs_vcf_out_filename  # type: str
        # wgs的vcf输出路径。
        self.wgs_vcf_out_path = wgs_vcf_out_path  # type: str
        # 工作流类型，可选值：wgs或mapping。
        self.workflow_type = workflow_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mapping_bam_out_filename is not None:
            result['mapping_bam_out_filename'] = self.mapping_bam_out_filename
        if self.mapping_bam_out_path is not None:
            result['mapping_bam_out_path'] = self.mapping_bam_out_path
        if self.mapping_bucket_name is not None:
            result['mapping_bucket_name'] = self.mapping_bucket_name
        if self.mapping_fastq_first_filename is not None:
            result['mapping_fastq_first_filename'] = self.mapping_fastq_first_filename
        if self.mapping_fastq_path is not None:
            result['mapping_fastq_path'] = self.mapping_fastq_path
        if self.mapping_fastq_second_filename is not None:
            result['mapping_fastq_second_filename'] = self.mapping_fastq_second_filename
        if self.mapping_is_mark_dup is not None:
            result['mapping_is_mark_dup'] = self.mapping_is_mark_dup
        if self.mapping_oss_region is not None:
            result['mapping_oss_region'] = self.mapping_oss_region
        if self.mapping_reference_path is not None:
            result['mapping_reference_path'] = self.mapping_reference_path
        if self.service is not None:
            result['service'] = self.service
        if self.wgs_bucket_name is not None:
            result['wgs_bucket_name'] = self.wgs_bucket_name
        if self.wgs_fastq_first_filename is not None:
            result['wgs_fastq_first_filename'] = self.wgs_fastq_first_filename
        if self.wgs_fastq_path is not None:
            result['wgs_fastq_path'] = self.wgs_fastq_path
        if self.wgs_fastq_second_filename is not None:
            result['wgs_fastq_second_filename'] = self.wgs_fastq_second_filename
        if self.wgs_oss_region is not None:
            result['wgs_oss_region'] = self.wgs_oss_region
        if self.wgs_reference_path is not None:
            result['wgs_reference_path'] = self.wgs_reference_path
        if self.wgs_vcf_out_filename is not None:
            result['wgs_vcf_out_filename'] = self.wgs_vcf_out_filename
        if self.wgs_vcf_out_path is not None:
            result['wgs_vcf_out_path'] = self.wgs_vcf_out_path
        if self.workflow_type is not None:
            result['workflow_type'] = self.workflow_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('mapping_bam_out_filename') is not None:
            self.mapping_bam_out_filename = m.get('mapping_bam_out_filename')
        if m.get('mapping_bam_out_path') is not None:
            self.mapping_bam_out_path = m.get('mapping_bam_out_path')
        if m.get('mapping_bucket_name') is not None:
            self.mapping_bucket_name = m.get('mapping_bucket_name')
        if m.get('mapping_fastq_first_filename') is not None:
            self.mapping_fastq_first_filename = m.get('mapping_fastq_first_filename')
        if m.get('mapping_fastq_path') is not None:
            self.mapping_fastq_path = m.get('mapping_fastq_path')
        if m.get('mapping_fastq_second_filename') is not None:
            self.mapping_fastq_second_filename = m.get('mapping_fastq_second_filename')
        if m.get('mapping_is_mark_dup') is not None:
            self.mapping_is_mark_dup = m.get('mapping_is_mark_dup')
        if m.get('mapping_oss_region') is not None:
            self.mapping_oss_region = m.get('mapping_oss_region')
        if m.get('mapping_reference_path') is not None:
            self.mapping_reference_path = m.get('mapping_reference_path')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('wgs_bucket_name') is not None:
            self.wgs_bucket_name = m.get('wgs_bucket_name')
        if m.get('wgs_fastq_first_filename') is not None:
            self.wgs_fastq_first_filename = m.get('wgs_fastq_first_filename')
        if m.get('wgs_fastq_path') is not None:
            self.wgs_fastq_path = m.get('wgs_fastq_path')
        if m.get('wgs_fastq_second_filename') is not None:
            self.wgs_fastq_second_filename = m.get('wgs_fastq_second_filename')
        if m.get('wgs_oss_region') is not None:
            self.wgs_oss_region = m.get('wgs_oss_region')
        if m.get('wgs_reference_path') is not None:
            self.wgs_reference_path = m.get('wgs_reference_path')
        if m.get('wgs_vcf_out_filename') is not None:
            self.wgs_vcf_out_filename = m.get('wgs_vcf_out_filename')
        if m.get('wgs_vcf_out_path') is not None:
            self.wgs_vcf_out_path = m.get('wgs_vcf_out_path')
        if m.get('workflow_type') is not None:
            self.workflow_type = m.get('workflow_type')
        return self


class StartWorkflowResponseBody(TeaModel):
    def __init__(self, job_name=None):
        # 工作流名称
        self.job_name = job_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartWorkflowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_name is not None:
            result['JobName'] = self.job_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        return self


class StartWorkflowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartWorkflowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartWorkflowResponse, self).to_map()
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
            temp_model = StartWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_ids=None, resource_type=None, tags=None):
        # 资源所属的地域ID
        self.region_id = region_id  # type: str
        # 资源ID列表
        self.resource_ids = resource_ids  # type: list[str]
        # 资源类型定义。取值范围：  只支持CLUSTER这一种资源类型
        self.resource_type = resource_type  # type: str
        # 资源的标签键值对。数组长度范围：1~20。一旦传值，则不允许为空字符串。最多支持128个字符，不能以aliyun和acs:开头，不能包含http://或者https://。
        self.tags = tags  # type: list[Tag]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UnInstallClusterAddonsRequestAddons(TeaModel):
    def __init__(self, name=None):
        # 组件名称。
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnInstallClusterAddonsRequestAddons, self).to_map()
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


class UnInstallClusterAddonsRequest(TeaModel):
    def __init__(self, addons=None):
        # 卸载组件列表。
        self.addons = addons  # type: list[UnInstallClusterAddonsRequestAddons]

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UnInstallClusterAddonsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['addons'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.addons = []
        if m.get('addons') is not None:
            for k in m.get('addons'):
                temp_model = UnInstallClusterAddonsRequestAddons()
                self.addons.append(temp_model.from_map(k))
        return self


class UnInstallClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UnInstallClusterAddonsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_ids=None, resource_type=None, tag_keys=None):
        # 资源所属的地域ID
        self.region_id = region_id  # type: str
        # 资源ID。数组长度取值范围为：1~50
        self.resource_ids = resource_ids  # type: list[str]
        # 资源类型定义。取值范围： 只支持CLUSTER这一种资源类型
        self.resource_type = resource_type  # type: str
        # 资源的标签键。N的取值范围：1~20
        self.tag_keys = tag_keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.tag_keys is not None:
            result['tag_keys'] = self.tag_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('tag_keys') is not None:
            self.tag_keys = m.get('tag_keys')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateK8sClusterUserConfigExpireResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpdateK8sClusterUserConfigExpireResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, description=None, name=None, tags=None, template=None, template_type=None):
        # 部署模板描述信息。
        self.description = description  # type: str
        # 部署模板名称。
        self.name = name  # type: str
        # 部署模板标签
        self.tags = tags  # type: str
        # 部署模板yaml。
        self.template = template  # type: str
        # 部署模板类型。
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template is not None:
            result['template'] = self.template
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpdateTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(self, component_name=None, next_version=None, version=None):
        # 组件名称，集群升级时取值"k8s"。
        self.component_name = component_name  # type: str
        # 目标版本。
        self.next_version = next_version  # type: str
        # 当前版本。
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['component_name'] = self.component_name
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('component_name') is not None:
            self.component_name = m.get('component_name')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpgradeClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpgradeClusterAddonsRequestBody(TeaModel):
    def __init__(self, component_name=None, next_version=None, version=None):
        # 组件名称
        self.component_name = component_name  # type: str
        # 可升级版本
        self.next_version = next_version  # type: str
        # 当前版本
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClusterAddonsRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['component_name'] = self.component_name
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('component_name') is not None:
            self.component_name = m.get('component_name')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpgradeClusterAddonsRequest(TeaModel):
    def __init__(self, body=None):
        # Request body，类型是对象数组
        self.body = body  # type: list[UpgradeClusterAddonsRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpgradeClusterAddonsRequest, self).to_map()
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
                temp_model = UpgradeClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class UpgradeClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(UpgradeClusterAddonsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class StandardComponentsValue(TeaModel):
    def __init__(self, name=None, version=None, description=None, required=None, disabled=None):
        # 组件名称。
        self.name = name  # type: str
        # 组件版本。
        self.version = version  # type: str
        # 组件描述信息。
        self.description = description  # type: str
        # 是否为必需组件。
        self.required = required  # type: str
        # 是否禁止默认安装。
        self.disabled = disabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StandardComponentsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        if self.description is not None:
            result['description'] = self.description
        if self.required is not None:
            result['required'] = self.required
        if self.disabled is not None:
            result['disabled'] = self.disabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        return self


