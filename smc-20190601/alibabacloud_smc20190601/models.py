# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateAccessTokenRequest(TeaModel):
    def __init__(self, count=None, description=None, name=None, owner_id=None, resource_owner_account=None,
                 time_to_live_in_days=None):
        # The maximum number of times that the activation code can be used to import the information of migration sources. Valid values: 1 to 1000.
        # 
        # Default value: 100.
        self.count = count  # type: str
        # The description of the activation code.
        self.description = description  # type: str
        # The name of the activation code. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain digits, colons (:), underscores (\_), and hyphens (-).
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        # The validity period of the activation code. The activation code can no longer be used to import the information of migration sources after the code expires. Unit: day. Valid values: 1 to 90.
        # 
        # Default value: 30.
        self.time_to_live_in_days = time_to_live_in_days  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.time_to_live_in_days is not None:
            result['TimeToLiveInDays'] = self.time_to_live_in_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TimeToLiveInDays') is not None:
            self.time_to_live_in_days = m.get('TimeToLiveInDays')
        return self


class CreateAccessTokenResponseBody(TeaModel):
    def __init__(self, access_token_code=None, access_token_id=None, request_id=None):
        # The value of the activation code. The value is returned only once after the CreateAccessToken operation is called and cannot be subsequently queried. Make sure that you properly save the returned value.
        self.access_token_code = access_token_code  # type: str
        # The ID of the activation code.
        self.access_token_id = access_token_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_code is not None:
            result['AccessTokenCode'] = self.access_token_code
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenCode') is not None:
            self.access_token_code = m.get('AccessTokenCode')
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccessTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccessTokenResponse, self).to_map()
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
            temp_model = CreateAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReplicationJobRequestDataDiskPart(TeaModel):
    def __init__(self, block=None, device=None, size_bytes=None):
        # Specifies whether to enable block replication for partition N in the destination data disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true
        self.block = block  # type: bool
        # The device ID of partition N in the destination data disk. The partitions in the destination data disk are arranged in the same sequential order as those in the source data disk.
        # 
        # >  You must set both the DataDisk.N.Part.N.Device and `DataDisk.N.Part.N.SizeBytes` parameters or leave both parameters empty.
        self.device = device  # type: str
        # The size of partition N in the destination data disk. Unit: bytes. The default value is equal to the corresponding partition size of the source data disk.
        # 
        # > 
        # 
        # *   The total size of all partitions in a destination data disk cannot exceed the size of the destination data disk.
        # 
        # *   You must set both the `DataDisk.N.Part.N.Device` and DataDisk.N.Part.N.SizeBytes parameters or leave both parameters empty.
        self.size_bytes = size_bytes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReplicationJobRequestDataDiskPart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class CreateReplicationJobRequestDataDisk(TeaModel):
    def __init__(self, index=None, part=None, size=None):
        # The index of data disk N on the destination ECS instance. Data disks on a destination ECS instance are arranged in a sequential order that starts from 1. Valid values: 1 to 16.
        # 
        # >  To create a destination data disk for a source server, make sure that the source server has data disks.
        self.index = index  # type: int
        # The data disk partitions.
        self.part = part  # type: list[CreateReplicationJobRequestDataDiskPart]
        # The size of the data disk on the destination ECS instance. Unit: GiB. Valid values: 20 to 32768.
        # 
        # >  The size of a destination data disk must be larger than the size of data in the source data disk. For example, if the size of the source data disk is 500 GiB and the used space is 100 GiB, you must set this parameter to a value greater than 100.
        self.size = size  # type: int

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateReplicationJobRequestDataDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = CreateReplicationJobRequestDataDiskPart()
                self.part.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateReplicationJobRequestSystemDiskPart(TeaModel):
    def __init__(self, block=None, device=None, size_bytes=None):
        # Specifies whether to enable block replication for partition N in the destination system disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true
        self.block = block  # type: bool
        # The ID of partition N in the destination system disk. The partitions in the destination system disk are arranged in the same sequential order as those in the source system disk.
        # 
        # >  You must set both the SystemDiskPart.N.Device and `SystemDiskPart.N.SizeBytes` parameters or leave both parameters empty.
        self.device = device  # type: str
        # The size of the partition N in the destination system disk. Unit: bytes. The default value is equal to the partition size of the source system disk.
        # 
        # > 
        # 
        # *   The total size of all partitions in the destination system disk cannot exceed the size of the destination system disk.
        # 
        # *   You must set both the `SystemDiskPart.N.Device` and SystemDiskPart.N.SizeBytes parameters or leave both parameters empty.
        self.size_bytes = size_bytes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReplicationJobRequestSystemDiskPart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class CreateReplicationJobRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag for the migration job. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.key = key  # type: str
        # The value of the tag for the migration job. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReplicationJobRequestTag, self).to_map()
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


class CreateReplicationJobRequest(TeaModel):
    def __init__(self, client_token=None, container_namespace=None, container_repository=None, container_tag=None,
                 data_disk=None, description=None, frequency=None, image_name=None, instance_id=None, instance_ram_role=None,
                 instance_type=None, job_type=None, launch_template_id=None, launch_template_version=None, license_type=None,
                 max_number_of_image_to_keep=None, name=None, net_mode=None, owner_id=None, region_id=None, replication_parameters=None,
                 resource_group_id=None, resource_owner_account=None, run_once=None, scheduled_start_time=None, source_id=None,
                 system_disk_part=None, system_disk_size=None, tag=None, target_type=None, v_switch_id=None, valid_time=None,
                 vpc_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The namespace of the destination Docker container image. For more information about Docker container images, see [Terms](~~60744~~).
        self.container_namespace = container_namespace  # type: str
        # The repository that stores the destination Docker container image. For more information about Docker container images, see [Terms](~~60744~~).
        self.container_repository = container_repository  # type: str
        # The tag of the destination Docker container image. For more information about Docker container images, see [Terms](~~60744~~).
        self.container_tag = container_tag  # type: str
        # The data disks.
        self.data_disk = data_disk  # type: list[CreateReplicationJobRequestDataDisk]
        # The description of the migration job.
        # 
        # The description must be 2 to 128 characters in length, and can contain digits, colons (:), underscores (\_), and hyphens (-). The description must start with a letter, but cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # The interval at which SMC synchronizes incremental data to Alibaba Cloud. Unit: hour. Valid values: 1 to 168.
        # 
        # This parameter is required if you set the `RunOnce` parameter to false.
        # 
        # By default, this parameter is empty.
        self.frequency = frequency  # type: int
        # The name of the destination image. The name must meet the following requirements:
        # 
        # *   The name must be unique within an Alibaba Cloud region.
        # *   The name must be 2 to 128 characters in length, and can contain digits, colons (:), underscores (\_), and hyphens (-). The name must start with a letter, but cannot start with `http://` or `https://`.
        # 
        # >  If you specify an image name that already exists in the destination region, the migration job ID is appended to the image name as a suffix. Example: ImageName_j-2zexxxxxxxxxxxxx.
        self.image_name = image_name  # type: str
        # The ID of the destination ECS instance.
        self.instance_id = instance_id  # type: str
        # The name of the Resource Access Management (RAM) role that is assigned to the instance.
        self.instance_ram_role = instance_ram_role  # type: str
        # The type of the intermediate instance.
        # 
        # You can call the [DescribeInstanceTypes](~~25620~~) operation to query the ECS instance types.
        # 
        # *   If you specify this parameter, SMC creates an intermediate instance of the specified instance type. If the specified instance type is unavailable, the migration job fails to be created.
        # *   If you do not specify this parameter, SMC selects an available instance type in a specific order to create an intermediate instance. For more information, see the "How does SMC create an intermediate instance?" section of the SMC FAQ topic.
        self.instance_type = instance_type  # type: str
        # The type of the migration job. Valid values:
        # 
        # *   0: server migration.
        # *   1: operating system migration.
        # *   2: cross-zone migration.
        # *   3: agentless migration for a VMware VM.
        self.job_type = job_type  # type: int
        # The ID of the launch template.
        self.launch_template_id = launch_template_id  # type: str
        # The version number of the launch template.
        self.launch_template_version = launch_template_version  # type: str
        # The license type. Valid values:
        # 
        # *   An empty value specifies no license.
        # *   A value of BYOL specifies Bring Your Own License (BYOL).
        # 
        # For more information, see [SMC FAQ](~~121707~~).
        self.license_type = license_type  # type: str
        # The maximum number of images retained for the incremental migration job. Valid values: 1 to 10.
        # 
        # This parameter is required if you set the `RunOnce` parameter to false.
        # 
        # By default, this parameter is empty.
        self.max_number_of_image_to_keep = max_number_of_image_to_keep  # type: int
        # The name of the migration job. The name must meet the following requirements:
        # 
        # *   The name must be unique.
        # *   The name must be 2 to 128 characters in length, and can contain digits, colons (:), underscores (\_), and hyphens (-). The name must start with a letter, but cannot start with `http://` or `https://`.
        self.name = name  # type: str
        # The network mode for data transmission. Valid values:
        # 
        # *   0: Data is transmitted over the Internet. Make sure that the source server can access the Internet.
        # *   2: Data is transmitted over a VPC. If you specify this value, you must specify the VSwitchId parameter. You do not need to specify the VpcId parameter because the value of the VpcId parameter can be retrieved based on the value of the VSwitchId parameter.
        # 
        # Default value: 0
        self.net_mode = net_mode  # type: int
        self.owner_id = owner_id  # type: long
        # The ID of the Alibaba Cloud region to which you want to migrate the source server.
        # 
        # For example, if you want to migrate the source server to the China (Hangzhou) region, set this parameter to `cn-hangzhou`. You can call the [DescribeRegions](~~25609~~) operation to query the latest regions.
        self.region_id = region_id  # type: str
        # The parameters of the replication driver. The parameters must be specified as key-value pairs in the JSON format. The keys are fixed for each type of replication driver. The JSON string can be up to 2,048 characters in length.
        # 
        # A replication driver is a tool that is used to migrate a source server to an intermediate instance. The parameters vary based on the replication driver type. If you use a Server Migration Tool (SMT) driver, you can specify the following parameters:
        # 
        # *   bandwidth_limit: the maximum bandwidth for data transmission.
        # *   compress_level: the compression ratio of data to be transmitted.
        # *   checksum: specifies whether to enable checksum verification.
        # 
        # For more information about replication drivers, see the response parameter `SourceServers.ReplicationDriver` of the [DescribeSourceServers](~~121818~~) operation.
        self.replication_parameters = replication_parameters  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # Specifies whether to disable incremental migration for the source server. Valid values:
        # 
        # *   true: creates a migration job that runs only once. This is the default value. Incremental data of the source server is not synchronized.
        # *   false: creates an incremental migration job. In this case, you must specify the `Frequency` parameter. SMC synchronizes incremental data of the source server to Alibaba Cloud at the specified frequency. You can use an incremental migration job to synchronize incremental data from the source server to Alibaba Cloud without the need to interrupt your business. A full data image is generated for the source server when the job is running.
        # 
        # >  You can specify this parameter only when you create a migration job. The parameter value cannot be changed after the migration job is created.
        self.run_once = run_once  # type: bool
        # The time when you want to run the migration job. The time must meet the following requirements:
        # 
        # *   The time must be specified in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. For example, 2018-01-01T12:00:00Z specifies 20:00:00 on January 1, 2018 (UTC+8).
        # *   The value must be within 30 days after the current time.
        # 
        # >  If you do not specify this parameter, you must manually start the migration job after the job is created. You can call the [StartReplicationJob](~~121823~~) operation to start the migration job.
        self.scheduled_start_time = scheduled_start_time  # type: str
        # The ID of the source server.
        self.source_id = source_id  # type: str
        # The information about system disk partitions.
        self.system_disk_part = system_disk_part  # type: list[CreateReplicationJobRequestSystemDiskPart]
        # The system disk size of the destination ECS instance. Unit: GiB. Valid values: 20 to 2048.
        # 
        # >  The value must be greater than the used space of the system disk on the source server. For example, if the total size of the source disk is 500 GiB and the used space is 100 GiB, the value of this parameter must be greater than 100 GiB.
        self.system_disk_size = system_disk_size  # type: int
        # The tags.
        self.tag = tag  # type: list[CreateReplicationJobRequestTag]
        # The type of destination to which you want to migrate the source server. Valid values:
        # 
        # *   Image: After the migration job is complete, SMC generates an Elastic Compute Service (ECS) image for the source server.
        # *   ContainerImage: After the migration job is complete, SMC generates a Docker container image for the source server.
        # *   TargetInstance: After the migration job is completed, SMC migrates the source server to the destination instance. If you set this parameter to TargetInstance, you must set the `InstanceId` parameter.
        self.target_type = target_type  # type: str
        # The ID of the vSwitch in the specified VPC.
        # 
        # You must set this parameter if you use a VPC to migrate data.
        self.v_switch_id = v_switch_id  # type: str
        # The time when the migration job expires. You can schedule the migration job to expire 7 to 90 days after the job is created.
        # 
        # *   The time must be specified in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. For example, 2018-01-01T12:00:00Z specifies 20:00:00 on January 1, 2018 (UTC+8).
        # *   If you do not specify this parameter, the migration job does not expire.
        # *   After a migration job expires, the job state changes to Expired. SMC retains the migration job for seven days after the job expires. After the job is retained for seven days, SMC deletes the migration job.
        # 
        # By default, a migration job is valid for 30 days after it is created.
        self.valid_time = valid_time  # type: str
        # The ID of a VPC for which you have configured an Express Connect circuit or a VPN gateway.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateReplicationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.name is not None:
            result['Name'] = self.name
        if self.net_mode is not None:
            result['NetMode'] = self.net_mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replication_parameters is not None:
            result['ReplicationParameters'] = self.replication_parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.run_once is not None:
            result['RunOnce'] = self.run_once
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = CreateReplicationJobRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetMode') is not None:
            self.net_mode = m.get('NetMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicationParameters') is not None:
            self.replication_parameters = m.get('ReplicationParameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RunOnce') is not None:
            self.run_once = m.get('RunOnce')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = CreateReplicationJobRequestSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateReplicationJobRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateReplicationJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the migration job.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReplicationJobResponseBody, self).to_map()
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


class CreateReplicationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateReplicationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateReplicationJobResponse, self).to_map()
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
            temp_model = CreateReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CutOverReplicationJobRequest(TeaModel):
    def __init__(self, job_id=None, owner_id=None, resource_owner_account=None, sync_data=None):
        # The ID of the incremental migration job.
        self.job_id = job_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        # Specifies whether to migrate full data for the last time. Valid Values:
        # 
        # *   true: migrates full data for the last time.
        # *   false: does not migrate full data for the last time.
        # 
        # Default value: false.
        self.sync_data = sync_data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CutOverReplicationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.sync_data is not None:
            result['SyncData'] = self.sync_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SyncData') is not None:
            self.sync_data = m.get('SyncData')
        return self


class CutOverReplicationJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CutOverReplicationJobResponseBody, self).to_map()
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


class CutOverReplicationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CutOverReplicationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CutOverReplicationJobResponse, self).to_map()
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
            temp_model = CutOverReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessTokenRequest(TeaModel):
    def __init__(self, access_token_id=None, owner_id=None, resource_owner_account=None):
        # The ID of the activation code.
        self.access_token_id = access_token_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DeleteAccessTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessTokenResponseBody, self).to_map()
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


class DeleteAccessTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccessTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccessTokenResponse, self).to_map()
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
            temp_model = DeleteAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReplicationJobRequest(TeaModel):
    def __init__(self, job_id=None, owner_id=None, resource_owner_account=None):
        # The migration job ID.
        self.job_id = job_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReplicationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DeleteReplicationJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReplicationJobResponseBody, self).to_map()
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


class DeleteReplicationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteReplicationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteReplicationJobResponse, self).to_map()
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
            temp_model = DeleteReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSourceServerRequest(TeaModel):
    def __init__(self, force=None, owner_id=None, resource_owner_account=None, source_id=None):
        # Specifies whether to forcibly delete the migration source. Valid values:
        # 
        # *   true: forcibly deletes the migration source and the migration job created for the migration source, and releases the intermediate resources of the migration job.
        # *   false: does not delete the migration source if a migration job is created for the migration source.
        self.force = force  # type: bool
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        # The migration source ID.
        self.source_id = source_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSourceServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class DeleteSourceServerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSourceServerResponseBody, self).to_map()
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


class DeleteSourceServerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSourceServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSourceServerResponse, self).to_map()
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
            temp_model = DeleteSourceServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeReplicationJobsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag key can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.
        self.key = key  # type: str
        # The value of tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.[](http://https://。)
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicationJobsRequestTag, self).to_map()
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


class DescribeReplicationJobsRequest(TeaModel):
    def __init__(self, business_status=None, instance_id=None, job_id=None, job_type=None, name=None, owner_id=None,
                 page_number=None, page_size=None, region_id=None, resource_group_id=None, resource_owner_account=None,
                 source_id=None, status=None, tag=None):
        # The business status of the migration job. Valid values:
        # 
        # *   Preparing: The migration is being prepared.
        # *   Syncing: Data is being synchronized.
        # *   Processing: The migration is in progress.
        # *   Cleaning: Intermediate resources are being released.
        self.business_status = business_status  # type: str
        # The IDs of the destination Elastic Compute Service (ECS) instances.
        self.instance_id = instance_id  # type: list[str]
        # The IDs of the migration jobs. You can specify a maximum of 50 IDs.
        self.job_id = job_id  # type: list[str]
        # The type of the migration job. Valid values:
        # 
        # *   0: server migration.
        # *   1: operating system migration.
        # *   2: cross-zone migration.
        # *   3: agentless migration for a VMware VM.
        self.job_type = job_type  # type: int
        # The name of the migration job.
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the Alibaba Cloud region to which you want to migrate the source server.
        # 
        # For example, if you want to migrate a source server to the China (Hangzhou) region, set this parameter to `cn-hangzhou`. You can call the [DescribeRegions](~~25609~~) operation to query the latest regions.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The IDs of the source servers. You can specify a maximum of 50 IDs.
        self.source_id = source_id  # type: list[str]
        # The status of the migration job. Valid values:
        # 
        # *   Ready: The migration job is not started.
        # *   Running: The migration job is running.
        # *   Stopped: The migration job is paused.
        # *   InError: An error occurs in the migration job.
        # *   Finished: The migration job is complete.
        # *   Waiting: The migration job is waiting to run.
        # *   Expired: The migration job has expired.
        # *   Deleting: The migration job is being deleted.
        self.status = status  # type: str
        # The information about tags that are attached to the SMC resource.
        self.tag = tag  # type: list[DescribeReplicationJobsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeReplicationJobsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart(TeaModel):
    def __init__(self, block=None, device=None, size_bytes=None):
        # Indicates whether block replication is enabled for the data disk partition.
        self.block = block  # type: bool
        # The device ID of the data disk partition.
        self.device = device  # type: str
        # The size of the data disk partition. Unit: bytes.
        self.size_bytes = size_bytes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts(TeaModel):
    def __init__(self, part=None):
        self.part = part  # type: list[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart]

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk(TeaModel):
    def __init__(self, index=None, parts=None, size=None):
        # The index number of the data disk.
        self.index = index  # type: int
        # The data disk partitions.
        self.parts = parts  # type: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts
        # The size of the data disk. Unit: GiB.
        self.size = size  # type: int

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Parts') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks(TeaModel):
    def __init__(self, data_disk=None):
        self.data_disk = data_disk  # type: list[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk]

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun(TeaModel):
    def __init__(self, end_time=None, image_id=None, start_time=None, type=None):
        # The time when the migration job ended. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.end_time = end_time  # type: str
        # The ID of the destination image.
        self.image_id = image_id  # type: str
        # The time when the migration job was started. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.start_time = start_time  # type: str
        # The method used to run the migration job. Valid values:
        # 
        # *   Manual: The migration job was manually started.
        # *   Schedule: The migration job was started at a scheduled time or at a specific interval.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns(TeaModel):
    def __init__(self, replication_job_run=None):
        self.replication_job_run = replication_job_run  # type: list[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun]

    def validate(self):
        if self.replication_job_run:
            for k in self.replication_job_run:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReplicationJobRun'] = []
        if self.replication_job_run is not None:
            for k in self.replication_job_run:
                result['ReplicationJobRun'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.replication_job_run = []
        if m.get('ReplicationJobRun') is not None:
            for k in m.get('ReplicationJobRun'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun()
                self.replication_job_run.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart(TeaModel):
    def __init__(self, block=None, device=None, size_bytes=None):
        # Indicates whether block replication is enabled for the system disk partition.
        self.block = block  # type: bool
        # The device ID of the system disk partition.
        self.device = device  # type: str
        # The size of the system disk partition. Unit: bytes.
        self.size_bytes = size_bytes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts(TeaModel):
    def __init__(self, system_disk_part=None):
        self.system_disk_part = system_disk_part  # type: list[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart]

    def validate(self):
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag key can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.[](http://https://。)
        self.key = key  # type: str
        # The value of tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.[](http://https://。)
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTagsTag, self).to_map()
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


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob(TeaModel):
    def __init__(self, business_status=None, container_namespace=None, container_repository=None,
                 container_tag=None, creation_time=None, data_disks=None, description=None, end_time=None, error_code=None,
                 frequency=None, image_id=None, image_name=None, instance_id=None, instance_ram_role=None, instance_type=None,
                 job_id=None, job_type=None, launch_template_id=None, launch_template_version=None, license_type=None,
                 max_number_of_image_to_keep=None, name=None, net_mode=None, progress=None, region_id=None, replication_job_runs=None,
                 replication_parameters=None, resource_group_id=None, run_once=None, scheduled_start_time=None, source_id=None,
                 start_time=None, status=None, status_info=None, system_disk_parts=None, system_disk_size=None, tags=None,
                 target_type=None, transition_instance_id=None, v_switch_id=None, valid_time=None, vpc_id=None):
        # The business status of the migration job. Valid values:
        # 
        # *   Preparing: The migration is being prepared.
        # *   Syncing: Data is being synchronized.
        # *   Processing: The migration is in progress.
        # *   Cleaning: Intermediate resources are being released.
        self.business_status = business_status  # type: str
        # The namespace of the destination Docker container image.
        self.container_namespace = container_namespace  # type: str
        # The repository that stores the destination Docker container image.
        self.container_repository = container_repository  # type: str
        # The tag of the destination Docker container image.
        self.container_tag = container_tag  # type: str
        # The time when the migration job was created.
        self.creation_time = creation_time  # type: str
        # The data disks on the destination ECS instance.
        self.data_disks = data_disks  # type: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks
        # The description of the migration job.
        self.description = description  # type: str
        # The time when the migration job was complete. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.end_time = end_time  # type: str
        # The error code returned if an error occurred in the migration job.
        self.error_code = error_code  # type: str
        # The interval at which the incremental migration job runs. Unit: hour. Valid values: 1 to 168.
        self.frequency = frequency  # type: int
        # The ID of the destination image.
        self.image_id = image_id  # type: str
        # The name of the destination image.
        self.image_name = image_name  # type: str
        # The ID of the destination ECS instance.
        self.instance_id = instance_id  # type: str
        # The name of the Resource Access Management (RAM) role that is assigned to the instance.
        self.instance_ram_role = instance_ram_role  # type: str
        # The instance type of the intermediate instance.
        self.instance_type = instance_type  # type: str
        # The ID of the migration job.
        self.job_id = job_id  # type: str
        # The type of the migration job. Valid values:
        # 
        # *   0: server migration.
        # *   1: operating system migration.
        # *   2: cross-zone migration.
        # *   3: agentless migration for a VMware VM.
        self.job_type = job_type  # type: int
        # The ID of the launch template.
        self.launch_template_id = launch_template_id  # type: str
        # The versions of the launch template.
        self.launch_template_version = launch_template_version  # type: str
        # The type of license for the migration job. Valid values:
        # 
        # *   An empty value indicates no license.
        # *   A value of BYOL indicates Bring Your Own License (BYOL).
        self.license_type = license_type  # type: str
        # The maximum number of images retained for the incremental migration job. Valid values: 1 to 10.
        self.max_number_of_image_to_keep = max_number_of_image_to_keep  # type: int
        # The name of the migration job.
        self.name = name  # type: str
        # The type of network used for the migration.
        self.net_mode = net_mode  # type: int
        # The progress of the migration job.
        self.progress = progress  # type: float
        # The ID of the Alibaba Cloud region to which the source server is migrated.
        self.region_id = region_id  # type: str
        # The execution records of the migration job.
        self.replication_job_runs = replication_job_runs  # type: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns
        # The string of key-value pairs configured for the replication driver.
        self.replication_parameters = replication_parameters  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # Indicates whether incremental migration is disabled for the source server. Valid values:
        # 
        # *   true: Incremental migration is disabled. A migration job runs only once after the job is created.
        # *   false: Incremental migration is enabled. For an incremental migration job, SMC synchronizes incremental data to Alibaba Cloud at the interval specified by the `Frequency` parameter.
        self.run_once = run_once  # type: bool
        # The time when the migration job is scheduled to run. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. The time must meet the following requirements:
        # 
        # *   The value must be within 30 days after the current time.
        # *   If you do not specify this parameter, you must manually start the migration job after the migration job is created. You can call the [StartReplicationJob](~~121823~~) operation to start the migration job.
        self.scheduled_start_time = scheduled_start_time  # type: str
        # The ID of the source server.
        self.source_id = source_id  # type: str
        # The time when the migration job was started. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.start_time = start_time  # type: str
        # The status of the migration job. Valid values:
        # 
        # *   Ready: The migration job is not started.
        # *   Running: The migration job is running.
        # *   Stopped: The migration job is paused.
        # *   InError: An error occurs in the migration job.
        # *   Finished: The migration job is complete.
        # *   Waiting: The migration job is waiting to run.
        # *   Expired: The migration job has expired.
        # *   Deleting: The migration job is being deleted.
        self.status = status  # type: str
        # The status information about the migration job.
        self.status_info = status_info  # type: str
        # The system disk partitions.
        self.system_disk_parts = system_disk_parts  # type: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts
        # The size of the system disk of the destination ECS instance.
        self.system_disk_size = system_disk_size  # type: int
        # The information about tags that are attached to the SMC resource.
        self.tags = tags  # type: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTags
        # The type of destination to which the source server is migrated. Valid values:
        # 
        # *   Image: After the migration job is complete, SMC generates an ECS image for the source server.
        # *   ContainerImage: After the migration job is complete, SMC generates a Docker container image for the source server.
        # *   TargetInstance: After the migration job is complete, SMC migrates the source server to the destination instance. If you set this parameter to TargetInstance, you must set the InstanceId parameter.
        self.target_type = target_type  # type: str
        # The ID of the intermediate instance.
        self.transition_instance_id = transition_instance_id  # type: str
        # The ID of the vSwitch in the specified VPC.
        self.v_switch_id = v_switch_id  # type: str
        # The time when the migration job expired. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.valid_time = valid_time  # type: str
        # The ID of a virtual private cloud (VPC) for which you have configured an Express Connect circuit or a VPN gateway.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()
        if self.replication_job_runs:
            self.replication_job_runs.validate()
        if self.system_disk_parts:
            self.system_disk_parts.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.name is not None:
            result['Name'] = self.name
        if self.net_mode is not None:
            result['NetMode'] = self.net_mode
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replication_job_runs is not None:
            result['ReplicationJobRuns'] = self.replication_job_runs.to_map()
        if self.replication_parameters is not None:
            result['ReplicationParameters'] = self.replication_parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.run_once is not None:
            result['RunOnce'] = self.run_once
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_info is not None:
            result['StatusInfo'] = self.status_info
        if self.system_disk_parts is not None:
            result['SystemDiskParts'] = self.system_disk_parts.to_map()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.transition_instance_id is not None:
            result['TransitionInstanceId'] = self.transition_instance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataDisks') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetMode') is not None:
            self.net_mode = m.get('NetMode')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicationJobRuns') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns()
            self.replication_job_runs = temp_model.from_map(m['ReplicationJobRuns'])
        if m.get('ReplicationParameters') is not None:
            self.replication_parameters = m.get('ReplicationParameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RunOnce') is not None:
            self.run_once = m.get('RunOnce')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusInfo') is not None:
            self.status_info = m.get('StatusInfo')
        if m.get('SystemDiskParts') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts()
            self.system_disk_parts = temp_model.from_map(m['SystemDiskParts'])
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Tags') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TransitionInstanceId') is not None:
            self.transition_instance_id = m.get('TransitionInstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobs(TeaModel):
    def __init__(self, replication_job=None):
        self.replication_job = replication_job  # type: list[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob]

    def validate(self):
        if self.replication_job:
            for k in self.replication_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBodyReplicationJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReplicationJob'] = []
        if self.replication_job is not None:
            for k in self.replication_job:
                result['ReplicationJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.replication_job = []
        if m.get('ReplicationJob') is not None:
            for k in m.get('ReplicationJob'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob()
                self.replication_job.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, replication_jobs=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page.
        self.page_size = page_size  # type: int
        # The details of migration jobs.
        self.replication_jobs = replication_jobs  # type: DescribeReplicationJobsResponseBodyReplicationJobs
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of migration jobs returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.replication_jobs:
            self.replication_jobs.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.replication_jobs is not None:
            result['ReplicationJobs'] = self.replication_jobs.to_map()
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
        if m.get('ReplicationJobs') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobs()
            self.replication_jobs = temp_model.from_map(m['ReplicationJobs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeReplicationJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeReplicationJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeReplicationJobsResponse, self).to_map()
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
            temp_model = DescribeReplicationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSourceServersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. It can be up to 64 characters in length and cannot start with acs: or aliyun. It cannot contain http:// or https://.
        self.key = key  # type: str
        # The value of tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSourceServersRequestTag, self).to_map()
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


class DescribeSourceServersRequest(TeaModel):
    def __init__(self, job_id=None, name=None, owner_id=None, page_number=None, page_size=None,
                 resource_group_id=None, resource_owner_account=None, source_id=None, state=None, tag=None):
        # The migration job ID.
        self.job_id = job_id  # type: str
        # The name of the migration source. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain digits, colons (:), underscores (\_), and hyphens (-).
        # 
        # Default value: null.
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        # The page number. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The migration source IDs. You can specify multiple IDs.
        self.source_id = source_id  # type: list[str]
        # The state of the migration source. Valid Values:
        # 
        # *   Unavailable: The migration source is inactive, or an error occurs in the migration source.
        # *   Available: The migration source is active.
        # *   InUse: The migration source is being migrated.
        # *   Deleting: The migration source is being deleted from Server Migration Center (SMC).
        self.state = state  # type: str
        # The tag.
        self.tag = tag  # type: list[DescribeSourceServersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSourceServersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.state is not None:
            result['State'] = self.state
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSourceServersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart(TeaModel):
    def __init__(self, can_block=None, device=None, need=None, path=None, size_bytes=None):
        # Indicates whether block replication is enabled for the data disk partition.
        self.can_block = can_block  # type: bool
        # The device ID of the data disk partition.
        self.device = device  # type: str
        # Indicates whether the data disk partition must be selected.
        self.need = need  # type: bool
        # The path of the data disk partition.
        self.path = path  # type: str
        # The size of the data disk partition. Unit: byte.
        self.size_bytes = size_bytes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_block is not None:
            result['CanBlock'] = self.can_block
        if self.device is not None:
            result['Device'] = self.device
        if self.need is not None:
            result['Need'] = self.need
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanBlock') is not None:
            self.can_block = m.get('CanBlock')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Need') is not None:
            self.need = m.get('Need')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts(TeaModel):
    def __init__(self, part=None):
        self.part = part  # type: list[DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart]

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk(TeaModel):
    def __init__(self, index=None, parts=None, path=None, size=None):
        # The index number of the data disk.
        self.index = index  # type: int
        # The information about the data disk partition.
        self.parts = parts  # type: DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts
        # The path of the data disk.
        self.path = path  # type: str
        # The size of the data disk. Unit: GiB.
        self.size = size  # type: int

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Parts') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisks(TeaModel):
    def __init__(self, data_disk=None):
        self.data_disk = data_disk  # type: list[DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk]

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServerDataDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart(TeaModel):
    def __init__(self, can_block=None, device=None, need=None, path=None, size_bytes=None):
        # Indicates whether block replication is enabled for the system disk partition.
        self.can_block = can_block  # type: bool
        # The device ID of the system disk partition.
        self.device = device  # type: str
        # Indicates whether the system disk partition must be selected.
        self.need = need  # type: bool
        # The path of the system disk partition.
        self.path = path  # type: str
        # The size of the system disk partition. Unit: byte.
        self.size_bytes = size_bytes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_block is not None:
            result['CanBlock'] = self.can_block
        if self.device is not None:
            result['Device'] = self.device
        if self.need is not None:
            result['Need'] = self.need
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanBlock') is not None:
            self.can_block = m.get('CanBlock')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Need') is not None:
            self.need = m.get('Need')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts(TeaModel):
    def __init__(self, system_disk_part=None):
        self.system_disk_part = system_disk_part  # type: list[DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart]

    def validate(self):
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N that is added to the SMC resource. Valid values of N: 1 to 20
        # 
        # You cannot specify empty strings as tag keys. It can be up to 64 characters in length and cannot start with acs: or aliyun. It cannot contain http:// or https://.
        self.key = key  # type: str
        # The value of tag N that is added to the SMC resource. Valid values of N: 1 to 20
        # 
        # The tag key can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServerTagsTag, self).to_map()
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


class DescribeSourceServersResponseBodySourceServersSourceServerTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeSourceServersResponseBodySourceServersSourceServerTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServerTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServer(TeaModel):
    def __init__(self, agent_version=None, architecture=None, creation_time=None, data_disks=None, description=None,
                 error_code=None, heartbeat_rate=None, job_id=None, kernel_level=None, name=None, platform=None,
                 replication_driver=None, resource_group_id=None, source_id=None, state=None, status_info=None, system_disk_parts=None,
                 system_disk_size=None, system_info=None, tags=None):
        # The version number of the SMC client.
        self.agent_version = agent_version  # type: str
        # The system architecture of the migration source.
        self.architecture = architecture  # type: str
        # The time when the migration source was created.
        self.creation_time = creation_time  # type: str
        # The data disk on the migration source.
        self.data_disks = data_disks  # type: DescribeSourceServersResponseBodySourceServersSourceServerDataDisks
        # The description of the migration source.
        self.description = description  # type: str
        # The error code of the migration source.
        self.error_code = error_code  # type: str
        # The interval at which heartbeats are sent from the SMC client. Unit: seconds.
        self.heartbeat_rate = heartbeat_rate  # type: int
        # The ID of the last migration job.
        self.job_id = job_id  # type: str
        # The kernel level of the migration source.
        self.kernel_level = kernel_level  # type: int
        # The name of the migration source.
        self.name = name  # type: str
        # The operating system of the migration source.
        self.platform = platform  # type: str
        # The replication driver used for migration. Default value: SMT.
        self.replication_driver = replication_driver  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the migration source.
        self.source_id = source_id  # type: str
        # The state of the migration source.
        self.state = state  # type: str
        # The status information of the migration source. This parameter is returned if the migration source is in the Unavailable state. The value of this parameter consists of key-value pairs in the JSON format. Sample keys:
        # 
        #     error_code: The error code.
        #     error_msg: The error message.
        self.status_info = status_info  # type: str
        # The information about the system disk partition.
        self.system_disk_parts = system_disk_parts  # type: DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts
        # The system disk size of the migration source. Unit: GiB.
        self.system_disk_size = system_disk_size  # type: int
        # The system information of the migration source. The value of this parameter consists of key-value pairs in the JSON format. The key-value pairs are extensible and have fixed keys. The JSON string does not exceed 1 KB in size. Sample keys:
        # 
        #     agent_mode: The migration mode.
        #     agent_type: The migration type.
        #     client_type: The client type.
        #     hostname: The host name.
        #     ipv4: The IPv4 address.
        #     ipv6: The IPv6 address.
        #     .cores: The number of CPU cores.
        #     cpu_usage: The CPU utilization.
        #     memory: The memory size.
        #     memory_usage: The memory usage.
        self.system_info = system_info  # type: str
        # The information about the tags.
        self.tags = tags  # type: DescribeSourceServersResponseBodySourceServersSourceServerTags

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()
        if self.system_disk_parts:
            self.system_disk_parts.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServersSourceServer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.heartbeat_rate is not None:
            result['HeartbeatRate'] = self.heartbeat_rate
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.kernel_level is not None:
            result['KernelLevel'] = self.kernel_level
        if self.name is not None:
            result['Name'] = self.name
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.replication_driver is not None:
            result['ReplicationDriver'] = self.replication_driver
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.state is not None:
            result['State'] = self.state
        if self.status_info is not None:
            result['StatusInfo'] = self.status_info
        if self.system_disk_parts is not None:
            result['SystemDiskParts'] = self.system_disk_parts.to_map()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_info is not None:
            result['SystemInfo'] = self.system_info
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataDisks') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HeartbeatRate') is not None:
            self.heartbeat_rate = m.get('HeartbeatRate')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('KernelLevel') is not None:
            self.kernel_level = m.get('KernelLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ReplicationDriver') is not None:
            self.replication_driver = m.get('ReplicationDriver')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StatusInfo') is not None:
            self.status_info = m.get('StatusInfo')
        if m.get('SystemDiskParts') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts()
            self.system_disk_parts = temp_model.from_map(m['SystemDiskParts'])
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemInfo') is not None:
            self.system_info = m.get('SystemInfo')
        if m.get('Tags') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeSourceServersResponseBodySourceServers(TeaModel):
    def __init__(self, source_server=None):
        self.source_server = source_server  # type: list[DescribeSourceServersResponseBodySourceServersSourceServer]

    def validate(self):
        if self.source_server:
            for k in self.source_server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponseBodySourceServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceServer'] = []
        if self.source_server is not None:
            for k in self.source_server:
                result['SourceServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source_server = []
        if m.get('SourceServer') is not None:
            for k in m.get('SourceServer'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServer()
                self.source_server.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, source_servers=None, total_count=None):
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The information about the migration source.
        self.source_servers = source_servers  # type: DescribeSourceServersResponseBodySourceServers
        # The total number of migration sources returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.source_servers:
            self.source_servers.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_servers is not None:
            result['SourceServers'] = self.source_servers.to_map()
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
        if m.get('SourceServers') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServers()
            self.source_servers = temp_model.from_map(m['SourceServers'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSourceServersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSourceServersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSourceServersResponse, self).to_map()
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
            temp_model = DescribeSourceServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAccessTokenRequest(TeaModel):
    def __init__(self, access_token_id=None, owner_id=None, resource_owner_account=None):
        # The ID of the activation code.
        self.access_token_id = access_token_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAccessTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DisableAccessTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAccessTokenResponseBody, self).to_map()
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


class DisableAccessTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableAccessTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableAccessTokenResponse, self).to_map()
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
            temp_model = DisableAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessTokensRequest(TeaModel):
    def __init__(self, access_token_id=None, name=None, owner_id=None, resource_owner_account=None, status=None):
        # The information about activation codes.
        self.access_token_id = access_token_id  # type: list[str]
        # The name of the activation code.
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        # The status of the activation code. Valid values:
        # 
        # *   activated
        # *   unactivated
        # *   expired
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessTokensRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAccessTokensResponseBodyAccessTokensAccessToken(TeaModel):
    def __init__(self, access_token_id=None, count=None, creation_time=None, description=None, name=None,
                 registered_count=None, status=None, time_to_live_in_days=None):
        # The ID of the activation code.
        self.access_token_id = access_token_id  # type: str
        # The maximum number of times that the activation code can be used. Valid values: 1 to 1000.
        # 
        # Default value: 100.
        self.count = count  # type: str
        # The time when the activation code was created. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time  # type: str
        # The description of the activation code.
        self.description = description  # type: str
        # The name of the activation code.
        self.name = name  # type: str
        # The number of migration sources whose information has been imported to Server Migration Center (SMC) by using the activation code.
        self.registered_count = registered_count  # type: str
        # The status of the activation code. Valid values:
        # 
        # *   activated
        # *   unactivated
        # *   expired
        self.status = status  # type: str
        # The validity period of the activation code. Unit: day. Valid values: 1 to 90. Default value: 30.
        self.time_to_live_in_days = time_to_live_in_days  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessTokensResponseBodyAccessTokensAccessToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.count is not None:
            result['Count'] = self.count
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.registered_count is not None:
            result['RegisteredCount'] = self.registered_count
        if self.status is not None:
            result['Status'] = self.status
        if self.time_to_live_in_days is not None:
            result['TimeToLiveInDays'] = self.time_to_live_in_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegisteredCount') is not None:
            self.registered_count = m.get('RegisteredCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeToLiveInDays') is not None:
            self.time_to_live_in_days = m.get('TimeToLiveInDays')
        return self


class ListAccessTokensResponseBodyAccessTokens(TeaModel):
    def __init__(self, access_token=None):
        self.access_token = access_token  # type: list[ListAccessTokensResponseBodyAccessTokensAccessToken]

    def validate(self):
        if self.access_token:
            for k in self.access_token:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccessTokensResponseBodyAccessTokens, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessToken'] = []
        if self.access_token is not None:
            for k in self.access_token:
                result['AccessToken'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.access_token = []
        if m.get('AccessToken') is not None:
            for k in m.get('AccessToken'):
                temp_model = ListAccessTokensResponseBodyAccessTokensAccessToken()
                self.access_token.append(temp_model.from_map(k))
        return self


class ListAccessTokensResponseBody(TeaModel):
    def __init__(self, access_tokens=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The activation codes returned.
        self.access_tokens = access_tokens  # type: ListAccessTokensResponseBodyAccessTokens
        # The number of entries per page. Valid values:
        # 
        # *   10
        # *   20
        # *   50
        # 
        # Default value: 20.
        self.page_number = page_number  # type: int
        # The page number.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of migration sources returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.access_tokens:
            self.access_tokens.validate()

    def to_map(self):
        _map = super(ListAccessTokensResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_tokens is not None:
            result['AccessTokens'] = self.access_tokens.to_map()
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
        if m.get('AccessTokens') is not None:
            temp_model = ListAccessTokensResponseBodyAccessTokens()
            self.access_tokens = temp_model.from_map(m['AccessTokens'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccessTokensResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccessTokensResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccessTokensResponse, self).to_map()
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
            temp_model = ListAccessTokensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N. The tag key must be 1 to 64 characters in length. Valid values of N: 1 to 20.
        # 
        # Tag.N is used for exact match of SMC resources to which the tag is attached. Tag N consists of a key-value pair.
        # 
        # *   Tag keys and values are case-sensitive.
        # *   If you set only the Tag.N.Key parameter, all resources to which the specified tags are attached are returned.
        # *   If you set only the Tag.N.Value parameter, the error message InvalidParameter.TagValue is returned.
        # *   If you specify multiple tag key-value pairs at a time, only SMC resources that match all tag key-value pairs are returned.
        self.key = key  # type: str
        # The value of tag N. The value must be 1 to 64 characters in length. Valid values of N: 1 to 20.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(self, next_token=None, owner_id=None, resource_id=None, resource_owner_account=None,
                 resource_type=None, tag=None):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        self.owner_id = owner_id  # type: long
        # The IDs of SMC resources. SMC resources include migration sources and migration jobs. You can specify a maximum of 50 SMC resource IDs.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        # The type of the SMC resource. Valid values:
        # 
        # *   sourceserver: migration source.
        # *   replicationjob: migration job.
        self.resource_type = resource_type  # type: str
        # The tags that are attached to SMC resources.
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The resource ID.
        self.resource_id = resource_id  # type: str
        # The type of the resource.
        self.resource_type = resource_type  # type: str
        # The key of the tag that is attached to the resource.
        self.tag_key = tag_key  # type: str
        # The value of the tag that is attached to the resource.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
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
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If NextToken is empty, no next page exists.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The information about SMC resources and tags, such as the IDs, types, and tag key-value pairs of the resources.
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
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReplicationJobAttributeRequestDataDiskPart(TeaModel):
    def __init__(self, block=None, device=None, size_bytes=None):
        # Specifies whether to enable block replication for partition N in the destination data disk. Valid values:
        # 
        # *   true
        # *   false
        self.block = block  # type: bool
        # The ID of partition N in the destination data disk.
        # 
        # >  The partitions in the destination data disk are arranged in the same sequential order as those in the source data disk.
        self.device = device  # type: str
        # The size of partition N in the destination data disk. Unit: bytes. The default value is equal to the corresponding size of the partition in the source data disk.
        # 
        # >  The total size of all partitions in the destination data disk cannot exceed the size of the destination data disk.
        self.size_bytes = size_bytes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReplicationJobAttributeRequestDataDiskPart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class ModifyReplicationJobAttributeRequestDataDisk(TeaModel):
    def __init__(self, index=None, part=None, size=None):
        # The index of data disk N on the destination ECS instance. Valid values of N: 1 to 16.
        # 
        # Data disks on a destination ECS instance are arranged in a sequential order that starts from 1.
        # 
        # >  You can create a destination data disk only for a source server that has data disks.
        self.index = index  # type: int
        # The information about partitions.
        self.part = part  # type: list[ModifyReplicationJobAttributeRequestDataDiskPart]
        # The size of the data disk on the destination ECS instance. Unit: GiB. Valid values: 20 to 32768.
        # 
        # >  The size of a destination data disk must be greater than the size of data in the source data disk. For example, if the source data disk has 500 GiB of storage space and 100 GiB of data, you must set this parameter to a value greater than 100.
        self.size = size  # type: int

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyReplicationJobAttributeRequestDataDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = ModifyReplicationJobAttributeRequestDataDiskPart()
                self.part.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ModifyReplicationJobAttributeRequestSystemDiskPart(TeaModel):
    def __init__(self, block=None, device=None, size_bytes=None):
        # Specifies whether to enable block replication for partition N in the destination system disk. Valid values:
        # 
        # *   true
        # *   false
        self.block = block  # type: bool
        # The ID of partition N in the destination system disk.
        # 
        # >  The partitions in the destination system disk are arranged in the same sequential order as those in the source system disk.
        self.device = device  # type: str
        # The size of partition N in the destination system disk. Unit: bytes. The default value is equal to the partition size of the source system disk.
        # 
        # >  The total size of all partitions in the destination system disk cannot exceed the size of the destination system disk.
        self.size_bytes = size_bytes  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReplicationJobAttributeRequestSystemDiskPart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class ModifyReplicationJobAttributeRequest(TeaModel):
    def __init__(self, container_namespace=None, container_repository=None, container_tag=None, data_disk=None,
                 description=None, frequency=None, image_name=None, instance_id=None, instance_ram_role=None,
                 instance_type=None, job_id=None, launch_template_id=None, launch_template_version=None, license_type=None,
                 max_number_of_image_to_keep=None, name=None, net_mode=None, owner_id=None, replication_parameters=None,
                 resource_owner_account=None, scheduled_start_time=None, system_disk_part=None, system_disk_size=None, target_type=None,
                 v_switch_id=None, valid_time=None, vpc_id=None):
        # The namespace of the destination Docker container image. For more information about Docker container images, see [Terms](~~60744~~).
        self.container_namespace = container_namespace  # type: str
        # The repository that stores the destination Docker container image. For more information about Docker container images, see [Terms](~~60744~~).
        self.container_repository = container_repository  # type: str
        # The tag of the destination Docker container image. For more information about Docker container images, see [Terms](~~60744~~).
        self.container_tag = container_tag  # type: str
        # The information about the data disk.
        self.data_disk = data_disk  # type: list[ModifyReplicationJobAttributeRequestDataDisk]
        # The description of the migration job.
        # 
        # The description must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (\_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # The interval at which an incremental migration job runs. Unit: hour. Valid values: 1 to 168.
        # 
        # This parameter is required if you set the `RunOnce` parameter to false.
        self.frequency = frequency  # type: int
        # The name of the destination image. The name must meet the following requirements:
        # 
        # *   The name must be unique within an Alibaba Cloud region.
        # *   The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (\_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        # 
        # >  If an image whose name is the same as that of the destination image already exists in the current region when the migration job is in progress, the system adds the migration job ID to the end of the image name by default. Example: ImageName-JobId.
        self.image_name = image_name  # type: str
        # The destination instance ID.
        self.instance_id = instance_id  # type: str
        # The name of the Resource Access Management (RAM) role that is attached to the intermediate instance.
        self.instance_ram_role = instance_ram_role  # type: str
        # The type of the intermediate instance.
        # 
        # You can call the [DescribeInstanceTypes](~~25620~~) operation to query the ECS instance types.
        # 
        # *   If you specify this parameter, SMC creates an intermediate instance of the specified instance type. If the specified instance type is unavailable, you cannot create the migration job.
        # *   If you do not specify this parameter, SMC selects an available instance type in a specific order to create an intermediate instance. For more information,
        # 
        # see the "How does SMC create an intermediate instance?" section of the "FAQ" topic.
        self.instance_type = instance_type  # type: str
        # The migration job ID.
        self.job_id = job_id  # type: str
        # The launch template ID.
        self.launch_template_id = launch_template_id  # type: str
        # The version number of the launch template.
        self.launch_template_version = launch_template_version  # type: str
        self.license_type = license_type  # type: str
        # The maximum number of images that are retained for an incremental migration job. Valid values: 1 to 10.
        # 
        # This parameter is required if you set the `RunOnce` parameter to false.
        self.max_number_of_image_to_keep = max_number_of_image_to_keep  # type: int
        # The name of the migration job. The name must meet the following requirements:
        # 
        # *   The name must be unique.
        # *   The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (\_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        self.name = name  # type: str
        self.net_mode = net_mode  # type: int
        self.owner_id = owner_id  # type: long
        self.replication_parameters = replication_parameters  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The time when the migration job is executed. SMC starts the migration job at the specified time.
        # 
        # Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2018-01-01T12:00:00Z indicates 20:00:00 on January 1, 2018 (UTC+8).
        # 
        # >  If ScheduledStartTime is left empty, SMC does not automatically start the migration job. In this case, you must call the [StartReplicationJob](~~121823~~) operation to start the migration job.
        self.scheduled_start_time = scheduled_start_time  # type: str
        # The partition information of the system disk.
        self.system_disk_part = system_disk_part  # type: list[ModifyReplicationJobAttributeRequestSystemDiskPart]
        # The system disk size of the destination ECS instance. Unit: GiB. Valid values: 20 to 500.
        # 
        # >  The size of a destination data disk must be greater than the size of data in the source data disk. For example, if the source data disk has 500 GiB of storage space and 100 GiB of data, you must set this parameter to a value greater than 100.
        self.system_disk_size = system_disk_size  # type: int
        # The type of destination to which the source server is migrated. You can modify the value only before the migration job starts. Valid values:
        # 
        # *   Image: After the migration job is complete, Server Migration Center (SMC) generates a destination Elastic Compute Service (ECS) image for the source server. You can use the image to create an ECS instance.
        # *   ContainerImage: After the migration job is complete, SMC generates a container image for the source server. You can use the container image in Container Registry.
        # *   TargetInstance: After the migration job is complete, SMC migrates the source server to the destination instance. If you set this parameter to TargetInstance, you must set the `InstanceId` parameter.
        # 
        # > 
        # 
        # *   The value of this parameter is not case-sensitive.
        # 
        # *   SMC does not allow you to migrate Windows servers or servers that run operating systems on the ARM architecture to Container Registry.
        self.target_type = target_type  # type: str
        self.v_switch_id = v_switch_id  # type: str
        # The time when the migration job expires. You can schedule the migration job to expire 7 to 90 days after the job is created.
        # 
        # *   This parameter can be modified only if the migration job is in the Ready, Running, Stopped, InError, or Waiting state.
        # *   Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC. For example, 2018-01-01T12:00:00Z indicates 20:00:00 on January 1, 2018 (UTC+8).
        # *   If you do not specify this parameter, the migration job does not expire.
        # *   After a migration job expires, the job state changes to Expired. SMC retains the migration job for seven days after the job expires. After the job is retained for seven days, SMC deletes the migration job.
        # 
        # By default, a migration job is valid for 30 days after it is created.
        self.valid_time = valid_time  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyReplicationJobAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.name is not None:
            result['Name'] = self.name
        if self.net_mode is not None:
            result['NetMode'] = self.net_mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replication_parameters is not None:
            result['ReplicationParameters'] = self.replication_parameters
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = ModifyReplicationJobAttributeRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetMode') is not None:
            self.net_mode = m.get('NetMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplicationParameters') is not None:
            self.replication_parameters = m.get('ReplicationParameters')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = ModifyReplicationJobAttributeRequestSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ModifyReplicationJobAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReplicationJobAttributeResponseBody, self).to_map()
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


class ModifyReplicationJobAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyReplicationJobAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyReplicationJobAttributeResponse, self).to_map()
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
            temp_model = ModifyReplicationJobAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySourceServerAttributeRequest(TeaModel):
    def __init__(self, description=None, name=None, owner_id=None, resource_owner_account=None, source_id=None):
        # The description of the migration source. The description can be up to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # The name of the migration source. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        # The migration source ID.
        self.source_id = source_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySourceServerAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class ModifySourceServerAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySourceServerAttributeResponseBody, self).to_map()
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


class ModifySourceServerAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySourceServerAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySourceServerAttributeResponse, self).to_map()
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
            temp_model = ModifySourceServerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartReplicationJobRequest(TeaModel):
    def __init__(self, job_id=None, owner_id=None, resource_owner_account=None):
        # The migration job ID.
        self.job_id = job_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartReplicationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class StartReplicationJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartReplicationJobResponseBody, self).to_map()
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


class StartReplicationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartReplicationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartReplicationJobResponse, self).to_map()
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
            temp_model = StartReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopReplicationJobRequest(TeaModel):
    def __init__(self, job_id=None, owner_id=None, resource_owner_account=None):
        # The migration job ID.
        self.job_id = job_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopReplicationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class StopReplicationJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopReplicationJobResponseBody, self).to_map()
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


class StopReplicationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopReplicationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopReplicationJobResponse, self).to_map()
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
            temp_model = StopReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to be added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. It can be up to 64 characters in length and cannot start with acs: or aliyun. It cannot contain http:// or https://.
        self.key = key  # type: str
        # The value of tag N to be added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
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


class TagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_id=None, resource_owner_account=None, resource_type=None, tag=None):
        self.owner_id = owner_id  # type: long
        # The IDs of N SMC resources. SMC resources include migration sources and jobs. Valid values of N: 1 to 50.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        # The type of the SMC resource. Valid values:
        # 
        # *   sourceserver: migration source.
        # *   replicationjob: migration job.
        self.resource_type = resource_type  # type: str
        # The tags.
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, owner_id=None, resource_id=None, resource_owner_account=None, resource_type=None,
                 tag_key=None):
        # Specifies whether to remove all tags that are added to the specified SMC resource. This parameter is valid only if you do not set `TagKey.N`. Valid values:
        # 
        # *   true: removes all tags that are added to the specified SMC resource. If no tags are added to the specified SMC resource, no operation is performed.
        # *   false: does not remove tags that are added to the specified SMC resource.
        # 
        # Default value: false.
        self.all = all  # type: bool
        self.owner_id = owner_id  # type: long
        # The IDs of N SMC resources. SMC resources include migration sources and jobs. Valid values of N: 1 to 50.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        # The type of the SMC resource. Valid values:
        # 
        # *   sourceserver: migration source.
        # *   replicationjob: migration job.
        self.resource_type = resource_type  # type: str
        # The key of tag N that is added to the SMC resource. Tag keys are case-sensitive. Valid values of N: 1 to 20.
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


