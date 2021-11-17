# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Cluster(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, config=None, name=None, nas=None, owner=None,
                 private_container_path=None, private_nas_path=None, public_container_path=None, public_nas_path=None, state=None,
                 v_switch_id=None, vpc_id=None):
        # 集群id
        self.cluster_id = cluster_id  # type: str
        # 集群类型
        self.cluster_type = cluster_type  # type: str
        # 集群配置
        self.config = config  # type: str
        # 集群名称
        self.name = name  # type: str
        # nas文件id
        self.nas = nas  # type: str
        # 集群owner
        self.owner = owner  # type: str
        # 个人nas挂载到容器路径
        self.private_container_path = private_container_path  # type: str
        # 个人nas挂载路径
        self.private_nas_path = private_nas_path  # type: str
        # 公共nas挂载到容器的路径
        self.public_container_path = public_container_path  # type: str
        # 公共nas挂载路径
        self.public_nas_path = public_nas_path  # type: str
        # 集群状态
        self.state = state  # type: str
        # 集群vSwitch
        self.v_switch_id = v_switch_id  # type: str
        # 集群vpc
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Cluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.nas is not None:
            result['Nas'] = self.nas
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.private_container_path is not None:
            result['PrivateContainerPath'] = self.private_container_path
        if self.private_nas_path is not None:
            result['PrivateNasPath'] = self.private_nas_path
        if self.public_container_path is not None:
            result['PublicContainerPath'] = self.public_container_path
        if self.public_nas_path is not None:
            result['PublicNasPath'] = self.public_nas_path
        if self.state is not None:
            result['State'] = self.state
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nas') is not None:
            self.nas = m.get('Nas')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PrivateContainerPath') is not None:
            self.private_container_path = m.get('PrivateContainerPath')
        if m.get('PrivateNasPath') is not None:
            self.private_nas_path = m.get('PrivateNasPath')
        if m.get('PublicContainerPath') is not None:
            self.public_container_path = m.get('PublicContainerPath')
        if m.get('PublicNasPath') is not None:
            self.public_nas_path = m.get('PublicNasPath')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class Config(TeaModel):
    def __init__(self, name=None, value=None):
        # 配置名称
        self.name = name  # type: str
        # 配置数值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Config, self).to_map()
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


class Dataset(TeaModel):
    def __init__(self, dataset_id=None, default_mount_path=None, file_system_id=None, mount_path=None, name=None,
                 nas_path=None):
        # 数据集id
        self.dataset_id = dataset_id  # type: str
        # 默认挂载路径
        self.default_mount_path = default_mount_path  # type: str
        # 文件系统Id
        self.file_system_id = file_system_id  # type: str
        # 挂载路径
        self.mount_path = mount_path  # type: str
        # 数据集名称
        self.name = name  # type: str
        # 文件系统被挂载路径
        self.nas_path = nas_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Dataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.default_mount_path is not None:
            result['DefaultMountPath'] = self.default_mount_path
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.name is not None:
            result['Name'] = self.name
        if self.nas_path is not None:
            result['NasPath'] = self.nas_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DefaultMountPath') is not None:
            self.default_mount_path = m.get('DefaultMountPath')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')
        return self


class EcsSpec(TeaModel):
    def __init__(self, cpu=None, gpu=None, gpu_type=None, instance_type=None, memory_in_gi_b=None,
                 system_disk_category=None, system_disk_size_in_gi_b=None):
        # cpu数量
        self.cpu = cpu  # type: long
        # gpu卡数
        self.gpu = gpu  # type: long
        # GPU卡类型
        self.gpu_type = gpu_type  # type: str
        # 实例类型
        self.instance_type = instance_type  # type: str
        # 内存(GiB)
        self.memory_in_gi_b = memory_in_gi_b  # type: long
        # 磁盘类型
        self.system_disk_category = system_disk_category  # type: str
        # 磁盘大小(GiB)
        self.system_disk_size_in_gi_b = system_disk_size_in_gi_b  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcsSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory_in_gi_b is not None:
            result['MemoryInGiB'] = self.memory_in_gi_b
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size_in_gi_b is not None:
            result['SystemDiskSizeInGiB'] = self.system_disk_size_in_gi_b
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemoryInGiB') is not None:
            self.memory_in_gi_b = m.get('MemoryInGiB')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSizeInGiB') is not None:
            self.system_disk_size_in_gi_b = m.get('SystemDiskSizeInGiB')
        return self


class Image(TeaModel):
    def __init__(self, accelerator_type=None, author=None, cuda_version=None, description=None, ecs_image_key=None,
                 framework=None, framework_version=None, from_image_id=None, from_image_name=None, gmt_create_time=None,
                 gmt_modified_time=None, image_id=None, image_name=None, image_url=None, instance_id=None, namespace=None, os=None,
                 osversion=None, python_version=None, region=None, repository=None, repository_page=None, resource_type=None,
                 root_image_id=None, shared=None, short_image_url=None, short_repository=None, stage=None, stage_code=None,
                 suggested_name=None, tag=None, type=None, workspace_image_id=None):
        # 资源类型
        self.accelerator_type = accelerator_type  # type: str
        # 镜像作者
        self.author = author  # type: str
        # Cuda版本
        self.cuda_version = cuda_version  # type: str
        # 镜像描述
        self.description = description  # type: str
        # Ecs镜像key
        self.ecs_image_key = ecs_image_key  # type: str
        # 算法框架
        self.framework = framework  # type: str
        # 算法框架版本
        self.framework_version = framework_version  # type: str
        # 镜像父镜像
        self.from_image_id = from_image_id  # type: str
        # 镜像名称
        self.from_image_name = from_image_name  # type: str
        # 创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 镜像ID
        self.image_id = image_id  # type: str
        # 镜像名称
        self.image_name = image_name  # type: str
        # 镜像url
        self.image_url = image_url  # type: str
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 镜像命名空间
        self.namespace = namespace  # type: str
        # 镜像操作系统分发版
        self.os = os  # type: str
        # 分发版版本
        self.osversion = osversion  # type: str
        # python版本
        self.python_version = python_version  # type: str
        # 地区
        self.region = region  # type: str
        # 镜像仓库
        self.repository = repository  # type: str
        # 跳转的镜像站点页面
        self.repository_page = repository_page  # type: str
        # 资源类型
        self.resource_type = resource_type  # type: long
        # 镜像的根镜像
        self.root_image_id = root_image_id  # type: str
        # 镜像是否被其他实例共享
        self.shared = shared  # type: bool
        # 镜像短url
        self.short_image_url = short_image_url  # type: str
        # 镜像仓库短名称
        self.short_repository = short_repository  # type: str
        # 镜像状态
        self.stage = stage  # type: str
        # 镜像状态代码
        self.stage_code = stage_code  # type: long
        # 保存镜像建议的名称
        self.suggested_name = suggested_name  # type: str
        # Tag
        self.tag = tag  # type: str
        # 镜像类型
        self.type = type  # type: str
        # 工作空间镜像id
        self.workspace_image_id = workspace_image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Image, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.author is not None:
            result['Author'] = self.author
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_image_key is not None:
            result['EcsImageKey'] = self.ecs_image_key
        if self.framework is not None:
            result['Framework'] = self.framework
        if self.framework_version is not None:
            result['FrameworkVersion'] = self.framework_version
        if self.from_image_id is not None:
            result['FromImageId'] = self.from_image_id
        if self.from_image_name is not None:
            result['FromImageName'] = self.from_image_name
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
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.os is not None:
            result['OS'] = self.os
        if self.osversion is not None:
            result['OSVersion'] = self.osversion
        if self.python_version is not None:
            result['PythonVersion'] = self.python_version
        if self.region is not None:
            result['Region'] = self.region
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.repository_page is not None:
            result['RepositoryPage'] = self.repository_page
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.root_image_id is not None:
            result['RootImageId'] = self.root_image_id
        if self.shared is not None:
            result['Shared'] = self.shared
        if self.short_image_url is not None:
            result['ShortImageUrl'] = self.short_image_url
        if self.short_repository is not None:
            result['ShortRepository'] = self.short_repository
        if self.stage is not None:
            result['Stage'] = self.stage
        if self.stage_code is not None:
            result['StageCode'] = self.stage_code
        if self.suggested_name is not None:
            result['SuggestedName'] = self.suggested_name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_image_id is not None:
            result['WorkspaceImageId'] = self.workspace_image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsImageKey') is not None:
            self.ecs_image_key = m.get('EcsImageKey')
        if m.get('Framework') is not None:
            self.framework = m.get('Framework')
        if m.get('FrameworkVersion') is not None:
            self.framework_version = m.get('FrameworkVersion')
        if m.get('FromImageId') is not None:
            self.from_image_id = m.get('FromImageId')
        if m.get('FromImageName') is not None:
            self.from_image_name = m.get('FromImageName')
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
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OS') is not None:
            self.os = m.get('OS')
        if m.get('OSVersion') is not None:
            self.osversion = m.get('OSVersion')
        if m.get('PythonVersion') is not None:
            self.python_version = m.get('PythonVersion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('RepositoryPage') is not None:
            self.repository_page = m.get('RepositoryPage')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RootImageId') is not None:
            self.root_image_id = m.get('RootImageId')
        if m.get('Shared') is not None:
            self.shared = m.get('Shared')
        if m.get('ShortImageUrl') is not None:
            self.short_image_url = m.get('ShortImageUrl')
        if m.get('ShortRepository') is not None:
            self.short_repository = m.get('ShortRepository')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        if m.get('StageCode') is not None:
            self.stage_code = m.get('StageCode')
        if m.get('SuggestedName') is not None:
            self.suggested_name = m.get('SuggestedName')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceImageId') is not None:
            self.workspace_image_id = m.get('WorkspaceImageId')
        return self


class ImageNamespace(TeaModel):
    def __init__(self, namespace=None, namespace_status=None):
        # 命名空间名称
        self.namespace = namespace  # type: str
        # 命名空间状态
        self.namespace_status = namespace_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageNamespace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        return self


class ImageRepository(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, region_id=None, repo_name=None,
                 repo_namespace=None, repo_status=None, repository=None):
        # 创建时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 地区Id
        self.region_id = region_id  # type: str
        # 仓库名称
        self.repo_name = repo_name  # type: str
        # 仓库命名空间
        self.repo_namespace = repo_namespace  # type: str
        # 仓库状态
        self.repo_status = repo_status  # type: str
        # 仓库地址
        self.repository = repository  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageRepository, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repository is not None:
            result['Repository'] = self.repository
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        return self


class Instance(TeaModel):
    def __init__(self, accumulative_running_time_in_millis=None, accumulative_running_time_in_minutes=None,
                 create_user=None, dataset_list=None, ecs_spec=None, gmt_create_time=None, gmt_modified_time=None,
                 image_id=None, image_name=None, image_type=None, image_url=None, instance_id=None, instance_name=None,
                 instance_shutdown_timer=None, instance_status=None, instance_url=None, instance_version=None, is_public=None,
                 jupyterlab_url=None, message=None, nas_file_system_id=None, pay_type=None, pay_type_name=None, resource=None,
                 resource_type=None, shutdown_enabled=None, terminal_url=None, user_id=None, user_image_list=None, user_vpc=None,
                 web_ide_url=None, workspace_id=None, workspace_name=None):
        # 运行时间，毫秒数
        self.accumulative_running_time_in_millis = accumulative_running_time_in_millis  # type: long
        # 累计运行时间(分钟)
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes  # type: long
        # 创建者
        self.create_user = create_user  # type: str
        # 数据集列表
        self.dataset_list = dataset_list  # type: list[Dataset]
        # ecs规格
        self.ecs_spec = ecs_spec  # type: str
        # 创建时间(GMT)
        self.gmt_create_time = gmt_create_time  # type: str
        # 修改时间(GMT)
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 镜像ID
        self.image_id = image_id  # type: str
        # 镜像名称
        self.image_name = image_name  # type: str
        # 镜像类型
        self.image_type = image_type  # type: str
        # 镜像链接
        self.image_url = image_url  # type: str
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer  # type: InstanceShutdownTimer
        # 实例状态
        self.instance_status = instance_status  # type: str
        # dsw实例链接
        self.instance_url = instance_url  # type: str
        # 实例版本
        self.instance_version = instance_version  # type: str
        # 是否他人可见
        self.is_public = is_public  # type: long
        # jupyter链接
        self.jupyterlab_url = jupyterlab_url  # type: str
        # 错误消息
        self.message = message  # type: str
        # nas文件系统ID
        self.nas_file_system_id = nas_file_system_id  # type: str
        # 付费类型代码
        self.pay_type = pay_type  # type: long
        # 付费类型名称
        self.pay_type_name = pay_type_name  # type: str
        # 资源类型名称
        self.resource = resource  # type: str
        # 资源类型代码
        self.resource_type = resource_type  # type: long
        # 是否支持定时关机
        self.shutdown_enabled = shutdown_enabled  # type: bool
        # 命令行终端链接
        self.terminal_url = terminal_url  # type: str
        # 用户ID
        self.user_id = user_id  # type: str
        # 保存用户镜像列表
        self.user_image_list = user_image_list  # type: list[Image]
        # 被打通VPC配置
        self.user_vpc = user_vpc  # type: UserVpc
        # webIde链接
        self.web_ide_url = web_ide_url  # type: str
        # 工作空间id
        self.workspace_id = workspace_id  # type: str
        # 工作空间名称
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        if self.dataset_list:
            for k in self.dataset_list:
                if k:
                    k.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.user_image_list:
            for k in self.user_image_list:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(Instance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulative_running_time_in_millis is not None:
            result['AccumulativeRunningTimeInMillis'] = self.accumulative_running_time_in_millis
        if self.accumulative_running_time_in_minutes is not None:
            result['AccumulativeRunningTimeInMinutes'] = self.accumulative_running_time_in_minutes
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        result['DatasetList'] = []
        if self.dataset_list is not None:
            for k in self.dataset_list:
                result['DatasetList'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.instance_version is not None:
            result['InstanceVersion'] = self.instance_version
        if self.is_public is not None:
            result['IsPublic'] = self.is_public
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.message is not None:
            result['Message'] = self.message
        if self.nas_file_system_id is not None:
            result['NasFileSystemId'] = self.nas_file_system_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pay_type_name is not None:
            result['PayTypeName'] = self.pay_type_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.shutdown_enabled is not None:
            result['ShutdownEnabled'] = self.shutdown_enabled
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        result['UserImageList'] = []
        if self.user_image_list is not None:
            for k in self.user_image_list:
                result['UserImageList'].append(k.to_map() if k else None)
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ide_url is not None:
            result['WebIdeUrl'] = self.web_ide_url
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccumulativeRunningTimeInMillis') is not None:
            self.accumulative_running_time_in_millis = m.get('AccumulativeRunningTimeInMillis')
        if m.get('AccumulativeRunningTimeInMinutes') is not None:
            self.accumulative_running_time_in_minutes = m.get('AccumulativeRunningTimeInMinutes')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        self.dataset_list = []
        if m.get('DatasetList') is not None:
            for k in m.get('DatasetList'):
                temp_model = Dataset()
                self.dataset_list.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = InstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('InstanceVersion') is not None:
            self.instance_version = m.get('InstanceVersion')
        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NasFileSystemId') is not None:
            self.nas_file_system_id = m.get('NasFileSystemId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PayTypeName') is not None:
            self.pay_type_name = m.get('PayTypeName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ShutdownEnabled') is not None:
            self.shutdown_enabled = m.get('ShutdownEnabled')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        self.user_image_list = []
        if m.get('UserImageList') is not None:
            for k in m.get('UserImageList'):
                temp_model = Image()
                self.user_image_list.append(temp_model.from_map(k))
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIdeUrl') is not None:
            self.web_ide_url = m.get('WebIdeUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class InstanceShutdownTimer(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, instance_id=None, schedule_time=None,
                 ttl_in_millis=None):
        # 定时关机修改时间
        self.gmt_create_time = gmt_create_time  # type: str
        # 定时关机创建时间
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 定时关机时间
        self.schedule_time = schedule_time  # type: str
        # 多少毫秒后定时关机（如果设定可以覆盖ScheduleTime）
        self.ttl_in_millis = ttl_in_millis  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstanceShutdownTimer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ttl_in_millis is not None:
            result['TtlInMillis'] = self.ttl_in_millis
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('TtlInMillis') is not None:
            self.ttl_in_millis = m.get('TtlInMillis')
        return self


class InstanceSnapshot(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, instance_id=None,
                 instance_snapshot_description=None, instance_snapshot_id=None, instance_snapshot_name=None, instance_snapshot_repo_url=None,
                 instance_snapshot_status=None, instance_snapshot_tag=None):
        # 实例快照保存时间（GMT）
        self.gmt_create_time = gmt_create_time  # type: str
        # 实例快照修改时间（GMT）
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 实例快照描述
        self.instance_snapshot_description = instance_snapshot_description  # type: str
        # 实例快照ID
        self.instance_snapshot_id = instance_snapshot_id  # type: str
        # 实例快照名称
        self.instance_snapshot_name = instance_snapshot_name  # type: str
        # 实例快照存储地址
        self.instance_snapshot_repo_url = instance_snapshot_repo_url  # type: str
        # 实例快照状态
        self.instance_snapshot_status = instance_snapshot_status  # type: str
        # 实例快照标签
        self.instance_snapshot_tag = instance_snapshot_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstanceSnapshot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_description is not None:
            result['InstanceSnapshotDescription'] = self.instance_snapshot_description
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.instance_snapshot_name is not None:
            result['InstanceSnapshotName'] = self.instance_snapshot_name
        if self.instance_snapshot_repo_url is not None:
            result['InstanceSnapshotRepoUrl'] = self.instance_snapshot_repo_url
        if self.instance_snapshot_status is not None:
            result['InstanceSnapshotStatus'] = self.instance_snapshot_status
        if self.instance_snapshot_tag is not None:
            result['InstanceSnapshotTag'] = self.instance_snapshot_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotDescription') is not None:
            self.instance_snapshot_description = m.get('InstanceSnapshotDescription')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('InstanceSnapshotName') is not None:
            self.instance_snapshot_name = m.get('InstanceSnapshotName')
        if m.get('InstanceSnapshotRepoUrl') is not None:
            self.instance_snapshot_repo_url = m.get('InstanceSnapshotRepoUrl')
        if m.get('InstanceSnapshotStatus') is not None:
            self.instance_snapshot_status = m.get('InstanceSnapshotStatus')
        if m.get('InstanceSnapshotTag') is not None:
            self.instance_snapshot_tag = m.get('InstanceSnapshotTag')
        return self


class InstanceStatus(TeaModel):
    def __init__(self, accumulative_running_time_in_minutes=None, instance_id=None, instance_shutdown_timer=None,
                 instance_status=None, msg=None, shutdown_enabled=None, type=None):
        # 累计运行时间（分钟）
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes  # type: long
        # 实例ID
        self.instance_id = instance_id  # type: str
        self.instance_shutdown_timer = instance_shutdown_timer  # type: InstanceShutdownTimer
        # 实例状态
        self.instance_status = instance_status  # type: str
        # 实例消息
        self.msg = msg  # type: str
        # 是否允许使用定时关机
        self.shutdown_enabled = shutdown_enabled  # type: bool
        # 实例类型
        self.type = type  # type: str

    def validate(self):
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()

    def to_map(self):
        _map = super(InstanceStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulative_running_time_in_minutes is not None:
            result['AccumulativeRunningTimeInMinutes'] = self.accumulative_running_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.shutdown_enabled is not None:
            result['ShutdownEnabled'] = self.shutdown_enabled
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccumulativeRunningTimeInMinutes') is not None:
            self.accumulative_running_time_in_minutes = m.get('AccumulativeRunningTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = InstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('ShutdownEnabled') is not None:
            self.shutdown_enabled = m.get('ShutdownEnabled')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InstanceType(TeaModel):
    def __init__(self, cpu_core_count=None, discount=None, domestic_price=None, gpuamount=None, gpuspec=None,
                 instance_bandwidth_rx=None, instance_bandwidth_tx=None, instance_pps_rx=None, instance_pps_tx=None,
                 instance_type_family=None, instance_type_id=None, international=None, local_storage_capacity=None, memory_size=None,
                 price=None, price_cny=None, price_usd=None, resource_type=None, system_disk_category=None,
                 system_disk_size=None):
        # CPU核数
        self.cpu_core_count = cpu_core_count  # type: long
        # 折扣
        self.discount = discount  # type: float
        # 内部价
        self.domestic_price = domestic_price  # type: float
        # GPU卡数
        self.gpuamount = gpuamount  # type: long
        # GPU规格
        self.gpuspec = gpuspec  # type: str
        # 实例接收带宽
        self.instance_bandwidth_rx = instance_bandwidth_rx  # type: long
        # 实例发送带宽
        self.instance_bandwidth_tx = instance_bandwidth_tx  # type: long
        # 实例每秒发包数量
        self.instance_pps_rx = instance_pps_rx  # type: long
        # 实例每秒收包数量
        self.instance_pps_tx = instance_pps_tx  # type: long
        # 实例规格族
        self.instance_type_family = instance_type_family  # type: str
        # 实例类型Id
        self.instance_type_id = instance_type_id  # type: str
        # 是否国际站
        self.international = international  # type: bool
        # 本地磁盘容量
        self.local_storage_capacity = local_storage_capacity  # type: long
        # 内存容量
        self.memory_size = memory_size  # type: float
        # 价格
        self.price = price  # type: float
        # 价格（人民币）
        self.price_cny = price_cny  # type: float
        # 价格（美元）
        self.price_usd = price_usd  # type: float
        # 资源类型
        self.resource_type = resource_type  # type: str
        # 磁盘存储类型
        self.system_disk_category = system_disk_category  # type: str
        # 磁盘容量
        self.system_disk_size = system_disk_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstanceType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.discount is not None:
            result['Discount'] = self.discount
        if self.domestic_price is not None:
            result['DomesticPrice'] = self.domestic_price
        if self.gpuamount is not None:
            result['GPUAmount'] = self.gpuamount
        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec
        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx
        if self.instance_bandwidth_tx is not None:
            result['InstanceBandwidthTx'] = self.instance_bandwidth_tx
        if self.instance_pps_rx is not None:
            result['InstancePpsRx'] = self.instance_pps_rx
        if self.instance_pps_tx is not None:
            result['InstancePpsTx'] = self.instance_pps_tx
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.international is not None:
            result['International'] = self.international
        if self.local_storage_capacity is not None:
            result['LocalStorageCapacity'] = self.local_storage_capacity
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.price is not None:
            result['Price'] = self.price
        if self.price_cny is not None:
            result['PriceCNY'] = self.price_cny
        if self.price_usd is not None:
            result['PriceUSD'] = self.price_usd
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('Discount') is not None:
            self.discount = m.get('Discount')
        if m.get('DomesticPrice') is not None:
            self.domestic_price = m.get('DomesticPrice')
        if m.get('GPUAmount') is not None:
            self.gpuamount = m.get('GPUAmount')
        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')
        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')
        if m.get('InstanceBandwidthTx') is not None:
            self.instance_bandwidth_tx = m.get('InstanceBandwidthTx')
        if m.get('InstancePpsRx') is not None:
            self.instance_pps_rx = m.get('InstancePpsRx')
        if m.get('InstancePpsTx') is not None:
            self.instance_pps_tx = m.get('InstancePpsTx')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('International') is not None:
            self.international = m.get('International')
        if m.get('LocalStorageCapacity') is not None:
            self.local_storage_capacity = m.get('LocalStorageCapacity')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PriceCNY') is not None:
            self.price_cny = m.get('PriceCNY')
        if m.get('PriceUSD') is not None:
            self.price_usd = m.get('PriceUSD')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class Nas(TeaModel):
    def __init__(self, description=None, file_system_id=None, status=None):
        # Nas盘描述
        self.description = description  # type: str
        # Nas文件系统Id
        self.file_system_id = file_system_id  # type: str
        # Nas盘状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Nas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class Region(TeaModel):
    def __init__(self, region_city=None, region_id=None, region_name=None, region_state=None, service_url=None):
        # 城市
        self.region_city = region_city  # type: str
        # id
        self.region_id = region_id  # type: str
        # 名称
        self.region_name = region_name  # type: str
        # 州省
        self.region_state = region_state  # type: str
        # 服务地址
        self.service_url = service_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Region, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_city is not None:
            result['RegionCity'] = self.region_city
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region_state is not None:
            result['RegionState'] = self.region_state
        if self.service_url is not None:
            result['ServiceUrl'] = self.service_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionCity') is not None:
            self.region_city = m.get('RegionCity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RegionState') is not None:
            self.region_state = m.get('RegionState')
        if m.get('ServiceUrl') is not None:
            self.service_url = m.get('ServiceUrl')
        return self


class ResourceInfo(TeaModel):
    def __init__(self, name=None, pay_type=None, resource_type=None):
        # 显卡类型
        self.name = name  # type: str
        # 支付类型
        self.pay_type = pay_type  # type: long
        # 资源类型
        self.resource_type = resource_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class SecurityGroup(TeaModel):
    def __init__(self, create_time=None, description=None, security_group_id=None, security_group_name=None,
                 vpc_id=None):
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 安全组id
        self.security_group_id = security_group_id  # type: str
        # 名称
        self.security_group_name = security_group_name  # type: str
        # vpc id
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SecurityGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class Status(TeaModel):
    def __init__(self, accumulative_running_time_in_minutes=None, instance_id=None, instance_shutdown_timer=None,
                 instance_status=None, msg=None, type=None):
        # 累计运行时间（分钟）
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes  # type: long
        # 实例ID
        self.instance_id = instance_id  # type: str
        self.instance_shutdown_timer = instance_shutdown_timer  # type: InstanceShutdownTimer
        # 实例状态
        self.instance_status = instance_status  # type: str
        # 实例消息
        self.msg = msg  # type: str
        # 实例类型
        self.type = type  # type: str

    def validate(self):
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()

    def to_map(self):
        _map = super(Status, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulative_running_time_in_minutes is not None:
            result['AccumulativeRunningTimeInMinutes'] = self.accumulative_running_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccumulativeRunningTimeInMinutes') is not None:
            self.accumulative_running_time_in_minutes = m.get('AccumulativeRunningTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = InstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UserVpc(TeaModel):
    def __init__(self, role_arn=None, security_group_id=None, vpc_id=None, vswitch_id=None):
        # 角色标识码
        self.role_arn = role_arn  # type: str
        # 安全组ID
        self.security_group_id = security_group_id  # type: str
        # 虚拟网络ID
        self.vpc_id = vpc_id  # type: str
        # 虚拟交换机ID
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class VSwitch(TeaModel):
    def __init__(self, available_ip_address_count=None, cidr_block=None, create_time=None, description=None,
                 is_default=None, status=None, v_switch_id=None, v_switch_name=None, vpc_id=None, zone_id=None):
        # 可用ip数量
        self.available_ip_address_count = available_ip_address_count  # type: long
        # 子网
        self.cidr_block = cidr_block  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 是否默认
        self.is_default = is_default  # type: bool
        # 状态
        self.status = status  # type: str
        # VSwitch Id
        self.v_switch_id = v_switch_id  # type: str
        # 名称
        self.v_switch_name = v_switch_name  # type: str
        # vpc id
        self.vpc_id = vpc_id  # type: str
        # 可用区
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VSwitch, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class Vpc(TeaModel):
    def __init__(self, cidr_block=None, create_time=None, description=None, is_default=None, status=None,
                 vrouter_id=None, vpc_id=None, vpc_name=None):
        # vpc子网
        self.cidr_block = cidr_block  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # vpc描述
        self.description = description  # type: str
        # 是否默认
        self.is_default = is_default  # type: bool
        # vpc状态
        self.status = status  # type: str
        # 路由id
        self.vrouter_id = vrouter_id  # type: str
        # vpc id
        self.vpc_id = vpc_id  # type: str
        # vpc名称
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Vpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class CreateImageRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, name=None, repository=None):
        # 镜像描述
        self.description = description  # type: str
        # 实例名称
        self.instance_id = instance_id  # type: str
        # 镜像名称
        self.name = name  # type: str
        # 镜像仓库
        self.repository = repository  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.repository is not None:
            result['Repository'] = self.repository
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(self, image_id=None, request_id=None):
        # 保存的镜像Id
        self.image_id = image_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageResponse, self).to_map()
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
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, dataset_list=None, ecs_spec=None, environments=None, image_id=None, image_url=None,
                 instance_name=None, is_public=None, nas_file_system_id=None, user_name=None, user_vpc=None, workspace_id=None):
        self.dataset_list = dataset_list  # type: list[Dataset]
        # 实例规格
        self.ecs_spec = ecs_spec  # type: str
        # 环境参数
        self.environments = environments  # type: dict[str, any]
        # 镜像id
        self.image_id = image_id  # type: str
        # 镜像地址
        self.image_url = image_url  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        self.is_public = is_public  # type: long
        # nas文件系统id
        self.nas_file_system_id = nas_file_system_id  # type: str
        # 实例的真实用户名称
        self.user_name = user_name  # type: str
        # 打通的vpc网络配置
        self.user_vpc = user_vpc  # type: UserVpc
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.dataset_list:
            for k in self.dataset_list:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetList'] = []
        if self.dataset_list is not None:
            for k in self.dataset_list:
                result['DatasetList'].append(k.to_map() if k else None)
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environments is not None:
            result['Environments'] = self.environments
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_public is not None:
            result['IsPublic'] = self.is_public
        if self.nas_file_system_id is not None:
            result['NasFileSystemId'] = self.nas_file_system_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dataset_list = []
        if m.get('DatasetList') is not None:
            for k in m.get('DatasetList'):
                temp_model = Dataset()
                self.dataset_list.append(temp_model.from_map(k))
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('Environments') is not None:
            self.environments = m.get('Environments')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')
        if m.get('NasFileSystemId') is not None:
            self.nas_file_system_id = m.get('NasFileSystemId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 请求ID
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
    def __init__(self, schedule_time=None, ttl_in_millis=None):
        # 定时关机时间（GMT）
        self.schedule_time = schedule_time  # type: str
        # 多少毫秒后定时关机（如果设定可以覆盖ScheduleTime）
        self.ttl_in_millis = ttl_in_millis  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceShutdownTimerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ttl_in_millis is not None:
            result['TtlInMillis'] = self.ttl_in_millis
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('TtlInMillis') is not None:
            self.ttl_in_millis = m.get('TtlInMillis')
        return self


class CreateInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 请求ID
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
    def __init__(self, instance_snapshot_description=None, instance_snapshot_name=None,
                 instance_snapshot_repo_url=None):
        # 实例快照描述
        self.instance_snapshot_description = instance_snapshot_description  # type: str
        # 实例快照名称
        self.instance_snapshot_name = instance_snapshot_name  # type: str
        # 实例快照存储地址（可选）
        self.instance_snapshot_repo_url = instance_snapshot_repo_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_snapshot_description is not None:
            result['InstanceSnapshotDescription'] = self.instance_snapshot_description
        if self.instance_snapshot_name is not None:
            result['InstanceSnapshotName'] = self.instance_snapshot_name
        if self.instance_snapshot_repo_url is not None:
            result['InstanceSnapshotRepoUrl'] = self.instance_snapshot_repo_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceSnapshotDescription') is not None:
            self.instance_snapshot_description = m.get('InstanceSnapshotDescription')
        if m.get('InstanceSnapshotName') is not None:
            self.instance_snapshot_name = m.get('InstanceSnapshotName')
        if m.get('InstanceSnapshotRepoUrl') is not None:
            self.instance_snapshot_repo_url = m.get('InstanceSnapshotRepoUrl')
        return self


class CreateInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, instance_id=None, instance_snapshot_id=None, request_id=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 实例快照ID
        self.instance_snapshot_id = instance_snapshot_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 请求ID
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
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 请求ID
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
    def __init__(self, instance_id=None, instance_snapshot_id=None, request_id=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 实例快照ID
        self.instance_snapshot_id = instance_snapshot_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetAuthorizationResponseBody(TeaModel):
    def __init__(self, authorization_failed_code=None, authorization_failed_message=None, authorized=None,
                 request_id=None):
        # 授权失败错误代码
        self.authorization_failed_code = authorization_failed_code  # type: str
        # 授权失败错误消息
        self.authorization_failed_message = authorization_failed_message  # type: str
        # 是否已经给DSW服务账号授权
        self.authorized = authorized  # type: bool
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_failed_code is not None:
            result['AuthorizationFailedCode'] = self.authorization_failed_code
        if self.authorization_failed_message is not None:
            result['AuthorizationFailedMessage'] = self.authorization_failed_message
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationFailedCode') is not None:
            self.authorization_failed_code = m.get('AuthorizationFailedCode')
        if m.get('AuthorizationFailedMessage') is not None:
            self.authorization_failed_message = m.get('AuthorizationFailedMessage')
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
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


class GetDashboardStatisticsRequest(TeaModel):
    def __init__(self, workspace_id=None):
        # 工作空间ID
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDashboardStatisticsRequest, self).to_map()
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


class GetDashboardStatisticsResponseBody(TeaModel):
    def __init__(self, instance_total=None, instsance_running_total=None, request_id=None):
        # 实例数
        self.instance_total = instance_total  # type: long
        # 运行实例数
        self.instsance_running_total = instsance_running_total  # type: long
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDashboardStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_total is not None:
            result['InstanceTotal'] = self.instance_total
        if self.instsance_running_total is not None:
            result['InstsanceRunningTotal'] = self.instsance_running_total
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceTotal') is not None:
            self.instance_total = m.get('InstanceTotal')
        if m.get('InstsanceRunningTotal') is not None:
            self.instsance_running_total = m.get('InstsanceRunningTotal')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDashboardStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDashboardStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDashboardStatisticsResponse, self).to_map()
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
            temp_model = GetDashboardStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, accumulative_running_time_in_minutes=None, ecs_spec=None, gmt_create_time=None,
                 gmt_modified_time=None, image_id=None, image_url=None, instance_id=None, instance_name=None,
                 instance_shutdown_timer=None, instance_status=None, jupyterlab_url=None, nas_file_system_id=None, request_id=None,
                 terminal_url=None, user_id=None, user_vpc=None, web_ide_url=None):
        # 累计运行时间(分钟)
        self.accumulative_running_time_in_minutes = accumulative_running_time_in_minutes  # type: long
        # ecs规格
        self.ecs_spec = ecs_spec  # type: str
        # 实例创建时间(GMT)
        self.gmt_create_time = gmt_create_time  # type: str
        # 实例修改时间(GMT)
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 镜像ID
        self.image_id = image_id  # type: str
        # 镜像链接
        self.image_url = image_url  # type: str
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        # 定时关机任务
        self.instance_shutdown_timer = instance_shutdown_timer  # type: InstanceShutdownTimer
        # 实例状态
        self.instance_status = instance_status  # type: str
        # jupyter链接
        self.jupyterlab_url = jupyterlab_url  # type: str
        # nas文件系统ID
        self.nas_file_system_id = nas_file_system_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 命令行终端链接
        self.terminal_url = terminal_url  # type: str
        # 用户ID
        self.user_id = user_id  # type: str
        # 被打通VPC配置
        self.user_vpc = user_vpc  # type: UserVpc
        # web ide链接
        self.web_ide_url = web_ide_url  # type: str

    def validate(self):
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulative_running_time_in_minutes is not None:
            result['AccumulativeRunningTimeInMinutes'] = self.accumulative_running_time_in_minutes
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
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
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_shutdown_timer is not None:
            result['InstanceShutdownTimer'] = self.instance_shutdown_timer.to_map()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        if self.nas_file_system_id is not None:
            result['NasFileSystemId'] = self.nas_file_system_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ide_url is not None:
            result['WebIdeUrl'] = self.web_ide_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccumulativeRunningTimeInMinutes') is not None:
            self.accumulative_running_time_in_minutes = m.get('AccumulativeRunningTimeInMinutes')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
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
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceShutdownTimer') is not None:
            temp_model = InstanceShutdownTimer()
            self.instance_shutdown_timer = temp_model.from_map(m['InstanceShutdownTimer'])
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        if m.get('NasFileSystemId') is not None:
            self.nas_file_system_id = m.get('NasFileSystemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = UserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIdeUrl') is not None:
            self.web_ide_url = m.get('WebIdeUrl')
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


class GetInstanceImageResponseBody(TeaModel):
    def __init__(self, image=None, request_id=None):
        self.image = image  # type: Image
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super(GetInstanceImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            temp_model = Image()
            self.image = temp_model.from_map(m['Image'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceImageResponse, self).to_map()
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
            temp_model = GetInstanceImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, instance_id=None, request_id=None,
                 schedule_time=None):
        # 任务创建时间(GMT)
        self.gmt_create_time = gmt_create_time  # type: str
        # 任务修改时间(GMT)
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 定时关机时间(GMT)
        self.schedule_time = schedule_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceShutdownTimerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
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
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, instance_id=None,
                 instance_snapshot_description=None, instance_snapshot_id=None, instance_snapshot_name=None, instance_snapshot_repo_url=None,
                 instance_snapshot_status=None, instance_snapshot_tag=None, request_id=None):
        # 实例快照保存时间（GMT）
        self.gmt_create_time = gmt_create_time  # type: str
        # 实例快照修改时间（GMT）
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 实例快照描述
        self.instance_snapshot_description = instance_snapshot_description  # type: str
        # 实例快照ID
        self.instance_snapshot_id = instance_snapshot_id  # type: str
        # 实例快照名称
        self.instance_snapshot_name = instance_snapshot_name  # type: str
        # 实例快照存储地址
        self.instance_snapshot_repo_url = instance_snapshot_repo_url  # type: str
        # 实例快照状态
        self.instance_snapshot_status = instance_snapshot_status  # type: str
        # 实例快照标签
        self.instance_snapshot_tag = instance_snapshot_tag  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_description is not None:
            result['InstanceSnapshotDescription'] = self.instance_snapshot_description
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.instance_snapshot_name is not None:
            result['InstanceSnapshotName'] = self.instance_snapshot_name
        if self.instance_snapshot_repo_url is not None:
            result['InstanceSnapshotRepoUrl'] = self.instance_snapshot_repo_url
        if self.instance_snapshot_status is not None:
            result['InstanceSnapshotStatus'] = self.instance_snapshot_status
        if self.instance_snapshot_tag is not None:
            result['InstanceSnapshotTag'] = self.instance_snapshot_tag
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotDescription') is not None:
            self.instance_snapshot_description = m.get('InstanceSnapshotDescription')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('InstanceSnapshotName') is not None:
            self.instance_snapshot_name = m.get('InstanceSnapshotName')
        if m.get('InstanceSnapshotRepoUrl') is not None:
            self.instance_snapshot_repo_url = m.get('InstanceSnapshotRepoUrl')
        if m.get('InstanceSnapshotStatus') is not None:
            self.instance_snapshot_status = m.get('InstanceSnapshotStatus')
        if m.get('InstanceSnapshotTag') is not None:
            self.instance_snapshot_tag = m.get('InstanceSnapshotTag')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetInstanceTypeResponseBody(TeaModel):
    def __init__(self, cpu_core_count=None, discount=None, domestic_price=None, gpuamount=None, gpuspec=None,
                 instance_bandwidth_rx=None, instance_bandwidth_tx=None, instance_pps_rx=None, instance_pps_tx=None,
                 instance_type_family=None, instance_type_id=None, international=None, local_storage_capacity=None, memory_size=None,
                 price=None, price_cny=None, price_usd=None, request_id=None, resource_type=None,
                 system_disk_category=None, system_disk_size=None):
        # cpu核数
        self.cpu_core_count = cpu_core_count  # type: long
        # 折扣
        self.discount = discount  # type: float
        # 国内价格
        self.domestic_price = domestic_price  # type: float
        # GPU卡数
        self.gpuamount = gpuamount  # type: long
        # GPU卡型
        self.gpuspec = gpuspec  # type: str
        # 实例接收带宽
        self.instance_bandwidth_rx = instance_bandwidth_rx  # type: long
        # 实例发送带宽
        self.instance_bandwidth_tx = instance_bandwidth_tx  # type: long
        # 实例每秒发包数
        self.instance_pps_rx = instance_pps_rx  # type: long
        # 实例每秒收包数
        self.instance_pps_tx = instance_pps_tx  # type: long
        # 规格族
        self.instance_type_family = instance_type_family  # type: str
        # 实例类型id
        self.instance_type_id = instance_type_id  # type: str
        # 是否国际站用户
        self.international = international  # type: bool
        # 存储盘容量
        self.local_storage_capacity = local_storage_capacity  # type: long
        # 内存容量
        self.memory_size = memory_size  # type: float
        # 价格
        self.price = price  # type: float
        # 价格（人民币）
        self.price_cny = price_cny  # type: float
        # 价格（美元）
        self.price_usd = price_usd  # type: float
        # Id of the request
        self.request_id = request_id  # type: str
        # 资源类型
        self.resource_type = resource_type  # type: str
        # 系统盘存储类型
        self.system_disk_category = system_disk_category  # type: str
        # 系统盘容量
        self.system_disk_size = system_disk_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.discount is not None:
            result['Discount'] = self.discount
        if self.domestic_price is not None:
            result['DomesticPrice'] = self.domestic_price
        if self.gpuamount is not None:
            result['GPUAmount'] = self.gpuamount
        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec
        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx
        if self.instance_bandwidth_tx is not None:
            result['InstanceBandwidthTx'] = self.instance_bandwidth_tx
        if self.instance_pps_rx is not None:
            result['InstancePpsRx'] = self.instance_pps_rx
        if self.instance_pps_tx is not None:
            result['InstancePpsTx'] = self.instance_pps_tx
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.international is not None:
            result['International'] = self.international
        if self.local_storage_capacity is not None:
            result['LocalStorageCapacity'] = self.local_storage_capacity
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.price is not None:
            result['Price'] = self.price
        if self.price_cny is not None:
            result['PriceCNY'] = self.price_cny
        if self.price_usd is not None:
            result['PriceUSD'] = self.price_usd
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('Discount') is not None:
            self.discount = m.get('Discount')
        if m.get('DomesticPrice') is not None:
            self.domestic_price = m.get('DomesticPrice')
        if m.get('GPUAmount') is not None:
            self.gpuamount = m.get('GPUAmount')
        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')
        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')
        if m.get('InstanceBandwidthTx') is not None:
            self.instance_bandwidth_tx = m.get('InstanceBandwidthTx')
        if m.get('InstancePpsRx') is not None:
            self.instance_pps_rx = m.get('InstancePpsRx')
        if m.get('InstancePpsTx') is not None:
            self.instance_pps_tx = m.get('InstancePpsTx')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('International') is not None:
            self.international = m.get('International')
        if m.get('LocalStorageCapacity') is not None:
            self.local_storage_capacity = m.get('LocalStorageCapacity')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PriceCNY') is not None:
            self.price_cny = m.get('PriceCNY')
        if m.get('PriceUSD') is not None:
            self.price_usd = m.get('PriceUSD')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class GetInstanceTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceTypeResponse, self).to_map()
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
            temp_model = GetInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceUrlResponseBody(TeaModel):
    def __init__(self, ide=None, lab=None, request_id=None, terminal=None):
        # webide的链接
        self.ide = ide  # type: str
        # jupyterlab的链接
        self.lab = lab  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # terminal终端的链接
        self.terminal = terminal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ide is not None:
            result['Ide'] = self.ide
        if self.lab is not None:
            result['Lab'] = self.lab
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terminal is not None:
            result['Terminal'] = self.terminal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ide') is not None:
            self.ide = m.get('Ide')
        if m.get('Lab') is not None:
            self.lab = m.get('Lab')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Terminal') is not None:
            self.terminal = m.get('Terminal')
        return self


class GetInstanceUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceUrlResponse, self).to_map()
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
            temp_model = GetInstanceUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstancesStatisticsRequest(TeaModel):
    def __init__(self, workspace_ids=None):
        # 工作空间id列表
        self.workspace_ids = workspace_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstancesStatisticsRequest, self).to_map()
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


class GetInstancesStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, statistics=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 统计数据
        self.statistics = statistics  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstancesStatisticsResponseBody, self).to_map()
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


class GetInstancesStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstancesStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstancesStatisticsResponse, self).to_map()
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
            temp_model = GetInstancesStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserConfigResponseBody(TeaModel):
    def __init__(self, current_feature_version=None, enable_emr_cluster=None, request_id=None,
                 use_on_sale_version=None, use_v21feature=None):
        # 当前版本
        self.current_feature_version = current_feature_version  # type: str
        # 是否启用v2功能
        self.enable_emr_cluster = enable_emr_cluster  # type: bool
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否显示特价版功能
        self.use_on_sale_version = use_on_sale_version  # type: bool
        # 是否使用团队版功能（v21）
        self.use_v21feature = use_v21feature  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_feature_version is not None:
            result['CurrentFeatureVersion'] = self.current_feature_version
        if self.enable_emr_cluster is not None:
            result['EnableEmrCluster'] = self.enable_emr_cluster
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.use_on_sale_version is not None:
            result['UseOnSaleVersion'] = self.use_on_sale_version
        if self.use_v21feature is not None:
            result['UseV21Feature'] = self.use_v21feature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentFeatureVersion') is not None:
            self.current_feature_version = m.get('CurrentFeatureVersion')
        if m.get('EnableEmrCluster') is not None:
            self.enable_emr_cluster = m.get('EnableEmrCluster')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UseOnSaleVersion') is not None:
            self.use_on_sale_version = m.get('UseOnSaleVersion')
        if m.get('UseV21Feature') is not None:
            self.use_v21feature = m.get('UseV21Feature')
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


class GetUserResourceAuthorizationStatusResponseBody(TeaModel):
    def __init__(self, account_balance=None, account_sufficient=None, account_top_up_page=None,
                 all_authorization_page=None, buy_page=None, coupon_balance=None, current_feature_version=None,
                 disable_balance_check=None, dsw_default_authorization_page=None, env=None, ess_console_page=None,
                 ess_service_available=None, has_all_authorization=None, has_dsw_default_authorization=None, international=None,
                 is_sub_user=None, nas_console_page=None, real_name_verified=None, real_name_verified_page=None, region=None,
                 request_id=None, sub_user_authorization_page=None, sub_user_authorized=None, total_balance=None):
        # 现金账户余额
        self.account_balance = account_balance  # type: float
        # 金额是否充足
        self.account_sufficient = account_sufficient  # type: bool
        # 充值页面
        self.account_top_up_page = account_top_up_page  # type: str
        # 授权开通页面
        self.all_authorization_page = all_authorization_page  # type: str
        # 购买页
        self.buy_page = buy_page  # type: str
        # 代金券金额
        self.coupon_balance = coupon_balance  # type: float
        # 当前版本
        self.current_feature_version = current_feature_version  # type: str
        # 是否禁止金额验证
        self.disable_balance_check = disable_balance_check  # type: bool
        # dsw默认角色授权页面
        self.dsw_default_authorization_page = dsw_default_authorization_page  # type: str
        # 环境
        self.env = env  # type: str
        # ess开通页面
        self.ess_console_page = ess_console_page  # type: str
        # ess是否开通
        self.ess_service_available = ess_service_available  # type: bool
        # 是否通过购买验证
        self.has_all_authorization = has_all_authorization  # type: bool
        # 是否通过授权验证
        self.has_dsw_default_authorization = has_dsw_default_authorization  # type: bool
        # 是否国际站账号
        self.international = international  # type: bool
        # 是否子账号登录
        self.is_sub_user = is_sub_user  # type: bool
        # nas控制台
        self.nas_console_page = nas_console_page  # type: str
        # 是否实名认证
        self.real_name_verified = real_name_verified  # type: bool
        # 实名认证页面
        self.real_name_verified_page = real_name_verified_page  # type: str
        # 地区
        self.region = region  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 子账号授权开通页面
        self.sub_user_authorization_page = sub_user_authorization_page  # type: str
        # 子账号是否授权通过
        self.sub_user_authorized = sub_user_authorized  # type: bool
        # 总金额
        self.total_balance = total_balance  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResourceAuthorizationStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_balance is not None:
            result['AccountBalance'] = self.account_balance
        if self.account_sufficient is not None:
            result['AccountSufficient'] = self.account_sufficient
        if self.account_top_up_page is not None:
            result['AccountTopUpPage'] = self.account_top_up_page
        if self.all_authorization_page is not None:
            result['AllAuthorizationPage'] = self.all_authorization_page
        if self.buy_page is not None:
            result['BuyPage'] = self.buy_page
        if self.coupon_balance is not None:
            result['CouponBalance'] = self.coupon_balance
        if self.current_feature_version is not None:
            result['CurrentFeatureVersion'] = self.current_feature_version
        if self.disable_balance_check is not None:
            result['DisableBalanceCheck'] = self.disable_balance_check
        if self.dsw_default_authorization_page is not None:
            result['DswDefaultAuthorizationPage'] = self.dsw_default_authorization_page
        if self.env is not None:
            result['Env'] = self.env
        if self.ess_console_page is not None:
            result['EssConsolePage'] = self.ess_console_page
        if self.ess_service_available is not None:
            result['EssServiceAvailable'] = self.ess_service_available
        if self.has_all_authorization is not None:
            result['HasAllAuthorization'] = self.has_all_authorization
        if self.has_dsw_default_authorization is not None:
            result['HasDswDefaultAuthorization'] = self.has_dsw_default_authorization
        if self.international is not None:
            result['International'] = self.international
        if self.is_sub_user is not None:
            result['IsSubUser'] = self.is_sub_user
        if self.nas_console_page is not None:
            result['NasConsolePage'] = self.nas_console_page
        if self.real_name_verified is not None:
            result['RealNameVerified'] = self.real_name_verified
        if self.real_name_verified_page is not None:
            result['RealNameVerifiedPage'] = self.real_name_verified_page
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_user_authorization_page is not None:
            result['SubUserAuthorizationPage'] = self.sub_user_authorization_page
        if self.sub_user_authorized is not None:
            result['SubUserAuthorized'] = self.sub_user_authorized
        if self.total_balance is not None:
            result['TotalBalance'] = self.total_balance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountBalance') is not None:
            self.account_balance = m.get('AccountBalance')
        if m.get('AccountSufficient') is not None:
            self.account_sufficient = m.get('AccountSufficient')
        if m.get('AccountTopUpPage') is not None:
            self.account_top_up_page = m.get('AccountTopUpPage')
        if m.get('AllAuthorizationPage') is not None:
            self.all_authorization_page = m.get('AllAuthorizationPage')
        if m.get('BuyPage') is not None:
            self.buy_page = m.get('BuyPage')
        if m.get('CouponBalance') is not None:
            self.coupon_balance = m.get('CouponBalance')
        if m.get('CurrentFeatureVersion') is not None:
            self.current_feature_version = m.get('CurrentFeatureVersion')
        if m.get('DisableBalanceCheck') is not None:
            self.disable_balance_check = m.get('DisableBalanceCheck')
        if m.get('DswDefaultAuthorizationPage') is not None:
            self.dsw_default_authorization_page = m.get('DswDefaultAuthorizationPage')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('EssConsolePage') is not None:
            self.ess_console_page = m.get('EssConsolePage')
        if m.get('EssServiceAvailable') is not None:
            self.ess_service_available = m.get('EssServiceAvailable')
        if m.get('HasAllAuthorization') is not None:
            self.has_all_authorization = m.get('HasAllAuthorization')
        if m.get('HasDswDefaultAuthorization') is not None:
            self.has_dsw_default_authorization = m.get('HasDswDefaultAuthorization')
        if m.get('International') is not None:
            self.international = m.get('International')
        if m.get('IsSubUser') is not None:
            self.is_sub_user = m.get('IsSubUser')
        if m.get('NasConsolePage') is not None:
            self.nas_console_page = m.get('NasConsolePage')
        if m.get('RealNameVerified') is not None:
            self.real_name_verified = m.get('RealNameVerified')
        if m.get('RealNameVerifiedPage') is not None:
            self.real_name_verified_page = m.get('RealNameVerifiedPage')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubUserAuthorizationPage') is not None:
            self.sub_user_authorization_page = m.get('SubUserAuthorizationPage')
        if m.get('SubUserAuthorized') is not None:
            self.sub_user_authorized = m.get('SubUserAuthorized')
        if m.get('TotalBalance') is not None:
            self.total_balance = m.get('TotalBalance')
        return self


class GetUserResourceAuthorizationStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserResourceAuthorizationStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResourceAuthorizationStatusResponse, self).to_map()
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
            temp_model = GetUserResourceAuthorizationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResourceStatusResponseBody(TeaModel):
    def __init__(self, account_balance=None, account_sufficient=None, account_top_up_page=None,
                 all_authorization_page=None, coupon_balance=None, env=None, has_all_authorization=None, international=None,
                 real_name_verified=None, real_name_verified_page=None, region=None, request_id=None, total_balance=None):
        # 现金账户余额
        self.account_balance = account_balance  # type: float
        # 金额是否充足
        self.account_sufficient = account_sufficient  # type: bool
        # 充值页面
        self.account_top_up_page = account_top_up_page  # type: str
        # 授权页面
        self.all_authorization_page = all_authorization_page  # type: str
        # 代金券余额
        self.coupon_balance = coupon_balance  # type: float
        # 环境
        self.env = env  # type: str
        # 是否通过购买条件验证
        self.has_all_authorization = has_all_authorization  # type: bool
        # 是否国际站账号
        self.international = international  # type: bool
        # 是否实名验证
        self.real_name_verified = real_name_verified  # type: bool
        # 实名验证页面
        self.real_name_verified_page = real_name_verified_page  # type: str
        # 地区
        self.region = region  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 总余额
        self.total_balance = total_balance  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResourceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_balance is not None:
            result['AccountBalance'] = self.account_balance
        if self.account_sufficient is not None:
            result['AccountSufficient'] = self.account_sufficient
        if self.account_top_up_page is not None:
            result['AccountTopUpPage'] = self.account_top_up_page
        if self.all_authorization_page is not None:
            result['AllAuthorizationPage'] = self.all_authorization_page
        if self.coupon_balance is not None:
            result['CouponBalance'] = self.coupon_balance
        if self.env is not None:
            result['Env'] = self.env
        if self.has_all_authorization is not None:
            result['HasAllAuthorization'] = self.has_all_authorization
        if self.international is not None:
            result['International'] = self.international
        if self.real_name_verified is not None:
            result['RealNameVerified'] = self.real_name_verified
        if self.real_name_verified_page is not None:
            result['RealNameVerifiedPage'] = self.real_name_verified_page
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_balance is not None:
            result['TotalBalance'] = self.total_balance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountBalance') is not None:
            self.account_balance = m.get('AccountBalance')
        if m.get('AccountSufficient') is not None:
            self.account_sufficient = m.get('AccountSufficient')
        if m.get('AccountTopUpPage') is not None:
            self.account_top_up_page = m.get('AccountTopUpPage')
        if m.get('AllAuthorizationPage') is not None:
            self.all_authorization_page = m.get('AllAuthorizationPage')
        if m.get('CouponBalance') is not None:
            self.coupon_balance = m.get('CouponBalance')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('HasAllAuthorization') is not None:
            self.has_all_authorization = m.get('HasAllAuthorization')
        if m.get('International') is not None:
            self.international = m.get('International')
        if m.get('RealNameVerified') is not None:
            self.real_name_verified = m.get('RealNameVerified')
        if m.get('RealNameVerifiedPage') is not None:
            self.real_name_verified_page = m.get('RealNameVerifiedPage')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalBalance') is not None:
            self.total_balance = m.get('TotalBalance')
        return self


class GetUserResourceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserResourceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResourceStatusResponse, self).to_map()
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
            temp_model = GetUserResourceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserSpecialVersionGpuResourceInfoRequest(TeaModel):
    def __init__(self, pay_type=None):
        # 付费类型
        self.pay_type = pay_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserSpecialVersionGpuResourceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class GetUserSpecialVersionGpuResourceInfoResponseBody(TeaModel):
    def __init__(self, gpu_available_quota=None, gpu_total_quota=None, request_id=None, resources=None):
        self.gpu_available_quota = gpu_available_quota  # type: long
        self.gpu_total_quota = gpu_total_quota  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[ResourceInfo]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserSpecialVersionGpuResourceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_available_quota is not None:
            result['GpuAvailableQuota'] = self.gpu_available_quota
        if self.gpu_total_quota is not None:
            result['GpuTotalQuota'] = self.gpu_total_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpuAvailableQuota') is not None:
            self.gpu_available_quota = m.get('GpuAvailableQuota')
        if m.get('GpuTotalQuota') is not None:
            self.gpu_total_quota = m.get('GpuTotalQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ResourceInfo()
                self.resources.append(temp_model.from_map(k))
        return self


class GetUserSpecialVersionGpuResourceInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserSpecialVersionGpuResourceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserSpecialVersionGpuResourceInfoResponse, self).to_map()
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
            temp_model = GetUserSpecialVersionGpuResourceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, request_id=None):
        self.configs = configs  # type: list[Config]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = Config()
                self.configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConfigsResponse, self).to_map()
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
            temp_model = ListConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetsRequest(TeaModel):
    def __init__(self, workspace_id=None):
        # 工作空间Id
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDatasetsRequest, self).to_map()
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


class ListDatasetsResponseBody(TeaModel):
    def __init__(self, datasets=None, request_id=None):
        self.datasets = datasets  # type: list[Dataset]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDatasetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = Dataset()
                self.datasets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDatasetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDatasetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDatasetsResponse, self).to_map()
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
            temp_model = ListDatasetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsRequest(TeaModel):
    def __init__(self, accelerator_type_equals=None):
        # 每页返回的实例数
        self.accelerator_type_equals = accelerator_type_equals  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsSpecsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type_equals is not None:
            result['AcceleratorTypeEquals'] = self.accelerator_type_equals
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorTypeEquals') is not None:
            self.accelerator_type_equals = m.get('AcceleratorTypeEquals')
        return self


class ListEcsSpecsResponseBody(TeaModel):
    def __init__(self, ecs_specs=None, request_id=None, total_count=None):
        # 请求ecs规格列表
        self.ecs_specs = ecs_specs  # type: list[EcsSpec]
        # 请求ID
        self.request_id = request_id  # type: str
        # 符合要求的ecs规格数量
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


class ListImagesRequest(TeaModel):
    def __init__(self, accelerator_type_equals=None, image_name_contains=None, image_type_equals=None,
                 product=None, workspace_id=None):
        # 资源类型
        self.accelerator_type_equals = accelerator_type_equals  # type: str
        # 容器名称关键字
        self.image_name_contains = image_name_contains  # type: str
        # 镜像类型
        self.image_type_equals = image_type_equals  # type: str
        # 产品
        self.product = product  # type: str
        # 工作空间Id
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type_equals is not None:
            result['AcceleratorTypeEquals'] = self.accelerator_type_equals
        if self.image_name_contains is not None:
            result['ImageNameContains'] = self.image_name_contains
        if self.image_type_equals is not None:
            result['ImageTypeEquals'] = self.image_type_equals
        if self.product is not None:
            result['Product'] = self.product
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorTypeEquals') is not None:
            self.accelerator_type_equals = m.get('AcceleratorTypeEquals')
        if m.get('ImageNameContains') is not None:
            self.image_name_contains = m.get('ImageNameContains')
        if m.get('ImageTypeEquals') is not None:
            self.image_type_equals = m.get('ImageTypeEquals')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(self, images=None, request_id=None):
        # 镜像列表
        self.images = images  # type: list[Image]
        # 请求ID
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = Image()
                self.images.append(temp_model.from_map(k))
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


class ListInstanceSnapshotsResponseBody(TeaModel):
    def __init__(self, instance_snapshots=None, request_id=None):
        # 镜像快照列表
        self.instance_snapshots = instance_snapshots  # type: list[InstanceSnapshot]
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_snapshots:
            for k in self.instance_snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceSnapshotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceSnapshots'] = []
        if self.instance_snapshots is not None:
            for k in self.instance_snapshots:
                result['InstanceSnapshots'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_snapshots = []
        if m.get('InstanceSnapshots') is not None:
            for k in m.get('InstanceSnapshots'):
                temp_model = InstanceSnapshot()
                self.instance_snapshots.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstanceSnapshotsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceSnapshotsResponse, self).to_map()
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
            temp_model = ListInstanceSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceTypesRequest(TeaModel):
    def __init__(self, accelerator_type=None):
        # AcceleratorType
        self.accelerator_type = accelerator_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        return self


class ListInstanceTypesResponseBody(TeaModel):
    def __init__(self, instance_types=None, request_id=None):
        self.instance_types = instance_types  # type: list[InstanceType]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_types:
            for k in self.instance_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypes'] = []
        if self.instance_types is not None:
            for k in self.instance_types:
                result['InstanceTypes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_types = []
        if m.get('InstanceTypes') is not None:
            for k in m.get('InstanceTypes'):
                temp_model = InstanceType()
                self.instance_types.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstanceTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceTypesResponse, self).to_map()
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
            temp_model = ListInstanceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, in_workspace=None, instance_name_contains=None, instance_status_equals=None,
                 page_number=None, page_size=None, sort_by=None, sort_order=None, workspace_id_equals=None):
        # 是否在工作空间内查询
        self.in_workspace = in_workspace  # type: bool
        # 实例名称关键字
        self.instance_name_contains = instance_name_contains  # type: str
        # 实例状态
        self.instance_status_equals = instance_status_equals  # type: str
        # 当前页
        self.page_number = page_number  # type: str
        # 每页返回的实例数
        self.page_size = page_size  # type: str
        # 排序字段
        self.sort_by = sort_by  # type: str
        # 升序降序
        self.sort_order = sort_order  # type: str
        # 工作空间Id
        self.workspace_id_equals = workspace_id_equals  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_workspace is not None:
            result['InWorkspace'] = self.in_workspace
        if self.instance_name_contains is not None:
            result['InstanceNameContains'] = self.instance_name_contains
        if self.instance_status_equals is not None:
            result['InstanceStatusEquals'] = self.instance_status_equals
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.workspace_id_equals is not None:
            result['WorkspaceIdEquals'] = self.workspace_id_equals
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InWorkspace') is not None:
            self.in_workspace = m.get('InWorkspace')
        if m.get('InstanceNameContains') is not None:
            self.instance_name_contains = m.get('InstanceNameContains')
        if m.get('InstanceStatusEquals') is not None:
            self.instance_status_equals = m.get('InstanceStatusEquals')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('WorkspaceIdEquals') is not None:
            self.workspace_id_equals = m.get('WorkspaceIdEquals')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # 实例列表
        self.instances = instances  # type: list[Instance]
        # 当前页
        self.page_number = page_number  # type: long
        # 每页返回的实例数
        self.page_size = page_size  # type: long
        # 请求ID
        self.request_id = request_id  # type: str
        # 符合条件的实例数
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


class ListInstancesStatusRequest(TeaModel):
    def __init__(self, instance_ids=None):
        # 实例Id列表
        self.instance_ids = instance_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class ListInstancesStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, statuses=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.statuses = statuses  # type: list[InstanceStatus]

    def validate(self):
        if self.statuses:
            for k in self.statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statuses'] = []
        if self.statuses is not None:
            for k in self.statuses:
                result['Statuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statuses = []
        if m.get('Statuses') is not None:
            for k in m.get('Statuses'):
                temp_model = InstanceStatus()
                self.statuses.append(temp_model.from_map(k))
        return self


class ListInstancesStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstancesStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesStatusResponse, self).to_map()
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
            temp_model = ListInstancesStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacesResponseBody(TeaModel):
    def __init__(self, namespaces=None, request_id=None):
        # 命名空间列表
        self.namespaces = namespaces  # type: list[ImageNamespace]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNamespacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ImageNamespace()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNamespacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNamespacesResponse, self).to_map()
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
            temp_model = ListNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNasesResponseBody(TeaModel):
    def __init__(self, nases=None, request_id=None):
        # nas文件系统列表
        self.nases = nases  # type: list[Nas]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.nases:
            for k in self.nases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nases'] = []
        if self.nases is not None:
            for k in self.nases:
                result['Nases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nases = []
        if m.get('Nases') is not None:
            for k in m.get('Nases'):
                temp_model = Nas()
                self.nases.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNasesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNasesResponse, self).to_map()
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
            temp_model = ListNasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkSecurityGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, security_groups=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # security groups
        self.security_groups = security_groups  # type: list[list[SecurityGroup]]

    def validate(self):
        if self.security_groups:
            for k in self.security_groups:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListNetworkSecurityGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k in self.security_groups:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['securityGroups'].append(l1)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k in m.get('SecurityGroups'):
                l1 = []
                for k1 in k:
                    temp_model = SecurityGroup()
                    l1.append(temp_model.from_map(k1))
                self.security_groups.append(l1)
        return self


class ListNetworkSecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNetworkSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkSecurityGroupsResponse, self).to_map()
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
            temp_model = ListNetworkSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkVSwitchesResponseBody(TeaModel):
    def __init__(self, request_id=None, v_switches=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.v_switches = v_switches  # type: list[VSwitch]

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNetworkVSwitchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = VSwitch()
                self.v_switches.append(temp_model.from_map(k))
        return self


class ListNetworkVSwitchesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNetworkVSwitchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkVSwitchesResponse, self).to_map()
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
            temp_model = ListNetworkVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkVpcsResponseBody(TeaModel):
    def __init__(self, request_id=None, vpcs=None):
        # RequestId
        self.request_id = request_id  # type: str
        # vpc列表
        self.vpcs = vpcs  # type: list[Vpc]

    def validate(self):
        if self.vpcs:
            for k in self.vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNetworkVpcsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = Vpc()
                self.vpcs.append(temp_model.from_map(k))
        return self


class ListNetworkVpcsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNetworkVpcsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkVpcsResponse, self).to_map()
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
            temp_model = ListNetworkVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[Region]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = Region()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoriesResponseBody(TeaModel):
    def __init__(self, repositories=None, request_id=None):
        self.repositories = repositories  # type: list[ImageRepository]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.repositories:
            for k in self.repositories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Repositories'] = []
        if self.repositories is not None:
            for k in self.repositories:
                result['Repositories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.repositories = []
        if m.get('Repositories') is not None:
            for k in m.get('Repositories'):
                temp_model = ImageRepository()
                self.repositories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRepositoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRepositoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoriesResponse, self).to_map()
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
            temp_model = ListRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None):
        self.clusters = clusters  # type: list[Cluster]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = Cluster()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserClustersResponse, self).to_map()
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
            temp_model = ListUserClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserWorkNodesRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # 集群id
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserWorkNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListUserWorkNodesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserWorkNodesResponseBody, self).to_map()
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


class ListUserWorkNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserWorkNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserWorkNodesResponse, self).to_map()
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
            temp_model = ListUserWorkNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 请求ID
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
        # 是否保存镜像后停止
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
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 请求ID
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
        # 修改后实例名称
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
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 请求ID
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


class UpdateInstanceSnapshotRequest(TeaModel):
    def __init__(self, instance_snapshot_name=None):
        # 实例快照名称
        self.instance_snapshot_name = instance_snapshot_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_snapshot_name is not None:
            result['InstanceSnapshotName'] = self.instance_snapshot_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceSnapshotName') is not None:
            self.instance_snapshot_name = m.get('InstanceSnapshotName')
        return self


class UpdateInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, instance_id=None, instance_snapshot_id=None, request_id=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 实例镜像ID
        self.instance_snapshot_id = instance_snapshot_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_snapshot_id is not None:
            result['InstanceSnapshotId'] = self.instance_snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSnapshotId') is not None:
            self.instance_snapshot_id = m.get('InstanceSnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceSnapshotResponse, self).to_map()
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
            temp_model = UpdateInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


