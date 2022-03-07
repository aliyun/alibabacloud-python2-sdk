# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateInstanceRequestDatasets(TeaModel):
    def __init__(self, dataset_id=None, mount_path=None):
        # 数据集Id
        self.dataset_id = dataset_id  # type: str
        # 容器内挂载路径
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestDatasets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class CreateInstanceRequestUserVpc(TeaModel):
    def __init__(self, security_group_id=None, v_switch_id=None, vpc_id=None):
        # Security Group Id
        self.security_group_id = security_group_id  # type: str
        # VSwitch Id
        self.v_switch_id = v_switch_id  # type: str
        # Vpc Id
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, accessibility=None, datasets=None, ecs_spec=None, environment_variables=None, image_id=None,
                 image_url=None, instance_name=None, user_vpc=None, workspace_id=None):
        # 工作空间内是否他人可见
        self.accessibility = accessibility  # type: str
        # 数据集集合
        self.datasets = datasets  # type: list[CreateInstanceRequestDatasets]
        # 实例对应的Ecs规格
        self.ecs_spec = ecs_spec  # type: str
        # 环境变量
        self.environment_variables = environment_variables  # type: dict[str, str]
        # 镜像Id
        self.image_id = image_id  # type: str
        # 镜像地址
        self.image_url = image_url  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        # user vpc配置
        self.user_vpc = user_vpc  # type: CreateInstanceRequestUserVpc
        # 工作空间Id
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = CreateInstanceRequestDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('UserVpc') is not None:
            temp_model = CreateInstanceRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceResponse, self).to_map()
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceShutdownTimerRequest(TeaModel):
    def __init__(self, due_time=None, remaining_time_in_ms=None):
        # 定时关机设定时间
        self.due_time = due_time  # type: str
        # 距离定时关机时间段
        self.remaining_time_in_ms = remaining_time_in_ms  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceShutdownTimerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        return self


class CreateInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceShutdownTimerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceShutdownTimerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateInstanceShutdownTimerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceShutdownTimerResponse, self).to_map()
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
            temp_model = CreateInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceSnapshotRequest(TeaModel):
    def __init__(self, image_url=None, snapshot_description=None, snapshot_name=None):
        # 镜像地址
        self.image_url = image_url  # type: str
        # 实例快照描述
        self.snapshot_description = snapshot_description  # type: str
        # 实例快照名称
        self.snapshot_name = snapshot_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.snapshot_description is not None:
            result['SnapshotDescription'] = self.snapshot_description
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('SnapshotDescription') is not None:
            self.snapshot_description = m.get('SnapshotDescription')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None, snapshot_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 实例快照Id
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceSnapshotResponse, self).to_map()
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
            temp_model = CreateInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceResponse, self).to_map()
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceShutdownTimerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceShutdownTimerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteInstanceShutdownTimerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceShutdownTimerResponse, self).to_map()
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
            temp_model = DeleteInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None, snapshot_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 实例快照Id
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceSnapshotResponse, self).to_map()
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
            temp_model = DeleteInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyDatasets(TeaModel):
    def __init__(self, dataset_id=None, mount_path=None):
        # 数据集Id
        self.dataset_id = dataset_id  # type: str
        # 容器内挂载路径
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyDatasets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class GetInstanceResponseBodyInstanceShutdownTimer(TeaModel):
    def __init__(self, due_time=None, gmt_create_time=None, gmt_modified_time=None, instance_id=None,
                 remaining_time_in_ms=None):
        # 设定关机时间
        self.due_time = due_time  # type: str
        # 创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 剩余关机时间（ms）
        self.remaining_time_in_ms = remaining_time_in_ms  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceShutdownTimer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        return self


class GetInstanceResponseBodyLatestSnapshot(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, image_id=None, image_name=None, image_url=None,
                 repository_url=None):
        # 快照创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 快照修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 镜像Id
        self.image_id = image_id  # type: str
        # 镜像名称
        self.image_name = image_name  # type: str
        # 镜像Url
        self.image_url = image_url  # type: str
        # 镜像仓库Url
        self.repository_url = repository_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyLatestSnapshot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        return self


class GetInstanceResponseBodyUserVpc(TeaModel):
    def __init__(self, security_group_id=None, v_switch_id=None, vpc_id=None):
        # Security Group Id
        self.security_group_id = security_group_id  # type: str
        # VSwitch Id
        self.v_switch_id = v_switch_id  # type: str
        # Vpc Id
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, accelerator_type=None, accessibility=None, accumulated_running_time_in_ms=None,
                 datasets=None, ecs_spec=None, environment_variables=None, gmt_create_time=None, gmt_modified_time=None,
                 image_id=None, image_name=None, image_url=None, instance_id=None, instance_name=None,
                 instance_shutdown_timer=None, instance_url=None, jupyterlab_url=None, latest_snapshot=None, payment_type=None,
                 reason_code=None, reason_message=None, request_id=None, status=None, terminal_url=None, user_id=None,
                 user_vpc=None, web_ideurl=None, workspace_id=None, workspace_name=None):
        # 实例计算类型
        self.accelerator_type = accelerator_type  # type: str
        # 工作空间内是否他人可见
        self.accessibility = accessibility  # type: str
        # 累计运行时间（ms）
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms  # type: long
        # 数据集集合
        self.datasets = datasets  # type: list[GetInstanceResponseBodyDatasets]
        # 实例对应的Ecs规格
        self.ecs_spec = ecs_spec  # type: str
        # 环境变量
        self.environment_variables = environment_variables  # type: dict[str, str]
        # 实例创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 实例修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 镜像Id
        self.image_id = image_id  # type: str
        # 镜像名称
        self.image_name = image_name  # type: str
        # 镜像地址
        self.image_url = image_url  # type: str
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer  # type: GetInstanceResponseBodyInstanceShutdownTimer
        # 实例Url
        self.instance_url = instance_url  # type: str
        # Jupyterlab Url
        self.jupyterlab_url = jupyterlab_url  # type: str
        # 最新保存的用户镜像
        self.latest_snapshot = latest_snapshot  # type: GetInstanceResponseBodyLatestSnapshot
        # 支付类型
        self.payment_type = payment_type  # type: str
        # 实例错误代码
        self.reason_code = reason_code  # type: str
        # 实例错误原因
        self.reason_message = reason_message  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 实例状态
        self.status = status  # type: str
        # 终端url
        self.terminal_url = terminal_url  # type: str
        # 用户Id
        self.user_id = user_id  # type: str
        # user vpc配置
        self.user_vpc = user_vpc  # type: GetInstanceResponseBodyUserVpc
        # Web IDE url
        self.web_ideurl = web_ideurl  # type: str
        # 工作空间Id
        self.workspace_id = workspace_id  # type: str
        # 工作空间名称
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.accumulated_running_time_in_ms is not None:
            result['AccumulatedRunningTimeInMs'] = self.accumulated_running_time_in_ms
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = GetInstanceResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = GetInstanceResponseBodyInstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('LatestSnapshot') is not None:
            temp_model = GetInstanceResponseBodyLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = GetInstanceResponseBodyUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceResponse, self).to_map()
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(self, due_time=None, gmt_create_time=None, gmt_modified_time=None, instance_id=None,
                 remaining_time_in_ms=None, request_id=None):
        # 设定关机时间
        self.due_time = due_time  # type: str
        # 创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 剩余关机时间（ms）
        self.remaining_time_in_ms = remaining_time_in_ms  # type: long
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceShutdownTimerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceShutdownTimerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceShutdownTimerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceShutdownTimerResponse, self).to_map()
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
            temp_model = GetInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, image_id=None, image_url=None,
                 instance_id=None, reason_code=None, reason_message=None, request_id=None, snapshot_id=None, snapshot_name=None,
                 status=None):
        # 实例快照创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 实例快照修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例快照的镜像Id
        self.image_id = image_id  # type: str
        # 实例快照的镜像地址
        self.image_url = image_url  # type: str
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 实例快照错误代码
        self.reason_code = reason_code  # type: str
        # 实例快照错误消息
        self.reason_message = reason_message  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 实例快照Id
        self.snapshot_id = snapshot_id  # type: str
        # 实例快照名称
        self.snapshot_name = snapshot_name  # type: str
        # 实例快照状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceSnapshotResponse, self).to_map()
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
            temp_model = GetInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserConfigResponseBody(TeaModel):
    def __init__(self, account_sufficient=None, request_id=None):
        # 用户账号金额是否充足
        self.account_sufficient = account_sufficient  # type: bool
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_sufficient is not None:
            result['AccountSufficient'] = self.account_sufficient
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountSufficient') is not None:
            self.account_sufficient = m.get('AccountSufficient')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserConfigResponse, self).to_map()
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
            temp_model = GetUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsRequest(TeaModel):
    def __init__(self, accelerator_type=None, order=None, page_number=None, page_size=None, sort_by=None):
        # 加速类型
        self.accelerator_type = accelerator_type  # type: str
        # 排序顺序
        self.order = order  # type: str
        # 页数
        self.page_number = page_number  # type: long
        # 每页大小
        self.page_size = page_size  # type: long
        # 排序字段
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


class ListEcsSpecsResponseBodyEcsSpecs(TeaModel):
    def __init__(self, accelerator_type=None, cpu=None, currency=None, gpu=None, gputype=None,
                 instance_bandwidth_rx=None, instance_type=None, memory=None, price=None, system_disk_capacity=None):
        # 资源类型
        self.accelerator_type = accelerator_type  # type: str
        # CPU核数
        self.cpu = cpu  # type: long
        # 货币单位
        self.currency = currency  # type: str
        # GPU卡数
        self.gpu = gpu  # type: long
        # 显卡类型
        self.gputype = gputype  # type: str
        # 实例接收带宽
        self.instance_bandwidth_rx = instance_bandwidth_rx  # type: long
        # 实例规格
        self.instance_type = instance_type  # type: str
        # 内存大小(GB)
        self.memory = memory  # type: float
        # 价格
        self.price = price  # type: float
        # 系统盘大小(GB)
        self.system_disk_capacity = system_disk_capacity  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsSpecsResponseBodyEcsSpecs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.price is not None:
            result['Price'] = self.price
        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        return self


class ListEcsSpecsResponseBody(TeaModel):
    def __init__(self, ecs_specs=None, request_id=None, total_count=None):
        # 本分页中请求的实例列表
        self.ecs_specs = ecs_specs  # type: list[ListEcsSpecsResponseBodyEcsSpecs]
        # 请求Id
        self.request_id = request_id  # type: str
        # 实例总数
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
                temp_model = ListEcsSpecsResponseBodyEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class ListInstanceSnapshotRequest(TeaModel):
    def __init__(self, order=None, page_number=None, page_size=None, sort_by=None):
        self.order = order  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListInstanceSnapshotResponseBodySnapshots(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, image_id=None, image_url=None,
                 instance_id=None, reason_code=None, reason_message=None, snapshot_id=None, snapshot_name=None, status=None):
        # 实例快照创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 实例快照修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例快照的镜像Id
        self.image_id = image_id  # type: str
        # 实例快照的镜像地址
        self.image_url = image_url  # type: str
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 实例快照错误代码
        self.reason_code = reason_code  # type: str
        # 实例快照错误消息
        self.reason_message = reason_message  # type: str
        # 实例快照Id
        self.snapshot_id = snapshot_id  # type: str
        # 实例快照名称
        self.snapshot_name = snapshot_name  # type: str
        # 实例快照状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceSnapshotResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, request_id=None, snapshots=None, total_count=None):
        # 请求Id
        self.request_id = request_id  # type: str
        # 本分页中请求的实例镜像列表
        self.snapshots = snapshots  # type: list[ListInstanceSnapshotResponseBodySnapshots]
        # 实例总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListInstanceSnapshotResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceSnapshotResponse, self).to_map()
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
            temp_model = ListInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceStatisticsRequest(TeaModel):
    def __init__(self, workspace_ids=None):
        # 工作空间列表
        self.workspace_ids = workspace_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceStatisticsRequest, self).to_map()
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


class ListInstanceStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, statistics=None):
        # 请求Id
        self.request_id = request_id  # type: str
        # 统计信息
        self.statistics = statistics  # type: dict[str, dict]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        return self


class ListInstanceStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstanceStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceStatisticsResponse, self).to_map()
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
            temp_model = ListInstanceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, accelerator_type=None, accessibility=None, instance_name=None, order=None, page_number=None,
                 page_size=None, payment_type=None, sort_by=None, status=None, workspace_id=None):
        self.accelerator_type = accelerator_type  # type: str
        self.accessibility = accessibility  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        # 排列顺序
        self.order = order  # type: str
        # 页码
        self.page_number = page_number  # type: long
        # 分页数量大小
        self.page_size = page_size  # type: long
        self.payment_type = payment_type  # type: str
        # 排序字段
        self.sort_by = sort_by  # type: str
        # 实例状态
        self.status = status  # type: str
        # 工作空间Id
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListInstancesResponseBodyInstancesDatasets(TeaModel):
    def __init__(self, dataset_id=None, mount_path=None):
        # 数据集Id
        self.dataset_id = dataset_id  # type: str
        # 容器内挂载路径
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesDatasets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class ListInstancesResponseBodyInstancesInstanceShutdownTimer(TeaModel):
    def __init__(self, due_time=None, gmt_create_time=None, gmt_modified_time=None, instance_id=None,
                 remaining_time_in_ms=None):
        # 设定关机时间
        self.due_time = due_time  # type: str
        # 创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 剩余关机时间（ms）
        self.remaining_time_in_ms = remaining_time_in_ms  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesInstanceShutdownTimer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        return self


class ListInstancesResponseBodyInstancesLatestSnapshot(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, image_id=None, image_name=None, image_url=None,
                 repository_url=None):
        # 快照创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 快照修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 镜像Id
        self.image_id = image_id  # type: str
        # 镜像名称
        self.image_name = image_name  # type: str
        # 镜像Url
        self.image_url = image_url  # type: str
        # 镜像仓库Url
        self.repository_url = repository_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesLatestSnapshot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        return self


class ListInstancesResponseBodyInstancesUserVpc(TeaModel):
    def __init__(self, security_group_id=None, v_switch_id=None, vpc_id=None):
        # Security Group Id
        self.security_group_id = security_group_id  # type: str
        # VSwitch Id
        self.v_switch_id = v_switch_id  # type: str
        # Vpc Id
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(self, accelerator_type=None, accessibility=None, accumulated_running_time_in_ms=None,
                 datasets=None, ecs_spec=None, environment_variables=None, gmt_create_time=None, gmt_modified_time=None,
                 image_id=None, image_name=None, image_url=None, instance_id=None, instance_name=None,
                 instance_shutdown_timer=None, instance_url=None, jupyterlab_url=None, latest_snapshot=None, payment_type=None,
                 reason_code=None, reason_message=None, status=None, terminal_url=None, user_id=None, user_vpc=None,
                 web_ideurl=None, workspace_id=None, workspace_name=None):
        # 实例计算类型
        self.accelerator_type = accelerator_type  # type: str
        # 工作空间内是否他人可见
        self.accessibility = accessibility  # type: str
        # 累计运行时间（ms）
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms  # type: long
        # 数据集集合
        self.datasets = datasets  # type: list[ListInstancesResponseBodyInstancesDatasets]
        # 实例对应的Ecs规格
        self.ecs_spec = ecs_spec  # type: str
        # 环境变量
        self.environment_variables = environment_variables  # type: dict[str, str]
        # 实例创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 实例修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 镜像Id
        self.image_id = image_id  # type: str
        # 镜像名称
        self.image_name = image_name  # type: str
        # 镜像地址
        self.image_url = image_url  # type: str
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer  # type: ListInstancesResponseBodyInstancesInstanceShutdownTimer
        # 实例Url
        self.instance_url = instance_url  # type: str
        # Jupyterlab Url
        self.jupyterlab_url = jupyterlab_url  # type: str
        # 最新保存的用户镜像
        self.latest_snapshot = latest_snapshot  # type: ListInstancesResponseBodyInstancesLatestSnapshot
        # 支付类型
        self.payment_type = payment_type  # type: str
        # 实例错误代码
        self.reason_code = reason_code  # type: str
        # 实例错误原因
        self.reason_message = reason_message  # type: str
        # 实例状态
        self.status = status  # type: str
        # 终端url
        self.terminal_url = terminal_url  # type: str
        # 用户Id
        self.user_id = user_id  # type: str
        # user vpc配置
        self.user_vpc = user_vpc  # type: ListInstancesResponseBodyInstancesUserVpc
        # Web IDE url
        self.web_ideurl = web_ideurl  # type: str
        # 工作空间Id
        self.workspace_id = workspace_id  # type: str
        # 工作空间名称
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.accumulated_running_time_in_ms is not None:
            result['AccumulatedRunningTimeInMs'] = self.accumulated_running_time_in_ms
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.status is not None:
            result['Status'] = self.status
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = ListInstancesResponseBodyInstancesDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = ListInstancesResponseBodyInstancesInstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('LatestSnapshot') is not None:
            temp_model = ListInstancesResponseBodyInstancesLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = ListInstancesResponseBodyInstancesUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        # 本分页中请求的实例列表
        self.instances = instances  # type: list[ListInstancesResponseBodyInstances]
        # 请求Id
        self.request_id = request_id  # type: str
        # 实例总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
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
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesResponse, self).to_map()
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartInstanceResponse, self).to_map()
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(self, save_image=None):
        # 是否保存环境后再关闭实例
        self.save_image = save_image  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.save_image is not None:
            result['SaveImage'] = self.save_image
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SaveImage') is not None:
            self.save_image = m.get('SaveImage')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopInstanceResponse, self).to_map()
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, instance_name=None):
        # 实例名称
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponse, self).to_map()
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


