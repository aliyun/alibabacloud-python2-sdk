# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DemoCategory(TeaModel):
    def __init__(self, category_code=None, category_name=None, order=None, sub_categories=None):
        self.category_code = category_code  # type: str
        self.category_name = category_name  # type: str
        self.order = order  # type: long
        self.sub_categories = sub_categories  # type: list[DemoCategory]

    def validate(self):
        if self.sub_categories:
            for k in self.sub_categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DemoCategory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.order is not None:
            result['Order'] = self.order
        result['SubCategories'] = []
        if self.sub_categories is not None:
            for k in self.sub_categories:
                result['SubCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        self.sub_categories = []
        if m.get('SubCategories') is not None:
            for k in m.get('SubCategories'):
                temp_model = DemoCategory()
                self.sub_categories.append(temp_model.from_map(k))
        return self


class ForwardInfo(TeaModel):
    def __init__(self, container_name=None, eip_allocation_id=None, enable=None, nat_gateway_id=None, port=None,
                 sshpublic_key=None):
        self.container_name = container_name  # type: str
        self.eip_allocation_id = eip_allocation_id  # type: str
        self.enable = enable  # type: bool
        self.nat_gateway_id = nat_gateway_id  # type: str
        self.port = port  # type: str
        self.sshpublic_key = sshpublic_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForwardInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.port is not None:
            result['Port'] = self.port
        if self.sshpublic_key is not None:
            result['SSHPublicKey'] = self.sshpublic_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SSHPublicKey') is not None:
            self.sshpublic_key = m.get('SSHPublicKey')
        return self


class ForwardInfoResponseConnectInfoInternet(TeaModel):
    def __init__(self, endpoint=None, port=None):
        self.endpoint = endpoint  # type: str
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForwardInfoResponseConnectInfoInternet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ForwardInfoResponseConnectInfoIntranet(TeaModel):
    def __init__(self, endpoint=None, port=None):
        self.endpoint = endpoint  # type: str
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForwardInfoResponseConnectInfoIntranet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ForwardInfoResponseConnectInfo(TeaModel):
    def __init__(self, internet=None, intranet=None, message=None, phase=None):
        self.internet = internet  # type: ForwardInfoResponseConnectInfoInternet
        self.intranet = intranet  # type: ForwardInfoResponseConnectInfoIntranet
        self.message = message  # type: str
        self.phase = phase  # type: str

    def validate(self):
        if self.internet:
            self.internet.validate()
        if self.intranet:
            self.intranet.validate()

    def to_map(self):
        _map = super(ForwardInfoResponseConnectInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet is not None:
            result['Internet'] = self.internet.to_map()
        if self.intranet is not None:
            result['Intranet'] = self.intranet.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.phase is not None:
            result['Phase'] = self.phase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Internet') is not None:
            temp_model = ForwardInfoResponseConnectInfoInternet()
            self.internet = temp_model.from_map(m['Internet'])
        if m.get('Intranet') is not None:
            temp_model = ForwardInfoResponseConnectInfoIntranet()
            self.intranet = temp_model.from_map(m['Intranet'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        return self


class ForwardInfoResponse(TeaModel):
    def __init__(self, connect_info=None, container_name=None, eip_allocation_id=None, enable=None,
                 nat_gateway_id=None, port=None, sshpublic_key=None):
        self.connect_info = connect_info  # type: ForwardInfoResponseConnectInfo
        self.container_name = container_name  # type: str
        self.eip_allocation_id = eip_allocation_id  # type: str
        self.enable = enable  # type: bool
        self.nat_gateway_id = nat_gateway_id  # type: str
        self.port = port  # type: str
        self.sshpublic_key = sshpublic_key  # type: str

    def validate(self):
        if self.connect_info:
            self.connect_info.validate()

    def to_map(self):
        _map = super(ForwardInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_info is not None:
            result['ConnectInfo'] = self.connect_info.to_map()
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.port is not None:
            result['Port'] = self.port
        if self.sshpublic_key is not None:
            result['SSHPublicKey'] = self.sshpublic_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectInfo') is not None:
            temp_model = ForwardInfoResponseConnectInfo()
            self.connect_info = temp_model.from_map(m['ConnectInfo'])
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SSHPublicKey') is not None:
            self.sshpublic_key = m.get('SSHPublicKey')
        return self


class CreateIdleInstanceCullerRequest(TeaModel):
    def __init__(self, cpu_percent_threshold=None, gpu_percent_threshold=None, max_idle_time_in_minutes=None):
        self.cpu_percent_threshold = cpu_percent_threshold  # type: int
        self.gpu_percent_threshold = gpu_percent_threshold  # type: int
        self.max_idle_time_in_minutes = max_idle_time_in_minutes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIdleInstanceCullerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold
        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold
        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')
        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')
        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')
        return self


class CreateIdleInstanceCullerResponseBody(TeaModel):
    def __init__(self, code=None, instance_id=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIdleInstanceCullerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIdleInstanceCullerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIdleInstanceCullerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIdleInstanceCullerResponse, self).to_map()
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
            temp_model = CreateIdleInstanceCullerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestCloudDisks(TeaModel):
    def __init__(self, capacity=None, mount_path=None, path=None, sub_type=None):
        self.capacity = capacity  # type: str
        self.mount_path = mount_path  # type: str
        self.path = path  # type: str
        self.sub_type = sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestCloudDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.path is not None:
            result['Path'] = self.path
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class CreateInstanceRequestDatasets(TeaModel):
    def __init__(self, dataset_id=None, mount_path=None):
        self.dataset_id = dataset_id  # type: str
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


class CreateInstanceRequestLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateInstanceRequestRequestedResource(TeaModel):
    def __init__(self, cpu=None, gpu=None, gputype=None, memory=None, shared_memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str
        self.shared_memory = shared_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestRequestedResource, self).to_map()
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


class CreateInstanceRequestUserVpc(TeaModel):
    def __init__(self, default_route=None, extended_cidrs=None, forward_infos=None, security_group_id=None,
                 v_switch_id=None, vpc_id=None):
        self.default_route = default_route  # type: str
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.forward_infos = forward_infos  # type: list[ForwardInfo]
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.forward_infos:
            for k in self.forward_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateInstanceRequestUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k in self.forward_infos:
                result['ForwardInfos'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k in m.get('ForwardInfos'):
                temp_model = ForwardInfo()
                self.forward_infos.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, accessibility=None, cloud_disks=None, datasets=None, driver=None, ecs_spec=None,
                 environment_variables=None, image_id=None, image_url=None, instance_name=None, labels=None, priority=None,
                 requested_resource=None, resource_id=None, user_id=None, user_vpc=None, workspace_id=None, workspace_source=None):
        self.accessibility = accessibility  # type: str
        self.cloud_disks = cloud_disks  # type: list[CreateInstanceRequestCloudDisks]
        self.datasets = datasets  # type: list[CreateInstanceRequestDatasets]
        self.driver = driver  # type: str
        self.ecs_spec = ecs_spec  # type: str
        self.environment_variables = environment_variables  # type: dict[str, str]
        self.image_id = image_id  # type: str
        self.image_url = image_url  # type: str
        self.instance_name = instance_name  # type: str
        self.labels = labels  # type: list[CreateInstanceRequestLabels]
        self.priority = priority  # type: long
        self.requested_resource = requested_resource  # type: CreateInstanceRequestRequestedResource
        self.resource_id = resource_id  # type: str
        self.user_id = user_id  # type: str
        self.user_vpc = user_vpc  # type: CreateInstanceRequestUserVpc
        self.workspace_id = workspace_id  # type: str
        self.workspace_source = workspace_source  # type: str

    def validate(self):
        if self.cloud_disks:
            for k in self.cloud_disks:
                if k:
                    k.validate()
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.requested_resource:
            self.requested_resource.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        result['CloudDisks'] = []
        if self.cloud_disks is not None:
            for k in self.cloud_disks:
                result['CloudDisks'].append(k.to_map() if k else None)
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.driver is not None:
            result['Driver'] = self.driver
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
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k in m.get('CloudDisks'):
                temp_model = CreateInstanceRequestCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k))
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = CreateInstanceRequestDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
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
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreateInstanceRequestLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RequestedResource') is not None:
            temp_model = CreateInstanceRequestRequestedResource()
            self.requested_resource = temp_model.from_map(m['RequestedResource'])
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = CreateInstanceRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceShutdownTimerRequest(TeaModel):
    def __init__(self, due_time=None, remaining_time_in_ms=None):
        self.due_time = due_time  # type: str
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
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceShutdownTimerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceShutdownTimerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceShutdownTimerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceSnapshotRequestLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceSnapshotRequestLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateInstanceSnapshotRequest(TeaModel):
    def __init__(self, exclude_paths=None, image_url=None, labels=None, overwrite=None, snapshot_description=None,
                 snapshot_name=None):
        self.exclude_paths = exclude_paths  # type: list[str]
        self.image_url = image_url  # type: str
        self.labels = labels  # type: list[CreateInstanceSnapshotRequestLabels]
        self.overwrite = overwrite  # type: bool
        self.snapshot_description = snapshot_description  # type: str
        self.snapshot_name = snapshot_name  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateInstanceSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_paths is not None:
            result['ExcludePaths'] = self.exclude_paths
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.snapshot_description is not None:
            result['SnapshotDescription'] = self.snapshot_description
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludePaths') is not None:
            self.exclude_paths = m.get('ExcludePaths')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreateInstanceSnapshotRequestLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('SnapshotDescription') is not None:
            self.snapshot_description = m.get('SnapshotDescription')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 snapshot_id=None, success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIdleInstanceCullerResponseBody(TeaModel):
    def __init__(self, code=None, instance_id=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIdleInstanceCullerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteIdleInstanceCullerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIdleInstanceCullerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIdleInstanceCullerResponse, self).to_map()
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
            temp_model = DeleteIdleInstanceCullerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceShutdownTimerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceShutdownTimerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceShutdownTimerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 snapshot_id=None, success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIdleInstanceCullerResponseBody(TeaModel):
    def __init__(self, code=None, cpu_percent_threshold=None, gpu_percent_threshold=None,
                 idle_time_in_minutes=None, instance_id=None, max_idle_time_in_minutes=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.cpu_percent_threshold = cpu_percent_threshold  # type: int
        self.gpu_percent_threshold = gpu_percent_threshold  # type: int
        self.idle_time_in_minutes = idle_time_in_minutes  # type: int
        self.instance_id = instance_id  # type: str
        self.max_idle_time_in_minutes = max_idle_time_in_minutes  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIdleInstanceCullerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold
        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold
        if self.idle_time_in_minutes is not None:
            result['IdleTimeInMinutes'] = self.idle_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')
        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')
        if m.get('IdleTimeInMinutes') is not None:
            self.idle_time_in_minutes = m.get('IdleTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIdleInstanceCullerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIdleInstanceCullerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIdleInstanceCullerResponse, self).to_map()
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
            temp_model = GetIdleInstanceCullerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyCloudDisks(TeaModel):
    def __init__(self, capacity=None, mount_path=None, path=None, sub_type=None):
        self.capacity = capacity  # type: str
        self.mount_path = mount_path  # type: str
        self.path = path  # type: str
        self.sub_type = sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyCloudDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.path is not None:
            result['Path'] = self.path
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class GetInstanceResponseBodyDatasets(TeaModel):
    def __init__(self, dataset_id=None, mount_path=None):
        self.dataset_id = dataset_id  # type: str
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


class GetInstanceResponseBodyIdleInstanceCuller(TeaModel):
    def __init__(self, cpu_percent_threshold=None, gpu_percent_threshold=None, idle_time_in_minutes=None,
                 instance_id=None, max_idle_time_in_minutes=None):
        self.cpu_percent_threshold = cpu_percent_threshold  # type: int
        self.gpu_percent_threshold = gpu_percent_threshold  # type: int
        self.idle_time_in_minutes = idle_time_in_minutes  # type: int
        self.instance_id = instance_id  # type: str
        self.max_idle_time_in_minutes = max_idle_time_in_minutes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyIdleInstanceCuller, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold
        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold
        if self.idle_time_in_minutes is not None:
            result['IdleTimeInMinutes'] = self.idle_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')
        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')
        if m.get('IdleTimeInMinutes') is not None:
            self.idle_time_in_minutes = m.get('IdleTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')
        return self


class GetInstanceResponseBodyInstanceShutdownTimer(TeaModel):
    def __init__(self, due_time=None, gmt_create_time=None, gmt_modified_time=None, instance_id=None,
                 remaining_time_in_ms=None):
        self.due_time = due_time  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.instance_id = instance_id  # type: str
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


class GetInstanceResponseBodyInstanceSnapshotList(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, image_id=None, image_name=None, image_url=None,
                 reason_code=None, reason_message=None, repository_url=None, status=None):
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
        # 实例快照错误代码
        self.reason_code = reason_code  # type: str
        # 实例快照错误消息
        self.reason_message = reason_message  # type: str
        # 镜像仓库Url
        self.repository_url = repository_url  # type: str
        # 实例快照状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceSnapshotList, self).to_map()
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
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
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
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceResponseBodyLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetInstanceResponseBodyLatestSnapshot(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, image_id=None, image_name=None, image_url=None,
                 reason_code=None, reason_message=None, repository_url=None, status=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.image_id = image_id  # type: str
        self.image_name = image_name  # type: str
        self.image_url = image_url  # type: str
        # 实例快照错误代码
        self.reason_code = reason_code  # type: str
        # 实例快照错误消息
        self.reason_message = reason_message  # type: str
        self.repository_url = repository_url  # type: str
        # 实例快照状态
        self.status = status  # type: str

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
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
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
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceResponseBodyRequestedResource(TeaModel):
    def __init__(self, cpu=None, gpu=None, gputype=None, memory=None, shared_memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str
        self.shared_memory = shared_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyRequestedResource, self).to_map()
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


class GetInstanceResponseBodyUserVpc(TeaModel):
    def __init__(self, default_route=None, extended_cidrs=None, forward_infos=None, security_group_id=None,
                 v_switch_id=None, vpc_id=None):
        self.default_route = default_route  # type: str
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.forward_infos = forward_infos  # type: list[ForwardInfoResponse]
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        # Vpc Id。
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.forward_infos:
            for k in self.forward_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k in self.forward_infos:
                result['ForwardInfos'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k in m.get('ForwardInfos'):
                temp_model = ForwardInfoResponse()
                self.forward_infos.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, accelerator_type=None, accessibility=None, accumulated_running_time_in_ms=None,
                 cloud_disks=None, code=None, datasets=None, driver=None, ecs_spec=None, environment_variables=None,
                 gmt_create_time=None, gmt_modified_time=None, http_status_code=None, idle_instance_culler=None, image_id=None,
                 image_name=None, image_url=None, instance_id=None, instance_name=None, instance_shutdown_timer=None,
                 instance_snapshot_list=None, instance_url=None, jupyterlab_url=None, labels=None, latest_snapshot=None, message=None,
                 payment_type=None, priority=None, reason_code=None, reason_message=None, request_id=None,
                 requested_resource=None, resource_id=None, resource_name=None, status=None, success=None, terminal_url=None,
                 user_id=None, user_name=None, user_vpc=None, web_ideurl=None, workspace_id=None, workspace_name=None,
                 workspace_source=None):
        self.accelerator_type = accelerator_type  # type: str
        self.accessibility = accessibility  # type: str
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms  # type: long
        self.cloud_disks = cloud_disks  # type: list[GetInstanceResponseBodyCloudDisks]
        self.code = code  # type: str
        self.datasets = datasets  # type: list[GetInstanceResponseBodyDatasets]
        self.driver = driver  # type: str
        self.ecs_spec = ecs_spec  # type: str
        self.environment_variables = environment_variables  # type: dict[str, str]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.http_status_code = http_status_code  # type: int
        self.idle_instance_culler = idle_instance_culler  # type: GetInstanceResponseBodyIdleInstanceCuller
        self.image_id = image_id  # type: str
        self.image_name = image_name  # type: str
        self.image_url = image_url  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_shutdown_timer = instance_shutdown_timer  # type: GetInstanceResponseBodyInstanceShutdownTimer
        self.instance_snapshot_list = instance_snapshot_list  # type: list[GetInstanceResponseBodyInstanceSnapshotList]
        self.instance_url = instance_url  # type: str
        # Jupyterlab Url。
        self.jupyterlab_url = jupyterlab_url  # type: str
        self.labels = labels  # type: list[GetInstanceResponseBodyLabels]
        self.latest_snapshot = latest_snapshot  # type: GetInstanceResponseBodyLatestSnapshot
        self.message = message  # type: str
        self.payment_type = payment_type  # type: str
        self.priority = priority  # type: long
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.request_id = request_id  # type: str
        self.requested_resource = requested_resource  # type: GetInstanceResponseBodyRequestedResource
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool
        self.terminal_url = terminal_url  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str
        self.user_vpc = user_vpc  # type: GetInstanceResponseBodyUserVpc
        # Web IDE url。
        self.web_ideurl = web_ideurl  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str
        self.workspace_source = workspace_source  # type: str

    def validate(self):
        if self.cloud_disks:
            for k in self.cloud_disks:
                if k:
                    k.validate()
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.idle_instance_culler:
            self.idle_instance_culler.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.instance_snapshot_list:
            for k in self.instance_snapshot_list:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.requested_resource:
            self.requested_resource.validate()
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
        result['CloudDisks'] = []
        if self.cloud_disks is not None:
            for k in self.cloud_disks:
                result['CloudDisks'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.idle_instance_culler is not None:
            result['IdleInstanceCuller'] = self.idle_instance_culler.to_map()
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
        result['InstanceSnapshotList'] = []
        if self.instance_snapshot_list is not None:
            for k in self.instance_snapshot_list:
                result['InstanceSnapshotList'].append(k.to_map() if k else None)
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k in m.get('CloudDisks'):
                temp_model = GetInstanceResponseBodyCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = GetInstanceResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('IdleInstanceCuller') is not None:
            temp_model = GetInstanceResponseBodyIdleInstanceCuller()
            self.idle_instance_culler = temp_model.from_map(m['IdleInstanceCuller'])
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
        self.instance_snapshot_list = []
        if m.get('InstanceSnapshotList') is not None:
            for k in m.get('InstanceSnapshotList'):
                temp_model = GetInstanceResponseBodyInstanceSnapshotList()
                self.instance_snapshot_list.append(temp_model.from_map(k))
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetInstanceResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestSnapshot') is not None:
            temp_model = GetInstanceResponseBodyLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestedResource') is not None:
            temp_model = GetInstanceResponseBodyRequestedResource()
            self.requested_resource = temp_model.from_map(m['RequestedResource'])
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserVpc') is not None:
            temp_model = GetInstanceResponseBodyUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceMetricsRequest(TeaModel):
    def __init__(self, end_time=None, metric_type=None, start_time=None, time_step=None):
        self.end_time = end_time  # type: str
        self.metric_type = metric_type  # type: str
        self.start_time = start_time  # type: str
        self.time_step = time_step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceMetricsRequest, self).to_map()
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
        return self


class GetInstanceMetricsResponseBodyPodMetricsMetrics(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: long
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceMetricsResponseBodyPodMetricsMetrics, self).to_map()
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


class GetInstanceMetricsResponseBodyPodMetrics(TeaModel):
    def __init__(self, metrics=None, pod_id=None):
        self.metrics = metrics  # type: list[GetInstanceMetricsResponseBodyPodMetricsMetrics]
        self.pod_id = pod_id  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceMetricsResponseBodyPodMetrics, self).to_map()
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
                temp_model = GetInstanceMetricsResponseBodyPodMetricsMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        return self


class GetInstanceMetricsResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, pod_metrics=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.pod_metrics = pod_metrics  # type: list[GetInstanceMetricsResponseBodyPodMetrics]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.pod_metrics:
            for k in self.pod_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        result['PodMetrics'] = []
        if self.pod_metrics is not None:
            for k in self.pod_metrics:
                result['PodMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.pod_metrics = []
        if m.get('PodMetrics') is not None:
            for k in m.get('PodMetrics'):
                temp_model = GetInstanceMetricsResponseBodyPodMetrics()
                self.pod_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceMetricsResponse, self).to_map()
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
            temp_model = GetInstanceMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceShutdownTimerResponseBody(TeaModel):
    def __init__(self, code=None, due_time=None, gmt_create_time=None, gmt_modified_time=None,
                 http_status_code=None, instance_id=None, message=None, remaining_time_in_ms=None, request_id=None, success=None):
        self.code = code  # type: str
        self.due_time = due_time  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.remaining_time_in_ms = remaining_time_in_ms  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceShutdownTimerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.remaining_time_in_ms is not None:
            result['RemainingTimeInMs'] = self.remaining_time_in_ms
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RemainingTimeInMs') is not None:
            self.remaining_time_in_ms = m.get('RemainingTimeInMs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceShutdownTimerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceShutdownTimerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetInstanceShutdownTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceSnapshotResponseBodyLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceSnapshotResponseBodyLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetInstanceSnapshotResponseBody(TeaModel):
    def __init__(self, code=None, exclude_paths=None, gmt_create_time=None, gmt_modified_time=None,
                 http_status_code=None, image_id=None, image_url=None, instance_id=None, labels=None, message=None, reason_code=None,
                 reason_message=None, request_id=None, snapshot_id=None, snapshot_name=None, status=None, success=None):
        self.code = code  # type: str
        self.exclude_paths = exclude_paths  # type: list[str]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.http_status_code = http_status_code  # type: int
        self.image_id = image_id  # type: str
        self.image_url = image_url  # type: str
        self.instance_id = instance_id  # type: str
        self.labels = labels  # type: list[GetInstanceSnapshotResponseBodyLabels]
        self.message = message  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.request_id = request_id  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.exclude_paths is not None:
            result['ExcludePaths'] = self.exclude_paths
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExcludePaths') is not None:
            self.exclude_paths = m.get('ExcludePaths')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetInstanceSnapshotResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLifecycleRequest(TeaModel):
    def __init__(self, end_time=None, limit=None, order=None, session_number=None, start_time=None):
        self.end_time = end_time  # type: str
        self.limit = limit  # type: int
        self.order = order  # type: str
        self.session_number = session_number  # type: int
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLifecycleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order is not None:
            result['Order'] = self.order
        if self.session_number is not None:
            result['SessionNumber'] = self.session_number
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('SessionNumber') is not None:
            self.session_number = m.get('SessionNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetLifecycleResponseBodyLifecycle(TeaModel):
    def __init__(self, status=None, reason_code=None, reason_message=None, gmt_create_time=None):
        self.status = status  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.gmt_create_time = gmt_create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLifecycleResponseBodyLifecycle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        return self


class GetLifecycleResponseBody(TeaModel):
    def __init__(self, code=None, lifecycle=None, message=None, request_id=None, success=None, total_count=None):
        self.code = code  # type: str
        self.lifecycle = lifecycle  # type: list[list[GetLifecycleResponseBodyLifecycle]]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.lifecycle:
            for k in self.lifecycle:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(GetLifecycleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Lifecycle'] = []
        if self.lifecycle is not None:
            for k in self.lifecycle:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['Lifecycle'].append(l1)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.lifecycle = []
        if m.get('Lifecycle') is not None:
            for k in m.get('Lifecycle'):
                l1 = []
                for k1 in k:
                    temp_model = GetLifecycleResponseBodyLifecycle()
                    l1.append(temp_model.from_map(k1))
                self.lifecycle.append(l1)
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetLifecycleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLifecycleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLifecycleResponse, self).to_map()
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
            temp_model = GetLifecycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupStatisticsRequest(TeaModel):
    def __init__(self, end_time=None, resource_id=None, start_time=None, workspace_ids=None):
        self.end_time = end_time  # type: str
        self.resource_id = resource_id  # type: str
        self.start_time = start_time  # type: str
        self.workspace_ids = workspace_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        return self


class GetResourceGroupStatisticsResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, statistics=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.statistics = statistics  # type: dict[str, dict]
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResourceGroupStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceGroupStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceGroupStatisticsResponse, self).to_map()
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
            temp_model = GetResourceGroupStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(self, expire_time=None, instance_id=None):
        self.expire_time = expire_time  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, token=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class GetUserConfigResponseBodyFreeTier(TeaModel):
    def __init__(self, end_time=None, init_base_unit=None, init_base_value=None, init_show_unit=None,
                 init_show_value=None, is_free_tier_user=None, period_base_unit=None, period_base_value=None,
                 period_show_unit=None, period_show_value=None, start_time=None, status=None):
        self.end_time = end_time  # type: str
        self.init_base_unit = init_base_unit  # type: str
        self.init_base_value = init_base_value  # type: float
        self.init_show_unit = init_show_unit  # type: str
        self.init_show_value = init_show_value  # type: str
        self.is_free_tier_user = is_free_tier_user  # type: bool
        self.period_base_unit = period_base_unit  # type: str
        self.period_base_value = period_base_value  # type: float
        self.period_show_unit = period_show_unit  # type: str
        self.period_show_value = period_show_value  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserConfigResponseBodyFreeTier, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.init_base_unit is not None:
            result['InitBaseUnit'] = self.init_base_unit
        if self.init_base_value is not None:
            result['InitBaseValue'] = self.init_base_value
        if self.init_show_unit is not None:
            result['InitShowUnit'] = self.init_show_unit
        if self.init_show_value is not None:
            result['InitShowValue'] = self.init_show_value
        if self.is_free_tier_user is not None:
            result['IsFreeTierUser'] = self.is_free_tier_user
        if self.period_base_unit is not None:
            result['PeriodBaseUnit'] = self.period_base_unit
        if self.period_base_value is not None:
            result['PeriodBaseValue'] = self.period_base_value
        if self.period_show_unit is not None:
            result['PeriodShowUnit'] = self.period_show_unit
        if self.period_show_value is not None:
            result['PeriodShowValue'] = self.period_show_value
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InitBaseUnit') is not None:
            self.init_base_unit = m.get('InitBaseUnit')
        if m.get('InitBaseValue') is not None:
            self.init_base_value = m.get('InitBaseValue')
        if m.get('InitShowUnit') is not None:
            self.init_show_unit = m.get('InitShowUnit')
        if m.get('InitShowValue') is not None:
            self.init_show_value = m.get('InitShowValue')
        if m.get('IsFreeTierUser') is not None:
            self.is_free_tier_user = m.get('IsFreeTierUser')
        if m.get('PeriodBaseUnit') is not None:
            self.period_base_unit = m.get('PeriodBaseUnit')
        if m.get('PeriodBaseValue') is not None:
            self.period_base_value = m.get('PeriodBaseValue')
        if m.get('PeriodShowUnit') is not None:
            self.period_show_unit = m.get('PeriodShowUnit')
        if m.get('PeriodShowValue') is not None:
            self.period_show_value = m.get('PeriodShowValue')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetUserConfigResponseBody(TeaModel):
    def __init__(self, account_sufficient=None, code=None, enable_eci_disk=None, free_tier=None,
                 free_tier_spec_available=None, http_status_code=None, message=None, request_id=None, success=None):
        self.account_sufficient = account_sufficient  # type: bool
        self.code = code  # type: str
        self.enable_eci_disk = enable_eci_disk  # type: bool
        self.free_tier = free_tier  # type: GetUserConfigResponseBodyFreeTier
        self.free_tier_spec_available = free_tier_spec_available  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.free_tier:
            self.free_tier.validate()

    def to_map(self):
        _map = super(GetUserConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_sufficient is not None:
            result['AccountSufficient'] = self.account_sufficient
        if self.code is not None:
            result['Code'] = self.code
        if self.enable_eci_disk is not None:
            result['EnableEciDisk'] = self.enable_eci_disk
        if self.free_tier is not None:
            result['FreeTier'] = self.free_tier.to_map()
        if self.free_tier_spec_available is not None:
            result['FreeTierSpecAvailable'] = self.free_tier_spec_available
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountSufficient') is not None:
            self.account_sufficient = m.get('AccountSufficient')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnableEciDisk') is not None:
            self.enable_eci_disk = m.get('EnableEciDisk')
        if m.get('FreeTier') is not None:
            temp_model = GetUserConfigResponseBodyFreeTier()
            self.free_tier = temp_model.from_map(m['FreeTier'])
        if m.get('FreeTierSpecAvailable') is not None:
            self.free_tier_spec_available = m.get('FreeTierSpecAvailable')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsRequest(TeaModel):
    def __init__(self, accelerator_type=None, order=None, page_number=None, page_size=None, sort_by=None):
        self.accelerator_type = accelerator_type  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
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


class ListEcsSpecsResponseBodyEcsSpecsLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsSpecsResponseBodyEcsSpecsLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEcsSpecsResponseBodyEcsSpecs(TeaModel):
    def __init__(self, accelerator_type=None, cpu=None, currency=None, gpu=None, gputype=None,
                 instance_bandwidth_rx=None, instance_type=None, is_available=None, labels=None, memory=None, price=None,
                 system_disk_capacity=None):
        self.accelerator_type = accelerator_type  # type: str
        self.cpu = cpu  # type: long
        self.currency = currency  # type: str
        self.gpu = gpu  # type: long
        self.gputype = gputype  # type: str
        self.instance_bandwidth_rx = instance_bandwidth_rx  # type: long
        self.instance_type = instance_type  # type: str
        self.is_available = is_available  # type: bool
        self.labels = labels  # type: list[ListEcsSpecsResponseBodyEcsSpecsLabels]
        self.memory = memory  # type: float
        self.price = price  # type: float
        self.system_disk_capacity = system_disk_capacity  # type: long

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

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
        if self.is_available is not None:
            result['IsAvailable'] = self.is_available
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
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
        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListEcsSpecsResponseBodyEcsSpecsLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        return self


class ListEcsSpecsResponseBody(TeaModel):
    def __init__(self, code=None, ecs_specs=None, http_status_code=None, message=None, request_id=None, success=None,
                 total_count=None):
        self.code = code  # type: str
        self.ecs_specs = ecs_specs  # type: list[ListEcsSpecsResponseBodyEcsSpecs]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
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
        if self.code is not None:
            result['Code'] = self.code
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k in self.ecs_specs:
                result['EcsSpecs'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k in m.get('EcsSpecs'):
                temp_model = ListEcsSpecsResponseBodyEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class ListInstanceSnapshotResponseBodySnapshotsLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceSnapshotResponseBodySnapshotsLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListInstanceSnapshotResponseBodySnapshots(TeaModel):
    def __init__(self, exclude_paths=None, gmt_create_time=None, gmt_modified_time=None, image_id=None,
                 image_url=None, instance_id=None, labels=None, reason_code=None, reason_message=None, snapshot_id=None,
                 snapshot_name=None, status=None):
        self.exclude_paths = exclude_paths  # type: list[str]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.image_id = image_id  # type: str
        self.image_url = image_url  # type: str
        self.instance_id = instance_id  # type: str
        self.labels = labels  # type: list[ListInstanceSnapshotResponseBodySnapshotsLabels]
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceSnapshotResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_paths is not None:
            result['ExcludePaths'] = self.exclude_paths
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
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
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
        if m.get('ExcludePaths') is not None:
            self.exclude_paths = m.get('ExcludePaths')
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
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListInstanceSnapshotResponseBodySnapshotsLabels()
                self.labels.append(temp_model.from_map(k))
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
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, snapshots=None, success=None,
                 total_count=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.snapshots = snapshots  # type: list[ListInstanceSnapshotResponseBodySnapshots]
        self.success = success  # type: bool
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListInstanceSnapshotResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListInstanceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceStatisticsRequest(TeaModel):
    def __init__(self, workspace_ids=None):
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
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, statistics=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.statistics = statistics  # type: dict[str, dict]
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstanceStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListInstanceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, accelerator_type=None, accessibility=None, instance_id=None, instance_name=None, order=None,
                 page_number=None, page_size=None, payment_type=None, resource_id=None, sort_by=None, status=None,
                 workspace_id=None):
        self.accelerator_type = accelerator_type  # type: str
        self.accessibility = accessibility  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.payment_type = payment_type  # type: str
        self.resource_id = resource_id  # type: str
        self.sort_by = sort_by  # type: str
        self.status = status  # type: str
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListInstancesResponseBodyInstancesCloudDisks(TeaModel):
    def __init__(self, capacity=None, mount_path=None, path=None, sub_type=None):
        self.capacity = capacity  # type: str
        self.mount_path = mount_path  # type: str
        self.path = path  # type: str
        self.sub_type = sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesCloudDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.path is not None:
            result['Path'] = self.path
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class ListInstancesResponseBodyInstancesDatasets(TeaModel):
    def __init__(self, dataset_id=None, mount_path=None):
        self.dataset_id = dataset_id  # type: str
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


class ListInstancesResponseBodyInstancesIdleInstanceCuller(TeaModel):
    def __init__(self, cpu_percent_threshold=None, gpu_percent_threshold=None, idle_time_in_minutes=None,
                 instance_id=None, max_idle_time_in_minutes=None):
        self.cpu_percent_threshold = cpu_percent_threshold  # type: int
        self.gpu_percent_threshold = gpu_percent_threshold  # type: int
        self.idle_time_in_minutes = idle_time_in_minutes  # type: int
        self.instance_id = instance_id  # type: str
        self.max_idle_time_in_minutes = max_idle_time_in_minutes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesIdleInstanceCuller, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_percent_threshold is not None:
            result['CpuPercentThreshold'] = self.cpu_percent_threshold
        if self.gpu_percent_threshold is not None:
            result['GpuPercentThreshold'] = self.gpu_percent_threshold
        if self.idle_time_in_minutes is not None:
            result['IdleTimeInMinutes'] = self.idle_time_in_minutes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_idle_time_in_minutes is not None:
            result['MaxIdleTimeInMinutes'] = self.max_idle_time_in_minutes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuPercentThreshold') is not None:
            self.cpu_percent_threshold = m.get('CpuPercentThreshold')
        if m.get('GpuPercentThreshold') is not None:
            self.gpu_percent_threshold = m.get('GpuPercentThreshold')
        if m.get('IdleTimeInMinutes') is not None:
            self.idle_time_in_minutes = m.get('IdleTimeInMinutes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxIdleTimeInMinutes') is not None:
            self.max_idle_time_in_minutes = m.get('MaxIdleTimeInMinutes')
        return self


class ListInstancesResponseBodyInstancesInstanceShutdownTimer(TeaModel):
    def __init__(self, due_time=None, gmt_create_time=None, gmt_modified_time=None, instance_id=None,
                 remaining_time_in_ms=None):
        self.due_time = due_time  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.instance_id = instance_id  # type: str
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


class ListInstancesResponseBodyInstancesInstanceSnapshotList(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, image_id=None, image_name=None, image_url=None,
                 reason_code=None, reason_message=None, repository_url=None, status=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.image_id = image_id  # type: str
        self.image_name = image_name  # type: str
        self.image_url = image_url  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.repository_url = repository_url  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesInstanceSnapshotList, self).to_map()
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
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
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
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstancesLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListInstancesResponseBodyInstancesLatestSnapshot(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, image_id=None, image_name=None, image_url=None,
                 reason_code=None, reason_message=None, repository_url=None, status=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.image_id = image_id  # type: str
        self.image_name = image_name  # type: str
        self.image_url = image_url  # type: str
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.repository_url = repository_url  # type: str
        self.status = status  # type: str

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
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url
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
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstancesRequestedResource(TeaModel):
    def __init__(self, cpu=None, gpu=None, gputype=None, memory=None, shared_memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str
        self.shared_memory = shared_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesRequestedResource, self).to_map()
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


class ListInstancesResponseBodyInstancesUserVpc(TeaModel):
    def __init__(self, default_route=None, extended_cidrs=None, forward_infos=None, security_group_id=None,
                 v_switch_id=None, vpc_id=None):
        self.default_route = default_route  # type: str
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.forward_infos = forward_infos  # type: list[ForwardInfoResponse]
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.forward_infos:
            for k in self.forward_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k in self.forward_infos:
                result['ForwardInfos'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k in m.get('ForwardInfos'):
                temp_model = ForwardInfoResponse()
                self.forward_infos.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(self, accelerator_type=None, accessibility=None, accumulated_running_time_in_ms=None,
                 cloud_disks=None, datasets=None, driver=None, ecs_spec=None, environment_variables=None, gmt_create_time=None,
                 gmt_modified_time=None, idle_instance_culler=None, image_id=None, image_name=None, image_url=None, instance_id=None,
                 instance_name=None, instance_shutdown_timer=None, instance_snapshot_list=None, instance_url=None,
                 jupyterlab_url=None, labels=None, latest_snapshot=None, payment_type=None, priority=None, reason_code=None,
                 reason_message=None, requested_resource=None, resource_id=None, resource_name=None, status=None,
                 terminal_url=None, user_id=None, user_name=None, user_vpc=None, web_ideurl=None, workspace_id=None,
                 workspace_name=None, workspace_source=None):
        self.accelerator_type = accelerator_type  # type: str
        self.accessibility = accessibility  # type: str
        self.accumulated_running_time_in_ms = accumulated_running_time_in_ms  # type: long
        self.cloud_disks = cloud_disks  # type: list[ListInstancesResponseBodyInstancesCloudDisks]
        self.datasets = datasets  # type: list[ListInstancesResponseBodyInstancesDatasets]
        self.driver = driver  # type: str
        self.ecs_spec = ecs_spec  # type: str
        self.environment_variables = environment_variables  # type: dict[str, str]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.idle_instance_culler = idle_instance_culler  # type: ListInstancesResponseBodyInstancesIdleInstanceCuller
        self.image_id = image_id  # type: str
        self.image_name = image_name  # type: str
        self.image_url = image_url  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_shutdown_timer = instance_shutdown_timer  # type: ListInstancesResponseBodyInstancesInstanceShutdownTimer
        self.instance_snapshot_list = instance_snapshot_list  # type: list[ListInstancesResponseBodyInstancesInstanceSnapshotList]
        self.instance_url = instance_url  # type: str
        # Jupyterlab Url。
        self.jupyterlab_url = jupyterlab_url  # type: str
        self.labels = labels  # type: list[ListInstancesResponseBodyInstancesLabels]
        self.latest_snapshot = latest_snapshot  # type: ListInstancesResponseBodyInstancesLatestSnapshot
        self.payment_type = payment_type  # type: str
        self.priority = priority  # type: long
        self.reason_code = reason_code  # type: str
        self.reason_message = reason_message  # type: str
        self.requested_resource = requested_resource  # type: ListInstancesResponseBodyInstancesRequestedResource
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.status = status  # type: str
        self.terminal_url = terminal_url  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str
        self.user_vpc = user_vpc  # type: ListInstancesResponseBodyInstancesUserVpc
        # Web IDE url。
        self.web_ideurl = web_ideurl  # type: str
        self.workspace_id = workspace_id  # type: str
        self.workspace_name = workspace_name  # type: str
        self.workspace_source = workspace_source  # type: str

    def validate(self):
        if self.cloud_disks:
            for k in self.cloud_disks:
                if k:
                    k.validate()
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.idle_instance_culler:
            self.idle_instance_culler.validate()
        if self.instance_shutdown_timer:
            self.instance_shutdown_timer.validate()
        if self.instance_snapshot_list:
            for k in self.instance_snapshot_list:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_snapshot:
            self.latest_snapshot.validate()
        if self.requested_resource:
            self.requested_resource.validate()
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
        result['CloudDisks'] = []
        if self.cloud_disks is not None:
            for k in self.cloud_disks:
                result['CloudDisks'].append(k.to_map() if k else None)
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.idle_instance_culler is not None:
            result['IdleInstanceCuller'] = self.idle_instance_culler.to_map()
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
        result['InstanceSnapshotList'] = []
        if self.instance_snapshot_list is not None:
            for k in self.instance_snapshot_list:
                result['InstanceSnapshotList'].append(k.to_map() if k else None)
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.jupyterlab_url is not None:
            result['JupyterlabUrl'] = self.jupyterlab_url
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_snapshot is not None:
            result['LatestSnapshot'] = self.latest_snapshot.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.status is not None:
            result['Status'] = self.status
        if self.terminal_url is not None:
            result['TerminalUrl'] = self.terminal_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.web_ideurl is not None:
            result['WebIDEUrl'] = self.web_ideurl
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('AccumulatedRunningTimeInMs') is not None:
            self.accumulated_running_time_in_ms = m.get('AccumulatedRunningTimeInMs')
        self.cloud_disks = []
        if m.get('CloudDisks') is not None:
            for k in m.get('CloudDisks'):
                temp_model = ListInstancesResponseBodyInstancesCloudDisks()
                self.cloud_disks.append(temp_model.from_map(k))
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = ListInstancesResponseBodyInstancesDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('IdleInstanceCuller') is not None:
            temp_model = ListInstancesResponseBodyInstancesIdleInstanceCuller()
            self.idle_instance_culler = temp_model.from_map(m['IdleInstanceCuller'])
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
        self.instance_snapshot_list = []
        if m.get('InstanceSnapshotList') is not None:
            for k in m.get('InstanceSnapshotList'):
                temp_model = ListInstancesResponseBodyInstancesInstanceSnapshotList()
                self.instance_snapshot_list.append(temp_model.from_map(k))
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('JupyterlabUrl') is not None:
            self.jupyterlab_url = m.get('JupyterlabUrl')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListInstancesResponseBodyInstancesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestSnapshot') is not None:
            temp_model = ListInstancesResponseBodyInstancesLatestSnapshot()
            self.latest_snapshot = temp_model.from_map(m['LatestSnapshot'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestedResource') is not None:
            temp_model = ListInstancesResponseBodyInstancesRequestedResource()
            self.requested_resource = temp_model.from_map(m['RequestedResource'])
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerminalUrl') is not None:
            self.terminal_url = m.get('TerminalUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserVpc') is not None:
            temp_model = ListInstancesResponseBodyInstancesUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WebIDEUrl') is not None:
            self.web_ideurl = m.get('WebIDEUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instances=None, message=None, request_id=None, success=None,
                 total_count=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instances = instances  # type: list[ListInstancesResponseBodyInstances]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(self, save_image=None):
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
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequestDatasets(TeaModel):
    def __init__(self, dataset_id=None, mount_path=None):
        self.dataset_id = dataset_id  # type: str
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequestDatasets, self).to_map()
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


class UpdateInstanceRequestRequestedResource(TeaModel):
    def __init__(self, cpu=None, gpu=None, gputype=None, memory=None, shared_memory=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gputype = gputype  # type: str
        self.memory = memory  # type: str
        self.shared_memory = shared_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequestRequestedResource, self).to_map()
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


class UpdateInstanceRequestUserVpc(TeaModel):
    def __init__(self, default_route=None, extended_cidrs=None, forward_infos=None, security_group_id=None,
                 v_switch_id=None, vpc_id=None):
        self.default_route = default_route  # type: str
        self.extended_cidrs = extended_cidrs  # type: list[str]
        self.forward_infos = forward_infos  # type: list[ForwardInfo]
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.forward_infos:
            for k in self.forward_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateInstanceRequestUserVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
        result['ForwardInfos'] = []
        if self.forward_infos is not None:
            for k in self.forward_infos:
                result['ForwardInfos'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        self.forward_infos = []
        if m.get('ForwardInfos') is not None:
            for k in m.get('ForwardInfos'):
                temp_model = ForwardInfo()
                self.forward_infos.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, accessibility=None, datasets=None, disassociate_datasets=None, disassociate_driver=None,
                 disassociate_vpc=None, driver=None, ecs_spec=None, image_id=None, image_url=None, instance_name=None, priority=None,
                 requested_resource=None, user_id=None, user_vpc=None, workspace_source=None):
        self.accessibility = accessibility  # type: str
        self.datasets = datasets  # type: list[UpdateInstanceRequestDatasets]
        self.disassociate_datasets = disassociate_datasets  # type: bool
        self.disassociate_driver = disassociate_driver  # type: bool
        self.disassociate_vpc = disassociate_vpc  # type: bool
        self.driver = driver  # type: str
        self.ecs_spec = ecs_spec  # type: str
        self.image_id = image_id  # type: str
        self.image_url = image_url  # type: str
        self.instance_name = instance_name  # type: str
        self.priority = priority  # type: long
        self.requested_resource = requested_resource  # type: UpdateInstanceRequestRequestedResource
        self.user_id = user_id  # type: str
        self.user_vpc = user_vpc  # type: UpdateInstanceRequestUserVpc
        self.workspace_source = workspace_source  # type: str

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()
        if self.requested_resource:
            self.requested_resource.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.disassociate_datasets is not None:
            result['DisassociateDatasets'] = self.disassociate_datasets
        if self.disassociate_driver is not None:
            result['DisassociateDriver'] = self.disassociate_driver
        if self.disassociate_vpc is not None:
            result['DisassociateVpc'] = self.disassociate_vpc
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.requested_resource is not None:
            result['RequestedResource'] = self.requested_resource.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_source is not None:
            result['WorkspaceSource'] = self.workspace_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = UpdateInstanceRequestDatasets()
                self.datasets.append(temp_model.from_map(k))
        if m.get('DisassociateDatasets') is not None:
            self.disassociate_datasets = m.get('DisassociateDatasets')
        if m.get('DisassociateDriver') is not None:
            self.disassociate_driver = m.get('DisassociateDriver')
        if m.get('DisassociateVpc') is not None:
            self.disassociate_vpc = m.get('DisassociateVpc')
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RequestedResource') is not None:
            temp_model = UpdateInstanceRequestRequestedResource()
            self.requested_resource = temp_model.from_map(m['RequestedResource'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserVpc') is not None:
            temp_model = UpdateInstanceRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceSource') is not None:
            self.workspace_source = m.get('WorkspaceSource')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, instance_id=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


