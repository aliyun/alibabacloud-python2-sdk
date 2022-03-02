# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ComponentVersion(TeaModel):
    def __init__(self, app_version=None, component_name=None, component_uid=None, description=None, documents=None,
                 images_mapping=None, namespace=None, orchestration_type=None, orchestration_values=None, package_url=None,
                 parent_component=None, platforms=None, readme=None, resources=None, source=None, uid=None, version=None):
        # appVersion
        self.app_version = app_version  # type: str
        # componentName
        self.component_name = component_name  # type: str
        # componentUID
        self.component_uid = component_uid  # type: str
        # description
        self.description = description  # type: str
        # documents
        self.documents = documents  # type: str
        # imagesMapping
        self.images_mapping = images_mapping  # type: str
        # namespace
        self.namespace = namespace  # type: str
        # orchestrationType
        self.orchestration_type = orchestration_type  # type: str
        # orchestrationValues
        self.orchestration_values = orchestration_values  # type: str
        # packageURL
        self.package_url = package_url  # type: str
        # parentComponent
        self.parent_component = parent_component  # type: bool
        # platforms
        self.platforms = platforms  # type: list[Platform]
        # readme
        self.readme = readme  # type: str
        # resources
        self.resources = resources  # type: str
        # source
        self.source = source  # type: str
        # uid
        self.uid = uid  # type: str
        # version
        self.version = version  # type: str

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ComponentVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Disk(TeaModel):
    def __init__(self, capacity=None, fs_type=None, mount_point=None, name=None, remain=None, type=None):
        # capacity
        self.capacity = capacity  # type: int
        # fsType
        self.fs_type = fs_type  # type: str
        # mountPoint
        self.mount_point = mount_point  # type: str
        # name
        self.name = name  # type: str
        # remain
        self.remain = remain  # type: int
        # type
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Disk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.fs_type is not None:
            result['fsType'] = self.fs_type
        if self.mount_point is not None:
            result['mountPoint'] = self.mount_point
        if self.name is not None:
            result['name'] = self.name
        if self.remain is not None:
            result['remain'] = self.remain
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('fsType') is not None:
            self.fs_type = m.get('fsType')
        if m.get('mountPoint') is not None:
            self.mount_point = m.get('mountPoint')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remain') is not None:
            self.remain = m.get('remain')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ExportPort(TeaModel):
    def __init__(self, cidr_ip=None, port_range=None, protocol=None, unallowed=None):
        # 目标IP 段
        self.cidr_ip = cidr_ip  # type: str
        # 端口范围，格式：start/end
        self.port_range = port_range  # type: str
        # 协议
        self.protocol = protocol  # type: str
        # 为true，则代表deny
        self.unallowed = unallowed  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportPort, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['cidrIP'] = self.cidr_ip
        if self.port_range is not None:
            result['portRange'] = self.port_range
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.unallowed is not None:
            result['unallowed'] = self.unallowed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cidrIP') is not None:
            self.cidr_ip = m.get('cidrIP')
        if m.get('portRange') is not None:
            self.port_range = m.get('portRange')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('unallowed') is not None:
            self.unallowed = m.get('unallowed')
        return self


class FoundationVersionPackageTools(TeaModel):
    def __init__(self, name=None, version=None):
        # 工具名
        self.name = name  # type: str
        # 工具版本
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FoundationVersionPackageTools, self).to_map()
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


class FoundationVersion(TeaModel):
    def __init__(self, description=None, documents=None, features=None, labels=None, name=None, package_tools=None,
                 platforms=None, status=None, type=None, uid=None, version=None):
        # description
        self.description = description  # type: str
        # documents
        self.documents = documents  # type: str
        # 底座功能列表
        self.features = features  # type: list[str]
        # 标签
        self.labels = labels  # type: str
        # name，目前仅能是 “ADP 底座“
        self.name = name  # type: str
        # 打包工具
        self.package_tools = package_tools  # type: list[FoundationVersionPackageTools]
        # platforms
        self.platforms = platforms  # type: list[Platform]
        # status，ENUM:["Testing","Published","Deprecated"] Published 后，则全平台所有用户可见，请谨慎操作
        self.status = status  # type: str
        # the type of foundation version,ENUM:["trident","ack"]
        self.type = type  # type: str
        # uid
        self.uid = uid  # type: str
        # version
        self.version = version  # type: str

    def validate(self):
        if self.package_tools:
            for k in self.package_tools:
                if k:
                    k.validate()
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FoundationVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.features is not None:
            result['features'] = self.features
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        result['packageTools'] = []
        if self.package_tools is not None:
            for k in self.package_tools:
                result['packageTools'].append(k.to_map() if k else None)
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('features') is not None:
            self.features = m.get('features')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.package_tools = []
        if m.get('packageTools') is not None:
            for k in m.get('packageTools'):
                temp_model = FoundationVersionPackageTools()
                self.package_tools.append(temp_model.from_map(k))
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetInstanceInfoResponseNetworkCards(TeaModel):
    def __init__(self, ip=None, name=None):
        # ip
        self.ip = ip  # type: str
        # name
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceInfoResponseNetworkCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetInstanceInfoResponseTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # effect
        self.effect = effect  # type: str
        # key
        self.key = key  # type: str
        # value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceInfoResponseTaints, self).to_map()
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


class GetInstanceInfoResponse(TeaModel):
    def __init__(self, annotations=None, arch=None, cpu=None, data_disk=None, host_name=None, identifier=None,
                 image_id=None, instance_type=None, internet_bandwidth=None, kernel=None, labels=None, mac_address=None,
                 memory=None, network_cards=None, os=None, os_version=None, private_ip=None, public_ip=None,
                 root_password=None, system_disk=None, system_info=None, taints=None, uid=None):
        # annotations
        self.annotations = annotations  # type: dict[str, str]
        # arch
        self.arch = arch  # type: str
        # cpu
        self.cpu = cpu  # type: str
        # dataDisk
        self.data_disk = data_disk  # type: list[Disk]
        # hostName
        self.host_name = host_name  # type: str
        # identifier
        self.identifier = identifier  # type: str
        # imageID
        self.image_id = image_id  # type: str
        # instanceType
        self.instance_type = instance_type  # type: str
        # internetBandwidth
        self.internet_bandwidth = internet_bandwidth  # type: int
        # kernel
        self.kernel = kernel  # type: str
        # labels
        self.labels = labels  # type: dict[str, str]
        # macAddress
        self.mac_address = mac_address  # type: str
        # memory
        self.memory = memory  # type: str
        # networkCards
        self.network_cards = network_cards  # type: list[GetInstanceInfoResponseNetworkCards]
        # os
        self.os = os  # type: str
        # osVersion
        self.os_version = os_version  # type: str
        # privateIP
        self.private_ip = private_ip  # type: str
        # publicIP
        self.public_ip = public_ip  # type: str
        # rootPassword
        self.root_password = root_password  # type: str
        # systemDisk
        self.system_disk = system_disk  # type: list[Disk]
        # systemInfo
        self.system_info = system_info  # type: str
        # taints
        self.taints = taints  # type: list[GetInstanceInfoResponseTaints]
        # uid
        self.uid = uid  # type: str

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.network_cards:
            for k in self.network_cards:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.arch is not None:
            result['arch'] = self.arch
        if self.cpu is not None:
            result['cpu'] = self.cpu
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image_id is not None:
            result['imageID'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth is not None:
            result['internetBandwidth'] = self.internet_bandwidth
        if self.kernel is not None:
            result['kernel'] = self.kernel
        if self.labels is not None:
            result['labels'] = self.labels
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        if self.memory is not None:
            result['memory'] = self.memory
        result['networkCards'] = []
        if self.network_cards is not None:
            for k in self.network_cards:
                result['networkCards'].append(k.to_map() if k else None)
        if self.os is not None:
            result['os'] = self.os
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        if self.system_info is not None:
            result['systemInfo'] = self.system_info
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('arch') is not None:
            self.arch = m.get('arch')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = Disk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('imageID') is not None:
            self.image_id = m.get('imageID')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidth') is not None:
            self.internet_bandwidth = m.get('internetBandwidth')
        if m.get('kernel') is not None:
            self.kernel = m.get('kernel')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        self.network_cards = []
        if m.get('networkCards') is not None:
            for k in m.get('networkCards'):
                temp_model = GetInstanceInfoResponseNetworkCards()
                self.network_cards.append(temp_model.from_map(k))
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('publicIP') is not None:
            self.public_ip = m.get('publicIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = Disk()
                self.system_disk.append(temp_model.from_map(k))
        if m.get('systemInfo') is not None:
            self.system_info = m.get('systemInfo')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = GetInstanceInfoResponseTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class InstanceInfoNetworkCards(TeaModel):
    def __init__(self, ip=None, name=None):
        # ip
        self.ip = ip  # type: str
        # name
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstanceInfoNetworkCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class InstanceInfoTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # effect
        self.effect = effect  # type: str
        # key
        self.key = key  # type: str
        # value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstanceInfoTaints, self).to_map()
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


class InstanceInfo(TeaModel):
    def __init__(self, annotations=None, arch=None, cpu=None, data_disk=None, disk_config_annotations=None,
                 host_name=None, identifier=None, image_id=None, instance_type=None, internet_bandwidth=None, kernel=None,
                 labels=None, mac_address=None, memory=None, network_cards=None, os=None, os_version=None, private_ip=None,
                 public_ip=None, root_password=None, system_disk=None, system_info=None, taints=None):
        # annotations
        self.annotations = annotations  # type: dict[str, str]
        # arch
        self.arch = arch  # type: str
        # cpu
        self.cpu = cpu  # type: str
        # dataDisk
        self.data_disk = data_disk  # type: list[Disk]
        # diskConfigAnnotations
        self.disk_config_annotations = disk_config_annotations  # type: dict[str, str]
        # hostName
        self.host_name = host_name  # type: str
        # identifier
        self.identifier = identifier  # type: str
        # imageID
        self.image_id = image_id  # type: str
        # instanceType
        self.instance_type = instance_type  # type: str
        # internetBandwidth
        self.internet_bandwidth = internet_bandwidth  # type: int
        # kernel
        self.kernel = kernel  # type: str
        # labels
        self.labels = labels  # type: dict[str, str]
        # macAddress
        self.mac_address = mac_address  # type: str
        # memory
        self.memory = memory  # type: str
        # networkCards
        self.network_cards = network_cards  # type: list[InstanceInfoNetworkCards]
        # os
        self.os = os  # type: str
        # osVersion
        self.os_version = os_version  # type: str
        # privateIP
        self.private_ip = private_ip  # type: str
        # publicIP
        self.public_ip = public_ip  # type: str
        # rootPassword
        self.root_password = root_password  # type: str
        # systemDisk
        self.system_disk = system_disk  # type: list[Disk]
        # systemInfo
        self.system_info = system_info  # type: str
        # taints
        self.taints = taints  # type: list[InstanceInfoTaints]

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.network_cards:
            for k in self.network_cards:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.arch is not None:
            result['arch'] = self.arch
        if self.cpu is not None:
            result['cpu'] = self.cpu
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.disk_config_annotations is not None:
            result['diskConfigAnnotations'] = self.disk_config_annotations
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image_id is not None:
            result['imageID'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth is not None:
            result['internetBandwidth'] = self.internet_bandwidth
        if self.kernel is not None:
            result['kernel'] = self.kernel
        if self.labels is not None:
            result['labels'] = self.labels
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        if self.memory is not None:
            result['memory'] = self.memory
        result['networkCards'] = []
        if self.network_cards is not None:
            for k in self.network_cards:
                result['networkCards'].append(k.to_map() if k else None)
        if self.os is not None:
            result['os'] = self.os
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        if self.system_info is not None:
            result['systemInfo'] = self.system_info
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('arch') is not None:
            self.arch = m.get('arch')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = Disk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('diskConfigAnnotations') is not None:
            self.disk_config_annotations = m.get('diskConfigAnnotations')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('imageID') is not None:
            self.image_id = m.get('imageID')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidth') is not None:
            self.internet_bandwidth = m.get('internetBandwidth')
        if m.get('kernel') is not None:
            self.kernel = m.get('kernel')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        self.network_cards = []
        if m.get('networkCards') is not None:
            for k in m.get('networkCards'):
                temp_model = InstanceInfoNetworkCards()
                self.network_cards.append(temp_model.from_map(k))
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('publicIP') is not None:
            self.public_ip = m.get('publicIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = Disk()
                self.system_disk.append(temp_model.from_map(k))
        if m.get('systemInfo') is not None:
            self.system_info = m.get('systemInfo')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = InstanceInfoTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class Platform(TeaModel):
    def __init__(self, architecture=None, os=None):
        # architecture
        self.architecture = architecture  # type: str
        # os
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Platform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ProductComponentRelationDetail(TeaModel):
    def __init__(self, app_version=None, category=None, class_=None, component_name=None,
                 component_orchestration_values=None, component_uid=None, component_version_uid=None, created_at=None, description=None,
                 documents=None, enable=None, images_mapping=None, namespace=None, orchestration_type=None,
                 parent_component=None, parent_component_version_relation_uid=None, parent_component_version_uid=None,
                 priority=None, product_version_uid=None, provider=None, public=None, readme=None, relation_uid=None,
                 release_name=None, resources=None, sequence=None, singleton=None, source=None, version=None):
        # appVersion
        self.app_version = app_version  # type: str
        # category
        self.category = category  # type: str
        # class
        self.class_ = class_  # type: str
        # componentName
        self.component_name = component_name  # type: str
        # componentOrchestrationValues
        self.component_orchestration_values = component_orchestration_values  # type: str
        # componentUID
        self.component_uid = component_uid  # type: str
        # componentVersionUID
        self.component_version_uid = component_version_uid  # type: str
        # createdAt
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # documents
        self.documents = documents  # type: str
        # enable
        self.enable = enable  # type: bool
        # imagesMapping
        self.images_mapping = images_mapping  # type: str
        # namespace
        self.namespace = namespace  # type: str
        # orchestrationType
        self.orchestration_type = orchestration_type  # type: str
        # parentComponent
        self.parent_component = parent_component  # type: bool
        # parentComponentVersionRelationUID
        self.parent_component_version_relation_uid = parent_component_version_relation_uid  # type: str
        # parentComponentVersionUID
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        # priority
        self.priority = priority  # type: int
        # productVersionUID
        self.product_version_uid = product_version_uid  # type: str
        # provider
        self.provider = provider  # type: str
        # public
        self.public = public  # type: bool
        # readme
        self.readme = readme  # type: str
        # relationUID
        self.relation_uid = relation_uid  # type: str
        # releaseName
        self.release_name = release_name  # type: str
        # resources
        self.resources = resources  # type: str
        # sequence
        self.sequence = sequence  # type: int
        # singleton
        self.singleton = singleton  # type: bool
        # source
        self.source = source  # type: str
        # version
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductComponentRelationDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.parent_component_version_relation_uid is not None:
            result['parentComponentVersionRelationUID'] = self.parent_component_version_relation_uid
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.priority is not None:
            result['priority'] = self.priority
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.resources is not None:
            result['resources'] = self.resources
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('parentComponentVersionRelationUID') is not None:
            self.parent_component_version_relation_uid = m.get('parentComponentVersionRelationUID')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ResourceCpu(TeaModel):
    def __init__(self, required=None):
        # 需要的数量
        self.required = required  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceCpu, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class ResourceImage(TeaModel):
    def __init__(self, id=None, name_regex=None):
        # image id
        self.id = id  # type: str
        # 名称正则
        self.name_regex = name_regex  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name_regex is not None:
            result['nameRegex'] = self.name_regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nameRegex') is not None:
            self.name_regex = m.get('nameRegex')
        return self


class ResourceMemory(TeaModel):
    def __init__(self, required=None):
        # 需要的内存，单位 G
        self.required = required  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class ResourcePublicIP(TeaModel):
    def __init__(self, bandwidth=None, required=None):
        # 带宽
        self.bandwidth = bandwidth  # type: int
        # 需要的数量
        self.required = required  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourcePublicIP, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class ResourceStorage(TeaModel):
    def __init__(self, required=None):
        # 磁盘大小
        self.required = required  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceStorage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class Resource(TeaModel):
    def __init__(self, cpu=None, hostname=None, identifier=None, image=None, instance_type=None, memory=None,
                 ports=None, public_ip=None, replica=None, storage=None):
        # cpu
        self.cpu = cpu  # type: ResourceCpu
        # 实例hostname
        self.hostname = hostname  # type: str
        # 资源分组名
        self.identifier = identifier  # type: str
        # 镜像
        self.image = image  # type: ResourceImage
        # 实例类型
        self.instance_type = instance_type  # type: str
        # memory
        self.memory = memory  # type: ResourceMemory
        # 需要开放的端口
        self.ports = ports  # type: list[ExportPort]
        # 公网IP 需求
        self.public_ip = public_ip  # type: ResourcePublicIP
        # 数量
        self.replica = replica  # type: int
        # 存储需求
        self.storage = storage  # type: list[ResourceStorage]

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.image:
            self.image.validate()
        if self.memory:
            self.memory.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.public_ip:
            self.public_ip.validate()
        if self.storage:
            for k in self.storage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Resource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu.to_map()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image is not None:
            result['image'] = self.image.to_map()
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.memory is not None:
            result['memory'] = self.memory.to_map()
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip.to_map()
        if self.replica is not None:
            result['replica'] = self.replica
        result['storage'] = []
        if self.storage is not None:
            for k in self.storage:
                result['storage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpu') is not None:
            temp_model = ResourceCpu()
            self.cpu = temp_model.from_map(m['cpu'])
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('image') is not None:
            temp_model = ResourceImage()
            self.image = temp_model.from_map(m['image'])
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('memory') is not None:
            temp_model = ResourceMemory()
            self.memory = temp_model.from_map(m['memory'])
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = ExportPort()
                self.ports.append(temp_model.from_map(k))
        if m.get('publicIP') is not None:
            temp_model = ResourcePublicIP()
            self.public_ip = temp_model.from_map(m['publicIP'])
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        self.storage = []
        if m.get('storage') is not None:
            for k in m.get('storage'):
                temp_model = ResourceStorage()
                self.storage.append(temp_model.from_map(k))
        return self


class AddEnvironmentNodesRequestDataDisk(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentNodesRequestDataDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class AddEnvironmentNodesRequestSystemDisk(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentNodesRequestSystemDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class AddEnvironmentNodesRequestTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        self.effect = effect  # type: str
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentNodesRequestTaints, self).to_map()
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


class AddEnvironmentNodesRequest(TeaModel):
    def __init__(self, application_disk=None, cpu=None, data_disk=None, etcd_disk=None, host_name=None, labels=None,
                 master_private_ips=None, memory=None, os=None, root_password=None, system_disk=None, taints=None,
                 trident_system_disk=None, trident_system_size_disk=None, worker_private_ips=None):
        # 保留业务分区
        self.application_disk = application_disk  # type: str
        self.cpu = cpu  # type: int
        self.data_disk = data_disk  # type: list[AddEnvironmentNodesRequestDataDisk]
        # etcd数据盘
        self.etcd_disk = etcd_disk  # type: str
        self.host_name = host_name  # type: str
        self.labels = labels  # type: dict[str, any]
        # master privateId
        self.master_private_ips = master_private_ips  # type: list[str]
        self.memory = memory  # type: int
        self.os = os  # type: str
        self.root_password = root_password  # type: str
        self.system_disk = system_disk  # type: list[AddEnvironmentNodesRequestSystemDisk]
        self.taints = taints  # type: list[AddEnvironmentNodesRequestTaints]
        # k8s管控数据盘
        self.trident_system_disk = trident_system_disk  # type: str
        # k8s管控数据盘大小
        self.trident_system_size_disk = trident_system_size_disk  # type: int
        # work privateIp
        self.worker_private_ips = worker_private_ips  # type: list[str]

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddEnvironmentNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_disk is not None:
            result['applicationDisk'] = self.application_disk
        if self.cpu is not None:
            result['cpu'] = self.cpu
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.etcd_disk is not None:
            result['etcdDisk'] = self.etcd_disk
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.labels is not None:
            result['labels'] = self.labels
        if self.master_private_ips is not None:
            result['masterPrivateIPs'] = self.master_private_ips
        if self.memory is not None:
            result['memory'] = self.memory
        if self.os is not None:
            result['os'] = self.os
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.trident_system_disk is not None:
            result['tridentSystemDisk'] = self.trident_system_disk
        if self.trident_system_size_disk is not None:
            result['tridentSystemSizeDisk'] = self.trident_system_size_disk
        if self.worker_private_ips is not None:
            result['workerPrivateIPs'] = self.worker_private_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applicationDisk') is not None:
            self.application_disk = m.get('applicationDisk')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = AddEnvironmentNodesRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('etcdDisk') is not None:
            self.etcd_disk = m.get('etcdDisk')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('masterPrivateIPs') is not None:
            self.master_private_ips = m.get('masterPrivateIPs')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = AddEnvironmentNodesRequestSystemDisk()
                self.system_disk.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = AddEnvironmentNodesRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('tridentSystemDisk') is not None:
            self.trident_system_disk = m.get('tridentSystemDisk')
        if m.get('tridentSystemSizeDisk') is not None:
            self.trident_system_size_disk = m.get('tridentSystemSizeDisk')
        if m.get('workerPrivateIPs') is not None:
            self.worker_private_ips = m.get('workerPrivateIPs')
        return self


class AddEnvironmentNodesResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AddEnvironmentNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddEnvironmentNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEnvironmentNodesResponse, self).to_map()
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
            temp_model = AddEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProductComponentVersionRequest(TeaModel):
    def __init__(self, release_name=None):
        self.release_name = release_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProductComponentVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        return self


class AddProductComponentVersionResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProductComponentVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class AddProductComponentVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: AddProductComponentVersionResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddProductComponentVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AddProductComponentVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AddProductComponentVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddProductComponentVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddProductComponentVersionResponse, self).to_map()
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
            temp_model = AddProductComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProductVersionConfigRequest(TeaModel):
    def __init__(self, component_version_uid=None, description=None, name=None, parent_component_version_uid=None,
                 value=None, value_type=None):
        # 组件uid
        self.component_version_uid = component_version_uid  # type: str
        # 配置说明
        self.description = description  # type: str
        # 配置信息key
        self.name = name  # type: str
        # 父组件uid
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        # 配置信息value
        self.value = value  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProductVersionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class AddProductVersionConfigResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        # product version config uid
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProductVersionConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class AddProductVersionConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AddProductVersionConfigResponseBodyData
        self.msg = msg  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddProductVersionConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AddProductVersionConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddProductVersionConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddProductVersionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddProductVersionConfigResponse, self).to_map()
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
            temp_model = AddProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddEnvironmentNodesRequest(TeaModel):
    def __init__(self, instance_list=None):
        self.instance_list = instance_list  # type: list[InstanceInfo]

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchAddEnvironmentNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['instanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_list = []
        if m.get('instanceList') is not None:
            for k in m.get('instanceList'):
                temp_model = InstanceInfo()
                self.instance_list.append(temp_model.from_map(k))
        return self


class BatchAddEnvironmentNodesResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddEnvironmentNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class BatchAddEnvironmentNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchAddEnvironmentNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchAddEnvironmentNodesResponse, self).to_map()
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
            temp_model = BatchAddEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddProductVersionConfigRequestProductVersionConfigList(TeaModel):
    def __init__(self, component_version_uid=None, description=None, name=None, parent_component_version_uid=None,
                 value=None, value_type=None):
        # 组件uid
        self.component_version_uid = component_version_uid  # type: str
        # 配置说明
        self.description = description  # type: str
        # 配置信息key
        self.name = name  # type: str
        # 父组件uid
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        # 配置信息value
        self.value = value  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddProductVersionConfigRequestProductVersionConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class BatchAddProductVersionConfigRequest(TeaModel):
    def __init__(self, product_version_config_list=None):
        self.product_version_config_list = product_version_config_list  # type: list[BatchAddProductVersionConfigRequestProductVersionConfigList]

    def validate(self):
        if self.product_version_config_list:
            for k in self.product_version_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchAddProductVersionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['productVersionConfigList'] = []
        if self.product_version_config_list is not None:
            for k in self.product_version_config_list:
                result['productVersionConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_version_config_list = []
        if m.get('productVersionConfigList') is not None:
            for k in m.get('productVersionConfigList'):
                temp_model = BatchAddProductVersionConfigRequestProductVersionConfigList()
                self.product_version_config_list.append(temp_model.from_map(k))
        return self


class BatchAddProductVersionConfigResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddProductVersionConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class BatchAddProductVersionConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchAddProductVersionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchAddProductVersionConfigResponse, self).to_map()
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
            temp_model = BatchAddProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateEnvironmentRequestPlatform(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentRequestPlatform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class CreateEnvironmentRequest(TeaModel):
    def __init__(self, description=None, location=None, name=None, platform=None, product_version_uid=None,
                 type=None, vendor_config=None, vendor_type=None):
        self.description = description  # type: str
        self.location = location  # type: str
        self.name = name  # type: str
        self.platform = platform  # type: CreateEnvironmentRequestPlatform
        self.product_version_uid = product_version_uid  # type: str
        # 环境类型
        self.type = type  # type: str
        self.vendor_config = vendor_config  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super(CreateEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.type is not None:
            result['type'] = self.type
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = CreateEnvironmentRequestPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class CreateEnvironmentResponseBodyData(TeaModel):
    def __init__(self, environment_uid=None, vendor_config=None):
        self.environment_uid = environment_uid  # type: str
        self.vendor_config = vendor_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class CreateEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: CreateEnvironmentResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnvironmentResponse, self).to_map()
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
            temp_model = CreateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentLicenseRequest(TeaModel):
    def __init__(self, company_name=None, contact=None, machine_fingerprint=None, scenario=None, type=None):
        # 企业名称
        self.company_name = company_name  # type: str
        # 联系方式
        self.contact = contact  # type: str
        # 机器指纹信息
        self.machine_fingerprint = machine_fingerprint  # type: str
        # 使用场景
        self.scenario = scenario  # type: str
        # 证书类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['companyName'] = self.company_name
        if self.contact is not None:
            result['contact'] = self.contact
        if self.machine_fingerprint is not None:
            result['machineFingerprint'] = self.machine_fingerprint
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('companyName') is not None:
            self.company_name = m.get('companyName')
        if m.get('contact') is not None:
            self.contact = m.get('contact')
        if m.get('machineFingerprint') is not None:
            self.machine_fingerprint = m.get('machineFingerprint')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateEnvironmentLicenseResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        # license uid
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentLicenseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateEnvironmentLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        # 业务数据
        self.data = data  # type: CreateEnvironmentLicenseResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEnvironmentLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateEnvironmentLicenseResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateEnvironmentLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEnvironmentLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnvironmentLicenseResponse, self).to_map()
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
            temp_model = CreateEnvironmentLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFoundationReferenceRequest(TeaModel):
    def __init__(self, cluster_config=None, foundation_version_uid=None):
        self.cluster_config = cluster_config  # type: str
        self.foundation_version_uid = foundation_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFoundationReferenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_config is not None:
            result['clusterConfig'] = self.cluster_config
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterConfig') is not None:
            self.cluster_config = m.get('clusterConfig')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        return self


class CreateFoundationReferenceResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFoundationReferenceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateFoundationReferenceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: CreateFoundationReferenceResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateFoundationReferenceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateFoundationReferenceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateFoundationReferenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFoundationReferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFoundationReferenceResponse, self).to_map()
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
            temp_model = CreateFoundationReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateProductRequest(TeaModel):
    def __init__(self, description=None, foundation_version_uid=None, product_name=None):
        self.description = description  # type: str
        self.foundation_version_uid = foundation_version_uid  # type: str
        self.product_name = product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.product_name is not None:
            result['productName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        return self


class CreateProductResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: CreateProductResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProductResponse, self).to_map()
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
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductDeploymentRequest(TeaModel):
    def __init__(self, environment_uid=None, old_product_version_uid=None, package_uid=None,
                 product_version_uid=None):
        # 环境uid
        self.environment_uid = environment_uid  # type: str
        # 旧产品版本uid
        self.old_product_version_uid = old_product_version_uid  # type: str
        # 部署包uid
        self.package_uid = package_uid  # type: str
        # 产品版本uid
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductDeploymentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.package_uid is not None:
            result['packageUID'] = self.package_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('packageUID') is not None:
            self.package_uid = m.get('packageUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class CreateProductDeploymentResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        # 部署uid
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductDeploymentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductDeploymentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        # 错误码
        self.code = code  # type: str
        # 数据
        self.data = data  # type: CreateProductDeploymentResponseBodyData
        # 错误信息
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProductDeploymentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductDeploymentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateProductDeploymentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProductDeploymentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProductDeploymentResponse, self).to_map()
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
            temp_model = CreateProductDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductVersionResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: CreateProductVersionResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProductVersionResponse, self).to_map()
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
            temp_model = CreateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductVersionPackageHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductVersionPackageHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateProductVersionPackageRequest(TeaModel):
    def __init__(self, old_product_version_uid=None, package_content_type=None, package_type=None, platform=None):
        self.old_product_version_uid = old_product_version_uid  # type: str
        # ENUM:["all","base"."application"]
        self.package_content_type = package_content_type  # type: str
        # ENUM:["full","upgrade"]
        self.package_type = package_type  # type: str
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductVersionPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.platform is not None:
            result['platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        return self


class CreateProductVersionPackageResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductVersionPackageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductVersionPackageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: CreateProductVersionPackageResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProductVersionPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductVersionPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateProductVersionPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProductVersionPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProductVersionPackageResponse, self).to_map()
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
            temp_model = CreateProductVersionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnvironmentResponse, self).to_map()
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
            temp_model = DeleteEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentNodeResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnvironmentNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteEnvironmentNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEnvironmentNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnvironmentNodeResponse, self).to_map()
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
            temp_model = DeleteEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentProductVersionResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnvironmentProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteEnvironmentProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEnvironmentProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnvironmentProductVersionResponse, self).to_map()
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
            temp_model = DeleteEnvironmentProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductResponse, self).to_map()
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
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductComponentVersionResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductComponentVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteProductComponentVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProductComponentVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductComponentVersionResponse, self).to_map()
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
            temp_model = DeleteProductComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductInstanceConfigRequest(TeaModel):
    def __init__(self, environment_uid=None, product_version_uid=None):
        self.environment_uid = environment_uid  # type: str
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductInstanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class DeleteProductInstanceConfigResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductInstanceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteProductInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProductInstanceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductInstanceConfigResponse, self).to_map()
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
            temp_model = DeleteProductInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductVersionResponseBody(TeaModel):
    def __init__(self, code=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.msg = msg  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductVersionResponse, self).to_map()
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
            temp_model = DeleteProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductVersionConfigResponseBody(TeaModel):
    def __init__(self, code=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.msg = msg  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductVersionConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProductVersionConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProductVersionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductVersionConfigResponse, self).to_map()
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
            temp_model = DeleteProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateProductInstanceDeploymentConfigRequest(TeaModel):
    def __init__(self, environment_uid=None, product_version_uid=None):
        self.environment_uid = environment_uid  # type: str
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateProductInstanceDeploymentConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class GenerateProductInstanceDeploymentConfigResponseBodyData(TeaModel):
    def __init__(self, package_config=None):
        self.package_config = package_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateProductInstanceDeploymentConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_config is not None:
            result['packageConfig'] = self.package_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('packageConfig') is not None:
            self.package_config = m.get('packageConfig')
        return self


class GenerateProductInstanceDeploymentConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GenerateProductInstanceDeploymentConfigResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateProductInstanceDeploymentConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GenerateProductInstanceDeploymentConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GenerateProductInstanceDeploymentConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateProductInstanceDeploymentConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateProductInstanceDeploymentConfigResponse, self).to_map()
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
            temp_model = GenerateProductInstanceDeploymentConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComponentResponseBodyData(TeaModel):
    def __init__(self, category=None, description=None, documents=None, name=None, public=None, singleton=None,
                 source=None, uid=None):
        self.category = category  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: str
        self.name = name  # type: str
        self.public = public  # type: bool
        self.singleton = singleton  # type: bool
        self.source = source  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetComponentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.public is not None:
            result['public'] = self.public
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetComponentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetComponentResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetComponentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetComponentResponse, self).to_map()
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
            temp_model = GetComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComponentVersionResponseBodyData(TeaModel):
    def __init__(self, component_name=None, component_uid=None, description=None, documents=None,
                 orchestration_values=None, package_url=None, parent_component=None, product_component_version_uid=None, provider=None,
                 readme=None, resources=None, uid=None, version=None):
        self.component_name = component_name  # type: str
        self.component_uid = component_uid  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: list[str]
        self.orchestration_values = orchestration_values  # type: str
        self.package_url = package_url  # type: str
        self.parent_component = parent_component  # type: bool
        self.product_component_version_uid = product_component_version_uid  # type: str
        self.provider = provider  # type: str
        self.readme = readme  # type: str
        self.resources = resources  # type: str
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetComponentVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.product_component_version_uid is not None:
            result['productComponentVersionUID'] = self.product_component_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('productComponentVersionUID') is not None:
            self.product_component_version_uid = m.get('productComponentVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetComponentVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetComponentVersionResponseBodyData]
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetComponentVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetComponentVersionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetComponentVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetComponentVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetComponentVersionResponse, self).to_map()
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
            temp_model = GetComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentResponseBodyDataPlatform(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentResponseBodyDataPlatform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class GetEnvironmentResponseBodyData(TeaModel):
    def __init__(self, cluster_id=None, created_at=None, description=None, foundation_version=None,
                 foundation_version_uid=None, instance_list=None, instance_status=None, location=None, name=None, old_product_version=None,
                 old_product_version_uid=None, platform=None, product_name=None, product_version=None, uid=None, vendor_config=None,
                 vendor_type=None):
        self.cluster_id = cluster_id  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.foundation_version = foundation_version  # type: str
        self.foundation_version_uid = foundation_version_uid  # type: str
        self.instance_list = instance_list  # type: list[InstanceInfo]
        self.instance_status = instance_status  # type: str
        self.location = location  # type: str
        self.name = name  # type: str
        self.old_product_version = old_product_version  # type: str
        self.old_product_version_uid = old_product_version_uid  # type: str
        self.platform = platform  # type: GetEnvironmentResponseBodyDataPlatform
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.uid = uid  # type: str
        self.vendor_config = vendor_config  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.foundation_version is not None:
            result['foundationVersion'] = self.foundation_version
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        result['instanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['instanceList'].append(k.to_map() if k else None)
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.old_product_version is not None:
            result['oldProductVersion'] = self.old_product_version
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foundationVersion') is not None:
            self.foundation_version = m.get('foundationVersion')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        self.instance_list = []
        if m.get('instanceList') is not None:
            for k in m.get('instanceList'):
                temp_model = InstanceInfo()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('oldProductVersion') is not None:
            self.old_product_version = m.get('oldProductVersion')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('platform') is not None:
            temp_model = GetEnvironmentResponseBodyDataPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetEnvironmentResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponse, self).to_map()
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
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentLicenseResponseBodyDataLicenseQuotaClusterQuota(TeaModel):
    def __init__(self, cpu_core_limit=None):
        # cpu核数限制
        self.cpu_core_limit = cpu_core_limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentLicenseResponseBodyDataLicenseQuotaClusterQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_limit is not None:
            result['cpuCoreLimit'] = self.cpu_core_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpuCoreLimit') is not None:
            self.cpu_core_limit = m.get('cpuCoreLimit')
        return self


class GetEnvironmentLicenseResponseBodyDataLicenseQuotaComponentQuotas(TeaModel):
    def __init__(self, component_name=None, component_source=None, instance_limit=None):
        # 组件名
        self.component_name = component_name  # type: str
        # 组件来源
        self.component_source = component_source  # type: str
        # 实例数限制
        self.instance_limit = instance_limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentLicenseResponseBodyDataLicenseQuotaComponentQuotas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_source is not None:
            result['componentSource'] = self.component_source
        if self.instance_limit is not None:
            result['instanceLimit'] = self.instance_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentSource') is not None:
            self.component_source = m.get('componentSource')
        if m.get('instanceLimit') is not None:
            self.instance_limit = m.get('instanceLimit')
        return self


class GetEnvironmentLicenseResponseBodyDataLicenseQuota(TeaModel):
    def __init__(self, cluster_quota=None, component_quotas=None):
        # 集群配额
        self.cluster_quota = cluster_quota  # type: GetEnvironmentLicenseResponseBodyDataLicenseQuotaClusterQuota
        # 组件配额
        self.component_quotas = component_quotas  # type: list[GetEnvironmentLicenseResponseBodyDataLicenseQuotaComponentQuotas]

    def validate(self):
        if self.cluster_quota:
            self.cluster_quota.validate()
        if self.component_quotas:
            for k in self.component_quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEnvironmentLicenseResponseBodyDataLicenseQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_quota is not None:
            result['clusterQuota'] = self.cluster_quota.to_map()
        result['componentQuotas'] = []
        if self.component_quotas is not None:
            for k in self.component_quotas:
                result['componentQuotas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterQuota') is not None:
            temp_model = GetEnvironmentLicenseResponseBodyDataLicenseQuotaClusterQuota()
            self.cluster_quota = temp_model.from_map(m['clusterQuota'])
        self.component_quotas = []
        if m.get('componentQuotas') is not None:
            for k in m.get('componentQuotas'):
                temp_model = GetEnvironmentLicenseResponseBodyDataLicenseQuotaComponentQuotas()
                self.component_quotas.append(temp_model.from_map(k))
        return self


class GetEnvironmentLicenseResponseBodyData(TeaModel):
    def __init__(self, expire_time=None, license_key=None, license_quota=None, reject_reason=None, status=None,
                 type=None, uid=None):
        # 过期时间
        self.expire_time = expire_time  # type: str
        # license内容
        self.license_key = license_key  # type: str
        # license配额
        self.license_quota = license_quota  # type: GetEnvironmentLicenseResponseBodyDataLicenseQuota
        # 拒绝原因
        self.reject_reason = reject_reason  # type: str
        # 状态
        self.status = status  # type: str
        # 类型
        self.type = type  # type: str
        # license uid
        self.uid = uid  # type: str

    def validate(self):
        if self.license_quota:
            self.license_quota.validate()

    def to_map(self):
        _map = super(GetEnvironmentLicenseResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        if self.license_quota is not None:
            result['licenseQuota'] = self.license_quota.to_map()
        if self.reject_reason is not None:
            result['rejectReason'] = self.reject_reason
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')
        if m.get('licenseQuota') is not None:
            temp_model = GetEnvironmentLicenseResponseBodyDataLicenseQuota()
            self.license_quota = temp_model.from_map(m['licenseQuota'])
        if m.get('rejectReason') is not None:
            self.reject_reason = m.get('rejectReason')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetEnvironmentLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        # 错误码
        self.code = code  # type: str
        self.data = data  # type: GetEnvironmentLicenseResponseBodyData
        # 错误信息
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnvironmentLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetEnvironmentLicenseResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetEnvironmentLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnvironmentLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentLicenseResponse, self).to_map()
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
            temp_model = GetEnvironmentLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentNodeResponseBodyDataNetworkCards(TeaModel):
    def __init__(self, ip=None, name=None):
        # ip
        self.ip = ip  # type: str
        # name
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentNodeResponseBodyDataNetworkCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetEnvironmentNodeResponseBodyDataTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # effect
        self.effect = effect  # type: str
        # key
        self.key = key  # type: str
        # value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentNodeResponseBodyDataTaints, self).to_map()
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


class GetEnvironmentNodeResponseBodyData(TeaModel):
    def __init__(self, arch=None, cluster_uid=None, cpu=None, created_at=None, data_disk=None, host_name=None,
                 identifier=None, image_id=None, instance_type=None, internet_bandwidth=None, kernel=None, labels=None,
                 mac_address=None, memory=None, network_cards=None, os=None, os_version=None, private_ip=None, public_ip=None,
                 root_password=None, system_disk=None, system_info=None, taints=None, uid=None):
        # arch
        self.arch = arch  # type: str
        self.cluster_uid = cluster_uid  # type: str
        # cpu
        self.cpu = cpu  # type: str
        self.created_at = created_at  # type: str
        # dataDisk
        self.data_disk = data_disk  # type: list[Disk]
        # hostName
        self.host_name = host_name  # type: str
        # identifier
        self.identifier = identifier  # type: str
        # imageID
        self.image_id = image_id  # type: str
        # instanceType
        self.instance_type = instance_type  # type: str
        # internetBandwidth
        self.internet_bandwidth = internet_bandwidth  # type: int
        # kernel
        self.kernel = kernel  # type: str
        # labels
        self.labels = labels  # type: dict[str, str]
        # macAddress
        self.mac_address = mac_address  # type: str
        # memory
        self.memory = memory  # type: str
        # networkCards
        self.network_cards = network_cards  # type: list[GetEnvironmentNodeResponseBodyDataNetworkCards]
        # os
        self.os = os  # type: str
        # osVersion
        self.os_version = os_version  # type: str
        # privateIP
        self.private_ip = private_ip  # type: str
        # publicIP
        self.public_ip = public_ip  # type: str
        # rootPassword
        self.root_password = root_password  # type: str
        # systemDisk
        self.system_disk = system_disk  # type: list[Disk]
        # systemInfo
        self.system_info = system_info  # type: str
        # taints
        self.taints = taints  # type: list[GetEnvironmentNodeResponseBodyDataTaints]
        self.uid = uid  # type: str

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.network_cards:
            for k in self.network_cards:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEnvironmentNodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arch is not None:
            result['arch'] = self.arch
        if self.cluster_uid is not None:
            result['clusterUID'] = self.cluster_uid
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image_id is not None:
            result['imageID'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth is not None:
            result['internetBandwidth'] = self.internet_bandwidth
        if self.kernel is not None:
            result['kernel'] = self.kernel
        if self.labels is not None:
            result['labels'] = self.labels
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        if self.memory is not None:
            result['memory'] = self.memory
        result['networkCards'] = []
        if self.network_cards is not None:
            for k in self.network_cards:
                result['networkCards'].append(k.to_map() if k else None)
        if self.os is not None:
            result['os'] = self.os
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        if self.system_info is not None:
            result['systemInfo'] = self.system_info
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arch') is not None:
            self.arch = m.get('arch')
        if m.get('clusterUID') is not None:
            self.cluster_uid = m.get('clusterUID')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = Disk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('imageID') is not None:
            self.image_id = m.get('imageID')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidth') is not None:
            self.internet_bandwidth = m.get('internetBandwidth')
        if m.get('kernel') is not None:
            self.kernel = m.get('kernel')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        self.network_cards = []
        if m.get('networkCards') is not None:
            for k in m.get('networkCards'):
                temp_model = GetEnvironmentNodeResponseBodyDataNetworkCards()
                self.network_cards.append(temp_model.from_map(k))
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('publicIP') is not None:
            self.public_ip = m.get('publicIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = Disk()
                self.system_disk.append(temp_model.from_map(k))
        if m.get('systemInfo') is not None:
            self.system_info = m.get('systemInfo')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = GetEnvironmentNodeResponseBodyDataTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetEnvironmentNodeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetEnvironmentNodeResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnvironmentNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetEnvironmentNodeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetEnvironmentNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnvironmentNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentNodeResponse, self).to_map()
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
            temp_model = GetEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationComponentReferenceResponseBodyData(TeaModel):
    def __init__(self, app_version=None, component_description=None, component_name=None,
                 component_reference_uid=None, component_uid=None, component_version_description=None, component_version_uid=None,
                 enable=None, namespace=None, orchestration_values=None, parent_component=None,
                 parent_component_version_relation_uid=None, parent_component_version_uid=None, release_name=None, resources=None, sequence=None,
                 values=None, version=None):
        self.app_version = app_version  # type: str
        self.component_description = component_description  # type: str
        self.component_name = component_name  # type: str
        self.component_reference_uid = component_reference_uid  # type: str
        self.component_uid = component_uid  # type: str
        self.component_version_description = component_version_description  # type: str
        self.component_version_uid = component_version_uid  # type: str
        self.enable = enable  # type: bool
        self.namespace = namespace  # type: str
        self.orchestration_values = orchestration_values  # type: str
        self.parent_component = parent_component  # type: bool
        self.parent_component_version_relation_uid = parent_component_version_relation_uid  # type: str
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        self.release_name = release_name  # type: str
        self.resources = resources  # type: str
        self.sequence = sequence  # type: int
        self.values = values  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFoundationComponentReferenceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_description is not None:
            result['componentDescription'] = self.component_description
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_reference_uid is not None:
            result['componentReferenceUID'] = self.component_reference_uid
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_description is not None:
            result['componentVersionDescription'] = self.component_version_description
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.enable is not None:
            result['enable'] = self.enable
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.parent_component_version_relation_uid is not None:
            result['parentComponentVersionRelationUID'] = self.parent_component_version_relation_uid
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.resources is not None:
            result['resources'] = self.resources
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.values is not None:
            result['values'] = self.values
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentDescription') is not None:
            self.component_description = m.get('componentDescription')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentReferenceUID') is not None:
            self.component_reference_uid = m.get('componentReferenceUID')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionDescription') is not None:
            self.component_version_description = m.get('componentVersionDescription')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('parentComponentVersionRelationUID') is not None:
            self.parent_component_version_relation_uid = m.get('parentComponentVersionRelationUID')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetFoundationComponentReferenceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetFoundationComponentReferenceResponseBodyData]
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFoundationComponentReferenceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetFoundationComponentReferenceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetFoundationComponentReferenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFoundationComponentReferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFoundationComponentReferenceResponse, self).to_map()
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
            temp_model = GetFoundationComponentReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationVersionResponseBodyData(TeaModel):
    def __init__(self, description=None, features=None, labels=None, name=None, platforms=None, status=None,
                 type=None, uid=None, version=None):
        # description
        self.description = description  # type: str
        # 底座功能列表
        self.features = features  # type: list[str]
        self.labels = labels  # type: str
        # name，目前仅能是 “ADP 底座“
        self.name = name  # type: str
        # platforms
        self.platforms = platforms  # type: list[Platform]
        # status，ENUM:["Testing","Published","Deprecated"] Published 后，则全平台所有用户可见，请谨慎操作
        self.status = status  # type: str
        # the type of foundation version,ENUM:["trident","ack"]
        self.type = type  # type: str
        # uid
        self.uid = uid  # type: str
        # version
        self.version = version  # type: str

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFoundationVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.features is not None:
            result['features'] = self.features
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('features') is not None:
            self.features = m.get('features')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetFoundationVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetFoundationVersionResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFoundationVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetFoundationVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetFoundationVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFoundationVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFoundationVersionResponse, self).to_map()
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
            temp_model = GetFoundationVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductResponseBodyData(TeaModel):
    def __init__(self, description=None, name=None, uid=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetProductResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetProductResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductResponse, self).to_map()
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
            temp_model = GetProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductComponentVersionResponseBodyData(TeaModel):
    def __init__(self, app_version=None, component_description=None, component_name=None, component_uid=None,
                 component_version_description=None, component_version_uid=None, enable=None, namespace=None, orchestration_values=None,
                 parent_component=None, parent_component_version_relation_uid=None, parent_component_version_uid=None,
                 product_version_uid=None, relation_uid=None, release_name=None, resources=None, sequence=None, values=None,
                 version=None):
        self.app_version = app_version  # type: str
        self.component_description = component_description  # type: str
        self.component_name = component_name  # type: str
        self.component_uid = component_uid  # type: str
        self.component_version_description = component_version_description  # type: str
        self.component_version_uid = component_version_uid  # type: str
        self.enable = enable  # type: bool
        self.namespace = namespace  # type: str
        self.orchestration_values = orchestration_values  # type: str
        self.parent_component = parent_component  # type: bool
        self.parent_component_version_relation_uid = parent_component_version_relation_uid  # type: str
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.relation_uid = relation_uid  # type: str
        self.release_name = release_name  # type: str
        self.resources = resources  # type: str
        self.sequence = sequence  # type: int
        self.values = values  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductComponentVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_description is not None:
            result['componentDescription'] = self.component_description
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_description is not None:
            result['componentVersionDescription'] = self.component_version_description
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.enable is not None:
            result['enable'] = self.enable
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.parent_component_version_relation_uid is not None:
            result['parentComponentVersionRelationUID'] = self.parent_component_version_relation_uid
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.resources is not None:
            result['resources'] = self.resources
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.values is not None:
            result['values'] = self.values
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentDescription') is not None:
            self.component_description = m.get('componentDescription')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionDescription') is not None:
            self.component_version_description = m.get('componentVersionDescription')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('parentComponentVersionRelationUID') is not None:
            self.parent_component_version_relation_uid = m.get('parentComponentVersionRelationUID')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductComponentVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetProductComponentVersionResponseBodyData]
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProductComponentVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetProductComponentVersionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductComponentVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductComponentVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductComponentVersionResponse, self).to_map()
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
            temp_model = GetProductComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductDeploymentRequest(TeaModel):
    def __init__(self, environment_uid=None, product_version_uid=None, with_param_config=None):
        self.environment_uid = environment_uid  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.with_param_config = with_param_config  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductDeploymentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.with_param_config is not None:
            result['withParamConfig'] = self.with_param_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('withParamConfig') is not None:
            self.with_param_config = m.get('withParamConfig')
        return self


class GetProductDeploymentResponseBodyData(TeaModel):
    def __init__(self, env_params=None, env_uid=None, status=None, uid=None):
        self.env_params = env_params  # type: str
        self.env_uid = env_uid  # type: str
        self.status = status  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductDeploymentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['envParams'] = self.env_params
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envParams') is not None:
            self.env_params = m.get('envParams')
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetProductDeploymentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetProductDeploymentResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductDeploymentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetProductDeploymentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductDeploymentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductDeploymentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductDeploymentResponse, self).to_map()
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
            temp_model = GetProductDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionResponseBodyData(TeaModel):
    def __init__(self, description=None, foundation_version_uid=None, package_url=None, platforms=None,
                 product_name=None, product_uid=None, provider=None, uid=None, version=None):
        self.description = description  # type: str
        self.foundation_version_uid = foundation_version_uid  # type: str
        self.package_url = package_url  # type: str
        self.platforms = platforms  # type: list[Platform]
        self.product_name = product_name  # type: str
        self.product_uid = product_uid  # type: str
        self.provider = provider  # type: str
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProductVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetProductVersionResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetProductVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductVersionResponse, self).to_map()
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
            temp_model = GetProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionDifferencesRequest(TeaModel):
    def __init__(self, pre_version_uid=None):
        # 上一个产品版本id
        self.pre_version_uid = pre_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionDifferencesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_version_uid is not None:
            result['preVersionUID'] = self.pre_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('preVersionUID') is not None:
            self.pre_version_uid = m.get('preVersionUID')
        return self


class GetProductVersionDifferencesResponseBodyData(TeaModel):
    def __init__(self, component_name=None, difference=None, message=None, pre_version=None, release_name=None,
                 upgrade_flag=None, version=None):
        # 组件名称
        self.component_name = component_name  # type: str
        # 变更类型，ENUM 类型
        self.difference = difference  # type: str
        # 变更描述信息
        self.message = message  # type: str
        # 组件之前的版本号
        self.pre_version = pre_version  # type: str
        # 组件实例名称
        self.release_name = release_name  # type: str
        self.upgrade_flag = upgrade_flag  # type: bool
        # 组件当前的版本号
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionDifferencesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.difference is not None:
            result['difference'] = self.difference
        if self.message is not None:
            result['message'] = self.message
        if self.pre_version is not None:
            result['preVersion'] = self.pre_version
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.upgrade_flag is not None:
            result['upgradeFlag'] = self.upgrade_flag
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('difference') is not None:
            self.difference = m.get('difference')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('preVersion') is not None:
            self.pre_version = m.get('preVersion')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('upgradeFlag') is not None:
            self.upgrade_flag = m.get('upgradeFlag')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductVersionDifferencesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetProductVersionDifferencesResponseBodyData]
        self.msg = msg  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProductVersionDifferencesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetProductVersionDifferencesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProductVersionDifferencesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductVersionDifferencesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductVersionDifferencesResponse, self).to_map()
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
            temp_model = GetProductVersionDifferencesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionPackageRequest(TeaModel):
    def __init__(self, old_product_version_uid=None, package_content_type=None, package_type=None,
                 package_uid=None, platform=None, with_url=None):
        self.old_product_version_uid = old_product_version_uid  # type: str
        self.package_content_type = package_content_type  # type: str
        self.package_type = package_type  # type: str
        self.package_uid = package_uid  # type: str
        self.platform = platform  # type: str
        self.with_url = with_url  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.package_uid is not None:
            result['packageUID'] = self.package_uid
        if self.platform is not None:
            result['platform'] = self.platform
        if self.with_url is not None:
            result['withURL'] = self.with_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('packageUID') is not None:
            self.package_uid = m.get('packageUID')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('withURL') is not None:
            self.with_url = m.get('withURL')
        return self


class GetProductVersionPackageResponseBodyData(TeaModel):
    def __init__(self, package_content_type=None, package_size=None, package_status=None, package_type=None,
                 package_uid=None, package_url=None, platform=None):
        self.package_content_type = package_content_type  # type: str
        self.package_size = package_size  # type: str
        self.package_status = package_status  # type: str
        self.package_type = package_type  # type: str
        self.package_uid = package_uid  # type: str
        self.package_url = package_url  # type: str
        self.platform = platform  # type: Platform

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super(GetProductVersionPackageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_size is not None:
            result['packageSize'] = self.package_size
        if self.package_status is not None:
            result['packageStatus'] = self.package_status
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.package_uid is not None:
            result['packageUID'] = self.package_uid
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
        if m.get('packageSize') is not None:
            self.package_size = m.get('packageSize')
        if m.get('packageStatus') is not None:
            self.package_status = m.get('packageStatus')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('packageUID') is not None:
            self.package_uid = m.get('packageUID')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('platform') is not None:
            temp_model = Platform()
            self.platform = temp_model.from_map(m['platform'])
        return self


class GetProductVersionPackageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetProductVersionPackageResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductVersionPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetProductVersionPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductVersionPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductVersionPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductVersionPackageResponse, self).to_map()
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
            temp_model = GetProductVersionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkflowStatusRequest(TeaModel):
    def __init__(self, workflow_type=None, xuid=None):
        # ENUM:["CreateCluster","DeleteCluster","Pack","Deploy","UnbindProductVersion"]
        self.workflow_type = workflow_type  # type: str
        # xuid，根据场景传递env_uid/package_uid/deploy_uid
        self.xuid = xuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkflowStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workflow_type is not None:
            result['workflowType'] = self.workflow_type
        if self.xuid is not None:
            result['xuid'] = self.xuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workflowType') is not None:
            self.workflow_type = m.get('workflowType')
        if m.get('xuid') is not None:
            self.xuid = m.get('xuid')
        return self


class GetWorkflowStatusResponseBodyDataStepStatusWorkflowTasks(TeaModel):
    def __init__(self, name=None, status=None):
        # task name
        self.name = name  # type: str
        # task status
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkflowStatusResponseBodyDataStepStatusWorkflowTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetWorkflowStatusResponseBodyDataStepStatus(TeaModel):
    def __init__(self, name=None, status=None, workflow_tasks=None):
        # step name
        self.name = name  # type: str
        # step status
        self.status = status  # type: str
        self.workflow_tasks = workflow_tasks  # type: list[GetWorkflowStatusResponseBodyDataStepStatusWorkflowTasks]

    def validate(self):
        if self.workflow_tasks:
            for k in self.workflow_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkflowStatusResponseBodyDataStepStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['workflowTasks'] = []
        if self.workflow_tasks is not None:
            for k in self.workflow_tasks:
                result['workflowTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.workflow_tasks = []
        if m.get('workflowTasks') is not None:
            for k in m.get('workflowTasks'):
                temp_model = GetWorkflowStatusResponseBodyDataStepStatusWorkflowTasks()
                self.workflow_tasks.append(temp_model.from_map(k))
        return self


class GetWorkflowStatusResponseBodyData(TeaModel):
    def __init__(self, status=None, step_status=None):
        self.status = status  # type: str
        self.step_status = step_status  # type: list[GetWorkflowStatusResponseBodyDataStepStatus]

    def validate(self):
        if self.step_status:
            for k in self.step_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkflowStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        result['stepStatus'] = []
        if self.step_status is not None:
            for k in self.step_status:
                result['stepStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        self.step_status = []
        if m.get('stepStatus') is not None:
            for k in m.get('stepStatus'):
                temp_model = GetWorkflowStatusResponseBodyDataStepStatus()
                self.step_status.append(temp_model.from_map(k))
        return self


class GetWorkflowStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: GetWorkflowStatusResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWorkflowStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetWorkflowStatusResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetWorkflowStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWorkflowStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkflowStatusResponse, self).to_map()
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
            temp_model = GetWorkflowStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitEnvironmentResourceRequest(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitEnvironmentResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyID'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyID') is not None:
            self.access_key_id = m.get('accessKeyID')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        return self


class InitEnvironmentResourceResponseBodyData(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitEnvironmentResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class InitEnvironmentResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: InitEnvironmentResourceResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InitEnvironmentResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = InitEnvironmentResourceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class InitEnvironmentResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitEnvironmentResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitEnvironmentResourceResponse, self).to_map()
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
            temp_model = InitEnvironmentResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentVersionsRequestPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentVersionsRequestPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListComponentVersionsRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, platforms=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.platforms = platforms  # type: list[ListComponentVersionsRequestPlatforms]

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListComponentVersionsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class ListComponentVersionsShrinkRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, platforms_shrink=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.platforms_shrink = platforms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentVersionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        return self


class ListComponentVersionsResponseBodyDataList(TeaModel):
    def __init__(self, app_version=None, component_name=None, component_uid=None, description=None, documents=None,
                 images_mapping=None, orchestration_values=None, package_url=None, parent_component=None, readme=None,
                 resources=None, uid=None, version=None):
        self.app_version = app_version  # type: str
        self.component_name = component_name  # type: str
        self.component_uid = component_uid  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: str
        self.images_mapping = images_mapping  # type: str
        self.orchestration_values = orchestration_values  # type: str
        self.package_url = package_url  # type: str
        self.parent_component = parent_component  # type: bool
        self.readme = readme  # type: str
        self.resources = resources  # type: str
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentVersionsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListComponentVersionsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListComponentVersionsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListComponentVersionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListComponentVersionsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None, msg=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: ListComponentVersionsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListComponentVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListComponentVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListComponentVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListComponentVersionsResponse, self).to_map()
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
            temp_model = ListComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentsRequest(TeaModel):
    def __init__(self, category=None, fuzzy=None, name=None, page_num=None, page_size=None, public=None):
        self.category = category  # type: str
        self.fuzzy = fuzzy  # type: str
        self.name = name  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.public = public  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class ListComponentsResponseBodyDataListAnnotations(TeaModel):
    def __init__(self, annotations=None):
        self.annotations = annotations  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsResponseBodyDataListAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        return self


class ListComponentsResponseBodyDataList(TeaModel):
    def __init__(self, annotations=None, category=None, description=None, documents=None, name=None, provider=None,
                 public=None, singleton=None, source=None, uid=None):
        self.annotations = annotations  # type: ListComponentsResponseBodyDataListAnnotations
        self.category = category  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: str
        self.name = name  # type: str
        self.provider = provider  # type: str
        self.public = public  # type: bool
        self.singleton = singleton  # type: bool
        self.source = source  # type: str
        self.uid = uid  # type: str

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = ListComponentsResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListComponentsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListComponentsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListComponentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListComponentsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListComponentsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListComponentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListComponentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListComponentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListComponentsResponse, self).to_map()
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
            temp_model = ListComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentLicensesRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, type=None):
        # 页码
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentLicensesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListEnvironmentLicensesResponseBodyDataListLicenseQuotaClusterQuota(TeaModel):
    def __init__(self, cpu_core_limit=None):
        # cpu核数限制
        self.cpu_core_limit = cpu_core_limit  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentLicensesResponseBodyDataListLicenseQuotaClusterQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_limit is not None:
            result['cpuCoreLimit'] = self.cpu_core_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpuCoreLimit') is not None:
            self.cpu_core_limit = m.get('cpuCoreLimit')
        return self


class ListEnvironmentLicensesResponseBodyDataListLicenseQuotaComponentQuotas(TeaModel):
    def __init__(self, component_name=None, component_source=None, instance_limit=None):
        # 组件名
        self.component_name = component_name  # type: str
        # 组件来源
        self.component_source = component_source  # type: str
        # 实例数限制
        self.instance_limit = instance_limit  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentLicensesResponseBodyDataListLicenseQuotaComponentQuotas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_source is not None:
            result['componentSource'] = self.component_source
        if self.instance_limit is not None:
            result['instanceLimit'] = self.instance_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentSource') is not None:
            self.component_source = m.get('componentSource')
        if m.get('instanceLimit') is not None:
            self.instance_limit = m.get('instanceLimit')
        return self


class ListEnvironmentLicensesResponseBodyDataListLicenseQuota(TeaModel):
    def __init__(self, cluster_quota=None, component_quotas=None):
        # 集群配额
        self.cluster_quota = cluster_quota  # type: ListEnvironmentLicensesResponseBodyDataListLicenseQuotaClusterQuota
        # 组件配额
        self.component_quotas = component_quotas  # type: list[ListEnvironmentLicensesResponseBodyDataListLicenseQuotaComponentQuotas]

    def validate(self):
        if self.cluster_quota:
            self.cluster_quota.validate()
        if self.component_quotas:
            for k in self.component_quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentLicensesResponseBodyDataListLicenseQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_quota is not None:
            result['clusterQuota'] = self.cluster_quota.to_map()
        result['componentQuotas'] = []
        if self.component_quotas is not None:
            for k in self.component_quotas:
                result['componentQuotas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterQuota') is not None:
            temp_model = ListEnvironmentLicensesResponseBodyDataListLicenseQuotaClusterQuota()
            self.cluster_quota = temp_model.from_map(m['clusterQuota'])
        self.component_quotas = []
        if m.get('componentQuotas') is not None:
            for k in m.get('componentQuotas'):
                temp_model = ListEnvironmentLicensesResponseBodyDataListLicenseQuotaComponentQuotas()
                self.component_quotas.append(temp_model.from_map(k))
        return self


class ListEnvironmentLicensesResponseBodyDataList(TeaModel):
    def __init__(self, expire_time=None, license_key=None, license_quota=None, reject_reason=None, status=None,
                 type=None, uid=None):
        # 过期时间
        self.expire_time = expire_time  # type: str
        # license内容
        self.license_key = license_key  # type: str
        # license配额
        self.license_quota = license_quota  # type: ListEnvironmentLicensesResponseBodyDataListLicenseQuota
        # 拒绝原因
        self.reject_reason = reject_reason  # type: str
        # 状态
        self.status = status  # type: str
        # 类型
        self.type = type  # type: str
        # license uid
        self.uid = uid  # type: str

    def validate(self):
        if self.license_quota:
            self.license_quota.validate()

    def to_map(self):
        _map = super(ListEnvironmentLicensesResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        if self.license_quota is not None:
            result['licenseQuota'] = self.license_quota.to_map()
        if self.reject_reason is not None:
            result['rejectReason'] = self.reject_reason
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')
        if m.get('licenseQuota') is not None:
            temp_model = ListEnvironmentLicensesResponseBodyDataListLicenseQuota()
            self.license_quota = temp_model.from_map(m['licenseQuota'])
        if m.get('rejectReason') is not None:
            self.reject_reason = m.get('rejectReason')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnvironmentLicensesResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        # license列表
        self.list = list  # type: list[ListEnvironmentLicensesResponseBodyDataList]
        # 页码
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总数
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentLicensesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentLicensesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentLicensesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        # 错误码
        self.code = code  # type: str
        # 业务数据
        self.data = data  # type: ListEnvironmentLicensesResponseBodyData
        # 错误信息
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentLicensesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListEnvironmentLicensesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListEnvironmentLicensesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentLicensesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentLicensesResponse, self).to_map()
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
            temp_model = ListEnvironmentLicensesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentNodesRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentNodesResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[GetInstanceInfoResponse]
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentNodesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetInstanceInfoResponse()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentNodesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListEnvironmentNodesResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListEnvironmentNodesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListEnvironmentNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentNodesResponse, self).to_map()
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
            temp_model = ListEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentTunnelsResponseBodyDataListTunnelConfig(TeaModel):
    def __init__(self, hostname=None, password=None, region_id=None, ssh_port=None, username=None, vpc_id=None):
        # 跳板机hostname
        self.hostname = hostname  # type: str
        # 跳板机密码
        self.password = password  # type: str
        # 直连regionId
        self.region_id = region_id  # type: str
        # 跳板机ssh端口号
        self.ssh_port = ssh_port  # type: int
        # 跳板机用户名
        self.username = username  # type: str
        # 直连vpcId
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentTunnelsResponseBodyDataListTunnelConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.ssh_port is not None:
            result['sshPort'] = self.ssh_port
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sshPort') is not None:
            self.ssh_port = m.get('sshPort')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListEnvironmentTunnelsResponseBodyDataList(TeaModel):
    def __init__(self, tunnel_config=None, tunnel_type=None):
        self.tunnel_config = tunnel_config  # type: ListEnvironmentTunnelsResponseBodyDataListTunnelConfig
        # 通道类型
        self.tunnel_type = tunnel_type  # type: str

    def validate(self):
        if self.tunnel_config:
            self.tunnel_config.validate()

    def to_map(self):
        _map = super(ListEnvironmentTunnelsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tunnel_config is not None:
            result['tunnelConfig'] = self.tunnel_config.to_map()
        if self.tunnel_type is not None:
            result['tunnelType'] = self.tunnel_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tunnelConfig') is not None:
            temp_model = ListEnvironmentTunnelsResponseBodyDataListTunnelConfig()
            self.tunnel_config = temp_model.from_map(m['tunnelConfig'])
        if m.get('tunnelType') is not None:
            self.tunnel_type = m.get('tunnelType')
        return self


class ListEnvironmentTunnelsResponseBodyData(TeaModel):
    def __init__(self, list=None):
        self.list = list  # type: list[ListEnvironmentTunnelsResponseBodyDataList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentTunnelsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentTunnelsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListEnvironmentTunnelsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        # 错误码
        self.code = code  # type: str
        self.data = data  # type: ListEnvironmentTunnelsResponseBodyData
        # 错误信息
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentTunnelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListEnvironmentTunnelsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListEnvironmentTunnelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentTunnelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentTunnelsResponse, self).to_map()
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
            temp_model = ListEnvironmentTunnelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(self, cluster_uid=None, foundation_type=None, fuzzy=None, instance_status=None, name=None,
                 page_num=None, page_size=None, type=None, vendor_type=None):
        self.cluster_uid = cluster_uid  # type: str
        self.foundation_type = foundation_type  # type: str
        self.fuzzy = fuzzy  # type: str
        self.instance_status = instance_status  # type: str
        self.name = name  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.type = type  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_uid is not None:
            result['clusterUID'] = self.cluster_uid
        if self.foundation_type is not None:
            result['foundationType'] = self.foundation_type
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterUID') is not None:
            self.cluster_uid = m.get('clusterUID')
        if m.get('foundationType') is not None:
            self.foundation_type = m.get('foundationType')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsResponseBodyDataListPlatform(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentsResponseBodyDataListPlatform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListEnvironmentsResponseBodyDataList(TeaModel):
    def __init__(self, created_at=None, description=None, id=None, location=None, name=None, platform=None,
                 product_name=None, product_version=None, product_version_uid=None, uid=None, vendor_type=None):
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: int
        self.location = location  # type: str
        self.name = name  # type: str
        self.platform = platform  # type: ListEnvironmentsResponseBodyDataListPlatform
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.uid = uid  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = ListEnvironmentsResponseBodyDataListPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListEnvironmentsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListEnvironmentsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponse, self).to_map()
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
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationComponentVersionsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ComponentVersion]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFoundationComponentVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ComponentVersion()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListFoundationComponentVersionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListFoundationComponentVersionsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListFoundationComponentVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListFoundationComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListFoundationComponentVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFoundationComponentVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFoundationComponentVersionsResponse, self).to_map()
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
            temp_model = ListFoundationComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationReferenceComponentsRequest(TeaModel):
    def __init__(self, foundation_version_uid=None, only_enabled=None, product_version_uid=None):
        # foundation version uid
        self.foundation_version_uid = foundation_version_uid  # type: str
        self.only_enabled = only_enabled  # type: bool
        # 产品版本uid
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFoundationReferenceComponentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.only_enabled is not None:
            result['onlyEnabled'] = self.only_enabled
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('onlyEnabled') is not None:
            self.only_enabled = m.get('onlyEnabled')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListFoundationReferenceComponentsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: list[ProductComponentRelationDetail]
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFoundationReferenceComponentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ProductComponentRelationDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListFoundationReferenceComponentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFoundationReferenceComponentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFoundationReferenceComponentsResponse, self).to_map()
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
            temp_model = ListFoundationReferenceComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationVersionsResponseBodyData(TeaModel):
    def __init__(self, list=None):
        self.list = list  # type: list[FoundationVersion]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFoundationVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = FoundationVersion()
                self.list.append(temp_model.from_map(k))
        return self


class ListFoundationVersionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListFoundationVersionsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListFoundationVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListFoundationVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListFoundationVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFoundationVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFoundationVersionsResponse, self).to_map()
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
            temp_model = ListFoundationVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductComponentVersionsRequest(TeaModel):
    def __init__(self, category=None, page_num=None, page_size=None, sort_direct=None, sort_key=None):
        # 组件类型，不填写则为全部
        self.category = category  # type: str
        self.page_num = page_num  # type: str
        self.page_size = page_size  # type: str
        self.sort_direct = sort_direct  # type: str
        self.sort_key = sort_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductComponentVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort_direct is not None:
            result['sortDirect'] = self.sort_direct
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sortDirect') is not None:
            self.sort_direct = m.get('sortDirect')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        return self


class ListProductComponentVersionsResponseBodyData(TeaModel):
    def __init__(self, list=None):
        self.list = list  # type: list[ProductComponentRelationDetail]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductComponentVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ProductComponentRelationDetail()
                self.list.append(temp_model.from_map(k))
        return self


class ListProductComponentVersionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListProductComponentVersionsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProductComponentVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductComponentVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductComponentVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductComponentVersionsResponse, self).to_map()
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
            temp_model = ListProductComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductDeploymentsRequest(TeaModel):
    def __init__(self, environment_uid=None, page_num=None, page_size=None, product_version_uid=None):
        self.environment_uid = environment_uid  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductDeploymentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductDeploymentsResponseBodyDataList(TeaModel):
    def __init__(self, env_params=None, env_uid=None, old_product_version=None, package_content_type=None,
                 package_info_uid=None, package_type=None, product_name=None, product_version=None, status=None, uid=None):
        self.env_params = env_params  # type: str
        self.env_uid = env_uid  # type: str
        self.old_product_version = old_product_version  # type: str
        self.package_content_type = package_content_type  # type: str
        self.package_info_uid = package_info_uid  # type: str
        self.package_type = package_type  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.status = status  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductDeploymentsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['envParams'] = self.env_params
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.old_product_version is not None:
            result['oldProductVersion'] = self.old_product_version
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_info_uid is not None:
            result['packageInfoUID'] = self.package_info_uid
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envParams') is not None:
            self.env_params = m.get('envParams')
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('oldProductVersion') is not None:
            self.old_product_version = m.get('oldProductVersion')
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
        if m.get('packageInfoUID') is not None:
            self.package_info_uid = m.get('packageInfoUID')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListProductDeploymentsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListProductDeploymentsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductDeploymentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductDeploymentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductDeploymentsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListProductDeploymentsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProductDeploymentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductDeploymentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductDeploymentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductDeploymentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductDeploymentsResponse, self).to_map()
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
            temp_model = ListProductDeploymentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductEnvironmentsRequestPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductEnvironmentsRequestPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListProductEnvironmentsRequest(TeaModel):
    def __init__(self, compatible_product_version_uid=None, env_type=None, platforms=None,
                 product_version_uid=None):
        # 兼容版本产品版本id
        self.compatible_product_version_uid = compatible_product_version_uid  # type: str
        self.env_type = env_type  # type: str
        self.platforms = platforms  # type: list[ListProductEnvironmentsRequestPlatforms]
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductEnvironmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_product_version_uid is not None:
            result['compatibleProductVersionUID'] = self.compatible_product_version_uid
        if self.env_type is not None:
            result['envType'] = self.env_type
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('compatibleProductVersionUID') is not None:
            self.compatible_product_version_uid = m.get('compatibleProductVersionUID')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListProductEnvironmentsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductEnvironmentsShrinkRequest(TeaModel):
    def __init__(self, compatible_product_version_uid=None, env_type=None, platforms_shrink=None,
                 product_version_uid=None):
        # 兼容版本产品版本id
        self.compatible_product_version_uid = compatible_product_version_uid  # type: str
        self.env_type = env_type  # type: str
        self.platforms_shrink = platforms_shrink  # type: str
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductEnvironmentsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_product_version_uid is not None:
            result['compatibleProductVersionUID'] = self.compatible_product_version_uid
        if self.env_type is not None:
            result['envType'] = self.env_type
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('compatibleProductVersionUID') is not None:
            self.compatible_product_version_uid = m.get('compatibleProductVersionUID')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductEnvironmentsResponseBodyData(TeaModel):
    def __init__(self, env_name=None, env_type=None, env_uid=None, instance_status=None, old_product_version=None,
                 old_product_version_uid=None, platform_status=None, product_name=None, product_uid=None, product_version=None,
                 product_version_uid=None, provider=None, uid=None, vendor_config=None, vendor_type=None):
        self.env_name = env_name  # type: str
        self.env_type = env_type  # type: str
        self.env_uid = env_uid  # type: str
        self.instance_status = instance_status  # type: str
        self.old_product_version = old_product_version  # type: str
        self.old_product_version_uid = old_product_version_uid  # type: str
        self.platform_status = platform_status  # type: str
        self.product_name = product_name  # type: str
        self.product_uid = product_uid  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.provider = provider  # type: str
        self.uid = uid  # type: str
        self.vendor_config = vendor_config  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductEnvironmentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.env_type is not None:
            result['envType'] = self.env_type
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.old_product_version is not None:
            result['oldProductVersion'] = self.old_product_version
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.platform_status is not None:
            result['platformStatus'] = self.platform_status
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('oldProductVersion') is not None:
            self.old_product_version = m.get('oldProductVersion')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('platformStatus') is not None:
            self.platform_status = m.get('platformStatus')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListProductEnvironmentsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListProductEnvironmentsResponseBodyData]
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductEnvironmentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProductEnvironmentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductEnvironmentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductEnvironmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductEnvironmentsResponse, self).to_map()
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
            temp_model = ListProductEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductInstanceConfigsRequest(TeaModel):
    def __init__(self, environment_uid=None, page_num=None, page_size=None, param_type=None,
                 product_version_uid=None):
        self.environment_uid = environment_uid  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        # 组件和全局类型字段
        self.param_type = param_type  # type: str
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductInstanceConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.param_type is not None:
            result['paramType'] = self.param_type
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('paramType') is not None:
            self.param_type = m.get('paramType')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductInstanceConfigsResponseBodyDataList(TeaModel):
    def __init__(self, component_name=None, component_release_name=None, component_uid=None,
                 component_version_uid=None, created_at=None, description=None, env_uid=None, name=None, parent_component_name=None,
                 parent_component_release_name=None, parent_component_version_uid=None, product_name=None, product_version=None,
                 product_version_uid=None, uid=None, value=None, value_type=None, vendor_type=None):
        self.component_name = component_name  # type: str
        self.component_release_name = component_release_name  # type: str
        self.component_uid = component_uid  # type: str
        self.component_version_uid = component_version_uid  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.env_uid = env_uid  # type: str
        self.name = name  # type: str
        self.parent_component_name = parent_component_name  # type: str
        self.parent_component_release_name = parent_component_release_name  # type: str
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.uid = uid  # type: str
        self.value = value  # type: str
        self.value_type = value_type  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductInstanceConfigsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_release_name is not None:
            result['componentReleaseName'] = self.component_release_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_name is not None:
            result['parentComponentName'] = self.parent_component_name
        if self.parent_component_release_name is not None:
            result['parentComponentReleaseName'] = self.parent_component_release_name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentReleaseName') is not None:
            self.component_release_name = m.get('componentReleaseName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentName') is not None:
            self.parent_component_name = m.get('parentComponentName')
        if m.get('parentComponentReleaseName') is not None:
            self.parent_component_release_name = m.get('parentComponentReleaseName')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListProductInstanceConfigsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListProductInstanceConfigsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductInstanceConfigsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductInstanceConfigsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductInstanceConfigsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListProductInstanceConfigsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProductInstanceConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductInstanceConfigsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductInstanceConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductInstanceConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductInstanceConfigsResponse, self).to_map()
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
            temp_model = ListProductInstanceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductInstancesRequest(TeaModel):
    def __init__(self, env_uid=None, page_num=None, page_size=None, product_version_uid=None):
        self.env_uid = env_uid  # type: str
        self.page_num = page_num  # type: str
        self.page_size = page_size  # type: str
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductInstancesResponseBodyDataList(TeaModel):
    def __init__(self, product_name=None, product_version=None, product_version_uid=None, status=None, uid=None):
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.status = status  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductInstancesResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListProductInstancesResponseBodyData(TeaModel):
    def __init__(self, list=None):
        self.list = list  # type: list[ListProductInstancesResponseBodyDataList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListProductInstancesResponseBody(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: ListProductInstancesResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProductInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProductInstancesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class ListProductInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductInstancesResponse, self).to_map()
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
            temp_model = ListProductInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionConfigsRequest(TeaModel):
    def __init__(self, config_type=None, page_num=None, page_size=None):
        self.config_type = config_type  # type: str
        self.page_num = page_num  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListProductVersionConfigsResponseBodyDataList(TeaModel):
    def __init__(self, component_name=None, component_release_name=None, component_version_uid=None,
                 description=None, name=None, parent_component_name=None, parent_component_release_name=None,
                 parent_component_version_uid=None, product_version_uid=None, uid=None, value=None):
        self.component_name = component_name  # type: str
        self.component_release_name = component_release_name  # type: str
        self.component_version_uid = component_version_uid  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.parent_component_name = parent_component_name  # type: str
        self.parent_component_release_name = parent_component_release_name  # type: str
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.uid = uid  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionConfigsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_release_name is not None:
            result['componentReleaseName'] = self.component_release_name
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_name is not None:
            result['parentComponentName'] = self.parent_component_name
        if self.parent_component_release_name is not None:
            result['parentComponentReleaseName'] = self.parent_component_release_name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentReleaseName') is not None:
            self.component_release_name = m.get('componentReleaseName')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentName') is not None:
            self.parent_component_name = m.get('parentComponentName')
        if m.get('parentComponentReleaseName') is not None:
            self.parent_component_release_name = m.get('parentComponentReleaseName')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListProductVersionConfigsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListProductVersionConfigsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductVersionConfigsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductVersionConfigsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductVersionConfigsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListProductVersionConfigsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProductVersionConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductVersionConfigsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductVersionConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductVersionConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductVersionConfigsResponse, self).to_map()
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
            temp_model = ListProductVersionConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionsRequestPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionsRequestPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListProductVersionsRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, platforms=None, product_name=None, product_uid=None,
                 released=None, supported_foundation_types=None, version=None):
        self.page_num = page_num  # type: str
        self.page_size = page_size  # type: str
        # 支持的platform，为空则不过滤
        self.platforms = platforms  # type: list[ListProductVersionsRequestPlatforms]
        # 过滤参数，产品名称
        self.product_name = product_name  # type: str
        # 过滤参数，产品uid
        self.product_uid = product_uid  # type: str
        # 过滤参数，是否已发布
        self.released = released  # type: bool
        # 过滤参数，支持的环境类型
        self.supported_foundation_types = supported_foundation_types  # type: list[str]
        # 过滤参数，产品版本号
        self.version = version  # type: str

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.released is not None:
            result['released'] = self.released
        if self.supported_foundation_types is not None:
            result['supportedFoundationTypes'] = self.supported_foundation_types
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListProductVersionsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('released') is not None:
            self.released = m.get('released')
        if m.get('supportedFoundationTypes') is not None:
            self.supported_foundation_types = m.get('supportedFoundationTypes')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListProductVersionsShrinkRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, platforms_shrink=None, product_name=None, product_uid=None,
                 released=None, supported_foundation_types_shrink=None, version=None):
        self.page_num = page_num  # type: str
        self.page_size = page_size  # type: str
        # 支持的platform，为空则不过滤
        self.platforms_shrink = platforms_shrink  # type: str
        # 过滤参数，产品名称
        self.product_name = product_name  # type: str
        # 过滤参数，产品uid
        self.product_uid = product_uid  # type: str
        # 过滤参数，是否已发布
        self.released = released  # type: bool
        # 过滤参数，支持的环境类型
        self.supported_foundation_types_shrink = supported_foundation_types_shrink  # type: str
        # 过滤参数，产品版本号
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.released is not None:
            result['released'] = self.released
        if self.supported_foundation_types_shrink is not None:
            result['supportedFoundationTypes'] = self.supported_foundation_types_shrink
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('released') is not None:
            self.released = m.get('released')
        if m.get('supportedFoundationTypes') is not None:
            self.supported_foundation_types_shrink = m.get('supportedFoundationTypes')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListProductVersionsResponseBodyDataListAnnotations(TeaModel):
    def __init__(self, additional_prop_1=None, additional_prop_2=None, additional_prop_3=None):
        self.additional_prop_1 = additional_prop_1  # type: str
        self.additional_prop_2 = additional_prop_2  # type: str
        self.additional_prop_3 = additional_prop_3  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionsResponseBodyDataListAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class ListProductVersionsResponseBodyDataList(TeaModel):
    def __init__(self, annotations=None, description=None, package_url=None, product_name=None, product_uid=None,
                 provider=None, uid=None, version=None):
        self.annotations = annotations  # type: ListProductVersionsResponseBodyDataListAnnotations
        self.description = description  # type: str
        self.package_url = package_url  # type: str
        self.product_name = product_name  # type: str
        self.product_uid = product_uid  # type: str
        self.provider = provider  # type: str
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = ListProductVersionsResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListProductVersionsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListProductVersionsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductVersionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductVersionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListProductVersionsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponse, self).to_map()
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
            temp_model = ListProductVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(self, fuzzy=None, name=None, page_num=None, page_size=None):
        self.fuzzy = fuzzy  # type: str
        self.name = name  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListProductsResponseBodyDataList(TeaModel):
    def __init__(self, description=None, name=None, uid=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListProductsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListProductsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListProductsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProductsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductsResponse, self).to_map()
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkflowTaskLogsRequest(TeaModel):
    def __init__(self, filter_values=None, order_type=None, page_num=None, page_size=None, workflow_type=None,
                 xuid=None):
        self.filter_values = filter_values  # type: list[str]
        # log 的顺序，positive 代表最新的数据在最后，reverse 代表最新的数据在最前
        self.order_type = order_type  # type: str
        self.page_num = page_num  # type: long
        # 每一页的行数，最大值 100
        self.page_size = page_size  # type: long
        # ENUM:["CreateCluster","DeleteCluster","Pack","Deploy"]
        self.workflow_type = workflow_type  # type: str
        self.xuid = xuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowTaskLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_values is not None:
            result['filterValues'] = self.filter_values
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.workflow_type is not None:
            result['workflowType'] = self.workflow_type
        if self.xuid is not None:
            result['xuid'] = self.xuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filterValues') is not None:
            self.filter_values = m.get('filterValues')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('workflowType') is not None:
            self.workflow_type = m.get('workflowType')
        if m.get('xuid') is not None:
            self.xuid = m.get('xuid')
        return self


class ListWorkflowTaskLogsShrinkRequest(TeaModel):
    def __init__(self, filter_values_shrink=None, order_type=None, page_num=None, page_size=None,
                 workflow_type=None, xuid=None):
        self.filter_values_shrink = filter_values_shrink  # type: str
        # log 的顺序，positive 代表最新的数据在最后，reverse 代表最新的数据在最前
        self.order_type = order_type  # type: str
        self.page_num = page_num  # type: long
        # 每一页的行数，最大值 100
        self.page_size = page_size  # type: long
        # ENUM:["CreateCluster","DeleteCluster","Pack","Deploy"]
        self.workflow_type = workflow_type  # type: str
        self.xuid = xuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowTaskLogsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_values_shrink is not None:
            result['filterValues'] = self.filter_values_shrink
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.workflow_type is not None:
            result['workflowType'] = self.workflow_type
        if self.xuid is not None:
            result['xuid'] = self.xuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filterValues') is not None:
            self.filter_values_shrink = m.get('filterValues')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('workflowType') is not None:
            self.workflow_type = m.get('workflowType')
        if m.get('xuid') is not None:
            self.xuid = m.get('xuid')
        return self


class ListWorkflowTaskLogsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        # 日志数据
        self.list = list  # type: list[str]
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowTaskLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['list'] = self.list
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('list') is not None:
            self.list = m.get('list')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListWorkflowTaskLogsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: ListWorkflowTaskLogsResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListWorkflowTaskLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListWorkflowTaskLogsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListWorkflowTaskLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListWorkflowTaskLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkflowTaskLogsResponse, self).to_map()
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
            temp_model = ListWorkflowTaskLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnvironmentTunnelRequestTunnelConfig(TeaModel):
    def __init__(self, hostname=None, password=None, region_id=None, ssh_port=None, username=None, vpc_id=None):
        # 跳板机hostname
        self.hostname = hostname  # type: str
        # 跳板机密码
        self.password = password  # type: str
        # 直连地域id
        self.region_id = region_id  # type: str
        # 跳板机ssh端口号
        self.ssh_port = ssh_port  # type: int
        # 跳板机用户名
        self.username = username  # type: str
        # 直连vpcId
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutEnvironmentTunnelRequestTunnelConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.ssh_port is not None:
            result['sshPort'] = self.ssh_port
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sshPort') is not None:
            self.ssh_port = m.get('sshPort')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class PutEnvironmentTunnelRequest(TeaModel):
    def __init__(self, tunnel_config=None, tunnel_type=None):
        # 通道配置
        self.tunnel_config = tunnel_config  # type: PutEnvironmentTunnelRequestTunnelConfig
        # 通道类型
        self.tunnel_type = tunnel_type  # type: str

    def validate(self):
        if self.tunnel_config:
            self.tunnel_config.validate()

    def to_map(self):
        _map = super(PutEnvironmentTunnelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tunnel_config is not None:
            result['tunnelConfig'] = self.tunnel_config.to_map()
        if self.tunnel_type is not None:
            result['tunnelType'] = self.tunnel_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tunnelConfig') is not None:
            temp_model = PutEnvironmentTunnelRequestTunnelConfig()
            self.tunnel_config = temp_model.from_map(m['tunnelConfig'])
        if m.get('tunnelType') is not None:
            self.tunnel_type = m.get('tunnelType')
        return self


class PutEnvironmentTunnelResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        # 通道id，可空
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutEnvironmentTunnelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PutEnvironmentTunnelResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        # 错误码
        self.code = code  # type: str
        # 数据
        self.data = data  # type: PutEnvironmentTunnelResponseBodyData
        # 错误信息
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PutEnvironmentTunnelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = PutEnvironmentTunnelResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class PutEnvironmentTunnelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PutEnvironmentTunnelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutEnvironmentTunnelResponse, self).to_map()
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
            temp_model = PutEnvironmentTunnelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutProductInstanceConfigRequest(TeaModel):
    def __init__(self, component_uid=None, component_version_uid=None, config_uid=None, description=None,
                 environment_uid=None, name=None, parent_component_name=None, parent_component_version_uid=None,
                 product_version_uid=None, release_name=None, scope=None, value=None, value_type=None):
        self.component_uid = component_uid  # type: str
        self.component_version_uid = component_version_uid  # type: str
        self.config_uid = config_uid  # type: str
        self.description = description  # type: str
        self.environment_uid = environment_uid  # type: str
        self.name = name  # type: str
        self.parent_component_name = parent_component_name  # type: str
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.release_name = release_name  # type: str
        self.scope = scope  # type: list[str]
        self.value = value  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutProductInstanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.config_uid is not None:
            result['configUID'] = self.config_uid
        if self.description is not None:
            result['description'] = self.description
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_name is not None:
            result['parentComponentName'] = self.parent_component_name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('configUID') is not None:
            self.config_uid = m.get('configUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentName') is not None:
            self.parent_component_name = m.get('parentComponentName')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class PutProductInstanceConfigResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutProductInstanceConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PutProductInstanceConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: PutProductInstanceConfigResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PutProductInstanceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = PutProductInstanceConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class PutProductInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PutProductInstanceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutProductInstanceConfigResponse, self).to_map()
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
            temp_model = PutProductInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEnvironmentFoundationReferenceResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEnvironmentFoundationReferenceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SetEnvironmentFoundationReferenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetEnvironmentFoundationReferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetEnvironmentFoundationReferenceResponse, self).to_map()
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
            temp_model = SetEnvironmentFoundationReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentRequest(TeaModel):
    def __init__(self, description=None, location=None, vendor_config=None):
        self.description = description  # type: str
        self.location = location  # type: str
        self.vendor_config = vendor_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class UpdateEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentResponse, self).to_map()
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
            temp_model = UpdateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentNodeRequestTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        self.effect = effect  # type: str
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentNodeRequestTaints, self).to_map()
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


class UpdateEnvironmentNodeRequest(TeaModel):
    def __init__(self, application_disk=None, etcd_disk=None, labels=None, root_password=None, taints=None,
                 trident_system_disk=None, trident_system_size_disk=None):
        # 保留业务分区
        self.application_disk = application_disk  # type: str
        # etcd数据盘
        self.etcd_disk = etcd_disk  # type: str
        self.labels = labels  # type: dict[str, any]
        self.root_password = root_password  # type: str
        self.taints = taints  # type: list[UpdateEnvironmentNodeRequestTaints]
        # k8s管控数据盘
        self.trident_system_disk = trident_system_disk  # type: str
        # k8s管控数据盘大小
        self.trident_system_size_disk = trident_system_size_disk  # type: int

    def validate(self):
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_disk is not None:
            result['applicationDisk'] = self.application_disk
        if self.etcd_disk is not None:
            result['etcdDisk'] = self.etcd_disk
        if self.labels is not None:
            result['labels'] = self.labels
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.trident_system_disk is not None:
            result['tridentSystemDisk'] = self.trident_system_disk
        if self.trident_system_size_disk is not None:
            result['tridentSystemSizeDisk'] = self.trident_system_size_disk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applicationDisk') is not None:
            self.application_disk = m.get('applicationDisk')
        if m.get('etcdDisk') is not None:
            self.etcd_disk = m.get('etcdDisk')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = UpdateEnvironmentNodeRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('tridentSystemDisk') is not None:
            self.trident_system_disk = m.get('tridentSystemDisk')
        if m.get('tridentSystemSizeDisk') is not None:
            self.trident_system_size_disk = m.get('tridentSystemSizeDisk')
        return self


class UpdateEnvironmentNodeResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateEnvironmentNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEnvironmentNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentNodeResponse, self).to_map()
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
            temp_model = UpdateEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentProductVersionRequest(TeaModel):
    def __init__(self, old_product_version_uid=None, product_version_uid=None):
        self.old_product_version_uid = old_product_version_uid  # type: str
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class UpdateEnvironmentProductVersionResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateEnvironmentProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEnvironmentProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentProductVersionResponse, self).to_map()
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
            temp_model = UpdateEnvironmentProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFoundationComponentReferenceRequest(TeaModel):
    def __init__(self, component_orchestration_values=None, enable=None):
        self.component_orchestration_values = component_orchestration_values  # type: str
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFoundationComponentReferenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class UpdateFoundationComponentReferenceResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFoundationComponentReferenceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateFoundationComponentReferenceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFoundationComponentReferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFoundationComponentReferenceResponse, self).to_map()
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
            temp_model = UpdateFoundationComponentReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductRequest(TeaModel):
    def __init__(self, description=None):
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateProductResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductResponse, self).to_map()
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
            temp_model = UpdateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductComponentVersionRequest(TeaModel):
    def __init__(self, component_orchestration_values=None, enable=None, new_component_version_uid=None,
                 release_name=None):
        self.component_orchestration_values = component_orchestration_values  # type: str
        self.enable = enable  # type: bool
        # 如果该参数不为空，则代表更新组件版本
        self.new_component_version_uid = new_component_version_uid  # type: str
        self.release_name = release_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductComponentVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.enable is not None:
            result['enable'] = self.enable
        if self.new_component_version_uid is not None:
            result['newComponentVersionUID'] = self.new_component_version_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('newComponentVersionUID') is not None:
            self.new_component_version_uid = m.get('newComponentVersionUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        return self


class UpdateProductComponentVersionResponseBodyData(TeaModel):
    def __init__(self, relation_uid=None):
        self.relation_uid = relation_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductComponentVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        return self


class UpdateProductComponentVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateProductComponentVersionResponseBodyData
        self.msg = msg  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateProductComponentVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = UpdateProductComponentVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateProductComponentVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductComponentVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductComponentVersionResponse, self).to_map()
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
            temp_model = UpdateProductComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductFoundationVersionRequest(TeaModel):
    def __init__(self, foundation_version_uid=None):
        # 底座版本uid
        self.foundation_version_uid = foundation_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductFoundationVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        return self


class UpdateProductFoundationVersionResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductFoundationVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateProductFoundationVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductFoundationVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductFoundationVersionResponse, self).to_map()
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
            temp_model = UpdateProductFoundationVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionRequest(TeaModel):
    def __init__(self, description=None, version=None):
        self.description = description  # type: str
        # 更新版本号，只允许从latest 更新到其他版本号，更新之后代表已发布
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateProductVersionResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductVersionResponse, self).to_map()
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
            temp_model = UpdateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionConfigRequest(TeaModel):
    def __init__(self, component_version_uid=None, description=None, name=None, parent_component_version_uid=None,
                 value=None, value_type=None):
        # 子组件versinid
        self.component_version_uid = component_version_uid  # type: str
        # 配置说明
        self.description = description  # type: str
        # 配置信息key
        self.name = name  # type: str
        # 父组件versionid
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        # 配置信息value
        self.value = value  # type: str
        # value类型
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class UpdateProductVersionConfigResponseBody(TeaModel):
    def __init__(self, code=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.msg = msg  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProductVersionConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductVersionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductVersionConfigResponse, self).to_map()
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
            temp_model = UpdateProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateEnvironmentTunnelRequestTunnelConfig(TeaModel):
    def __init__(self, hostname=None, password=None, region_id=None, ssh_port=None, username=None, vpc_id=None):
        # 跳板机hostname
        self.hostname = hostname  # type: str
        # 跳板机密码
        self.password = password  # type: str
        # 直连地域id
        self.region_id = region_id  # type: str
        # 跳板机ssh端口号
        self.ssh_port = ssh_port  # type: int
        # 跳板机用户名
        self.username = username  # type: str
        # 直连vpcId
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateEnvironmentTunnelRequestTunnelConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.ssh_port is not None:
            result['sshPort'] = self.ssh_port
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sshPort') is not None:
            self.ssh_port = m.get('sshPort')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ValidateEnvironmentTunnelRequest(TeaModel):
    def __init__(self, tunnel_config=None, tunnel_type=None):
        # 通道配置
        self.tunnel_config = tunnel_config  # type: ValidateEnvironmentTunnelRequestTunnelConfig
        # 通道类型
        self.tunnel_type = tunnel_type  # type: str

    def validate(self):
        if self.tunnel_config:
            self.tunnel_config.validate()

    def to_map(self):
        _map = super(ValidateEnvironmentTunnelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tunnel_config is not None:
            result['tunnelConfig'] = self.tunnel_config.to_map()
        if self.tunnel_type is not None:
            result['tunnelType'] = self.tunnel_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tunnelConfig') is not None:
            temp_model = ValidateEnvironmentTunnelRequestTunnelConfig()
            self.tunnel_config = temp_model.from_map(m['tunnelConfig'])
        if m.get('tunnelType') is not None:
            self.tunnel_type = m.get('tunnelType')
        return self


class ValidateEnvironmentTunnelResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateEnvironmentTunnelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ValidateEnvironmentTunnelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ValidateEnvironmentTunnelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateEnvironmentTunnelResponse, self).to_map()
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
            temp_model = ValidateEnvironmentTunnelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


