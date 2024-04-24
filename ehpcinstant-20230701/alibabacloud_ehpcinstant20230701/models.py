# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddImageRequestContainerImageSpecRegistryCredential(TeaModel):
    def __init__(self, password=None, server=None, user_name=None):
        self.password = password  # type: str
        self.server = server  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageRequestContainerImageSpecRegistryCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class AddImageRequestContainerImageSpec(TeaModel):
    def __init__(self, is_acrenterprise=None, is_acrregistry=None, registry_credential=None, registry_cri_id=None,
                 registry_url=None):
        self.is_acrenterprise = is_acrenterprise  # type: bool
        self.is_acrregistry = is_acrregistry  # type: bool
        self.registry_credential = registry_credential  # type: AddImageRequestContainerImageSpecRegistryCredential
        self.registry_cri_id = registry_cri_id  # type: str
        self.registry_url = registry_url  # type: str

    def validate(self):
        if self.registry_credential:
            self.registry_credential.validate()

    def to_map(self):
        _map = super(AddImageRequestContainerImageSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_acrenterprise is not None:
            result['IsACREnterprise'] = self.is_acrenterprise
        if self.is_acrregistry is not None:
            result['IsACRRegistry'] = self.is_acrregistry
        if self.registry_credential is not None:
            result['RegistryCredential'] = self.registry_credential.to_map()
        if self.registry_cri_id is not None:
            result['RegistryCriId'] = self.registry_cri_id
        if self.registry_url is not None:
            result['RegistryUrl'] = self.registry_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsACREnterprise') is not None:
            self.is_acrenterprise = m.get('IsACREnterprise')
        if m.get('IsACRRegistry') is not None:
            self.is_acrregistry = m.get('IsACRRegistry')
        if m.get('RegistryCredential') is not None:
            temp_model = AddImageRequestContainerImageSpecRegistryCredential()
            self.registry_credential = temp_model.from_map(m['RegistryCredential'])
        if m.get('RegistryCriId') is not None:
            self.registry_cri_id = m.get('RegistryCriId')
        if m.get('RegistryUrl') is not None:
            self.registry_url = m.get('RegistryUrl')
        return self


class AddImageRequestVMImageSpec(TeaModel):
    def __init__(self, image_id=None):
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageRequestVMImageSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class AddImageRequest(TeaModel):
    def __init__(self, container_image_spec=None, description=None, image_version=None, name=None,
                 vmimage_spec=None):
        self.container_image_spec = container_image_spec  # type: AddImageRequestContainerImageSpec
        self.description = description  # type: str
        self.image_version = image_version  # type: str
        self.name = name  # type: str
        self.vmimage_spec = vmimage_spec  # type: AddImageRequestVMImageSpec

    def validate(self):
        if self.container_image_spec:
            self.container_image_spec.validate()
        if self.vmimage_spec:
            self.vmimage_spec.validate()

    def to_map(self):
        _map = super(AddImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_image_spec is not None:
            result['ContainerImageSpec'] = self.container_image_spec.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.name is not None:
            result['Name'] = self.name
        if self.vmimage_spec is not None:
            result['VMImageSpec'] = self.vmimage_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            temp_model = AddImageRequestContainerImageSpec()
            self.container_image_spec = temp_model.from_map(m['ContainerImageSpec'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VMImageSpec') is not None:
            temp_model = AddImageRequestVMImageSpec()
            self.vmimage_spec = temp_model.from_map(m['VMImageSpec'])
        return self


class AddImageShrinkRequest(TeaModel):
    def __init__(self, container_image_spec_shrink=None, description=None, image_version=None, name=None,
                 vmimage_spec_shrink=None):
        self.container_image_spec_shrink = container_image_spec_shrink  # type: str
        self.description = description  # type: str
        self.image_version = image_version  # type: str
        self.name = name  # type: str
        self.vmimage_spec_shrink = vmimage_spec_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_image_spec_shrink is not None:
            result['ContainerImageSpec'] = self.container_image_spec_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.name is not None:
            result['Name'] = self.name
        if self.vmimage_spec_shrink is not None:
            result['VMImageSpec'] = self.vmimage_spec_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            self.container_image_spec_shrink = m.get('ContainerImageSpec')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VMImageSpec') is not None:
            self.vmimage_spec_shrink = m.get('VMImageSpec')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(self, image_id=None, request_id=None, success=None):
        self.image_id = image_id  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddImageResponse, self).to_map()
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequestDeploymentPolicyNetwork(TeaModel):
    def __init__(self, vswitch=None):
        self.vswitch = vswitch  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestDeploymentPolicyNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class CreateJobRequestDeploymentPolicy(TeaModel):
    def __init__(self, allocation_spec=None, network=None):
        self.allocation_spec = allocation_spec  # type: str
        self.network = network  # type: CreateJobRequestDeploymentPolicyNetwork

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super(CreateJobRequestDeploymentPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')
        if m.get('Network') is not None:
            temp_model = CreateJobRequestDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class CreateJobRequestTasksExecutorPolicyArraySpec(TeaModel):
    def __init__(self, index_end=None, index_start=None, index_step=None):
        self.index_end = index_end  # type: int
        self.index_start = index_start  # type: int
        self.index_step = index_step  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestTasksExecutorPolicyArraySpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_end is not None:
            result['IndexEnd'] = self.index_end
        if self.index_start is not None:
            result['IndexStart'] = self.index_start
        if self.index_step is not None:
            result['IndexStep'] = self.index_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IndexEnd') is not None:
            self.index_end = m.get('IndexEnd')
        if m.get('IndexStart') is not None:
            self.index_start = m.get('IndexStart')
        if m.get('IndexStep') is not None:
            self.index_step = m.get('IndexStep')
        return self


class CreateJobRequestTasksExecutorPolicy(TeaModel):
    def __init__(self, array_spec=None, max_count=None):
        self.array_spec = array_spec  # type: CreateJobRequestTasksExecutorPolicyArraySpec
        self.max_count = max_count  # type: int

    def validate(self):
        if self.array_spec:
            self.array_spec.validate()

    def to_map(self):
        _map = super(CreateJobRequestTasksExecutorPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_spec is not None:
            result['ArraySpec'] = self.array_spec.to_map()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArraySpec') is not None:
            temp_model = CreateJobRequestTasksExecutorPolicyArraySpec()
            self.array_spec = temp_model.from_map(m['ArraySpec'])
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class CreateJobRequestTasksTaskSpecResourceDisks(TeaModel):
    def __init__(self, size=None, type=None):
        self.size = size  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestTasksTaskSpecResourceDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateJobRequestTasksTaskSpecResource(TeaModel):
    def __init__(self, cores=None, disks=None, memory=None):
        self.cores = cores  # type: float
        self.disks = disks  # type: list[CreateJobRequestTasksTaskSpecResourceDisks]
        self.memory = memory  # type: float

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateJobRequestTasksTaskSpecResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cores is not None:
            result['Cores'] = self.cores
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = CreateJobRequestTasksTaskSpecResourceDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars, self).to_map()
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


class CreateJobRequestTasksTaskSpecTaskExecutorContainer(TeaModel):
    def __init__(self, command=None, environment_vars=None, image=None, working_dir=None):
        self.command = command  # type: list[str]
        self.environment_vars = environment_vars  # type: list[CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars]
        self.image = image  # type: str
        self.working_dir = working_dir  # type: str

    def validate(self):
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateJobRequestTasksTaskSpecTaskExecutorContainer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutorVM(TeaModel):
    def __init__(self, image=None, prolog_script=None, script=None):
        self.image = image  # type: str
        self.prolog_script = prolog_script  # type: str
        self.script = script  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestTasksTaskSpecTaskExecutorVM, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.prolog_script is not None:
            result['PrologScript'] = self.prolog_script
        if self.script is not None:
            result['Script'] = self.script
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class CreateJobRequestTasksTaskSpecTaskExecutor(TeaModel):
    def __init__(self, container=None, vm=None):
        self.container = container  # type: CreateJobRequestTasksTaskSpecTaskExecutorContainer
        self.vm = vm  # type: CreateJobRequestTasksTaskSpecTaskExecutorVM

    def validate(self):
        if self.container:
            self.container.validate()
        if self.vm:
            self.vm.validate()

    def to_map(self):
        _map = super(CreateJobRequestTasksTaskSpecTaskExecutor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container is not None:
            result['Container'] = self.container.to_map()
        if self.vm is not None:
            result['VM'] = self.vm.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Container') is not None:
            temp_model = CreateJobRequestTasksTaskSpecTaskExecutorContainer()
            self.container = temp_model.from_map(m['Container'])
        if m.get('VM') is not None:
            temp_model = CreateJobRequestTasksTaskSpecTaskExecutorVM()
            self.vm = temp_model.from_map(m['VM'])
        return self


class CreateJobRequestTasksTaskSpecVolumeMount(TeaModel):
    def __init__(self, mount_options=None, mount_path=None, volume_driver=None):
        self.mount_options = mount_options  # type: str
        self.mount_path = mount_path  # type: str
        self.volume_driver = volume_driver  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestTasksTaskSpecVolumeMount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_options is not None:
            result['MountOptions'] = self.mount_options
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.volume_driver is not None:
            result['VolumeDriver'] = self.volume_driver
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountOptions') is not None:
            self.mount_options = m.get('MountOptions')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('VolumeDriver') is not None:
            self.volume_driver = m.get('VolumeDriver')
        return self


class CreateJobRequestTasksTaskSpec(TeaModel):
    def __init__(self, resource=None, task_executor=None, volume_mount=None):
        self.resource = resource  # type: CreateJobRequestTasksTaskSpecResource
        self.task_executor = task_executor  # type: list[CreateJobRequestTasksTaskSpecTaskExecutor]
        self.volume_mount = volume_mount  # type: list[CreateJobRequestTasksTaskSpecVolumeMount]

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.task_executor:
            for k in self.task_executor:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateJobRequestTasksTaskSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        result['TaskExecutor'] = []
        if self.task_executor is not None:
            for k in self.task_executor:
                result['TaskExecutor'].append(k.to_map() if k else None)
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Resource') is not None:
            temp_model = CreateJobRequestTasksTaskSpecResource()
            self.resource = temp_model.from_map(m['Resource'])
        self.task_executor = []
        if m.get('TaskExecutor') is not None:
            for k in m.get('TaskExecutor'):
                temp_model = CreateJobRequestTasksTaskSpecTaskExecutor()
                self.task_executor.append(temp_model.from_map(k))
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = CreateJobRequestTasksTaskSpecVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        return self


class CreateJobRequestTasks(TeaModel):
    def __init__(self, executor_policy=None, task_name=None, task_spec=None, task_sustainable=None):
        self.executor_policy = executor_policy  # type: CreateJobRequestTasksExecutorPolicy
        self.task_name = task_name  # type: str
        self.task_spec = task_spec  # type: CreateJobRequestTasksTaskSpec
        self.task_sustainable = task_sustainable  # type: bool

    def validate(self):
        if self.executor_policy:
            self.executor_policy.validate()
        if self.task_spec:
            self.task_spec.validate()

    def to_map(self):
        _map = super(CreateJobRequestTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_policy is not None:
            result['ExecutorPolicy'] = self.executor_policy.to_map()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_spec is not None:
            result['TaskSpec'] = self.task_spec.to_map()
        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutorPolicy') is not None:
            temp_model = CreateJobRequestTasksExecutorPolicy()
            self.executor_policy = temp_model.from_map(m['ExecutorPolicy'])
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskSpec') is not None:
            temp_model = CreateJobRequestTasksTaskSpec()
            self.task_spec = temp_model.from_map(m['TaskSpec'])
        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')
        return self


class CreateJobRequest(TeaModel):
    def __init__(self, deployment_policy=None, job_description=None, job_name=None, tasks=None):
        self.deployment_policy = deployment_policy  # type: CreateJobRequestDeploymentPolicy
        self.job_description = job_description  # type: str
        self.job_name = job_name  # type: str
        self.tasks = tasks  # type: list[CreateJobRequestTasks]

    def validate(self):
        if self.deployment_policy:
            self.deployment_policy.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_policy is not None:
            result['DeploymentPolicy'] = self.deployment_policy.to_map()
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_name is not None:
            result['JobName'] = self.job_name
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeploymentPolicy') is not None:
            temp_model = CreateJobRequestDeploymentPolicy()
            self.deployment_policy = temp_model.from_map(m['DeploymentPolicy'])
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = CreateJobRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class CreateJobShrinkRequest(TeaModel):
    def __init__(self, deployment_policy_shrink=None, job_description=None, job_name=None, tasks_shrink=None):
        self.deployment_policy_shrink = deployment_policy_shrink  # type: str
        self.job_description = job_description  # type: str
        self.job_name = job_name  # type: str
        self.tasks_shrink = tasks_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_policy_shrink is not None:
            result['DeploymentPolicy'] = self.deployment_policy_shrink
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.tasks_shrink is not None:
            result['Tasks'] = self.tasks_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeploymentPolicy') is not None:
            self.deployment_policy_shrink = m.get('DeploymentPolicy')
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Tasks') is not None:
            self.tasks_shrink = m.get('Tasks')
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


class DeleteJobsRequestJobSpecTaskSpec(TeaModel):
    def __init__(self, array_index=None, task_name=None):
        self.array_index = array_index  # type: list[int]
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobsRequestJobSpecTaskSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DeleteJobsRequestJobSpec(TeaModel):
    def __init__(self, job_id=None, task_spec=None):
        self.job_id = job_id  # type: str
        self.task_spec = task_spec  # type: list[DeleteJobsRequestJobSpecTaskSpec]

    def validate(self):
        if self.task_spec:
            for k in self.task_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteJobsRequestJobSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['TaskSpec'] = []
        if self.task_spec is not None:
            for k in self.task_spec:
                result['TaskSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.task_spec = []
        if m.get('TaskSpec') is not None:
            for k in m.get('TaskSpec'):
                temp_model = DeleteJobsRequestJobSpecTaskSpec()
                self.task_spec.append(temp_model.from_map(k))
        return self


class DeleteJobsRequest(TeaModel):
    def __init__(self, executor_ids=None, job_spec=None):
        self.executor_ids = executor_ids  # type: list[str]
        self.job_spec = job_spec  # type: list[DeleteJobsRequestJobSpec]

    def validate(self):
        if self.job_spec:
            for k in self.job_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids
        result['JobSpec'] = []
        if self.job_spec is not None:
            for k in self.job_spec:
                result['JobSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids = m.get('ExecutorIds')
        self.job_spec = []
        if m.get('JobSpec') is not None:
            for k in m.get('JobSpec'):
                temp_model = DeleteJobsRequestJobSpec()
                self.job_spec.append(temp_model.from_map(k))
        return self


class DeleteJobsShrinkRequest(TeaModel):
    def __init__(self, executor_ids_shrink=None, job_spec_shrink=None):
        self.executor_ids_shrink = executor_ids_shrink  # type: str
        self.job_spec_shrink = job_spec_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_ids_shrink is not None:
            result['ExecutorIds'] = self.executor_ids_shrink
        if self.job_spec_shrink is not None:
            result['JobSpec'] = self.job_spec_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids_shrink = m.get('ExecutorIds')
        if m.get('JobSpec') is not None:
            self.job_spec_shrink = m.get('JobSpec')
        return self


class DeleteJobsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobsResponseBody, self).to_map()
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


class DeleteJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteJobsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteJobsResponse, self).to_map()
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
            temp_model = DeleteJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobMetricDataRequest(TeaModel):
    def __init__(self, array_index=None, job_id=None, metric_name=None, task_name=None):
        self.array_index = array_index  # type: list[int]
        self.job_id = job_id  # type: str
        self.metric_name = metric_name  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobMetricDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeJobMetricDataShrinkRequest(TeaModel):
    def __init__(self, array_index_shrink=None, job_id=None, metric_name=None, task_name=None):
        self.array_index_shrink = array_index_shrink  # type: str
        self.job_id = job_id  # type: str
        self.metric_name = metric_name  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobMetricDataShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index_shrink is not None:
            result['ArrayIndex'] = self.array_index_shrink
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index_shrink = m.get('ArrayIndex')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeJobMetricDataResponseBody(TeaModel):
    def __init__(self, data_points=None, period=None, request_id=None):
        self.data_points = data_points  # type: str
        self.period = period  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobMetricDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_points is not None:
            result['DataPoints'] = self.data_points
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPoints') is not None:
            self.data_points = m.get('DataPoints')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeJobMetricDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeJobMetricDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeJobMetricDataResponse, self).to_map()
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
            temp_model = DescribeJobMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobMetricLastRequest(TeaModel):
    def __init__(self, array_index=None, job_id=None, task_name=None):
        self.array_index = array_index  # type: list[int]
        self.job_id = job_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobMetricLastRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeJobMetricLastShrinkRequest(TeaModel):
    def __init__(self, array_index_shrink=None, job_id=None, task_name=None):
        self.array_index_shrink = array_index_shrink  # type: str
        self.job_id = job_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobMetricLastShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index_shrink is not None:
            result['ArrayIndex'] = self.array_index_shrink
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index_shrink = m.get('ArrayIndex')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeJobMetricLastResponseBodyMetrics(TeaModel):
    def __init__(self, array_index=None, metric=None):
        self.array_index = array_index  # type: int
        self.metric = metric  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobMetricLastResponseBodyMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.metric is not None:
            result['Metric'] = self.metric
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        return self


class DescribeJobMetricLastResponseBody(TeaModel):
    def __init__(self, metrics=None, request_id=None):
        self.metrics = metrics  # type: list[DescribeJobMetricLastResponseBodyMetrics]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeJobMetricLastResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeJobMetricLastResponseBodyMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeJobMetricLastResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeJobMetricLastResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeJobMetricLastResponse, self).to_map()
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
            temp_model = DescribeJobMetricLastResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(self, image_id=None):
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class GetImageResponseBodyImageContainerImageSpecRegistryCredential(TeaModel):
    def __init__(self, password=None, server=None, user_name=None):
        self.password = password  # type: str
        self.server = server  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyImageContainerImageSpecRegistryCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetImageResponseBodyImageContainerImageSpec(TeaModel):
    def __init__(self, is_acrenterprise=None, is_acrregistry=None, registry_credential=None, registry_cri_id=None,
                 registry_url=None):
        self.is_acrenterprise = is_acrenterprise  # type: bool
        self.is_acrregistry = is_acrregistry  # type: bool
        self.registry_credential = registry_credential  # type: GetImageResponseBodyImageContainerImageSpecRegistryCredential
        self.registry_cri_id = registry_cri_id  # type: str
        self.registry_url = registry_url  # type: str

    def validate(self):
        if self.registry_credential:
            self.registry_credential.validate()

    def to_map(self):
        _map = super(GetImageResponseBodyImageContainerImageSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_acrenterprise is not None:
            result['IsACREnterprise'] = self.is_acrenterprise
        if self.is_acrregistry is not None:
            result['IsACRRegistry'] = self.is_acrregistry
        if self.registry_credential is not None:
            result['RegistryCredential'] = self.registry_credential.to_map()
        if self.registry_cri_id is not None:
            result['RegistryCriId'] = self.registry_cri_id
        if self.registry_url is not None:
            result['RegistryUrl'] = self.registry_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsACREnterprise') is not None:
            self.is_acrenterprise = m.get('IsACREnterprise')
        if m.get('IsACRRegistry') is not None:
            self.is_acrregistry = m.get('IsACRRegistry')
        if m.get('RegistryCredential') is not None:
            temp_model = GetImageResponseBodyImageContainerImageSpecRegistryCredential()
            self.registry_credential = temp_model.from_map(m['RegistryCredential'])
        if m.get('RegistryCriId') is not None:
            self.registry_cri_id = m.get('RegistryCriId')
        if m.get('RegistryUrl') is not None:
            self.registry_url = m.get('RegistryUrl')
        return self


class GetImageResponseBodyImageVMImageSpec(TeaModel):
    def __init__(self, architecture=None, image_id=None, os_tag=None, platform=None):
        self.architecture = architecture  # type: str
        self.image_id = image_id  # type: str
        self.os_tag = os_tag  # type: str
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyImageVMImageSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class GetImageResponseBodyImage(TeaModel):
    def __init__(self, container_image_spec=None, create_time=None, description=None, image_type=None, name=None,
                 size=None, vmimage_spec=None, version=None):
        self.container_image_spec = container_image_spec  # type: GetImageResponseBodyImageContainerImageSpec
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.image_type = image_type  # type: str
        self.name = name  # type: str
        self.size = size  # type: str
        self.vmimage_spec = vmimage_spec  # type: GetImageResponseBodyImageVMImageSpec
        self.version = version  # type: str

    def validate(self):
        if self.container_image_spec:
            self.container_image_spec.validate()
        if self.vmimage_spec:
            self.vmimage_spec.validate()

    def to_map(self):
        _map = super(GetImageResponseBodyImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_image_spec is not None:
            result['ContainerImageSpec'] = self.container_image_spec.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.vmimage_spec is not None:
            result['VMImageSpec'] = self.vmimage_spec.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerImageSpec') is not None:
            temp_model = GetImageResponseBodyImageContainerImageSpec()
            self.container_image_spec = temp_model.from_map(m['ContainerImageSpec'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('VMImageSpec') is not None:
            temp_model = GetImageResponseBodyImageVMImageSpec()
            self.vmimage_spec = temp_model.from_map(m['VMImageSpec'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(self, image=None, request_id=None, success=None, total_count=None):
        self.image = image  # type: GetImageResponseBodyImage
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super(GetImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            temp_model = GetImageResponseBodyImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageResponse, self).to_map()
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
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetJobResponseBodyJobInfoDeploymentPolicyNetwork(TeaModel):
    def __init__(self, vswitch=None):
        self.vswitch = vswitch  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoDeploymentPolicyNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class GetJobResponseBodyJobInfoDeploymentPolicy(TeaModel):
    def __init__(self, allocation_spec=None, network=None):
        self.allocation_spec = allocation_spec  # type: str
        self.network = network  # type: GetJobResponseBodyJobInfoDeploymentPolicyNetwork

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoDeploymentPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')
        if m.get('Network') is not None:
            temp_model = GetJobResponseBodyJobInfoDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec(TeaModel):
    def __init__(self, index_end=None, index_start=None, index_step=None):
        self.index_end = index_end  # type: int
        self.index_start = index_start  # type: int
        self.index_step = index_step  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_end is not None:
            result['IndexEnd'] = self.index_end
        if self.index_start is not None:
            result['IndexStart'] = self.index_start
        if self.index_step is not None:
            result['IndexStep'] = self.index_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IndexEnd') is not None:
            self.index_end = m.get('IndexEnd')
        if m.get('IndexStart') is not None:
            self.index_start = m.get('IndexStart')
        if m.get('IndexStep') is not None:
            self.index_step = m.get('IndexStep')
        return self


class GetJobResponseBodyJobInfoTasksExecutorPolicy(TeaModel):
    def __init__(self, array_spec=None, max_count=None):
        self.array_spec = array_spec  # type: GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec
        self.max_count = max_count  # type: int

    def validate(self):
        if self.array_spec:
            self.array_spec.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasksExecutorPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_spec is not None:
            result['ArraySpec'] = self.array_spec.to_map()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArraySpec') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec()
            self.array_spec = temp_model.from_map(m['ArraySpec'])
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class GetJobResponseBodyJobInfoTasksExecutorStatus(TeaModel):
    def __init__(self, array_id=None, create_time=None, end_time=None, start_time=None, status=None,
                 status_reason=None):
        self.array_id = array_id  # type: int
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.status_reason = status_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasksExecutorStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_id is not None:
            result['ArrayId'] = self.array_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayId') is not None:
            self.array_id = m.get('ArrayId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks(TeaModel):
    def __init__(self, size=None, type=None):
        self.size = size  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecResource(TeaModel):
    def __init__(self, cores=None, disks=None, memory=None):
        self.cores = cores  # type: float
        self.disks = disks  # type: list[GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks]
        self.memory = memory  # type: int

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasksTaskSpecResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cores is not None:
            result['Cores'] = self.cores
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM(TeaModel):
    def __init__(self, image=None, prolog_script=None, script=None):
        self.image = image  # type: str
        self.prolog_script = prolog_script  # type: str
        self.script = script  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.prolog_script is not None:
            result['PrologScript'] = self.prolog_script
        if self.script is not None:
            result['Script'] = self.script
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor(TeaModel):
    def __init__(self, vm=None):
        self.vm = vm  # type: GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM

    def validate(self):
        if self.vm:
            self.vm.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vm is not None:
            result['VM'] = self.vm.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VM') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM()
            self.vm = temp_model.from_map(m['VM'])
        return self


class GetJobResponseBodyJobInfoTasksTaskSpec(TeaModel):
    def __init__(self, resource=None, task_executor=None):
        self.resource = resource  # type: GetJobResponseBodyJobInfoTasksTaskSpecResource
        self.task_executor = task_executor  # type: list[GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor]

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.task_executor:
            for k in self.task_executor:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasksTaskSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        result['TaskExecutor'] = []
        if self.task_executor is not None:
            for k in self.task_executor:
                result['TaskExecutor'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Resource') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksTaskSpecResource()
            self.resource = temp_model.from_map(m['Resource'])
        self.task_executor = []
        if m.get('TaskExecutor') is not None:
            for k in m.get('TaskExecutor'):
                temp_model = GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor()
                self.task_executor.append(temp_model.from_map(k))
        return self


class GetJobResponseBodyJobInfoTasks(TeaModel):
    def __init__(self, executor_policy=None, executor_status=None, task_name=None, task_spec=None,
                 task_sustainable=None):
        self.executor_policy = executor_policy  # type: GetJobResponseBodyJobInfoTasksExecutorPolicy
        self.executor_status = executor_status  # type: list[GetJobResponseBodyJobInfoTasksExecutorStatus]
        self.task_name = task_name  # type: str
        self.task_spec = task_spec  # type: GetJobResponseBodyJobInfoTasksTaskSpec
        self.task_sustainable = task_sustainable  # type: bool

    def validate(self):
        if self.executor_policy:
            self.executor_policy.validate()
        if self.executor_status:
            for k in self.executor_status:
                if k:
                    k.validate()
        if self.task_spec:
            self.task_spec.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfoTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_policy is not None:
            result['ExecutorPolicy'] = self.executor_policy.to_map()
        result['ExecutorStatus'] = []
        if self.executor_status is not None:
            for k in self.executor_status:
                result['ExecutorStatus'].append(k.to_map() if k else None)
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_spec is not None:
            result['TaskSpec'] = self.task_spec.to_map()
        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutorPolicy') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksExecutorPolicy()
            self.executor_policy = temp_model.from_map(m['ExecutorPolicy'])
        self.executor_status = []
        if m.get('ExecutorStatus') is not None:
            for k in m.get('ExecutorStatus'):
                temp_model = GetJobResponseBodyJobInfoTasksExecutorStatus()
                self.executor_status.append(temp_model.from_map(k))
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskSpec') is not None:
            temp_model = GetJobResponseBodyJobInfoTasksTaskSpec()
            self.task_spec = temp_model.from_map(m['TaskSpec'])
        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')
        return self


class GetJobResponseBodyJobInfo(TeaModel):
    def __init__(self, create_time=None, deployment_policy=None, end_time=None, job_description=None, job_id=None,
                 job_name=None, start_time=None, status=None, tasks=None):
        self.create_time = create_time  # type: str
        self.deployment_policy = deployment_policy  # type: GetJobResponseBodyJobInfoDeploymentPolicy
        self.end_time = end_time  # type: str
        self.job_description = job_description  # type: str
        self.job_id = job_id  # type: str
        self.job_name = job_name  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.tasks = tasks  # type: list[GetJobResponseBodyJobInfoTasks]

    def validate(self):
        if self.deployment_policy:
            self.deployment_policy.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetJobResponseBodyJobInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deployment_policy is not None:
            result['DeploymentPolicy'] = self.deployment_policy.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeploymentPolicy') is not None:
            temp_model = GetJobResponseBodyJobInfoDeploymentPolicy()
            self.deployment_policy = temp_model.from_map(m['DeploymentPolicy'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = GetJobResponseBodyJobInfoTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class GetJobResponseBody(TeaModel):
    def __init__(self, job_info=None, request_id=None):
        self.job_info = job_info  # type: GetJobResponseBodyJobInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.job_info:
            self.job_info.validate()

    def to_map(self):
        _map = super(GetJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_info is not None:
            result['JobInfo'] = self.job_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobInfo') is not None:
            temp_model = GetJobResponseBodyJobInfo()
            self.job_info = temp_model.from_map(m['JobInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobResponseBody

    def validate(self):
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


class ListExecutorsRequestFilter(TeaModel):
    def __init__(self, executor_ids=None, ip_addresses=None, job_name=None, time_created_after=None,
                 time_created_before=None):
        self.executor_ids = executor_ids  # type: list[str]
        self.ip_addresses = ip_addresses  # type: list[str]
        self.job_name = job_name  # type: str
        self.time_created_after = time_created_after  # type: int
        self.time_created_before = time_created_before  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutorsRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after
        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids = m.get('ExecutorIds')
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')
        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')
        return self


class ListExecutorsRequest(TeaModel):
    def __init__(self, filter=None, page_number=None, page_size=None):
        self.filter = filter  # type: ListExecutorsRequestFilter
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super(ListExecutorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = ListExecutorsRequestFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListExecutorsShrinkRequest(TeaModel):
    def __init__(self, filter_shrink=None, page_number=None, page_size=None):
        self.filter_shrink = filter_shrink  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutorsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListExecutorsResponseBodyExecutors(TeaModel):
    def __init__(self, array_index=None, create_time=None, end_time=None, executor_id=None, host_name=None,
                 ip_address=None, job_id=None, job_name=None, status=None, status_reason=None, task_name=None):
        self.array_index = array_index  # type: int
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.executor_id = executor_id  # type: str
        self.host_name = host_name  # type: list[str]
        self.ip_address = ip_address  # type: list[str]
        self.job_id = job_id  # type: str
        self.job_name = job_name  # type: str
        self.status = status  # type: str
        self.status_reason = status_reason  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExecutorsResponseBodyExecutors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListExecutorsResponseBody(TeaModel):
    def __init__(self, executors=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.executors = executors  # type: list[ListExecutorsResponseBodyExecutors]
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.executors:
            for k in self.executors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExecutorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executors'] = []
        if self.executors is not None:
            for k in self.executors:
                result['Executors'].append(k.to_map() if k else None)
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
        self.executors = []
        if m.get('Executors') is not None:
            for k in m.get('Executors'):
                temp_model = ListExecutorsResponseBodyExecutors()
                self.executors.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExecutorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExecutorsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExecutorsResponse, self).to_map()
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
            temp_model = ListExecutorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(self, image_ids=None, image_names=None, page_number=None, page_size=None):
        self.image_ids = image_ids  # type: list[str]
        self.image_names = image_names  # type: list[str]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListImagesShrinkRequest(TeaModel):
    def __init__(self, image_ids_shrink=None, image_names_shrink=None, page_number=None, page_size=None):
        self.image_ids_shrink = image_ids_shrink  # type: str
        self.image_names_shrink = image_names_shrink  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids_shrink is not None:
            result['ImageIds'] = self.image_ids_shrink
        if self.image_names_shrink is not None:
            result['ImageNames'] = self.image_names_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids_shrink = m.get('ImageIds')
        if m.get('ImageNames') is not None:
            self.image_names_shrink = m.get('ImageNames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(self, create_time=None, description=None, image_id=None, image_type=None, name=None, version=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.image_id = image_id  # type: str
        self.image_type = image_type  # type: str
        self.name = name  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(self, images=None, page_number=None, page_size=None, request_id=None, success=None,
                 total_count=None):
        self.images = images  # type: list[ListImagesResponseBodyImages]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListImagesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListImagesResponse, self).to_map()
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobExecutorsRequest(TeaModel):
    def __init__(self, job_id=None, page_number=None, page_size=None, task_name=None):
        self.job_id = job_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobExecutorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListJobExecutorsResponseBodyExecutors(TeaModel):
    def __init__(self, array_index=None, create_time=None, end_time=None, host_name=None, ip_address=None,
                 status=None, status_reason=None):
        self.array_index = array_index  # type: int
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.host_name = host_name  # type: list[str]
        self.ip_address = ip_address  # type: list[str]
        self.status = status  # type: str
        self.status_reason = status_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobExecutorsResponseBodyExecutors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class ListJobExecutorsResponseBody(TeaModel):
    def __init__(self, executors=None, job_id=None, page_number=None, page_size=None, request_id=None,
                 task_name=None, total_count=None):
        self.executors = executors  # type: list[ListJobExecutorsResponseBodyExecutors]
        self.job_id = job_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.request_id = request_id  # type: str
        self.task_name = task_name  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.executors:
            for k in self.executors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobExecutorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executors'] = []
        if self.executors is not None:
            for k in self.executors:
                result['Executors'].append(k.to_map() if k else None)
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.executors = []
        if m.get('Executors') is not None:
            for k in m.get('Executors'):
                temp_model = ListJobExecutorsResponseBodyExecutors()
                self.executors.append(temp_model.from_map(k))
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobExecutorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobExecutorsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobExecutorsResponse, self).to_map()
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
            temp_model = ListJobExecutorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequestFilter(TeaModel):
    def __init__(self, job_id=None, job_name=None, status=None, time_created_after=None, time_created_before=None):
        self.job_id = job_id  # type: str
        self.job_name = job_name  # type: str
        self.status = status  # type: str
        self.time_created_after = time_created_after  # type: int
        self.time_created_before = time_created_before  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.status is not None:
            result['Status'] = self.status
        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after
        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')
        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')
        return self


class ListJobsRequestSortBy(TeaModel):
    def __init__(self, label=None, order=None):
        self.label = label  # type: str
        self.order = order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequestSortBy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, filter=None, page_number=None, page_size=None, sort_by=None):
        self.filter = filter  # type: ListJobsRequestFilter
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.sort_by = sort_by  # type: ListJobsRequestSortBy

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.sort_by:
            self.sort_by.validate()

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = ListJobsRequestFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            temp_model = ListJobsRequestSortBy()
            self.sort_by = temp_model.from_map(m['SortBy'])
        return self


class ListJobsShrinkRequest(TeaModel):
    def __init__(self, filter_shrink=None, page_number=None, page_size=None, sort_by_shrink=None):
        self.filter_shrink = filter_shrink  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.sort_by_shrink = sort_by_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by_shrink is not None:
            result['SortBy'] = self.sort_by_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by_shrink = m.get('SortBy')
        return self


class ListJobsResponseBodyJobList(TeaModel):
    def __init__(self, create_time=None, end_time=None, executor_count=None, job_description=None, job_id=None,
                 job_name=None, owner_uid=None, start_time=None, status=None, task_count=None, task_sustainable=None):
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.executor_count = executor_count  # type: int
        self.job_description = job_description  # type: str
        self.job_id = job_id  # type: str
        self.job_name = job_name  # type: str
        self.owner_uid = owner_uid  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_count = task_count  # type: int
        self.task_sustainable = task_sustainable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.job_description is not None:
            result['JobDescription'] = self.job_description
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, job_list=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.job_list = job_list  # type: list[ListJobsResponseBodyJobList]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
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
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = ListJobsResponseBodyJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
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


class RemoveImageRequest(TeaModel):
    def __init__(self, image_id=None):
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class RemoveImageResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveImageResponse, self).to_map()
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
            temp_model = RemoveImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


