# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CommitContainerRequestAcrRegistryInfo(TeaModel):
    def __init__(self, arn_service=None, arn_user=None, instance_id=None, region_id=None):
        # The RAM role ARN of the account to which permissions are granted during a cross-account authorization.
        self.arn_service = arn_service  # type: str
        # The RAM role ARN of the account that is used to grant permissions during a cross-account authorization.
        self.arn_user = arn_user  # type: str
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the Container Registry Enterprise Edition instance resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitContainerRequestAcrRegistryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn_service is not None:
            result['ArnService'] = self.arn_service
        if self.arn_user is not None:
            result['ArnUser'] = self.arn_user
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArnService') is not None:
            self.arn_service = m.get('ArnService')
        if m.get('ArnUser') is not None:
            self.arn_user = m.get('ArnUser')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CommitContainerRequestArn(TeaModel):
    def __init__(self, role_arn=None, role_type=None):
        # The ARN of the RAM role of the Container Registry Enterprise Edition instance.
        self.role_arn = role_arn  # type: str
        # The type of the authorization.
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitContainerRequestArn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class CommitContainerRequestImage(TeaModel):
    def __init__(self, author=None, message=None, repository=None, tag=None):
        # The authorization of the image.
        self.author = author  # type: str
        # The message about the image.
        self.message = message  # type: str
        # The image repository.
        self.repository = repository  # type: str
        # The tag of the image. This parameter is empty by default, which indicates that the tag is not modified.
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitContainerRequestImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.message is not None:
            result['Message'] = self.message
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CommitContainerRequest(TeaModel):
    def __init__(self, acr_registry_info=None, arn=None, container_group_id=None, container_name=None, image=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        # The access credential configurations of the Container Registry Enterprise Edition instance.\
        # If you use a Container Registry Personal Edition instance, you can leave this parameter empty.
        self.acr_registry_info = acr_registry_info  # type: CommitContainerRequestAcrRegistryInfo
        # The ARN that is required for authorization.
        self.arn = arn  # type: CommitContainerRequestArn
        # The ID of the container group.
        self.container_group_id = container_group_id  # type: str
        # The name of the container.
        self.container_name = container_name  # type: str
        # The image of the container.
        self.image = image  # type: CommitContainerRequestImage
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        if self.acr_registry_info:
            self.acr_registry_info.validate()
        if self.arn:
            self.arn.validate()
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super(CommitContainerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_registry_info is not None:
            result['AcrRegistryInfo'] = self.acr_registry_info.to_map()
        if self.arn is not None:
            result['Arn'] = self.arn.to_map()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcrRegistryInfo') is not None:
            temp_model = CommitContainerRequestAcrRegistryInfo()
            self.acr_registry_info = temp_model.from_map(m['AcrRegistryInfo'])
        if m.get('Arn') is not None:
            temp_model = CommitContainerRequestArn()
            self.arn = temp_model.from_map(m['Arn'])
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Image') is not None:
            temp_model = CommitContainerRequestImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CommitContainerResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitContainerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CommitContainerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CommitContainerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CommitContainerResponse, self).to_map()
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
            temp_model = CommitContainerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyDataCacheRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyDataCacheRequestTag, self).to_map()
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


class CopyDataCacheRequest(TeaModel):
    def __init__(self, bucket=None, client_token=None, data_cache_id=None, destination_region_id=None, name=None,
                 owner_account=None, owner_id=None, path=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, retention_days=None, tag=None):
        # The bucket in which the DataCache is stored.
        self.bucket = bucket  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the DataCache in the source region.
        self.data_cache_id = data_cache_id  # type: str
        # The destination region of the DataCache.
        self.destination_region_id = destination_region_id  # type: str
        # The DataCache name.
        self.name = name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The storage path of the data.
        self.path = path  # type: str
        # The source region of the DataCache.
        self.region_id = region_id  # type: str
        # The resource group to which the DataCache belongs.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The number of days for which the DataCache is retained.
        self.retention_days = retention_days  # type: int
        # The tags of the DataCache.
        self.tag = tag  # type: list[CopyDataCacheRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CopyDataCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CopyDataCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CopyDataCacheResponseBody(TeaModel):
    def __init__(self, data_cache_id=None, request_id=None):
        # The ID generated for the DataCache in the destination region.
        self.data_cache_id = data_cache_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyDataCacheResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyDataCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CopyDataCacheResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CopyDataCacheResponse, self).to_map()
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
            temp_model = CopyDataCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateContainerGroupRequestDnsConfigOption(TeaModel):
    def __init__(self, name=None, value=None):
        # The name of the option.
        self.name = name  # type: str
        # The value of the option.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestDnsConfigOption, self).to_map()
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


class CreateContainerGroupRequestDnsConfig(TeaModel):
    def __init__(self, name_server=None, option=None, search=None):
        # The IP addresses of the DNS servers.
        self.name_server = name_server  # type: list[str]
        # Configuration options of the DNS server.
        self.option = option  # type: list[CreateContainerGroupRequestDnsConfigOption]
        # The search domains of the DNS server.
        self.search = search  # type: list[str]

    def validate(self):
        if self.option:
            for k in self.option:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestDnsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_server is not None:
            result['NameServer'] = self.name_server
        result['Option'] = []
        if self.option is not None:
            for k in self.option:
                result['Option'].append(k.to_map() if k else None)
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NameServer') is not None:
            self.name_server = m.get('NameServer')
        self.option = []
        if m.get('Option') is not None:
            for k in m.get('Option'):
                temp_model = CreateContainerGroupRequestDnsConfigOption()
                self.option.append(temp_model.from_map(k))
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class CreateContainerGroupRequestHostSecurityContextSysctl(TeaModel):
    def __init__(self, name=None, value=None):
        # The key of the unsafe sysctl when you modify sysctls by configuring a security context. Valid values:
        # 
        # *   kernel.shm \* (except kernel.shm_rmid_forced)
        # *   kernel.msg\*kernel.sem
        # *   fs.mqueue.\*\
        # *   net.\*(except net.ipv4.tcp_syncookies, net.ipv4.ping_group_range, and net.ipv4.ip_unprivileged_port_start)
        self.name = name  # type: str
        # The value of the unsafe sysctl when you modify sysctls by configuring a security context.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestHostSecurityContextSysctl, self).to_map()
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


class CreateContainerGroupRequestHostSecurityContext(TeaModel):
    def __init__(self, sysctl=None):
        # Configure a security context to modify unsafe sysctls. For more information, see [Configure a security context](~~462313~~).
        self.sysctl = sysctl  # type: list[CreateContainerGroupRequestHostSecurityContextSysctl]

    def validate(self):
        if self.sysctl:
            for k in self.sysctl:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestHostSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sysctl'] = []
        if self.sysctl is not None:
            for k in self.sysctl:
                result['Sysctl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sysctl = []
        if m.get('Sysctl') is not None:
            for k in m.get('Sysctl'):
                temp_model = CreateContainerGroupRequestHostSecurityContextSysctl()
                self.sysctl.append(temp_model.from_map(k))
        return self


class CreateContainerGroupRequestSecurityContextSysctl(TeaModel):
    def __init__(self, name=None, value=None):
        # The name of the safe sysctl when you configure a security context to modify sysctls. Valid values:
        # 
        # *   net.ipv4.ping_group_range
        # *   net.ipv4.ip_unprivileged_port_start
        self.name = name  # type: str
        # The value of the safe sysctl when you configure a security context to modify sysctls.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestSecurityContextSysctl, self).to_map()
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


class CreateContainerGroupRequestSecurityContext(TeaModel):
    def __init__(self, sysctl=None):
        # Configure a security context to modify sysctls. For more information, see [Configure a security context](~~462313~~)
        self.sysctl = sysctl  # type: list[CreateContainerGroupRequestSecurityContextSysctl]

    def validate(self):
        if self.sysctl:
            for k in self.sysctl:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sysctl'] = []
        if self.sysctl is not None:
            for k in self.sysctl:
                result['Sysctl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sysctl = []
        if m.get('Sysctl') is not None:
            for k in m.get('Sysctl'):
                temp_model = CreateContainerGroupRequestSecurityContextSysctl()
                self.sysctl.append(temp_model.from_map(k))
        return self


class CreateContainerGroupRequestAcrRegistryInfo(TeaModel):
    def __init__(self, arn_service=None, arn_user=None, domain=None, instance_id=None, instance_name=None,
                 region_id=None):
        # The Alibaba Cloud Resource Name (ARN) of the RAM roles in the Alibaba Cloud account to which the elastic container instance belongs.
        self.arn_service = arn_service  # type: str
        # The ARN of the RAM roles in the Alibaba Cloud account to which the Container Registry instance belongs.
        self.arn_user = arn_user  # type: str
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. You can specify multiple domain names. Separate multiple domain names with commas (,).
        self.domain = domain  # type: list[str]
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id  # type: str
        # The name of the Container Registry Enterprise Edition instance.
        self.instance_name = instance_name  # type: str
        # The region ID of the Container Registry Enterprise Edition instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestAcrRegistryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn_service is not None:
            result['ArnService'] = self.arn_service
        if self.arn_user is not None:
            result['ArnUser'] = self.arn_user
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArnService') is not None:
            self.arn_service = m.get('ArnService')
        if m.get('ArnUser') is not None:
            self.arn_user = m.get('ArnUser')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateContainerGroupRequestContainerLivenessProbeExec(TeaModel):
    def __init__(self, command=None):
        self.command = command  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerLivenessProbeExec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class CreateContainerGroupRequestContainerLivenessProbeHttpGet(TeaModel):
    def __init__(self, path=None, port=None, scheme=None):
        self.path = path  # type: str
        self.port = port  # type: int
        self.scheme = scheme  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerLivenessProbeHttpGet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class CreateContainerGroupRequestContainerLivenessProbeTcpSocket(TeaModel):
    def __init__(self, port=None):
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerLivenessProbeTcpSocket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestContainerLivenessProbe(TeaModel):
    def __init__(self, exec_=None, failure_threshold=None, http_get=None, initial_delay_seconds=None,
                 period_seconds=None, success_threshold=None, tcp_socket=None, timeout_seconds=None):
        self.exec_ = exec_  # type: CreateContainerGroupRequestContainerLivenessProbeExec
        self.failure_threshold = failure_threshold  # type: int
        self.http_get = http_get  # type: CreateContainerGroupRequestContainerLivenessProbeHttpGet
        self.initial_delay_seconds = initial_delay_seconds  # type: int
        self.period_seconds = period_seconds  # type: int
        self.success_threshold = success_threshold  # type: int
        self.tcp_socket = tcp_socket  # type: CreateContainerGroupRequestContainerLivenessProbeTcpSocket
        self.timeout_seconds = timeout_seconds  # type: int

    def validate(self):
        if self.exec_:
            self.exec_.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerLivenessProbe, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_ is not None:
            result['Exec'] = self.exec_.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeExec()
            self.exec_ = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class CreateContainerGroupRequestContainerReadinessProbeExec(TeaModel):
    def __init__(self, command=None):
        self.command = command  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerReadinessProbeExec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class CreateContainerGroupRequestContainerReadinessProbeHttpGet(TeaModel):
    def __init__(self, path=None, port=None, scheme=None):
        self.path = path  # type: str
        self.port = port  # type: int
        self.scheme = scheme  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerReadinessProbeHttpGet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class CreateContainerGroupRequestContainerReadinessProbeTcpSocket(TeaModel):
    def __init__(self, port=None):
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerReadinessProbeTcpSocket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateContainerGroupRequestContainerReadinessProbe(TeaModel):
    def __init__(self, exec_=None, failure_threshold=None, http_get=None, initial_delay_seconds=None,
                 period_seconds=None, success_threshold=None, tcp_socket=None, timeout_seconds=None):
        self.exec_ = exec_  # type: CreateContainerGroupRequestContainerReadinessProbeExec
        self.failure_threshold = failure_threshold  # type: int
        self.http_get = http_get  # type: CreateContainerGroupRequestContainerReadinessProbeHttpGet
        self.initial_delay_seconds = initial_delay_seconds  # type: int
        self.period_seconds = period_seconds  # type: int
        self.success_threshold = success_threshold  # type: int
        self.tcp_socket = tcp_socket  # type: CreateContainerGroupRequestContainerReadinessProbeTcpSocket
        self.timeout_seconds = timeout_seconds  # type: int

    def validate(self):
        if self.exec_:
            self.exec_.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerReadinessProbe, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_ is not None:
            result['Exec'] = self.exec_.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeExec()
            self.exec_ = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class CreateContainerGroupRequestContainerSecurityContextCapability(TeaModel):
    def __init__(self, add=None):
        self.add = add  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerSecurityContextCapability, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class CreateContainerGroupRequestContainerSecurityContext(TeaModel):
    def __init__(self, capability=None, read_only_root_filesystem=None, run_as_user=None):
        self.capability = capability  # type: CreateContainerGroupRequestContainerSecurityContextCapability
        self.read_only_root_filesystem = read_only_root_filesystem  # type: bool
        self.run_as_user = run_as_user  # type: long

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = CreateContainerGroupRequestContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class CreateContainerGroupRequestContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(self, field_path=None):
        self.field_path = field_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerEnvironmentVarFieldRef, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class CreateContainerGroupRequestContainerEnvironmentVar(TeaModel):
    def __init__(self, field_ref=None, key=None, value=None):
        self.field_ref = field_ref  # type: CreateContainerGroupRequestContainerEnvironmentVarFieldRef
        # The name of the environment variable. The name must be 1 to 128 bits in length and can contain letters, digits, and underscores (\_). It cannot start with a digit.``
        self.key = key  # type: str
        # The value of the environment variable. The value must be 0 to 256 bits in length.
        self.value = value  # type: str

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerEnvironmentVar, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = CreateContainerGroupRequestContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader(TeaModel):
    def __init__(self, name=None, value=None):
        # The name of the custom field in the HTTP GET request header when you use HTTP requests to specify the postStart callback function.
        self.name = name  # type: str
        # The value of the custom field in the HTTP GET request header when you use HTTP requests to specify the postStart callback function.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader, self).to_map()
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


class CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader(TeaModel):
    def __init__(self, name=None, value=None):
        # The key of the custom field in the HTTP GET request header when you use HTTP requests to specify the preStop callback function.
        self.name = name  # type: str
        # The value of the custom field in the HTTP GET request header when you use HTTP requests to specify the preStop callback function.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader, self).to_map()
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


class CreateContainerGroupRequestContainerPort(TeaModel):
    def __init__(self, port=None, protocol=None):
        # The port number. Valid values: 1 to 65535.
        self.port = port  # type: int
        # The protocol type. Valid values:
        # 
        # *   TCP
        # *   UDP
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerPort, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class CreateContainerGroupRequestContainerVolumeMount(TeaModel):
    def __init__(self, mount_path=None, mount_propagation=None, name=None, read_only=None, sub_path=None):
        # The directory to which the volume is mounted.
        # 
        # >  The data stored in this directory is overwritten by the data on the volume. Specify this parameter with caution.
        self.mount_path = mount_path  # type: str
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume.
        # *   Bidirectional: This value is similar to HostToContainer. The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume. In addition, all volume mounts that are mounted on the container are propagated back to the host and all containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation  # type: str
        # The name of the volume. The name of this parameter is the same as the name of the volume that is mounted to the containers.
        self.name = name  # type: str
        # Specifies whether the volume is read-only. Default value: false.
        self.read_only = read_only  # type: bool
        # The subdirectory of the volume.
        self.sub_path = sub_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainerVolumeMount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class CreateContainerGroupRequestContainer(TeaModel):
    def __init__(self, liveness_probe=None, readiness_probe=None, security_context=None, arg=None, command=None,
                 cpu=None, environment_var=None, environment_var_hide=None, gpu=None, image=None,
                 image_pull_policy=None, lifecycle_post_start_handler_exec=None, lifecycle_post_start_handler_http_get_host=None,
                 lifecycle_post_start_handler_http_get_http_header=None, lifecycle_post_start_handler_http_get_path=None,
                 lifecycle_post_start_handler_http_get_port=None, lifecycle_post_start_handler_http_get_scheme=None,
                 lifecycle_post_start_handler_tcp_socket_host=None, lifecycle_post_start_handler_tcp_socket_port=None, lifecycle_pre_stop_handler_exec=None,
                 lifecycle_pre_stop_handler_http_get_host=None, lifecycle_pre_stop_handler_http_get_http_header=None,
                 lifecycle_pre_stop_handler_http_get_path=None, lifecycle_pre_stop_handler_http_get_port=None,
                 lifecycle_pre_stop_handler_http_get_scheme=None, lifecycle_pre_stop_handler_tcp_socket_host=None,
                 lifecycle_pre_stop_handler_tcp_socket_port=None, memory=None, name=None, port=None, security_context_run_as_group=None,
                 security_context_run_as_non_root=None, stdin=None, stdin_once=None, termination_message_path=None, termination_message_policy=None,
                 tty=None, volume_mount=None, working_dir=None):
        self.liveness_probe = liveness_probe  # type: CreateContainerGroupRequestContainerLivenessProbe
        self.readiness_probe = readiness_probe  # type: CreateContainerGroupRequestContainerReadinessProbe
        self.security_context = security_context  # type: CreateContainerGroupRequestContainerSecurityContext
        # The arguments that are passed to the startup command of the container. You can specify up to 10 arguments.
        self.arg = arg  # type: list[str]
        # The commands that you want to run to perform health checks on containers.
        self.command = command  # type: list[str]
        # The number of vCPUs that you want to allocate to the container.
        self.cpu = cpu  # type: float
        # The value of the environment variable for the container.
        self.environment_var = environment_var  # type: list[CreateContainerGroupRequestContainerEnvironmentVar]
        # Specifies whether to hide the information about environment variables when you query the details of an elastic container instance. Default value: false. Valid values:
        # 
        # *   false
        # *   true If environment variables contain sensitive information, you can set this parameter to true to improve security of the information.
        self.environment_var_hide = environment_var_hide  # type: bool
        # The number of GPUs that you want to allocate to the container.
        self.gpu = gpu  # type: int
        # The image of the container.
        self.image = image  # type: str
        # The policy that you want to use to pull an image. Valid values:
        # 
        # *   Always: Each time instances are created, image pulling is performed.
        # *   IfNotPresent: On-premises images are preferentially used. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy  # type: str
        # The commands to be executed in containers when you use a CLI to specify the postStart callback function.
        self.lifecycle_post_start_handler_exec = lifecycle_post_start_handler_exec  # type: list[str]
        # The IP address of the host that receives the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host  # type: str
        # The HTTP GET request header.
        self.lifecycle_post_start_handler_http_get_http_header = lifecycle_post_start_handler_http_get_http_header  # type: list[CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader]
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path  # type: str
        # The port to which the system sends an HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port  # type: int
        # The protocol type of HTTP GET requests when you use HTTP requests to specify the postStart callback function. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme  # type: str
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify the postStart callback function.
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host  # type: str
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify the postStart callback function.
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port  # type: int
        # The commands to be executed in containers when you use a CLI to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_exec = lifecycle_pre_stop_handler_exec  # type: list[str]
        # The IP address of the host that receives the HTTP GET request when you use an HTTP request to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host  # type: str
        # The HTTP GET request header.
        self.lifecycle_pre_stop_handler_http_get_http_header = lifecycle_pre_stop_handler_http_get_http_header  # type: list[CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader]
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify the preSop callback function.
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path  # type: str
        # The port to which the system sends an HTTP GET request for a health check when you use HTTP requests to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port  # type: int
        # The protocol type of the HTTP GET request when you use an HTTP request to specify the preStop callback function. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme  # type: str
        # The IP address of the host that receives the TCP socket request when you use a TCP socket request to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host  # type: str
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port  # type: int
        # The memory size that you want to allocate to the container. Unit: GiB
        self.memory = memory  # type: float
        # The name of the container.
        self.name = name  # type: str
        # The port to which the system sends an HTTP GET request for a health check when you use HTTP requests to perform health checks.
        self.port = port  # type: list[CreateContainerGroupRequestContainerPort]
        # The user group that runs the container.
        self.security_context_run_as_group = security_context_run_as_group  # type: long
        # Specifies whether to run the container as a non-root user.
        self.security_context_run_as_non_root = security_context_run_as_non_root  # type: bool
        # Specifies whether the container allocates buffer resources to standard input streams when the container is running. If you do not specify this parameter, an end-of-file (EOF) error may occur when standard input streams in the container are read. Default value: false.
        self.stdin = stdin  # type: bool
        # Specifies whether standard input streams are disconnected from multiple sessions after a client is disconnected.\
        # If StdinOnce is set to true, standard input streams are connected after the container is started, and remain idle until a client is connected to receive data. After the client is disconnected, standard input streams are also disconnected, and remain disconnected until the container restarts.
        self.stdin_once = stdin_once  # type: bool
        # The path of the file from which the system retrieves termination messages of the container when the container exits.
        self.termination_message_path = termination_message_path  # type: str
        # The message notification policy. This parameter is empty by default. Only Message Service (MNS) queue message notifications can be sent.
        self.termination_message_policy = termination_message_policy  # type: str
        # Specifies whether to enable interaction. Default value: false.
        # 
        # If the command is a /bin/bash command, set the value to true.
        self.tty = tty  # type: bool
        # The information about the volume that you want to mount to the container.
        self.volume_mount = volume_mount  # type: list[CreateContainerGroupRequestContainerVolumeMount]
        # The working directory of the container.
        self.working_dir = working_dir  # type: str

    def validate(self):
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.readiness_probe:
            self.readiness_probe.validate()
        if self.security_context:
            self.security_context.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.lifecycle_post_start_handler_http_get_http_header:
            for k in self.lifecycle_post_start_handler_http_get_http_header:
                if k:
                    k.validate()
        if self.lifecycle_pre_stop_handler_http_get_http_header:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestContainer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.environment_var_hide is not None:
            result['EnvironmentVarHide'] = self.environment_var_hide
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.lifecycle_post_start_handler_exec is not None:
            result['LifecyclePostStartHandlerExec'] = self.lifecycle_post_start_handler_exec
        if self.lifecycle_post_start_handler_http_get_host is not None:
            result['LifecyclePostStartHandlerHttpGetHost'] = self.lifecycle_post_start_handler_http_get_host
        result['LifecyclePostStartHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_post_start_handler_http_get_http_header is not None:
            for k in self.lifecycle_post_start_handler_http_get_http_header:
                result['LifecyclePostStartHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        if self.lifecycle_post_start_handler_http_get_path is not None:
            result['LifecyclePostStartHandlerHttpGetPath'] = self.lifecycle_post_start_handler_http_get_path
        if self.lifecycle_post_start_handler_http_get_port is not None:
            result['LifecyclePostStartHandlerHttpGetPort'] = self.lifecycle_post_start_handler_http_get_port
        if self.lifecycle_post_start_handler_http_get_scheme is not None:
            result['LifecyclePostStartHandlerHttpGetScheme'] = self.lifecycle_post_start_handler_http_get_scheme
        if self.lifecycle_post_start_handler_tcp_socket_host is not None:
            result['LifecyclePostStartHandlerTcpSocketHost'] = self.lifecycle_post_start_handler_tcp_socket_host
        if self.lifecycle_post_start_handler_tcp_socket_port is not None:
            result['LifecyclePostStartHandlerTcpSocketPort'] = self.lifecycle_post_start_handler_tcp_socket_port
        if self.lifecycle_pre_stop_handler_exec is not None:
            result['LifecyclePreStopHandlerExec'] = self.lifecycle_pre_stop_handler_exec
        if self.lifecycle_pre_stop_handler_http_get_host is not None:
            result['LifecyclePreStopHandlerHttpGetHost'] = self.lifecycle_pre_stop_handler_http_get_host
        result['LifecyclePreStopHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_pre_stop_handler_http_get_http_header is not None:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                result['LifecyclePreStopHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        if self.lifecycle_pre_stop_handler_http_get_path is not None:
            result['LifecyclePreStopHandlerHttpGetPath'] = self.lifecycle_pre_stop_handler_http_get_path
        if self.lifecycle_pre_stop_handler_http_get_port is not None:
            result['LifecyclePreStopHandlerHttpGetPort'] = self.lifecycle_pre_stop_handler_http_get_port
        if self.lifecycle_pre_stop_handler_http_get_scheme is not None:
            result['LifecyclePreStopHandlerHttpGetScheme'] = self.lifecycle_pre_stop_handler_http_get_scheme
        if self.lifecycle_pre_stop_handler_tcp_socket_host is not None:
            result['LifecyclePreStopHandlerTcpSocketHost'] = self.lifecycle_pre_stop_handler_tcp_socket_host
        if self.lifecycle_pre_stop_handler_tcp_socket_port is not None:
            result['LifecyclePreStopHandlerTcpSocketPort'] = self.lifecycle_pre_stop_handler_tcp_socket_port
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.security_context_run_as_group is not None:
            result['SecurityContextRunAsGroup'] = self.security_context_run_as_group
        if self.security_context_run_as_non_root is not None:
            result['SecurityContextRunAsNonRoot'] = self.security_context_run_as_non_root
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.termination_message_path is not None:
            result['TerminationMessagePath'] = self.termination_message_path
        if self.termination_message_policy is not None:
            result['TerminationMessagePolicy'] = self.termination_message_policy
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LivenessProbe') is not None:
            temp_model = CreateContainerGroupRequestContainerLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('ReadinessProbe') is not None:
            temp_model = CreateContainerGroupRequestContainerReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = CreateContainerGroupRequestContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('EnvironmentVarHide') is not None:
            self.environment_var_hide = m.get('EnvironmentVarHide')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('LifecyclePostStartHandlerExec') is not None:
            self.lifecycle_post_start_handler_exec = m.get('LifecyclePostStartHandlerExec')
        if m.get('LifecyclePostStartHandlerHttpGetHost') is not None:
            self.lifecycle_post_start_handler_http_get_host = m.get('LifecyclePostStartHandlerHttpGetHost')
        self.lifecycle_post_start_handler_http_get_http_header = []
        if m.get('LifecyclePostStartHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePostStartHandlerHttpGetHttpHeader'):
                temp_model = CreateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeader()
                self.lifecycle_post_start_handler_http_get_http_header.append(temp_model.from_map(k))
        if m.get('LifecyclePostStartHandlerHttpGetPath') is not None:
            self.lifecycle_post_start_handler_http_get_path = m.get('LifecyclePostStartHandlerHttpGetPath')
        if m.get('LifecyclePostStartHandlerHttpGetPort') is not None:
            self.lifecycle_post_start_handler_http_get_port = m.get('LifecyclePostStartHandlerHttpGetPort')
        if m.get('LifecyclePostStartHandlerHttpGetScheme') is not None:
            self.lifecycle_post_start_handler_http_get_scheme = m.get('LifecyclePostStartHandlerHttpGetScheme')
        if m.get('LifecyclePostStartHandlerTcpSocketHost') is not None:
            self.lifecycle_post_start_handler_tcp_socket_host = m.get('LifecyclePostStartHandlerTcpSocketHost')
        if m.get('LifecyclePostStartHandlerTcpSocketPort') is not None:
            self.lifecycle_post_start_handler_tcp_socket_port = m.get('LifecyclePostStartHandlerTcpSocketPort')
        if m.get('LifecyclePreStopHandlerExec') is not None:
            self.lifecycle_pre_stop_handler_exec = m.get('LifecyclePreStopHandlerExec')
        if m.get('LifecyclePreStopHandlerHttpGetHost') is not None:
            self.lifecycle_pre_stop_handler_http_get_host = m.get('LifecyclePreStopHandlerHttpGetHost')
        self.lifecycle_pre_stop_handler_http_get_http_header = []
        if m.get('LifecyclePreStopHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePreStopHandlerHttpGetHttpHeader'):
                temp_model = CreateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader()
                self.lifecycle_pre_stop_handler_http_get_http_header.append(temp_model.from_map(k))
        if m.get('LifecyclePreStopHandlerHttpGetPath') is not None:
            self.lifecycle_pre_stop_handler_http_get_path = m.get('LifecyclePreStopHandlerHttpGetPath')
        if m.get('LifecyclePreStopHandlerHttpGetPort') is not None:
            self.lifecycle_pre_stop_handler_http_get_port = m.get('LifecyclePreStopHandlerHttpGetPort')
        if m.get('LifecyclePreStopHandlerHttpGetScheme') is not None:
            self.lifecycle_pre_stop_handler_http_get_scheme = m.get('LifecyclePreStopHandlerHttpGetScheme')
        if m.get('LifecyclePreStopHandlerTcpSocketHost') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_host = m.get('LifecyclePreStopHandlerTcpSocketHost')
        if m.get('LifecyclePreStopHandlerTcpSocketPort') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_port = m.get('LifecyclePreStopHandlerTcpSocketPort')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = CreateContainerGroupRequestContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('SecurityContextRunAsGroup') is not None:
            self.security_context_run_as_group = m.get('SecurityContextRunAsGroup')
        if m.get('SecurityContextRunAsNonRoot') is not None:
            self.security_context_run_as_non_root = m.get('SecurityContextRunAsNonRoot')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('TerminationMessagePath') is not None:
            self.termination_message_path = m.get('TerminationMessagePath')
        if m.get('TerminationMessagePolicy') is not None:
            self.termination_message_policy = m.get('TerminationMessagePolicy')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = CreateContainerGroupRequestContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateContainerGroupRequestHostAliase(TeaModel):
    def __init__(self, hostname=None, ip=None):
        # The hostname of the elastic container instance.
        self.hostname = hostname  # type: list[str]
        # The IP address of the host.
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestHostAliase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class CreateContainerGroupRequestImageRegistryCredential(TeaModel):
    def __init__(self, password=None, server=None, user_name=None):
        # The password that you use to access the image repository.
        self.password = password  # type: str
        # The address of the image repository.
        self.server = server  # type: str
        # The username that you use to access the image repository.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestImageRegistryCredential, self).to_map()
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


class CreateContainerGroupRequestInitContainerSecurityContextCapability(TeaModel):
    def __init__(self, add=None):
        self.add = add  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestInitContainerSecurityContextCapability, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class CreateContainerGroupRequestInitContainerSecurityContext(TeaModel):
    def __init__(self, capability=None, read_only_root_filesystem=None, run_as_user=None):
        self.capability = capability  # type: CreateContainerGroupRequestInitContainerSecurityContextCapability
        self.read_only_root_filesystem = read_only_root_filesystem  # type: bool
        self.run_as_user = run_as_user  # type: long

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestInitContainerSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = CreateContainerGroupRequestInitContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(self, field_path=None):
        self.field_path = field_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class CreateContainerGroupRequestInitContainerEnvironmentVar(TeaModel):
    def __init__(self, field_ref=None, key=None, value=None):
        self.field_ref = field_ref  # type: CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef
        # The name of the environment variable. The name must be 1 to 128 characters in length, and can contain letters, digits, and underscores (\_). It cannot start with a digit.``
        self.key = key  # type: str
        # The value of the environment variable. The value can be up to 256 characters in length.
        self.value = value  # type: str

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestInitContainerEnvironmentVar, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = CreateContainerGroupRequestInitContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateContainerGroupRequestInitContainerPort(TeaModel):
    def __init__(self, port=None, protocol=None):
        # The port number. Valid values: 1 to 65535.
        self.port = port  # type: int
        # The protocol type. Valid values:
        # 
        # *   TCP
        # *   UDP
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestInitContainerPort, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class CreateContainerGroupRequestInitContainerVolumeMount(TeaModel):
    def __init__(self, mount_path=None, mount_propagation=None, name=None, read_only=None, sub_path=None):
        # The directory to which the volume is mounted. The data stored in this directory is overwritten by the data on the volume. Specify this parameter with caution.
        self.mount_path = mount_path  # type: str
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are mounted to the volume or to the subdirectories of the volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are mounted to the volume or to the subdirectories of the volume.
        # *   Bidirectional: The volume mount behaves the same as the HostToCotainer mount. The volume mount receives subsequent mounts that are mounted to the volume or to the subdirectories of the volume. In addition, all volume mounts created by the container are propagated back to the host and to all containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation  # type: str
        # The volume name.
        self.name = name  # type: str
        # Specifies whether the mount path is read-only. Default value: false.
        self.read_only = read_only  # type: bool
        # The subdirectory of the volume. The pod can mount different directories of the same volume to different directories of the init container.
        self.sub_path = sub_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestInitContainerVolumeMount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class CreateContainerGroupRequestInitContainer(TeaModel):
    def __init__(self, security_context=None, arg=None, command=None, cpu=None, environment_var=None, gpu=None,
                 image=None, image_pull_policy=None, memory=None, name=None, port=None, termination_message_path=None,
                 termination_message_policy=None, volume_mount=None, working_dir=None):
        self.security_context = security_context  # type: CreateContainerGroupRequestInitContainerSecurityContext
        # The arguments that are passed to the startup command of the init container.
        self.arg = arg  # type: list[str]
        # The startup commands of the init container.
        self.command = command  # type: list[str]
        # The number of vCPUs that you want to allocate to the init container. Unit: cores.
        self.cpu = cpu  # type: float
        # The environment variable of the init container.
        self.environment_var = environment_var  # type: list[CreateContainerGroupRequestInitContainerEnvironmentVar]
        # The number of GPUs that you want to allocate to the init container.
        self.gpu = gpu  # type: int
        # The image of the init container.
        self.image = image  # type: str
        # The policy for image pulling. Valid values:
        # 
        # *   Always: Each time instances are created, image pulling is performed.
        # *   IfNotPresent: On-premises images are preferentially used. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy  # type: str
        # The memory size of the init container. Unit: GiB.
        self.memory = memory  # type: float
        # The container name.
        self.name = name  # type: str
        # The port number of the init container.
        self.port = port  # type: list[CreateContainerGroupRequestInitContainerPort]
        # The path of the file from which the system retrieves termination messages of the init container when the init container exits.
        self.termination_message_path = termination_message_path  # type: str
        # The message notification policy. This parameter is empty by default.
        self.termination_message_policy = termination_message_policy  # type: str
        # The information about the volume that you want to mount on the init container.
        self.volume_mount = volume_mount  # type: list[CreateContainerGroupRequestInitContainerVolumeMount]
        # The working directory of the init container.
        self.working_dir = working_dir  # type: str

    def validate(self):
        if self.security_context:
            self.security_context.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestInitContainer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.termination_message_path is not None:
            result['TerminationMessagePath'] = self.termination_message_path
        if self.termination_message_policy is not None:
            result['TerminationMessagePolicy'] = self.termination_message_policy
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestInitContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = CreateContainerGroupRequestInitContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = CreateContainerGroupRequestInitContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('TerminationMessagePath') is not None:
            self.termination_message_path = m.get('TerminationMessagePath')
        if m.get('TerminationMessagePolicy') is not None:
            self.termination_message_policy = m.get('TerminationMessagePolicy')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = CreateContainerGroupRequestInitContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateContainerGroupRequestOverheadReservationOption(TeaModel):
    def __init__(self, enable_overhead_reservation=None):
        # Specify whether to enable the overhead reservation feature. Default: false. Valid values: true and false. After you enable the overhead reservation feature, the system automatically adds the overhead to the specification of the elastic container instance, and then adjusts the specification of the instance upward to the most approximate specification. You are charged based on the new specification after the adjustment.
        self.enable_overhead_reservation = enable_overhead_reservation  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestOverheadReservationOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_overhead_reservation is not None:
            result['EnableOverheadReservation'] = self.enable_overhead_reservation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableOverheadReservation') is not None:
            self.enable_overhead_reservation = m.get('EnableOverheadReservation')
        return self


class CreateContainerGroupRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of a tag. The tag key cannot be an empty string and must be unique. The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The value of a tag. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestTag, self).to_map()
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


class CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath(TeaModel):
    def __init__(self, content=None, mode=None, path=None):
        self.content = content  # type: str
        self.mode = mode  # type: int
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateContainerGroupRequestVolumeConfigFileVolume(TeaModel):
    def __init__(self, config_file_to_path=None, default_mode=None):
        self.config_file_to_path = config_file_to_path  # type: list[CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath]
        self.default_mode = default_mode  # type: int

    def validate(self):
        if self.config_file_to_path:
            for k in self.config_file_to_path:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestVolumeConfigFileVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigFileToPath'] = []
        if self.config_file_to_path is not None:
            for k in self.config_file_to_path:
                result['ConfigFileToPath'].append(k.to_map() if k else None)
        if self.default_mode is not None:
            result['DefaultMode'] = self.default_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_file_to_path = []
        if m.get('ConfigFileToPath') is not None:
            for k in m.get('ConfigFileToPath'):
                temp_model = CreateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath()
                self.config_file_to_path.append(temp_model.from_map(k))
        if m.get('DefaultMode') is not None:
            self.default_mode = m.get('DefaultMode')
        return self


class CreateContainerGroupRequestVolumeDiskVolume(TeaModel):
    def __init__(self, disk_id=None, disk_size=None, fs_type=None):
        self.disk_id = disk_id  # type: str
        self.disk_size = disk_size  # type: int
        self.fs_type = fs_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestVolumeDiskVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        return self


class CreateContainerGroupRequestVolumeEmptyDirVolume(TeaModel):
    def __init__(self, medium=None, size_limit=None):
        self.medium = medium  # type: str
        self.size_limit = size_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestVolumeEmptyDirVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        return self


class CreateContainerGroupRequestVolumeFlexVolume(TeaModel):
    def __init__(self, driver=None, fs_type=None, options=None):
        self.driver = driver  # type: str
        self.fs_type = fs_type  # type: str
        self.options = options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestVolumeFlexVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class CreateContainerGroupRequestVolumeHostPathVolume(TeaModel):
    def __init__(self, path=None, type=None):
        self.path = path  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestVolumeHostPathVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateContainerGroupRequestVolumeNFSVolume(TeaModel):
    def __init__(self, path=None, read_only=None, server=None):
        self.path = path  # type: str
        self.read_only = read_only  # type: bool
        self.server = server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupRequestVolumeNFSVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class CreateContainerGroupRequestVolume(TeaModel):
    def __init__(self, config_file_volume=None, disk_volume=None, empty_dir_volume=None, flex_volume=None,
                 host_path_volume=None, nfsvolume=None, name=None, type=None):
        self.config_file_volume = config_file_volume  # type: CreateContainerGroupRequestVolumeConfigFileVolume
        self.disk_volume = disk_volume  # type: CreateContainerGroupRequestVolumeDiskVolume
        self.empty_dir_volume = empty_dir_volume  # type: CreateContainerGroupRequestVolumeEmptyDirVolume
        self.flex_volume = flex_volume  # type: CreateContainerGroupRequestVolumeFlexVolume
        self.host_path_volume = host_path_volume  # type: CreateContainerGroupRequestVolumeHostPathVolume
        self.nfsvolume = nfsvolume  # type: CreateContainerGroupRequestVolumeNFSVolume
        # The name of the volume.
        self.name = name  # type: str
        # The type of the volume when you set the Type parameter to HostPathVolume. Valid values:
        # 
        # *   Directory
        # *   File
        self.type = type  # type: str

    def validate(self):
        if self.config_file_volume:
            self.config_file_volume.validate()
        if self.disk_volume:
            self.disk_volume.validate()
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()
        if self.flex_volume:
            self.flex_volume.validate()
        if self.host_path_volume:
            self.host_path_volume.validate()
        if self.nfsvolume:
            self.nfsvolume.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequestVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_volume is not None:
            result['ConfigFileVolume'] = self.config_file_volume.to_map()
        if self.disk_volume is not None:
            result['DiskVolume'] = self.disk_volume.to_map()
        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()
        if self.flex_volume is not None:
            result['FlexVolume'] = self.flex_volume.to_map()
        if self.host_path_volume is not None:
            result['HostPathVolume'] = self.host_path_volume.to_map()
        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigFileVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeConfigFileVolume()
            self.config_file_volume = temp_model.from_map(m['ConfigFileVolume'])
        if m.get('DiskVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeDiskVolume()
            self.disk_volume = temp_model.from_map(m['DiskVolume'])
        if m.get('EmptyDirVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m['EmptyDirVolume'])
        if m.get('FlexVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeFlexVolume()
            self.flex_volume = temp_model.from_map(m['FlexVolume'])
        if m.get('HostPathVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeHostPathVolume()
            self.host_path_volume = temp_model.from_map(m['HostPathVolume'])
        if m.get('NFSVolume') is not None:
            temp_model = CreateContainerGroupRequestVolumeNFSVolume()
            self.nfsvolume = temp_model.from_map(m['NFSVolume'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateContainerGroupRequest(TeaModel):
    def __init__(self, dns_config=None, host_security_context=None, security_context=None, acr_registry_info=None,
                 active_deadline_seconds=None, auto_create_eip=None, auto_match_image_cache=None, client_token=None, compute_category=None,
                 container=None, container_group_name=None, container_resource_view=None, core_pattern=None, cpu=None,
                 cpu_architecture=None, cpu_options_core=None, cpu_options_numa=None, cpu_options_threads_per_core=None,
                 data_cache_bucket=None, data_cache_bursting_enabled=None, data_cache_pl=None, data_cache_provisioned_iops=None,
                 dns_policy=None, dry_run=None, egress_bandwidth=None, eip_bandwidth=None, eip_common_bandwidth_package=None,
                 eip_isp=None, eip_instance_id=None, ephemeral_storage=None, fixed_ip=None, fixed_ip_retain_hour=None,
                 gpu_driver_version=None, host_aliase=None, host_name=None, image_accelerate_mode=None,
                 image_registry_credential=None, image_snapshot_id=None, ingress_bandwidth=None, init_container=None, insecure_registry=None,
                 instance_type=None, ipv_6address_count=None, ipv_6gateway_bandwidth=None, ipv_6gateway_bandwidth_enable=None,
                 memory=None, ntp_server=None, os_type=None, overhead_reservation_option=None, owner_account=None,
                 owner_id=None, plain_http_registry=None, private_ip_address=None, ram_role_name=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, restart_policy=None,
                 schedule_strategy=None, security_group_id=None, share_process_namespace=None, spot_duration=None,
                 spot_price_limit=None, spot_strategy=None, strict_spot=None, tag=None, termination_grace_period_seconds=None,
                 v_switch_id=None, volume=None, zone_id=None):
        self.dns_config = dns_config  # type: CreateContainerGroupRequestDnsConfig
        self.host_security_context = host_security_context  # type: CreateContainerGroupRequestHostSecurityContext
        self.security_context = security_context  # type: CreateContainerGroupRequestSecurityContext
        # The information about the Container Registry Enterprise Edition instance. For more information, see [Pull images from a Container Registry Enterprise Edition instance without using secrets](~~194250~~).
        self.acr_registry_info = acr_registry_info  # type: list[CreateContainerGroupRequestAcrRegistryInfo]
        # The validity period of the elastic container instance. When this period expires, the instance is forced to exit. Unit: seconds.
        self.active_deadline_seconds = active_deadline_seconds  # type: long
        # Specifies whether to automatically create an EIP and associate it with the elastic container instance.
        self.auto_create_eip = auto_create_eip  # type: bool
        # Specifies whether to automatically match image caches. Default value: false.
        self.auto_match_image_cache = auto_match_image_cache  # type: bool
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency of requests?](~~25693~~)
        self.client_token = client_token  # type: str
        # The computing power type of the instance.
        self.compute_category = compute_category  # type: list[str]
        # The information about the containers.
        self.container = container  # type: list[CreateContainerGroupRequestContainer]
        # The name of the elastic container instance. Format requirements:
        # 
        # *   The name must be 2 to 128 characters in length
        # *   The name can contain lowercase letters, digits, and hyphens (-). It cannot start or end with a hyphen (-).
        self.container_group_name = container_group_name  # type: str
        # Specifies whether to enable container resource view. Container resource view displays the actual container resource data instead of data of the host. If the specifications of the generated elastic container instance are larger than the specifications that you request for when you create the instance, you can enable the ContainerResourceView feature to ensure that the resources that you view in the container are the same as the resources that you request for.
        self.container_resource_view = container_resource_view  # type: bool
        # The path to store core dump files. For more information, see [Save core files to volumes](~~167801~~).
        # 
        # > The path cannot start with a vertical bar (`|`). You cannot use core dump files to configure executable programs.
        self.core_pattern = core_pattern  # type: str
        # The number of vCPUs that you want to allocate to the elastic container instance.
        self.cpu = cpu  # type: float
        # The CPU architecture of the instance. Default value: AMD64. Valid values:
        # 
        # *   AMD64
        # *   ARM64
        self.cpu_architecture = cpu_architecture  # type: str
        # The number of physical CPU cores. You can specify this parameter only for specific instance types. For more information, see [Specify custom CPU options](~~197781~~).
        self.cpu_options_core = cpu_options_core  # type: int
        # This parameter is not available.
        self.cpu_options_numa = cpu_options_numa  # type: str
        # The number of threads per core. You can specify this parameter only for specific instance types. If you set this parameter to 1, Hyper-Threading is disabled. For more information, see [Specify custom CPU options](~~197781~~).
        self.cpu_options_threads_per_core = cpu_options_threads_per_core  # type: int
        # The bucket to store data caches.
        self.data_cache_bucket = data_cache_bucket  # type: str
        # Specifies whether to enable the performance burst feature when ESSDs AutoPL are used for data caching. For more information, see [ESSDs AutoPL](~~368372~~).
        self.data_cache_bursting_enabled = data_cache_bursting_enabled  # type: bool
        # The performance level of the disk used by data caches.\
        # Enhanced SSDs (ESSDs) are preferentially used. The default performance level is PL1.
        self.data_cache_pl = data_cache_pl  # type: str
        # The input/output operations per second (IOPS) provisioned for ESSDs AutoPL when ESSDs AutoPL are used for data caching.\
        # Valid values: 0 to min{50000, 1000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.\
        # For more information, see [ESSDs AutoPL](~~368372~~).
        self.data_cache_provisioned_iops = data_cache_provisioned_iops  # type: long
        # The Domain Name System (DNS) policy. Valid values:
        # 
        # *   None: uses the DNS that is specified for DnsConfig-related parameters.
        # *   Default: uses the DNS that is specified for the runtime environment.
        self.dns_policy = dns_policy  # type: str
        # Specifies whether to perform only a dry run without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run without creating an elastic container instance. The check items include the request format, service limits, resource inventory, and whether the required parameters are specified. If the request fails the dry run, an error is returned. If the request passes the dry run, the DryRun.Success error code is returned.
        # *   false (default): performs a dry run, and creates an elastic container instance after the request passes the dry run.
        self.dry_run = dry_run  # type: bool
        # The maximum outbound bandwidth. Unit: bytes.
        self.egress_bandwidth = egress_bandwidth  # type: long
        # The bandwidth of the EIP. Unit: Mbit/s. Default value: 5.\
        # You can specify this parameter when you set AutoCreateEip to true.
        self.eip_bandwidth = eip_bandwidth  # type: int
        # Specifies the EIP bandwidth plan that you want to use.
        self.eip_common_bandwidth_package = eip_common_bandwidth_package  # type: str
        # The line type of the elastic IP address (EIP). Valid values:
        # 
        # *   BGP: BGP (Multi-ISP) lines
        # *   BGP_PRO: BGP (Multi-ISP) Pro lines
        self.eip_isp = eip_isp  # type: str
        # The ID of the elastic IP address (EIP).
        self.eip_instance_id = eip_instance_id  # type: str
        # The increased storage capacity of the temporary storage space. Unit: GiB.\
        # For more information, see [Increase the storage capacity of the temporary storage space](~~204066~~).
        self.ephemeral_storage = ephemeral_storage  # type: int
        # Specifies whether to configure the instance to use a fixed IP address. For more information, see [Configure an elastic container instance to use a fixed IP address](~~2381086~~).
        self.fixed_ip = fixed_ip  # type: str
        # The retention period of the fixed IP address after the original instance is released and the fixed IP address becomes idle. Unit: hours. Default value: 48.
        self.fixed_ip_retain_hour = fixed_ip_retain_hour  # type: int
        self.gpu_driver_version = gpu_driver_version  # type: str
        # The alias of the elastic container instance.
        self.host_aliase = host_aliase  # type: list[CreateContainerGroupRequestHostAliase]
        # The hostname of the instance.
        self.host_name = host_name  # type: str
        # The image acceleration mode. Valid values:
        # 
        # *   nydus: Nydus is used to accelerate image pulling. The images must support Nydus.
        # *   dadi: DADI is used to accelerate image pulling. The images must support DADI.
        # *   p2p: P2P is used to accelerate image pulling. The images must support P2P.
        # *   imc: Image caches are used to accelerate image pulling.
        self.image_accelerate_mode = image_accelerate_mode  # type: str
        # The information about the image repository.
        self.image_registry_credential = image_registry_credential  # type: list[CreateContainerGroupRequestImageRegistryCredential]
        # The ID of the image cache. For more information, see [Use image caches to accelerate the creation of instances](~~141281~~).
        self.image_snapshot_id = image_snapshot_id  # type: str
        # The maximum inbound bandwidth. Unit: bytes.
        self.ingress_bandwidth = ingress_bandwidth  # type: long
        # The information about the init containers.
        self.init_container = init_container  # type: list[CreateContainerGroupRequestInitContainer]
        # The address of the self-managed image repository. When you create an elastic container instance by using an image in a self-managed image repository that uses a self-signed certificate, you must specify this parameter to skip the certificate authentication. This prevents image pull failures caused by certificate authentication failures.
        self.insecure_registry = insecure_registry  # type: str
        # The ECS instance type. Different instance types are supported. For more information, see [Specify an ECS instance type to create an elastic container instance](~~114664~~).
        self.instance_type = instance_type  # type: str
        # The number of IPv6 addresses. Set the value to 1. You can assign only one IPv6 address to an elastic container instance.
        self.ipv_6address_count = ipv_6address_count  # type: int
        # The peak Internet bandwidth of the IPv6 address when the Ipv6GatewayBandwidthEnable parameter is set to true. Valid values:
        # 
        # *   If the billing method for the Internet bandwidth of the IPv6 gateway is pay-by-bandwidth, the Internet bandwidth of the IPv6 address ranges from 1 to 2,000 Mbit/s.
        # 
        # *   If the billing method for the Internet bandwidth of the IPv6 gateway is pay-by-traffic, the Internet bandwidth range of the IPv6 address is based on the edition of the IPv6 gateway.
        # 
        #     *   If the IPv6 gateway is of Free Edition, the Internet bandwidth of the IPv6 address ranges from 1 to 200 Mbit/s.
        #     *   If the IPv6 gateway is of Enterprise Edition, the Internet bandwidth of the IPv6 address ranges from 1 to 500 Mbit/s.
        #     *   If the IPv6 gateway is of Enhanced Enterprise Edition, the Internet bandwidth of the IPv6 address ranges from 1 to 1,000 Mbit/s.
        # 
        # The default value is the maximum value in the Internet bandwidth range of the IPv6 gateway.
        self.ipv_6gateway_bandwidth = ipv_6gateway_bandwidth  # type: str
        # Specifies whether to enable IPv6 Internet access for the elastic container instance.
        self.ipv_6gateway_bandwidth_enable = ipv_6gateway_bandwidth_enable  # type: bool
        # The memory size that you want to allocate to the elastic container instance. Unit: GiB.
        self.memory = memory  # type: float
        # The domain names of the NTP server.
        self.ntp_server = ntp_server  # type: list[str]
        # The operating system of the elastic container instance. Default value: Linux. Valid values:
        # 
        # *   Linux
        # *   Windows
        # 
        # >  Windows instances are in invitational preview. To use the operating system, submit a ticket.
        self.os_type = os_type  # type: str
        # The options that you can configure when you enable the overhead reservation feature.
        self.overhead_reservation_option = overhead_reservation_option  # type: CreateContainerGroupRequestOverheadReservationOption
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The address of the self-managed image repository. When you create an elastic container instance by using an image in a self-managed image repository that uses the HTTP protocol, you must specify this parameter. This allows Elastic Container Instance to pull the image over the HTTP protocol instead over the default HTTPS protocol. This prevents image pull failures caused by different protocols.
        self.plain_http_registry = plain_http_registry  # type: str
        # The private IP address of the elastic container instance. Only IPv4 addresses are supported. Make sure that the IP address is idle.
        self.private_ip_address = private_ip_address  # type: str
        # The name of the RAM role that you want to associate with the elastic container instance. You can use the RAM role to access elastic container instances and ECS instances. For more information, see [Use an instance RAM role by calling API operations](~~61178~~).
        self.ram_role_name = ram_role_name  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The restart policy of the elastic container instance. Valid values:
        # 
        # *   Always: Always restarts the instance.
        # *   Never: Never restarts the instance.
        # *   OnFailure: Restarts the instance when the last start failed.
        # 
        # Default value: Always.
        self.restart_policy = restart_policy  # type: str
        # The resource scheduling policy when you specify multiple zones to create an elastic container instance. To specify multiple zones, you can use the VSwitchId to specify multiple vSwitches. Valid values:
        # 
        # *   VSwitchOrdered: The system schedules resources in the sequence of the vSwitches.
        # *   VSwitchRandom: The system schedules resources at random.
        # 
        # For more information, see [Specify multiple zones to create an elastic container instance](~~157290~~).
        self.schedule_strategy = schedule_strategy  # type: str
        # The ID of the security group to which the instance is assigned. Instances within the same security group can access each other.
        # 
        # If you do not specify a security group, the system automatically uses the default security group in the region that you selected. Make sure that the inbound rules of the security group contain the container protocols and port numbers that you want to expose. If you do not have a default security group in the region, the system creates a default security group, and then adds the container protocols and port numbers that you specified to the inbound rules of the security group.
        self.security_group_id = security_group_id  # type: str
        # Specifies whether to use a shared namespace. Default value: false.
        self.share_process_namespace = share_process_namespace  # type: bool
        # The protection period of the preemptible instance. Unit: hours. Default value: 1. A value of 0 indicates no protection period.
        self.spot_duration = spot_duration  # type: long
        # The maximum hourly price of the preemptible elastic container instance. The value can contain up to three decimal places.
        # 
        # If you set SpotStrategy to SpotWithPriceLimit, you must specify SpotPriceLimit.
        self.spot_price_limit = spot_price_limit  # type: float
        # The bidding policy for the instance. Valid values:
        # 
        # *   NoSpot: The instance is created as a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is created as a preemptible instance with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is created as a preemptible instance whose bidding price is based on the market price at the time of purchase.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy  # type: str
        # Specifies whether to enable periodical execution.
        # 
        # *   true: enables periodical execution.
        # *   false: disables periodical execution.
        self.strict_spot = strict_spot  # type: bool
        # The tags that you want to bind with the instance. You can bind a maximum of 20 tags. For more information, see [Use tags to manage elastic container instances](~~146608~~).
        self.tag = tag  # type: list[CreateContainerGroupRequestTag]
        # The buffer time during which the program handles operations before the program stops. Unit: seconds.
        self.termination_grace_period_seconds = termination_grace_period_seconds  # type: long
        # The ID of the vSwitch to which the instance is connected. You can specify up to 10 vSwitch IDs. Separate multiple vSwitch IDs with commas (,). Example: `vsw-***,vsw-***`.
        # 
        # If no vSwitch is specified, the system automatically uses the default vSwitch in the default VPC in the region that you selected. If you do not have a default VPC or a default vSwitch in the region, the system automatically creates a default VPC and a default vSwitch.
        # 
        # > The number of IP addresses in the vSwitch CIDR block determines the maximum number of elastic container instances that can be created for the vSwitch. Before you create elastic container instances, plan the CIDR block of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # Information about volumes.
        self.volume = volume  # type: list[CreateContainerGroupRequestVolume]
        # The ID of the zone in which the elastic container instance is deployed. If you do not specify this parameter, the system selects a zone.
        # 
        # This parameter is empty by default.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.dns_config:
            self.dns_config.validate()
        if self.host_security_context:
            self.host_security_context.validate()
        if self.security_context:
            self.security_context.validate()
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()
        if self.container:
            for k in self.container:
                if k:
                    k.validate()
        if self.host_aliase:
            for k in self.host_aliase:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.init_container:
            for k in self.init_container:
                if k:
                    k.validate()
        if self.overhead_reservation_option:
            self.overhead_reservation_option.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.volume:
            for k in self.volume:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateContainerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        if self.host_security_context is not None:
            result['HostSecurityContext'] = self.host_security_context.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        if self.active_deadline_seconds is not None:
            result['ActiveDeadlineSeconds'] = self.active_deadline_seconds
        if self.auto_create_eip is not None:
            result['AutoCreateEip'] = self.auto_create_eip
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compute_category is not None:
            result['ComputeCategory'] = self.compute_category
        result['Container'] = []
        if self.container is not None:
            for k in self.container:
                result['Container'].append(k.to_map() if k else None)
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        if self.container_resource_view is not None:
            result['ContainerResourceView'] = self.container_resource_view
        if self.core_pattern is not None:
            result['CorePattern'] = self.core_pattern
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_architecture is not None:
            result['CpuArchitecture'] = self.cpu_architecture
        if self.cpu_options_core is not None:
            result['CpuOptionsCore'] = self.cpu_options_core
        if self.cpu_options_numa is not None:
            result['CpuOptionsNuma'] = self.cpu_options_numa
        if self.cpu_options_threads_per_core is not None:
            result['CpuOptionsThreadsPerCore'] = self.cpu_options_threads_per_core
        if self.data_cache_bucket is not None:
            result['DataCacheBucket'] = self.data_cache_bucket
        if self.data_cache_bursting_enabled is not None:
            result['DataCacheBurstingEnabled'] = self.data_cache_bursting_enabled
        if self.data_cache_pl is not None:
            result['DataCachePL'] = self.data_cache_pl
        if self.data_cache_provisioned_iops is not None:
            result['DataCacheProvisionedIops'] = self.data_cache_provisioned_iops
        if self.dns_policy is not None:
            result['DnsPolicy'] = self.dns_policy
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.egress_bandwidth is not None:
            result['EgressBandwidth'] = self.egress_bandwidth
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.eip_common_bandwidth_package is not None:
            result['EipCommonBandwidthPackage'] = self.eip_common_bandwidth_package
        if self.eip_isp is not None:
            result['EipISP'] = self.eip_isp
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        if self.fixed_ip is not None:
            result['FixedIp'] = self.fixed_ip
        if self.fixed_ip_retain_hour is not None:
            result['FixedIpRetainHour'] = self.fixed_ip_retain_hour
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        result['HostAliase'] = []
        if self.host_aliase is not None:
            for k in self.host_aliase:
                result['HostAliase'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_accelerate_mode is not None:
            result['ImageAccelerateMode'] = self.image_accelerate_mode
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        if self.image_snapshot_id is not None:
            result['ImageSnapshotId'] = self.image_snapshot_id
        if self.ingress_bandwidth is not None:
            result['IngressBandwidth'] = self.ingress_bandwidth
        result['InitContainer'] = []
        if self.init_container is not None:
            for k in self.init_container:
                result['InitContainer'].append(k.to_map() if k else None)
        if self.insecure_registry is not None:
            result['InsecureRegistry'] = self.insecure_registry
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.ipv_6gateway_bandwidth is not None:
            result['Ipv6GatewayBandwidth'] = self.ipv_6gateway_bandwidth
        if self.ipv_6gateway_bandwidth_enable is not None:
            result['Ipv6GatewayBandwidthEnable'] = self.ipv_6gateway_bandwidth_enable
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.ntp_server is not None:
            result['NtpServer'] = self.ntp_server
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.overhead_reservation_option is not None:
            result['OverheadReservationOption'] = self.overhead_reservation_option.to_map()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plain_http_registry is not None:
            result['PlainHttpRegistry'] = self.plain_http_registry
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.schedule_strategy is not None:
            result['ScheduleStrategy'] = self.schedule_strategy
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.share_process_namespace is not None:
            result['ShareProcessNamespace'] = self.share_process_namespace
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.strict_spot is not None:
            result['StrictSpot'] = self.strict_spot
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        result['Volume'] = []
        if self.volume is not None:
            for k in self.volume:
                result['Volume'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsConfig') is not None:
            temp_model = CreateContainerGroupRequestDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        if m.get('HostSecurityContext') is not None:
            temp_model = CreateContainerGroupRequestHostSecurityContext()
            self.host_security_context = temp_model.from_map(m['HostSecurityContext'])
        if m.get('SecurityContext') is not None:
            temp_model = CreateContainerGroupRequestSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = CreateContainerGroupRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        if m.get('ActiveDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('ActiveDeadlineSeconds')
        if m.get('AutoCreateEip') is not None:
            self.auto_create_eip = m.get('AutoCreateEip')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ComputeCategory') is not None:
            self.compute_category = m.get('ComputeCategory')
        self.container = []
        if m.get('Container') is not None:
            for k in m.get('Container'):
                temp_model = CreateContainerGroupRequestContainer()
                self.container.append(temp_model.from_map(k))
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        if m.get('ContainerResourceView') is not None:
            self.container_resource_view = m.get('ContainerResourceView')
        if m.get('CorePattern') is not None:
            self.core_pattern = m.get('CorePattern')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuArchitecture') is not None:
            self.cpu_architecture = m.get('CpuArchitecture')
        if m.get('CpuOptionsCore') is not None:
            self.cpu_options_core = m.get('CpuOptionsCore')
        if m.get('CpuOptionsNuma') is not None:
            self.cpu_options_numa = m.get('CpuOptionsNuma')
        if m.get('CpuOptionsThreadsPerCore') is not None:
            self.cpu_options_threads_per_core = m.get('CpuOptionsThreadsPerCore')
        if m.get('DataCacheBucket') is not None:
            self.data_cache_bucket = m.get('DataCacheBucket')
        if m.get('DataCacheBurstingEnabled') is not None:
            self.data_cache_bursting_enabled = m.get('DataCacheBurstingEnabled')
        if m.get('DataCachePL') is not None:
            self.data_cache_pl = m.get('DataCachePL')
        if m.get('DataCacheProvisionedIops') is not None:
            self.data_cache_provisioned_iops = m.get('DataCacheProvisionedIops')
        if m.get('DnsPolicy') is not None:
            self.dns_policy = m.get('DnsPolicy')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EgressBandwidth') is not None:
            self.egress_bandwidth = m.get('EgressBandwidth')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EipCommonBandwidthPackage') is not None:
            self.eip_common_bandwidth_package = m.get('EipCommonBandwidthPackage')
        if m.get('EipISP') is not None:
            self.eip_isp = m.get('EipISP')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        if m.get('FixedIp') is not None:
            self.fixed_ip = m.get('FixedIp')
        if m.get('FixedIpRetainHour') is not None:
            self.fixed_ip_retain_hour = m.get('FixedIpRetainHour')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        self.host_aliase = []
        if m.get('HostAliase') is not None:
            for k in m.get('HostAliase'):
                temp_model = CreateContainerGroupRequestHostAliase()
                self.host_aliase.append(temp_model.from_map(k))
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageAccelerateMode') is not None:
            self.image_accelerate_mode = m.get('ImageAccelerateMode')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = CreateContainerGroupRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        if m.get('ImageSnapshotId') is not None:
            self.image_snapshot_id = m.get('ImageSnapshotId')
        if m.get('IngressBandwidth') is not None:
            self.ingress_bandwidth = m.get('IngressBandwidth')
        self.init_container = []
        if m.get('InitContainer') is not None:
            for k in m.get('InitContainer'):
                temp_model = CreateContainerGroupRequestInitContainer()
                self.init_container.append(temp_model.from_map(k))
        if m.get('InsecureRegistry') is not None:
            self.insecure_registry = m.get('InsecureRegistry')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('Ipv6GatewayBandwidth') is not None:
            self.ipv_6gateway_bandwidth = m.get('Ipv6GatewayBandwidth')
        if m.get('Ipv6GatewayBandwidthEnable') is not None:
            self.ipv_6gateway_bandwidth_enable = m.get('Ipv6GatewayBandwidthEnable')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NtpServer') is not None:
            self.ntp_server = m.get('NtpServer')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OverheadReservationOption') is not None:
            temp_model = CreateContainerGroupRequestOverheadReservationOption()
            self.overhead_reservation_option = temp_model.from_map(m['OverheadReservationOption'])
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlainHttpRegistry') is not None:
            self.plain_http_registry = m.get('PlainHttpRegistry')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('ScheduleStrategy') is not None:
            self.schedule_strategy = m.get('ScheduleStrategy')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('ShareProcessNamespace') is not None:
            self.share_process_namespace = m.get('ShareProcessNamespace')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('StrictSpot') is not None:
            self.strict_spot = m.get('StrictSpot')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateContainerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        self.volume = []
        if m.get('Volume') is not None:
            for k in m.get('Volume'):
                temp_model = CreateContainerGroupRequestVolume()
                self.volume.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateContainerGroupResponseBody(TeaModel):
    def __init__(self, container_group_id=None, request_id=None):
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContainerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateContainerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateContainerGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateContainerGroupResponse, self).to_map()
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
            temp_model = CreateContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataCacheRequestDataSource(TeaModel):
    def __init__(self, options=None, type=None):
        # The parameters that are configured for the data source.
        self.options = options  # type: dict[str, str]
        # The type of the data source. Valid values:
        # 
        # *   URL
        # *   NAS
        # *   OSS
        # *   SNAPSHOT
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataCacheRequestDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['Options'] = self.options
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDataCacheRequestEipCreateParam(TeaModel):
    def __init__(self, bandwidth=None, common_bandwidth_package=None, isp=None, internet_charge_type=None,
                 public_ip_address_pool_id=None):
        # The bandwidth of the EIP. Unit: Mbit/s. Default value: 5.
        self.bandwidth = bandwidth  # type: int
        # The EIP bandwidth plan to be associated.
        self.common_bandwidth_package = common_bandwidth_package  # type: str
        # The line type of the EIP. Valid values:
        # 
        # *   BGP: BGP (Multi-ISP) line
        # *   BGP_PRO: BGP (Multi-ISP) Pro line
        self.isp = isp  # type: str
        # The metering method of the EIP. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth
        # *   PayByTraffic: pay-by-data-transfer
        self.internet_charge_type = internet_charge_type  # type: str
        # The ID of the IP address pool. The EIP is allocated from the IP address pool. You cannot use the IP address pool feature by default. To use this feature, you must apply for the privilege in the Quota Center console.
        self.public_ip_address_pool_id = public_ip_address_pool_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataCacheRequestEipCreateParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.common_bandwidth_package is not None:
            result['CommonBandwidthPackage'] = self.common_bandwidth_package
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CommonBandwidthPackage') is not None:
            self.common_bandwidth_package = m.get('CommonBandwidthPackage')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')
        return self


class CreateDataCacheRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataCacheRequestTag, self).to_map()
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


class CreateDataCacheRequest(TeaModel):
    def __init__(self, bucket=None, client_token=None, data_source=None, eip_create_param=None,
                 eip_instance_id=None, name=None, owner_account=None, owner_id=None, path=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, retention_days=None,
                 security_group_id=None, size=None, tag=None, v_switch_id=None):
        # The bucket in which the data is stored. By default, the default bucket is used. You can use a custom bucket for business grouping and to prevent path conflicts.
        # 
        # >  eci-system is the reserved bucket of the ECI and cannot be used.
        self.bucket = bucket  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The data source.
        self.data_source = data_source  # type: CreateDataCacheRequestDataSource
        # The elastic IP address (EIP) to be created and associated. If no NAT gateway is configured for the virtual private cloud (VPC), you can associate an EIP to pull data from the Internet.
        self.eip_create_param = eip_create_param  # type: CreateDataCacheRequestEipCreateParam
        # The existing elastic IP address (EIP) to be associated. If no NAT gateway is configured for the virtual private cloud (VPC), you can associate an EIP to pull data from the Internet.
        self.eip_instance_id = eip_instance_id  # type: str
        # The DataCache name.
        self.name = name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The storage path of the data.
        self.path = path  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The number of days for which the DataCache is retained. When the retention days end, the DataCache is deleted. By default, DataCaches do not expire.
        self.retention_days = retention_days  # type: int
        # The ID of the security group to which the generated ECI belongs during the creation of the data cache.
        self.security_group_id = security_group_id  # type: str
        # The size of the data cache. Unit: GiB. Default value: 20. Evaluate the required size based on the actual data size.
        self.size = size  # type: int
        # The tags to be bound to the data cache.
        self.tag = tag  # type: list[CreateDataCacheRequestTag]
        # The ID of the vSwitch to which the generated ECI belongs during the creation of the data cache.
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.eip_create_param:
            self.eip_create_param.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDataCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.eip_create_param is not None:
            result['EipCreateParam'] = self.eip_create_param.to_map()
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.size is not None:
            result['Size'] = self.size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataSource') is not None:
            temp_model = CreateDataCacheRequestDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('EipCreateParam') is not None:
            temp_model = CreateDataCacheRequestEipCreateParam()
            self.eip_create_param = temp_model.from_map(m['EipCreateParam'])
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDataCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateDataCacheResponseBody(TeaModel):
    def __init__(self, data_cache_id=None, request_id=None):
        # The DataCache ID.
        self.data_cache_id = data_cache_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataCacheResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDataCacheResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataCacheResponse, self).to_map()
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
            temp_model = CreateDataCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageCacheRequestAcrRegistryInfo(TeaModel):
    def __init__(self, arn_service=None, arn_user=None, domain=None, instance_id=None, instance_name=None,
                 region_id=None):
        # The Alibaba Cloud Resource Name (ARN) of the RAM roles in the Alibaba Cloud account to which the elastic container instance belongs.
        self.arn_service = arn_service  # type: str
        # The ARN of the RAM roles in the Alibaba Cloud account to which the Container Registry Enterprise Edition instance belongs.
        self.arn_user = arn_user  # type: str
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. You can specify multiple domain names. Separate multiple domain names with commas (,).
        self.domain = domain  # type: list[str]
        # The ID of Container Registry Enterprise Edition instance N.
        self.instance_id = instance_id  # type: str
        # The name of Container Registry Enterprise Edition instance N.
        self.instance_name = instance_name  # type: str
        # The region ID of Container Registry Enterprise Edition instance N.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageCacheRequestAcrRegistryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn_service is not None:
            result['ArnService'] = self.arn_service
        if self.arn_user is not None:
            result['ArnUser'] = self.arn_user
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArnService') is not None:
            self.arn_service = m.get('ArnService')
        if m.get('ArnUser') is not None:
            self.arn_user = m.get('ArnUser')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateImageCacheRequestImageRegistryCredential(TeaModel):
    def __init__(self, password=None, server=None, user_name=None):
        # The password that is used to log on to image repository N.
        self.password = password  # type: str
        # The address of the image repository without the `http://` or `https://` prefix.
        self.server = server  # type: str
        # The username that is used to log on to image repository N.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageCacheRequestImageRegistryCredential, self).to_map()
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


class CreateImageCacheRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N of the image cache. Valid values of N: 1 to 20.
        self.key = key  # type: str
        # The value of tag N of the image cache. Valid values of N: 1 to 20.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageCacheRequestTag, self).to_map()
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


class CreateImageCacheRequest(TeaModel):
    def __init__(self, acr_registry_info=None, annotations=None, auto_match_image_cache=None, client_token=None,
                 eip_instance_id=None, elimination_strategy=None, flash=None, flash_copy_count=None, image=None,
                 image_cache_name=None, image_cache_size=None, image_registry_credential=None, insecure_registry=None,
                 owner_account=None, owner_id=None, plain_http_registry=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, retention_days=None, security_group_id=None,
                 standard_copy_count=None, tag=None, v_switch_id=None, zone_id=None):
        # Information about the Container Registry Enterprise Edition instance. For more information, see [Pull images from a Container Registry Enterprise Edition instance without using secrets](~~194250~~).
        self.acr_registry_info = acr_registry_info  # type: list[CreateImageCacheRequestAcrRegistryInfo]
        # Comments.
        self.annotations = annotations  # type: str
        # Specifies whether to enable reuse of image cache layers. If you enable this feature, and the image cache that you want to create and an existing image cache contain duplicate image layers, the system reuses the duplicate image layers to create the new image cache. This accelerates the creation of the image cache. Valid values:
        # 
        # *   true: enables reuse of image cache layers.
        # *   false: disables reuse of image cache layers.
        # 
        # Default value: false.
        self.auto_match_image_cache = auto_match_image_cache  # type: bool
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the elastic IP address (EIP). If you want to pull images over the Internet, make sure that the elastic container instance can access the Internet. You can configure an EIP or a NAT gateway for the elastic container instance to access the Internet.
        self.eip_instance_id = eip_instance_id  # type: str
        # The elimination policy of the image cache. This parameter is empty by default, which indicates that the image cache is always retained.
        # 
        # You can set this parameter to LRU, which indicates that the image cache can be automatically deleted. When the number of image caches reaches the quota, the system automatically deletes the image caches whose EliminationStrategy parameter is set to LRU and that are least commonly used.
        self.elimination_strategy = elimination_strategy  # type: str
        # Specifies whether to enable the instant image cache feature. The feature can accelerate the creation of image caches. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.flash = flash  # type: bool
        # The number of temporary local snapshots. By default, the system creates one snapshot for each image cache. If an image cache is used to create multiple elastic container instances at a time, we recommend that you set this parameter to create multiple snapshots for the image cache. We recommend that you create one snapshot for creation of every 1,000 elastic container instances.
        # 
        # >  If you set the Flash parameter to true, instant image cache is enabled. During the creation of the image cache, the system first creates a temporary local snapshot for you to instantly use the snapshot. After the temporary local snapshot is created, the system begins to create a regular snapshot. After the regular snapshot is created, the temporary local snapshot is automatically deleted.
        self.flash_copy_count = flash_copy_count  # type: int
        # Container image N that is used to create the image cache.
        self.image = image  # type: list[str]
        # The name of the image cache.
        self.image_cache_name = image_cache_name  # type: str
        # The size of the image cache. Unit: GiB. Default value: 20.
        self.image_cache_size = image_cache_size  # type: int
        # The image repository.
        self.image_registry_credential = image_registry_credential  # type: list[CreateImageCacheRequestImageRegistryCredential]
        # The address of the self-managed image repository.
        # 
        # When you create an image cache by using an image in a self-managed image repository that uses a self-signed certificate, you must specify this parameter to skip the certificate authentication. This can prevent the image from failing to pull due to certificate authentication failures.
        self.insecure_registry = insecure_registry  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The address of the self-managed image repository. When you create an image cache by using an image in a self-managed image repository that uses the HTTP protocol, you must specify this parameter. This way, Elastic Container Instance uses the HTTP protocol instead of the default HTTPS protocol to pull the image. This can prevent the image from failing to pull due to different protocols.
        self.plain_http_registry = plain_http_registry  # type: str
        # The region ID of the image cache.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The retention period of the image cache. Unit: days. When the retention period ends, the image cache expires and is deleted. By default, image caches never expire.
        # 
        # >  The image caches that fail to be created are only retained for one day.
        self.retention_days = retention_days  # type: int
        # The ID of the security group.
        self.security_group_id = security_group_id  # type: str
        # The number of regular snapshots. By default, the system creates one snapshot for each image cache. If an image cache is used to create multiple elastic container instances at a time, we recommend that you set this parameter to create multiple snapshots for the image cache. We recommend that you create one snapshot for creation of every 1,000 elastic container instances.
        # 
        # >  If you set the Flash parameter to false, instant image cache is disabled. In this case, only regular snapshots are generated during the creation of the image cache.
        self.standard_copy_count = standard_copy_count  # type: int
        # The tag of the image cache.
        self.tag = tag  # type: list[CreateImageCacheRequestTag]
        # The ID of the vSwitch. You can specify up to 10 vSwitch IDs. Separate multiple vSwitch IDs with commas (,). Example: `vsw-***,vsw-***`.
        self.v_switch_id = v_switch_id  # type: str
        # The zone ID of the image cache.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateImageCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.elimination_strategy is not None:
            result['EliminationStrategy'] = self.elimination_strategy
        if self.flash is not None:
            result['Flash'] = self.flash
        if self.flash_copy_count is not None:
            result['FlashCopyCount'] = self.flash_copy_count
        if self.image is not None:
            result['Image'] = self.image
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.image_cache_size is not None:
            result['ImageCacheSize'] = self.image_cache_size
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        if self.insecure_registry is not None:
            result['InsecureRegistry'] = self.insecure_registry
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plain_http_registry is not None:
            result['PlainHttpRegistry'] = self.plain_http_registry
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.standard_copy_count is not None:
            result['StandardCopyCount'] = self.standard_copy_count
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = CreateImageCacheRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('EliminationStrategy') is not None:
            self.elimination_strategy = m.get('EliminationStrategy')
        if m.get('Flash') is not None:
            self.flash = m.get('Flash')
        if m.get('FlashCopyCount') is not None:
            self.flash_copy_count = m.get('FlashCopyCount')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('ImageCacheSize') is not None:
            self.image_cache_size = m.get('ImageCacheSize')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = CreateImageCacheRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        if m.get('InsecureRegistry') is not None:
            self.insecure_registry = m.get('InsecureRegistry')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlainHttpRegistry') is not None:
            self.plain_http_registry = m.get('PlainHttpRegistry')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StandardCopyCount') is not None:
            self.standard_copy_count = m.get('StandardCopyCount')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateImageCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateImageCacheResponseBody(TeaModel):
    def __init__(self, container_group_id=None, image_cache_id=None, request_id=None):
        # The ID of the intermediate elastic container instance that is used to create the image cache.
        self.container_group_id = container_group_id  # type: str
        # The ID of the image cache.
        self.image_cache_id = image_cache_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageCacheResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateImageCacheResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageCacheResponse, self).to_map()
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
            temp_model = CreateImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceOpsTaskRequest(TeaModel):
    def __init__(self, container_group_id=None, ops_type=None, ops_value=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        # The ID of the container group.
        self.container_group_id = container_group_id  # type: str
        # The type of the O&M task. Valid values:
        # 
        # *   coredump
        # *   tcpdump
        self.ops_type = ops_type  # type: str
        # The value of the O\&M task. You can set this parameter based on the value of OpsType.
        # 
        # *   If OpsType is set to coredump, the valid values of OpsValue are:
        # 
        #     *   enable: enables coredump.
        #     *   disable: disables coredump.
        # 
        # *   If OpsType is set to tcpdump, the value of OpsValue is a JSON-formatted parameter string. Example: `{"Enable":true, "IfDeviceName":"eth0"}`. The value may contain the following parameters:
        # 
        #     *   Enable: specifies whether to enable tcpdump. You must specify this parameter. Valid values: true and false.
        #     *   Protocol: the network protocol. Valid values: tcp, udp, and icmpv4.
        #     *   SourceIp: the source IP address.
        #     *   SourceCidr: the source CIDR block. If you specify both an IP address and a CIDR block, the IP address is ignored if the CIDR block is valid.
        #     *   SourcePort: the source port. Valid values: 1 to 65535.
        #     *   DestIp: the destination IP address.
        #     *   DestCidr: the destination CIDR block. If you specify both an IP address and a CIDR block, the IP address is ignored if the CIDR block is valid.
        #     *   DestPort: the destination port. Valid values: 1 to 65535.
        #     *   IfDeviceName: the destination network interface controller. Default value: eth0.
        #     *   Snaplen: the length to be captured. Default value: 65535. Unit: bytes.
        #     *   Duration: the captured period. Unit: seconds.
        #     *   PacketNum: the number of packets to be captured.
        #     *   FileSize: the size of the destination files on packets. Unit: bytes. Maximum value: 1073741824. 1073741824 bytes is equal to 1 GB.
        self.ops_value = ops_value  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the O&M task.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceOpsTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.ops_type is not None:
            result['OpsType'] = self.ops_type
        if self.ops_value is not None:
            result['OpsValue'] = self.ops_value
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')
        if m.get('OpsValue') is not None:
            self.ops_value = m.get('OpsValue')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateInstanceOpsTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The creation result of the O&M task.
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceOpsTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateInstanceOpsTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceOpsTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceOpsTaskResponse, self).to_map()
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
            temp_model = CreateInstanceOpsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualNodeRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVirtualNodeRequestTag, self).to_map()
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


class CreateVirtualNodeRequestTaint(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # The effect of taint N. Valid values of N: 1 to 20. Valid values:
        # 
        # - NoSchedule: No pods are scheduled to the nodes that have the taint.
        # - NoExecute: Existing pods in the node are evicted while no pods are scheduled to the nodes that have the taint.
        # - PreferNoSchedule: Pods are preferentially not scheduled to the nodes that have the taint.
        self.effect = effect  # type: str
        # The key of taint.
        self.key = key  # type: str
        # The value of taint.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVirtualNodeRequestTaint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateVirtualNodeRequest(TeaModel):
    def __init__(self, client_token=None, cluster_dns=None, cluster_domain=None, custom_resources=None,
                 eip_instance_id=None, enable_public_network=None, kube_config=None, owner_account=None, owner_id=None,
                 region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_group_id=None, tag=None, taint=None, tls_bootstrap_enabled=None, v_switch_id=None, virtual_node_name=None,
                 zone_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The IP address of the DNS server. If dnsPolicy=ClusterFirst is configured for the Elastic Container Instance pod, Elastic Container Instance uses the configuration to provide DNS services to containers. You can configure multiple IP addresses. Separate multiple IP addresses with commas (,).
        self.cluster_dns = cluster_dns  # type: str
        # The domain name of the cluster. If this parameter is specified, in addition to the search domain of the host, Kubelet configures all containers to search for the specified domain name.
        self.cluster_domain = cluster_domain  # type: str
        # The custom resources that are supported by the virtual node. If a custom resource is specified in the request of an Elastic Container Instance pod, the pod is scheduled to run on the virtual node that supports the custom resource. You can use the Resource name = Number of resources format to specify custom resources. Separate multiple resources with commas (,).
        self.custom_resources = custom_resources  # type: str
        # The ID of the elastic IP address (EIP).
        self.eip_instance_id = eip_instance_id  # type: str
        # Specifies whether to enable Internet access for the VNode. Default value: false.
        # 
        # If the value of this parameter is true, the VNode exposes a public IP address to external services.
        self.enable_public_network = enable_public_network  # type: bool
        # KubeConfig of the Kubernetes cluster to which the VNode is to be connected. The value must be Base64-encoded.
        self.kube_config = kube_config  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the virtual node.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the security group. The VNode and the elastic container instances in the VNode are added to the security group.
        self.security_group_id = security_group_id  # type: str
        # Tag.
        self.tag = tag  # type: list[CreateVirtualNodeRequestTag]
        # Taint.
        self.taint = taint  # type: list[CreateVirtualNodeRequestTaint]
        # Specifies whether to enable TLS bootstrapping. If you set this parameter to true, use the KubeConfig certificate for TLS bootstrapping. Valid values:
        # 
        # - true
        # - false
        # 
        # Default value: false.
        self.tls_bootstrap_enabled = tls_bootstrap_enabled  # type: bool
        # The ID of the vSwitch. The vSwitch is connected to the VNode and the elastic container instances in the VNode.
        # 
        # You can specify 1 to 10 vSwitches for a VPC.
        self.v_switch_id = v_switch_id  # type: str
        # The name of the VNode. The name must be 2 to 128 characters in length, and can contain lowercase letters, digits, periods (.), and hyphens (-).
        self.virtual_node_name = virtual_node_name  # type: str
        # The zone ID of the VNode.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.taint:
            for k in self.taint:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateVirtualNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_dns is not None:
            result['ClusterDNS'] = self.cluster_dns
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.custom_resources is not None:
            result['CustomResources'] = self.custom_resources
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.enable_public_network is not None:
            result['EnablePublicNetwork'] = self.enable_public_network
        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['Taint'] = []
        if self.taint is not None:
            for k in self.taint:
                result['Taint'].append(k.to_map() if k else None)
        if self.tls_bootstrap_enabled is not None:
            result['TlsBootstrapEnabled'] = self.tls_bootstrap_enabled
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.virtual_node_name is not None:
            result['VirtualNodeName'] = self.virtual_node_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterDNS') is not None:
            self.cluster_dns = m.get('ClusterDNS')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('CustomResources') is not None:
            self.custom_resources = m.get('CustomResources')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('EnablePublicNetwork') is not None:
            self.enable_public_network = m.get('EnablePublicNetwork')
        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateVirtualNodeRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.taint = []
        if m.get('Taint') is not None:
            for k in m.get('Taint'):
                temp_model = CreateVirtualNodeRequestTaint()
                self.taint.append(temp_model.from_map(k))
        if m.get('TlsBootstrapEnabled') is not None:
            self.tls_bootstrap_enabled = m.get('TlsBootstrapEnabled')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VirtualNodeName') is not None:
            self.virtual_node_name = m.get('VirtualNodeName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateVirtualNodeResponseBody(TeaModel):
    def __init__(self, request_id=None, virtual_node_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the VNode.
        self.virtual_node_id = virtual_node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVirtualNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.virtual_node_id is not None:
            result['VirtualNodeId'] = self.virtual_node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VirtualNodeId') is not None:
            self.virtual_node_id = m.get('VirtualNodeId')
        return self


class CreateVirtualNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVirtualNodeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVirtualNodeResponse, self).to_map()
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
            temp_model = CreateVirtualNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContainerGroupRequest(TeaModel):
    def __init__(self, client_token=None, container_group_id=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request?](~~25693~~)
        self.client_token = client_token  # type: str
        # The instance ID.
        self.container_group_id = container_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContainerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteContainerGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContainerGroupResponseBody, self).to_map()
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


class DeleteContainerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteContainerGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteContainerGroupResponse, self).to_map()
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
            temp_model = DeleteContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataCacheRequest(TeaModel):
    def __init__(self, bucket=None, client_token=None, data_cache_id=None, owner_account=None, owner_id=None,
                 path=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        # The bucket that stores the DataCache. By default, the bucket is named default.
        self.bucket = bucket  # type: str
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the DataCache.
        self.data_cache_id = data_cache_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The directory in which the virtual host of the DataCache is located.
        self.path = path  # type: str
        # The region ID of the DataCache.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDataCacheResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataCacheResponseBody, self).to_map()
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


class DeleteDataCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDataCacheResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataCacheResponse, self).to_map()
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
            temp_model = DeleteDataCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageCacheRequest(TeaModel):
    def __init__(self, client_token=None, image_cache_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the image cache.
        self.image_cache_id = image_cache_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the image cache.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteImageCacheResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageCacheResponseBody, self).to_map()
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


class DeleteImageCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteImageCacheResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageCacheResponse, self).to_map()
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
            temp_model = DeleteImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualNodeRequest(TeaModel):
    def __init__(self, client_token=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, virtual_node_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency of requests](~~25693~~).
        self.client_token = client_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the virtual node.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the virtual node.
        self.virtual_node_id = virtual_node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVirtualNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.virtual_node_id is not None:
            result['VirtualNodeId'] = self.virtual_node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VirtualNodeId') is not None:
            self.virtual_node_id = m.get('VirtualNodeId')
        return self


class DeleteVirtualNodeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVirtualNodeResponseBody, self).to_map()
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


class DeleteVirtualNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVirtualNodeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVirtualNodeResponse, self).to_map()
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
            temp_model = DeleteVirtualNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequestDestinationResource(TeaModel):
    def __init__(self, category=None, cores=None, memory=None, value=None):
        # The type of the resource. Valid values:
        # 
        # *   InstanceTypeFamily: queries instance families. If you use this parameter value, you must also specify the Value parameter.
        # *   InstanceType: queries instance types. If you use this parameter value, you must also specify the Value, Cores, and Memory parameters.
        self.category = category  # type: str
        # The number of vCPUs. This parameter is available only when the Category parameter is set to InstanceType.
        self.cores = cores  # type: float
        # The size of the memory. Unit: GiB. This parameter is available only when the Category parameter is set to InstanceType.
        self.memory = memory  # type: float
        # Instance families or instance types.
        # 
        # *   If you set Category to InstanceTypeFamily, you must set this parameter to instance families such as ecs.c5.
        # *   If you set Category to InstanceType, you must set this parameter to instance types such as ecs.c5.large.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceRequestDestinationResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAvailableResourceRequestSpotResource(TeaModel):
    def __init__(self, spot_duration=None, spot_price_limit=None, spot_strategy=None):
        # The protection period of the preemptible instance. Unit: hours. Default value: 1. The value of 0 indicates no protection period.
        self.spot_duration = spot_duration  # type: int
        # The maximum hourly price of the preemptible elastic container instance. The value can be accurate to three decimal places. If you set SpotStrategy to SpotWithPriceLimit, you must specify the SpotPriceLimit parameter.
        self.spot_price_limit = spot_price_limit  # type: float
        # The bidding policy for the elastic container instance. Valid values:
        # 
        # *   NoSpot: The instance is created as a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is created as a preemptible instance with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is created as a preemptible instance for which the market price at the time of purchase is automatically used as the bid price.
        # 
        # Default value: NoSpot.
        # 
        # > If you set this parameter to SpotWithPriceLimit or SpotAsPriceGo to query preemptible instances, you must set Category to InstanceType. You must also use the Value parameter to specify instance types, or use the Cores and Memory parameters to specify the number of vCPUs and memory size.
        self.spot_strategy = spot_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceRequestSpotResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, destination_resource=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, spot_resource=None, zone_id=None):
        # The information about the resource that you want to query.
        self.destination_resource = destination_resource  # type: DescribeAvailableResourceRequestDestinationResource
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the ECS instance families.
        # 
        # You can call the [DescribeRegions](~~146965~~) operation to query the most recent list of regions.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The information about the preemptible instances that you want to query.
        self.spot_resource = spot_resource  # type: DescribeAvailableResourceRequestSpotResource
        # The zone ID of the ECS instance families.
        # 
        # This parameter is empty by default, which indicates that ECS instance families available in all zones in the specified region are queried.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.destination_resource:
            self.destination_resource.validate()
        if self.spot_resource:
            self.spot_resource.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_resource is not None:
            result['DestinationResource'] = self.destination_resource.to_map()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spot_resource is not None:
            result['SpotResource'] = self.spot_resource.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationResource') is not None:
            temp_model = DescribeAvailableResourceRequestDestinationResource()
            self.destination_resource = temp_model.from_map(m['DestinationResource'])
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpotResource') is not None:
            temp_model = DescribeAvailableResourceRequestSpotResource()
            self.spot_resource = temp_model.from_map(m['SpotResource'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource(TeaModel):
    def __init__(self, status_category=None, value=None):
        # The category of resources based on stock status. Valid values:
        # 
        # *   WithStock: Resources are in sufficient stock.
        # *   ClosedWithStock: Resources are insufficient. We recommend that you use instance types that are in sufficient stock.
        # *   WithoutStock: Resources are sold out and will be replenished. We recommend that you use instance types that are in sufficient stock.
        # *   ClosedWithoutStock: Resources are sold out and will not be replenished. We recommend that you use instance types that are in sufficient stock.
        self.status_category = status_category  # type: str
        # The ECS instance types or instance families that are available in the zones.
        # 
        # *   If the return value of the Type parameter is InstanceTypeFamily, this parameter indicates instance families that are returned.
        # *   If the return value of the Type parameter is InstanceType, this parameter indicates instance types that are returned.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_category is not None:
            result['StatusCategory'] = self.status_category
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StatusCategory') is not None:
            self.status_category = m.get('StatusCategory')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources(TeaModel):
    def __init__(self, supported_resource=None):
        self.supported_resource = supported_resource  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource]

    def validate(self):
        if self.supported_resource:
            for k in self.supported_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedResource'] = []
        if self.supported_resource is not None:
            for k in self.supported_resource:
                result['SupportedResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_resource = []
        if m.get('SupportedResource') is not None:
            for k in m.get('SupportedResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResourcesSupportedResource()
                self.supported_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource(TeaModel):
    def __init__(self, supported_resources=None, type=None):
        # The information about the resources that are available in the zones.
        self.supported_resources = supported_resources  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources
        # The type of the resource. Valid values:
        # 
        # *   InstanceTypeFamily: instance families.
        # *   InstanceType: instance types.
        self.type = type  # type: str

    def validate(self):
        if self.supported_resources:
            self.supported_resources.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_resources is not None:
            result['SupportedResources'] = self.supported_resources.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResourceSupportedResources()
            self.supported_resources = temp_model.from_map(m['SupportedResources'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources(TeaModel):
    def __init__(self, available_resource=None):
        self.available_resource = available_resource  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource]

    def validate(self):
        if self.available_resource:
            for k in self.available_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableResource'] = []
        if self.available_resource is not None:
            for k in self.available_resource:
                result['AvailableResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_resource = []
        if m.get('AvailableResource') is not None:
            for k in m.get('AvailableResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone(TeaModel):
    def __init__(self, available_resources=None, region_id=None, zone_id=None):
        # The resources that are available in the specified zone.
        self.available_resources = available_resources  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources
        # The region ID of the resources.
        self.region_id = region_id  # type: str
        # The zone ID of the resources.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneAvailableResources()
            self.available_resources = temp_model.from_map(m['AvailableResources'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZones(TeaModel):
    def __init__(self, available_zone=None):
        self.available_zone = available_zone  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone]

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k in self.available_zone:
                result['AvailableZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k in m.get('AvailableZone'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(self, available_zones=None, request_id=None):
        # The zones in which the specified resources are available.
        self.available_zones = available_zones  # type: DescribeAvailableResourceResponseBodyAvailableZones
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m['AvailableZones'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAvailableResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponse, self).to_map()
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
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCommitContainerTaskRequest(TeaModel):
    def __init__(self, container_group_id=None, max_results=None, next_token=None, owner_account=None,
                 owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None,
                 task_status=None):
        # The ID of the elastic container instance on which the CommitContainer task is executed.\
        # You must enter the instance ID, the task ID, or both for the request.
        self.container_group_id = container_group_id  # type: str
        # The number of entries to return on each page.\
        # Maximum value: 50.\
        # Default value: 10.
        self.max_results = max_results  # type: int
        # The token that determines the start point of the query. Set the value to the value of NextToken that is returned from the last request.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the region.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the task.
        self.task_id = task_id  # type: list[str]
        # The status of the task. Valid values:
        # 
        # *   Running
        # *   Succeeded
        # *   Failed
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCommitContainerTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class DescribeCommitContainerTaskResponseBodyCommitTasksCommitPhaseInfos(TeaModel):
    def __init__(self, message=None, phase=None, record_time=None, status=None):
        # The message about the phase.
        self.message = message  # type: str
        # The phase name. Valid values:
        # 
        # *   PullBaseImage: Pull the original container image.
        # *   CommitContainer: Commit the container to generate an image.
        # *   PushCommittedImage: Push the image to Container Registry.
        self.phase = phase  # type: str
        # The record time of the phase.
        self.record_time = record_time  # type: str
        # The state of the phase.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCommitContainerTaskResponseBodyCommitTasksCommitPhaseInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.record_time is not None:
            result['RecordTime'] = self.record_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('RecordTime') is not None:
            self.record_time = m.get('RecordTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCommitContainerTaskResponseBodyCommitTasks(TeaModel):
    def __init__(self, commit_phase_infos=None, container_name=None, status_message=None, task_creation_time=None,
                 task_finished_time=None, task_id=None, task_progress=None, task_status=None):
        # The information about the phase that the task arrives.
        self.commit_phase_infos = commit_phase_infos  # type: list[DescribeCommitContainerTaskResponseBodyCommitTasksCommitPhaseInfos]
        # The container name.
        self.container_name = container_name  # type: str
        # The message about the state.
        self.status_message = status_message  # type: str
        # The time when the task was started.
        self.task_creation_time = task_creation_time  # type: str
        # The time when the task was complete.
        self.task_finished_time = task_finished_time  # type: str
        # The task ID.
        self.task_id = task_id  # type: str
        # The progress of the task in percentage.
        self.task_progress = task_progress  # type: str
        # The state of the task. Valid values:
        # 
        # *   Running
        # *   Succeeded
        # *   Failed
        self.task_status = task_status  # type: str

    def validate(self):
        if self.commit_phase_infos:
            for k in self.commit_phase_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCommitContainerTaskResponseBodyCommitTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommitPhaseInfos'] = []
        if self.commit_phase_infos is not None:
            for k in self.commit_phase_infos:
                result['CommitPhaseInfos'].append(k.to_map() if k else None)
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_creation_time is not None:
            result['TaskCreationTime'] = self.task_creation_time
        if self.task_finished_time is not None:
            result['TaskFinishedTime'] = self.task_finished_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.commit_phase_infos = []
        if m.get('CommitPhaseInfos') is not None:
            for k in m.get('CommitPhaseInfos'):
                temp_model = DescribeCommitContainerTaskResponseBodyCommitTasksCommitPhaseInfos()
                self.commit_phase_infos.append(temp_model.from_map(k))
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskCreationTime') is not None:
            self.task_creation_time = m.get('TaskCreationTime')
        if m.get('TaskFinishedTime') is not None:
            self.task_finished_time = m.get('TaskFinishedTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class DescribeCommitContainerTaskResponseBody(TeaModel):
    def __init__(self, commit_tasks=None, max_results=None, next_token=None, request_id=None, total_count=None):
        # Details of the task.
        self.commit_tasks = commit_tasks  # type: list[DescribeCommitContainerTaskResponseBodyCommitTasks]
        # The number of entries returned per page.
        self.max_results = max_results  # type: str
        # The query token that is returned in this request.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.commit_tasks:
            for k in self.commit_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCommitContainerTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommitTasks'] = []
        if self.commit_tasks is not None:
            for k in self.commit_tasks:
                result['CommitTasks'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.commit_tasks = []
        if m.get('CommitTasks') is not None:
            for k in m.get('CommitTasks'):
                temp_model = DescribeCommitContainerTaskResponseBodyCommitTasks()
                self.commit_tasks.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCommitContainerTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCommitContainerTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCommitContainerTaskResponse, self).to_map()
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
            temp_model = DescribeCommitContainerTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupEventsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupEventsRequestTag, self).to_map()
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


class DescribeContainerGroupEventsRequest(TeaModel):
    def __init__(self, container_group_ids=None, event_source=None, limit=None, next_token=None, region_id=None,
                 resource_group_id=None, since_second=None, tag=None, v_switch_id=None, zone_id=None):
        # The IDs of the elastic container instances. You can specify up to 20 IDs. Each ID must be a JSON string.
        self.container_group_ids = container_group_ids  # type: str
        # The event source. Valid values:
        # 
        # *   EciService
        # *   K8sAgent
        # 
        # This parameter is empty by default. This indicates that all events are queried.
        self.event_source = event_source  # type: str
        # The maximum number of elastic container instances to be returned for this request. Default value: 200.
        # 
        # >  The number of elastic container instances to be returned is no greater than this parameter value.
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        # 
        # You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # A relative time in seconds before the current time from which to show event information. This parameter is used to poll incremental events.
        self.since_second = since_second  # type: int
        # The tag that is added to the elastic container instances.
        self.tag = tag  # type: list[DescribeContainerGroupEventsRequestTag]
        # The vSwitch ID.
        self.v_switch_id = v_switch_id  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.since_second is not None:
            result['SinceSecond'] = self.since_second
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SinceSecond') is not None:
            self.since_second = m.get('SinceSecond')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeContainerGroupEventsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupEventsResponseBodyDataEventsMetadata(TeaModel):
    def __init__(self, name=None, namespace=None):
        # The event name.
        self.name = name  # type: str
        # The namespace.
        self.namespace = namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupEventsResponseBodyDataEventsMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class DescribeContainerGroupEventsResponseBodyDataEventsSource(TeaModel):
    def __init__(self, component=None, host=None):
        # The component.
        self.component = component  # type: str
        # The host.
        self.host = host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupEventsResponseBodyDataEventsSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component is not None:
            result['Component'] = self.component
        if self.host is not None:
            result['Host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Component') is not None:
            self.component = m.get('Component')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        return self


class DescribeContainerGroupEventsResponseBodyDataEventsInvolvedObject(TeaModel):
    def __init__(self, api_version=None, kind=None, name=None, namespace=None, uid=None):
        # The version of Kubernetes.
        self.api_version = api_version  # type: str
        # The resource type.
        self.kind = kind  # type: str
        # The resource name.
        self.name = name  # type: str
        # The namespace where the resource resides.
        self.namespace = namespace  # type: str
        # The resource ID.
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupEventsResponseBodyDataEventsInvolvedObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeContainerGroupEventsResponseBodyDataEvents(TeaModel):
    def __init__(self, count=None, first_timestamp=None, last_timestamp=None, message=None, metadata=None,
                 reason=None, reporting_component=None, reporting_instance=None, source=None, type=None,
                 involved_object=None):
        # The number of events.
        self.count = count  # type: int
        # The first occurrence time of the event.
        self.first_timestamp = first_timestamp  # type: str
        # The most recent occurrence time of the event.
        self.last_timestamp = last_timestamp  # type: str
        # The message about the event.
        self.message = message  # type: str
        # The metadata of the event.
        self.metadata = metadata  # type: DescribeContainerGroupEventsResponseBodyDataEventsMetadata
        # The cause of the event.
        self.reason = reason  # type: str
        # The component from which the event is reported.
        self.reporting_component = reporting_component  # type: str
        # The instance from which the event is reported.
        self.reporting_instance = reporting_instance  # type: str
        # The source.
        self.source = source  # type: DescribeContainerGroupEventsResponseBodyDataEventsSource
        # The event type. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type  # type: str
        # The resource object that the event is about.
        self.involved_object = involved_object  # type: DescribeContainerGroupEventsResponseBodyDataEventsInvolvedObject

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.source:
            self.source.validate()
        if self.involved_object:
            self.involved_object.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupEventsResponseBodyDataEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reporting_component is not None:
            result['ReportingComponent'] = self.reporting_component
        if self.reporting_instance is not None:
            result['ReportingInstance'] = self.reporting_instance
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.involved_object is not None:
            result['involvedObject'] = self.involved_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Metadata') is not None:
            temp_model = DescribeContainerGroupEventsResponseBodyDataEventsMetadata()
            self.metadata = temp_model.from_map(m['Metadata'])
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ReportingComponent') is not None:
            self.reporting_component = m.get('ReportingComponent')
        if m.get('ReportingInstance') is not None:
            self.reporting_instance = m.get('ReportingInstance')
        if m.get('Source') is not None:
            temp_model = DescribeContainerGroupEventsResponseBodyDataEventsSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('involvedObject') is not None:
            temp_model = DescribeContainerGroupEventsResponseBodyDataEventsInvolvedObject()
            self.involved_object = temp_model.from_map(m['involvedObject'])
        return self


class DescribeContainerGroupEventsResponseBodyData(TeaModel):
    def __init__(self, annotations=None, container_group_id=None, events=None, name=None, namespace=None, uuid=None):
        # The annotations of the elastic container instance.
        self.annotations = annotations  # type: str
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id  # type: str
        # The events.
        self.events = events  # type: list[DescribeContainerGroupEventsResponseBodyDataEvents]
        # The name of the elastic container instance.
        self.name = name  # type: str
        # The namespace where the elastic container instance resides.
        self.namespace = namespace  # type: str
        # The UUID of the elastic container instance.
        self.uuid = uuid  # type: str

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupEventsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeContainerGroupEventsResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class DescribeContainerGroupEventsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, total_count=None):
        # Details of the events.
        self.data = data  # type: list[DescribeContainerGroupEventsResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries of returned events.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeContainerGroupEventsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeContainerGroupEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContainerGroupEventsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupEventsResponse, self).to_map()
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
            temp_model = DescribeContainerGroupEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupMetricRequest(TeaModel):
    def __init__(self, container_group_id=None, end_time=None, owner_account=None, owner_id=None, period=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, start_time=None):
        # The instance ID.
        self.container_group_id = container_group_id  # type: str
        # The end of the time range to query. The default value is the current time.
        # 
        # Specify the time in RFC 3339 format.
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The data aggregation period. Unit: seconds. Valid values: 15, 30, 60, and 600. Default value: 60.
        # 
        # >  If the StartTime and EndTime parameters are not specified, the system returns the monitoring data generated in the last 5 minutes with a data aggregation period of 15s. The Period parameter is ignored.
        self.period = period  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The beginning of the time range to query. The beginning of the time range must be a time point in the last 30 days. The default value is 5 minutes before the value of EndTime.
        # 
        # Specify the time in RFC 3339 format. For example, to query the data starting from March 12, 2019, 09:00 UTC+8, you can set the parameter to 2019-03-12T09:00:00.000+08:00 or 2019-03-12T01:00:00.000Z.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsCPU(TeaModel):
    def __init__(self, limit=None, load=None, usage_core_nano_seconds=None, usage_nano_cores=None):
        # The upper limit of vCPU usage. The calculation formula for this parameter: The number of vCPUs × 1000.
        self.limit = limit  # type: long
        # The average load in the last 10 seconds.
        self.load = load  # type: long
        # The cumulative usage of vCPUs.
        self.usage_core_nano_seconds = usage_core_nano_seconds  # type: long
        # The vCPU usage in the sampling window. Unit for the sampling window: nanoseconds.
        self.usage_nano_cores = usage_nano_cores  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsCPU, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.load is not None:
            result['Load'] = self.load
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainersCPU(TeaModel):
    def __init__(self, limit=None, load=None, usage_core_nano_seconds=None, usage_nano_cores=None):
        # The upper limit of vCPU usage. The calculation formula for this parameter: The number of vCPUs × 1000.
        self.limit = limit  # type: long
        # The average load in the last 10 seconds.
        self.load = load  # type: long
        # The cumulative usage of vCPUs.
        self.usage_core_nano_seconds = usage_core_nano_seconds  # type: long
        # The vCPU usage in the sampling window. Unit for the sampling window: nanoseconds.
        self.usage_nano_cores = usage_nano_cores  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsContainersCPU, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.load is not None:
            result['Load'] = self.load
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainersMemory(TeaModel):
    def __init__(self, available_bytes=None, cache=None, rss=None, usage_bytes=None, working_set=None):
        # The size of the available memory. Unit: bytes.
        self.available_bytes = available_bytes  # type: long
        # The size of the cache. Unit: bytes.
        self.cache = cache  # type: long
        # The size of the resident memory set, which indicates the size of the physical memory that is actually used. Unit: bytes.
        self.rss = rss  # type: long
        # The size of the used memory. Unit: bytes.
        self.usage_bytes = usage_bytes  # type: long
        # The usage of the working set. Unit: bytes.
        self.working_set = working_set  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsContainersMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsContainers(TeaModel):
    def __init__(self, cpu=None, memory=None, name=None):
        # The vCPU monitoring data of the container.
        self.cpu = cpu  # type: DescribeContainerGroupMetricResponseBodyRecordsContainersCPU
        # The memory monitoring data of the container.
        self.memory = memory  # type: DescribeContainerGroupMetricResponseBodyRecordsContainersMemory
        # The name of the container.
        self.name = name  # type: str

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsContainers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainersCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        if m.get('Memory') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainersMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsDisk(TeaModel):
    def __init__(self, device=None, read_bytes=None, read_io=None, write_bytes=None, write_io=None):
        # The name of the disk.
        self.device = device  # type: str
        # The amount of data that was read from the disk. Unit: bytes.
        self.read_bytes = read_bytes  # type: long
        # This parameter is unavailable for public use.
        self.read_io = read_io  # type: long
        # The amount of data that was written to the disk. Unit: bytes.
        self.write_bytes = write_bytes  # type: long
        # This parameter is unavailable for public use.
        self.write_io = write_io  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device
        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes
        if self.read_io is not None:
            result['ReadIO'] = self.read_io
        if self.write_bytes is not None:
            result['WriteBytes'] = self.write_bytes
        if self.write_io is not None:
            result['WriteIO'] = self.write_io
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')
        if m.get('ReadIO') is not None:
            self.read_io = m.get('ReadIO')
        if m.get('WriteBytes') is not None:
            self.write_bytes = m.get('WriteBytes')
        if m.get('WriteIO') is not None:
            self.write_io = m.get('WriteIO')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsFilesystem(TeaModel):
    def __init__(self, available=None, capacity=None, category=None, fs_name=None, usage=None):
        # The size of the available space.
        self.available = available  # type: long
        # The total file system space.
        self.capacity = capacity  # type: long
        # The type of the partition. Valid values:
        # 
        # *   System
        # *   Volume
        # *   Other
        self.category = category  # type: str
        # The name of the partition.
        self.fs_name = fs_name  # type: str
        # The size of used space.
        self.usage = usage  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsFilesystem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.category is not None:
            result['Category'] = self.category
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsMemory(TeaModel):
    def __init__(self, available_bytes=None, cache=None, rss=None, usage_bytes=None, working_set=None):
        # The size of the available memory. Unit: bytes.
        self.available_bytes = available_bytes  # type: long
        # The size of the cache. Unit: bytes.
        self.cache = cache  # type: long
        # The size of the resident memory set, which indicates the size of the physical memory that is actually used. Unit: bytes.
        self.rss = rss  # type: long
        # The size of the used memory. Unit: bytes.
        self.usage_bytes = usage_bytes  # type: long
        # The usage of the working set. Unit: bytes.
        self.working_set = working_set  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces(TeaModel):
    def __init__(self, name=None, rx_bytes=None, rx_drops=None, rx_errors=None, rx_packets=None, tx_bytes=None,
                 tx_drops=None, tx_errors=None, tx_packets=None):
        # The name of the NIC.
        self.name = name  # type: str
        # The number of bytes received by the NIC.
        self.rx_bytes = rx_bytes  # type: long
        # The number of received packets dropped on the NIC.
        self.rx_drops = rx_drops  # type: long
        # The number of received packet errors on the NIC.
        self.rx_errors = rx_errors  # type: long
        # The number of packets received by the NIC.
        self.rx_packets = rx_packets  # type: long
        # The number of bytes transmitted by the NIC.
        self.tx_bytes = tx_bytes  # type: long
        # The number of transmitted packets dropped on the NIC.
        self.tx_drops = tx_drops  # type: long
        # The number of transmitted packet errors on the NIC.
        self.tx_errors = tx_errors  # type: long
        # The number of packets transmitted by the NIC.
        self.tx_packets = tx_packets  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rx_bytes is not None:
            result['RxBytes'] = self.rx_bytes
        if self.rx_drops is not None:
            result['RxDrops'] = self.rx_drops
        if self.rx_errors is not None:
            result['RxErrors'] = self.rx_errors
        if self.rx_packets is not None:
            result['RxPackets'] = self.rx_packets
        if self.tx_bytes is not None:
            result['TxBytes'] = self.tx_bytes
        if self.tx_drops is not None:
            result['TxDrops'] = self.tx_drops
        if self.tx_errors is not None:
            result['TxErrors'] = self.tx_errors
        if self.tx_packets is not None:
            result['TxPackets'] = self.tx_packets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RxBytes') is not None:
            self.rx_bytes = m.get('RxBytes')
        if m.get('RxDrops') is not None:
            self.rx_drops = m.get('RxDrops')
        if m.get('RxErrors') is not None:
            self.rx_errors = m.get('RxErrors')
        if m.get('RxPackets') is not None:
            self.rx_packets = m.get('RxPackets')
        if m.get('TxBytes') is not None:
            self.tx_bytes = m.get('TxBytes')
        if m.get('TxDrops') is not None:
            self.tx_drops = m.get('TxDrops')
        if m.get('TxErrors') is not None:
            self.tx_errors = m.get('TxErrors')
        if m.get('TxPackets') is not None:
            self.tx_packets = m.get('TxPackets')
        return self


class DescribeContainerGroupMetricResponseBodyRecordsNetwork(TeaModel):
    def __init__(self, interfaces=None):
        # The monitoring data of network interface controllers (NICs).
        self.interfaces = interfaces  # type: list[DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces]

    def validate(self):
        if self.interfaces:
            for k in self.interfaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecordsNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Interfaces'] = []
        if self.interfaces is not None:
            for k in self.interfaces:
                result['Interfaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.interfaces = []
        if m.get('Interfaces') is not None:
            for k in m.get('Interfaces'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsNetworkInterfaces()
                self.interfaces.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupMetricResponseBodyRecords(TeaModel):
    def __init__(self, cpu=None, containers=None, disk=None, filesystem=None, memory=None, network=None,
                 timestamp=None):
        # The monitoring data of vCPUs.
        self.cpu = cpu  # type: DescribeContainerGroupMetricResponseBodyRecordsCPU
        # The monitoring data of containers.
        self.containers = containers  # type: list[DescribeContainerGroupMetricResponseBodyRecordsContainers]
        # The monitoring data of disks.
        self.disk = disk  # type: list[DescribeContainerGroupMetricResponseBodyRecordsDisk]
        # The monitoring data of file system partitions.
        self.filesystem = filesystem  # type: list[DescribeContainerGroupMetricResponseBodyRecordsFilesystem]
        # The monitoring data of the memory.
        self.memory = memory  # type: DescribeContainerGroupMetricResponseBodyRecordsMemory
        # The monitoring data of the network.
        self.network = network  # type: DescribeContainerGroupMetricResponseBodyRecordsNetwork
        # The time when the monitoring data entry was collected. The time follows the RFC 3339 format.
        self.timestamp = timestamp  # type: str

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()
        if self.filesystem:
            for k in self.filesystem:
                if k:
                    k.validate()
        if self.memory:
            self.memory.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        result['Filesystem'] = []
        if self.filesystem is not None:
            for k in self.filesystem:
                result['Filesystem'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsContainers()
                self.containers.append(temp_model.from_map(k))
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsDisk()
                self.disk.append(temp_model.from_map(k))
        self.filesystem = []
        if m.get('Filesystem') is not None:
            for k in m.get('Filesystem'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecordsFilesystem()
                self.filesystem.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Network') is not None:
            temp_model = DescribeContainerGroupMetricResponseBodyRecordsNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeContainerGroupMetricResponseBody(TeaModel):
    def __init__(self, container_group_id=None, records=None, request_id=None):
        # The instance ID.
        self.container_group_id = container_group_id  # type: str
        # The monitoring data of the elastic container instance.
        self.records = records  # type: list[DescribeContainerGroupMetricResponseBodyRecords]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeContainerGroupMetricResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerGroupMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContainerGroupMetricResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupMetricResponse, self).to_map()
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
            temp_model = DescribeContainerGroupMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupPriceRequest(TeaModel):
    def __init__(self, compute_category=None, cpu=None, ephemeral_storage=None, instance_type=None, memory=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 spot_duration=None, spot_price_limit=None, spot_strategy=None, zone_id=None):
        # The computing power type. A value of economy specifies economic instances.
        self.compute_category = compute_category  # type: str
        # The number of vCPUs. For information about the vCPU and memory specifications that are supported by Elastic Container Instance, see [vCPU and memory specifications](~~114662~~).
        self.cpu = cpu  # type: float
        # The storage size of the temporary storage space. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage  # type: int
        # The instance type of the Elastic Compute Service (ECS) instance that is used to create the elastic container instance. For information about the ECS instance types that are supported by Elastic Container Instance, see [ECS instance types that are supported by Elastic Container Instance](~~114664~~).
        # 
        # > If you specify this parameter, the specified specifications of vCPUs and memory are ignored. Only the price of the ECS instance type is returned.
        self.instance_type = instance_type  # type: str
        # The size of the memory. Unit: GiB. For information about the vCPU and memory specifications that are supported by Elastic Container Instance, see [vCPU and memory specifications](~~114662~~).
        self.memory = memory  # type: float
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~146965~~) operation to query the most recent region and zone list.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The protection period of the preemptible instance. Unit: hours. Default value: 1. The value of 0 indicates no protection period.
        self.spot_duration = spot_duration  # type: int
        # The maximum hourly price of the preemptible elastic container instance. The value can contain up to three decimal places. If you set SpotStrategy to SpotWithPriceLimit, you must specify SpotPriceLimit.
        self.spot_price_limit = spot_price_limit  # type: float
        # The bidding policy for the elastic container instance. Valid values:
        # 
        # *   NoSpot: The instance is a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is a preemptible instance with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is automatically used as the bid price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy  # type: str
        # The zone ID of the instance. You can call the [DescribeRegions](~~146965~~) operation to query the most recent region and zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_category is not None:
            result['ComputeCategory'] = self.compute_category
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComputeCategory') is not None:
            self.compute_category = m.get('ComputeCategory')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule(TeaModel):
    def __init__(self, description=None, rule_id=None):
        # The description of the rule.
        self.description = description  # type: str
        # The rule ID.
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules(TeaModel):
    def __init__(self, rule=None):
        self.rule = rule  # type: list[DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule]

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo(TeaModel):
    def __init__(self, discount_price=None, original_price=None, resource=None, rules=None, trade_price=None):
        # The discount.
        self.discount_price = discount_price  # type: float
        # The original price.
        self.original_price = original_price  # type: float
        # The name of the resource.
        self.resource = resource  # type: str
        # Details about the pricing rules.
        self.rules = rules  # type: DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules
        # The transaction price.
        self.trade_price = trade_price  # type: float

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Rules') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos(TeaModel):
    def __init__(self, detail_info=None):
        self.detail_info = detail_info  # type: list[DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo]

    def validate(self):
        if self.detail_info:
            for k in self.detail_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailInfo'] = []
        if self.detail_info is not None:
            for k in self.detail_info:
                result['DetailInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail_info = []
        if m.get('DetailInfo') is not None:
            for k in m.get('DetailInfo'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo()
                self.detail_info.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(self, currency=None, detail_infos=None, discount_price=None, original_price=None, trade_price=None):
        # The currency unit. Valid values:
        # 
        # *   CNY: This value only applies to the China site (aliyun.com).
        # *   USD: This value only applies to the International site (alibabacloud.com).
        self.currency = currency  # type: str
        # The information about the price.
        self.detail_infos = detail_infos  # type: DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos
        # The discount.
        self.discount_price = discount_price  # type: float
        # The original price.
        self.original_price = original_price  # type: float
        # The transaction price, which is equal to the original price minus the discount.
        self.trade_price = trade_price  # type: float

    def validate(self):
        if self.detail_infos:
            self.detail_infos.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.detail_infos is not None:
            result['DetailInfos'] = self.detail_infos.to_map()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DetailInfos') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPriceDetailInfos()
            self.detail_infos = temp_model.from_map(m['DetailInfos'])
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule(TeaModel):
    def __init__(self, description=None, rule_id=None):
        # The description of the promotion rule.
        self.description = description  # type: str
        # The ID of the promotion rule.
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(self, rule=None):
        self.rule = rule  # type: list[DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule]

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice(TeaModel):
    def __init__(self, instance_type=None, origin_price=None, spot_price=None, zone_id=None):
        # The ECS instance type.
        self.instance_type = instance_type  # type: str
        # The original price.
        self.origin_price = origin_price  # type: float
        # The prices of preemptible elastic container instances.
        self.spot_price = spot_price  # type: float
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.spot_price is not None:
            result['SpotPrice'] = self.spot_price
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SpotPrice') is not None:
            self.spot_price = m.get('SpotPrice')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices(TeaModel):
    def __init__(self, spot_price=None):
        self.spot_price = spot_price  # type: list[DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice]

    def validate(self):
        if self.spot_price:
            for k in self.spot_price:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SpotPrice'] = []
        if self.spot_price is not None:
            for k in self.spot_price:
                result['SpotPrice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.spot_price = []
        if m.get('SpotPrice') is not None:
            for k in m.get('SpotPrice'):
                temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoSpotPricesSpotPrice()
                self.spot_price.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupPriceResponseBodyPriceInfo(TeaModel):
    def __init__(self, price=None, rules=None, spot_prices=None):
        # The price.
        self.price = price  # type: DescribeContainerGroupPriceResponseBodyPriceInfoPrice
        # Details about the promotion rules.
        self.rules = rules  # type: DescribeContainerGroupPriceResponseBodyPriceInfoRules
        # The information about the prices of preemptible elastic container instances.
        self.spot_prices = spot_prices  # type: DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            self.rules.validate()
        if self.spot_prices:
            self.spot_prices.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBodyPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.spot_prices is not None:
            result['SpotPrices'] = self.spot_prices.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        if m.get('Rules') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('SpotPrices') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfoSpotPrices()
            self.spot_prices = temp_model.from_map(m['SpotPrices'])
        return self


class DescribeContainerGroupPriceResponseBody(TeaModel):
    def __init__(self, price_info=None, request_id=None):
        # The information about the prices and discount rules.
        self.price_info = price_info  # type: DescribeContainerGroupPriceResponseBodyPriceInfo
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = DescribeContainerGroupPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerGroupPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContainerGroupPriceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupPriceResponse, self).to_map()
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
            temp_model = DescribeContainerGroupPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupStatusRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusRequestTag, self).to_map()
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


class DescribeContainerGroupStatusRequest(TeaModel):
    def __init__(self, container_group_ids=None, limit=None, next_token=None, region_id=None,
                 resource_group_id=None, since_second=None, tag=None, v_switch_id=None, zone_id=None):
        # The IDs of the instances. You can specify up to 20 IDs. Each ID must be a string in the JSON format.
        self.container_group_ids = container_group_ids  # type: str
        # Specifies the maximum number of elastic container instances to be returned for this request. Default value: 200.
        # 
        # > The number of returned resources can be less than or equal to the value of this parameter.
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.\
        # You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The region ID of the instances.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instances belong.
        self.resource_group_id = resource_group_id  # type: str
        # A relative time in seconds before the current time from which to show elastic container instances whose status changes. This parameter is used to poll status of elastic container instances.
        self.since_second = since_second  # type: int
        # The tag that is bound to the instances.
        self.tag = tag  # type: list[DescribeContainerGroupStatusRequestTag]
        # The vSwitch ID.
        self.v_switch_id = v_switch_id  # type: str
        # The zone ID of the instances.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.since_second is not None:
            result['SinceSecond'] = self.since_second
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SinceSecond') is not None:
            self.since_second = m.get('SinceSecond')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeContainerGroupStatusRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusConditions(TeaModel):
    def __init__(self, message=None, reason=None, last_transition_time=None, status=None, type=None):
        # The message about the event.
        self.message = message  # type: str
        # The cause of the event.
        self.reason = reason  # type: str
        # The time when the status last changed.
        self.last_transition_time = last_transition_time  # type: str
        # The state of the pod condition.
        self.status = status  # type: str
        # The type of the pod condition. Valid values:
        # 
        # *   PodScheduled
        # *   Ready
        # *   Initialized
        # *   Unschedulable
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateRunning(TeaModel):
    def __init__(self, started_atstarted_at=None):
        # The start time.
        self.started_atstarted_at = started_atstarted_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateRunning, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.started_atstarted_at is not None:
            result['StartedAtstartedAt'] = self.started_atstarted_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartedAtstartedAt') is not None:
            self.started_atstarted_at = m.get('StartedAtstartedAt')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateTerminated(TeaModel):
    def __init__(self, container_id=None, exit_code=None, finished_at=None, message=None, reason=None, signal=None,
                 started_at=None):
        # The container ID.
        self.container_id = container_id  # type: str
        # The exit code.
        self.exit_code = exit_code  # type: int
        # The end time.
        self.finished_at = finished_at  # type: str
        # The message about the event.
        self.message = message  # type: str
        # The cause of the event.
        self.reason = reason  # type: str
        # The signal code.
        self.signal = signal  # type: int
        # The start time.
        self.started_at = started_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateTerminated, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerID'] = self.container_id
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerID') is not None:
            self.container_id = m.get('ContainerID')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateWaiting(TeaModel):
    def __init__(self, message=None, reason=None):
        # The message about the event.
        self.message = message  # type: str
        # The cause of the event.
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateWaiting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastState(TeaModel):
    def __init__(self, running=None, terminated=None, waiting=None):
        # The container is created and running.
        self.running = running  # type: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateRunning
        # The container is terminated and exits after a successful or failed run.
        self.terminated = terminated  # type: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateTerminated
        # The container is waiting for being created.
        self.waiting = waiting  # type: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateWaiting

    def validate(self):
        if self.running:
            self.running.validate()
        if self.terminated:
            self.terminated.validate()
        if self.waiting:
            self.waiting.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.running is not None:
            result['Running'] = self.running.to_map()
        if self.terminated is not None:
            result['Terminated'] = self.terminated.to_map()
        if self.waiting is not None:
            result['Waiting'] = self.waiting.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Running') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateRunning()
            self.running = temp_model.from_map(m['Running'])
        if m.get('Terminated') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateTerminated()
            self.terminated = temp_model.from_map(m['Terminated'])
        if m.get('Waiting') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastStateWaiting()
            self.waiting = temp_model.from_map(m['Waiting'])
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateRunning(TeaModel):
    def __init__(self, started_atstarted_at=None):
        # The start time.
        self.started_atstarted_at = started_atstarted_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateRunning, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.started_atstarted_at is not None:
            result['StartedAtstartedAt'] = self.started_atstarted_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartedAtstartedAt') is not None:
            self.started_atstarted_at = m.get('StartedAtstartedAt')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateTerminated(TeaModel):
    def __init__(self, container_id=None, exit_code=None, finished_at=None, message=None, reason=None, signal=None,
                 started_at=None):
        # The container ID.
        self.container_id = container_id  # type: str
        # The exit code.
        self.exit_code = exit_code  # type: int
        # The end time.
        self.finished_at = finished_at  # type: str
        # The message about the event.
        self.message = message  # type: str
        # The cause of the event.
        self.reason = reason  # type: str
        # The signal code.
        self.signal = signal  # type: int
        # The start time.
        self.started_at = started_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateTerminated, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerID'] = self.container_id
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerID') is not None:
            self.container_id = m.get('ContainerID')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateWaiting(TeaModel):
    def __init__(self, message=None, reason=None):
        # The message about the event.
        self.message = message  # type: str
        # The cause of the event.
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateWaiting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesState(TeaModel):
    def __init__(self, running=None, terminated=None, waiting=None):
        # The container is created and running.
        self.running = running  # type: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateRunning
        # The container is terminated and exits after a successful or failed run.
        self.terminated = terminated  # type: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateTerminated
        # The container is waiting for being created.
        self.waiting = waiting  # type: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateWaiting

    def validate(self):
        if self.running:
            self.running.validate()
        if self.terminated:
            self.terminated.validate()
        if self.waiting:
            self.waiting.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.running is not None:
            result['Running'] = self.running.to_map()
        if self.terminated is not None:
            result['Terminated'] = self.terminated.to_map()
        if self.waiting is not None:
            result['Waiting'] = self.waiting.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Running') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateRunning()
            self.running = temp_model.from_map(m['Running'])
        if m.get('Terminated') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateTerminated()
            self.terminated = temp_model.from_map(m['Terminated'])
        if m.get('Waiting') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesStateWaiting()
            self.waiting = temp_model.from_map(m['Waiting'])
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatuses(TeaModel):
    def __init__(self, image=None, image_id=None, last_state=None, name=None, ready=None, restart_count=None,
                 started=None, state=None):
        # The image of the container.
        self.image = image  # type: str
        # The image ID.
        self.image_id = image_id  # type: str
        # The most recent state of the container.
        self.last_state = last_state  # type: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastState
        # The container name.
        self.name = name  # type: str
        # Indicates whether the container is ready for use.
        self.ready = ready  # type: bool
        # The number of restarts.
        self.restart_count = restart_count  # type: int
        # Indicates whether the container is started.
        self.started = started  # type: bool
        # The state of the container. Valid values:
        # 
        # *   Waiting
        # *   Running
        # *   Terminated
        self.state = state  # type: DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesState

    def validate(self):
        if self.last_state:
            self.last_state.validate()
        if self.state:
            self.state.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.image_id is not None:
            result['ImageID'] = self.image_id
        if self.last_state is not None:
            result['LastState'] = self.last_state.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.started is not None:
            result['Started'] = self.started
        if self.state is not None:
            result['State'] = self.state.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageID') is not None:
            self.image_id = m.get('ImageID')
        if m.get('LastState') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesLastState()
            self.last_state = temp_model.from_map(m['LastState'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('Started') is not None:
            self.started = m.get('Started')
        if m.get('State') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatusesState()
            self.state = temp_model.from_map(m['State'])
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatusPodIps(TeaModel):
    def __init__(self, ip=None):
        # The IP address of the pod.
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatusPodIps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeContainerGroupStatusResponseBodyDataPodStatus(TeaModel):
    def __init__(self, conditions=None, container_statuses=None, host_ip=None, phase=None, pod_ip=None, pod_ips=None,
                 qos_class=None, start_time=None):
        # The information about the pod conditions.
        self.conditions = conditions  # type: list[DescribeContainerGroupStatusResponseBodyDataPodStatusConditions]
        # The state information about the container.
        self.container_statuses = container_statuses  # type: list[DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatuses]
        # The IP address of the host.
        self.host_ip = host_ip  # type: str
        # The lifecycle phase of the pod.
        self.phase = phase  # type: str
        # The IP address of the pod.
        self.pod_ip = pod_ip  # type: str
        # The collection of pod IP addresses.
        self.pod_ips = pod_ips  # type: list[DescribeContainerGroupStatusResponseBodyDataPodStatusPodIps]
        # The quality of service (QoS) of the pod.
        self.qos_class = qos_class  # type: str
        # The time when the container started to run.
        self.start_time = start_time  # type: str

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.container_statuses:
            for k in self.container_statuses:
                if k:
                    k.validate()
        if self.pod_ips:
            for k in self.pod_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyDataPodStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        result['ContainerStatuses'] = []
        if self.container_statuses is not None:
            for k in self.container_statuses:
                result['ContainerStatuses'].append(k.to_map() if k else None)
        if self.host_ip is not None:
            result['HostIp'] = self.host_ip
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip
        result['PodIps'] = []
        if self.pod_ips is not None:
            for k in self.pod_ips:
                result['PodIps'].append(k.to_map() if k else None)
        if self.qos_class is not None:
            result['QosClass'] = self.qos_class
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusConditions()
                self.conditions.append(temp_model.from_map(k))
        self.container_statuses = []
        if m.get('ContainerStatuses') is not None:
            for k in m.get('ContainerStatuses'):
                temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusContainerStatuses()
                self.container_statuses.append(temp_model.from_map(k))
        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')
        self.pod_ips = []
        if m.get('PodIps') is not None:
            for k in m.get('PodIps'):
                temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatusPodIps()
                self.pod_ips.append(temp_model.from_map(k))
        if m.get('QosClass') is not None:
            self.qos_class = m.get('QosClass')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeContainerGroupStatusResponseBodyData(TeaModel):
    def __init__(self, annotations=None, container_group_id=None, name=None, namespace=None, pod_status=None,
                 status=None, uuid=None):
        # The annotations of the elastic container instance.
        self.annotations = annotations  # type: str
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id  # type: str
        # The name of the elastic container instance.
        self.name = name  # type: str
        # The namespace where the elastic container instance resides.
        self.namespace = namespace  # type: str
        # The state information about the elastic container instance.
        self.pod_status = pod_status  # type: DescribeContainerGroupStatusResponseBodyDataPodStatus
        # The state of the elastic container instance.
        self.status = status  # type: str
        # The UUID of the elastic container instance. The UUID of an elastic container instance is similar to the UID of a Kubernetes pod in concept and usage.
        self.uuid = uuid  # type: str

    def validate(self):
        if self.pod_status:
            self.pod_status.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PodStatus') is not None:
            temp_model = DescribeContainerGroupStatusResponseBodyDataPodStatus()
            self.pod_status = temp_model.from_map(m['PodStatus'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class DescribeContainerGroupStatusResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None, total_count=None):
        # The collection of status of the elastic container instances.
        self.data = data  # type: list[DescribeContainerGroupStatusResponseBodyData]
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeContainerGroupStatusResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeContainerGroupStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContainerGroupStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupStatusResponse, self).to_map()
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
            temp_model = DescribeContainerGroupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerGroupsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the instances.
        self.key = key  # type: str
        # The tag value of the instances.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsRequestTag, self).to_map()
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


class DescribeContainerGroupsRequest(TeaModel):
    def __init__(self, compute_category=None, container_group_ids=None, container_group_name=None, limit=None,
                 next_token=None, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_group_id=None, status=None, tag=None, v_switch_id=None,
                 with_event=None, zone_id=None):
        # The computing power type of the elastic container instance. A value of economy specifies economic elastic container instances.
        self.compute_category = compute_category  # type: str
        # The IDs of the elastic container instances in JSON format. You can specify up to 20 IDs.
        self.container_group_ids = container_group_ids  # type: str
        # The name of the elastic container instance.
        self.container_group_name = container_group_name  # type: str
        # The maximum number of resources to return. Default value: 20. Maximum value: 20.
        # 
        # >  The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The token that determines the start point of the query. If this parameter is left empty, all results have been returned.
        # 
        # > You do not need to specify this parameter in the first request. Starting from the second request, you can obtain the token from the result returned by the previous request.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the security group to which the instance belongs.
        self.security_group_id = security_group_id  # type: str
        # The status of the elastic container instance. Valid values:
        # 
        # *   Pending: The instance is being started.
        # *   Running: The instance is running.
        # *   Succeeded: The instance runs successfully.
        # *   Failed: The instance fails to run.
        # *   Scheduling: The instance is being created.
        # *   ScheduleFailed: The instance fails to be created.
        # *   Restarting: The instance is being restarted.
        # *   Updating: The instance is being updated.
        # *   Terminating: The instance is being terminated.
        # *   Expired: The instance expires.
        self.status = status  # type: str
        # The tag of the instances.
        self.tag = tag  # type: list[DescribeContainerGroupsRequestTag]
        # The ID of the vSwitch to which the elastic container instances are connected.
        self.v_switch_id = v_switch_id  # type: str
        # Specify whether to return event information.
        self.with_event = with_event  # type: bool
        # The ID of the zone in which the elastic container instances are deployed. If you do not specify this parameter, the system selects a zone.
        # 
        # This parameter is empty by default.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_category is not None:
            result['ComputeCategory'] = self.compute_category
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.with_event is not None:
            result['WithEvent'] = self.with_event
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComputeCategory') is not None:
            self.compute_category = m.get('ComputeCategory')
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeContainerGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('WithEvent') is not None:
            self.with_event = m.get('WithEvent')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState(TeaModel):
    def __init__(self, detail_status=None, exit_code=None, finish_time=None, message=None, reason=None, signal=None,
                 start_time=None, state=None):
        # The details of the container status.
        self.detail_status = detail_status  # type: str
        # The exit code of the container.
        self.exit_code = exit_code  # type: int
        # The time when the container stopped running.
        self.finish_time = finish_time  # type: str
        # The message about the container status.
        self.message = message  # type: str
        # The reason why the container is in this state.
        self.reason = reason  # type: str
        # The code of the container status.
        self.signal = signal  # type: int
        # The time when the container started to run.
        self.start_time = start_time  # type: str
        # The container status. Valid values:
        # 
        # *   Waiting
        # *   Running
        # *   Terminated
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef(TeaModel):
    def __init__(self, field_path=None):
        # The path of the field.
        self.field_path = field_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom(TeaModel):
    def __init__(self, field_ref=None):
        # The specified field.
        self.field_ref = field_ref  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFromFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars(TeaModel):
    def __init__(self, key=None, value=None, value_from=None):
        # The name of the environment variable.
        self.key = key  # type: str
        # The value of the environment variable.
        self.value = value  # type: str
        # The source of the environment variable value. This parameter has a value only when the Value parameter is not empty.
        self.value_from = value_from  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom

    def validate(self):
        if self.value_from:
            self.value_from.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.value_from is not None:
            result['ValueFrom'] = self.value_from.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueFrom') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVarsValueFrom()
            self.value_from = temp_model.from_map(m['ValueFrom'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet(TeaModel):
    def __init__(self, path=None, port=None, scheme=None):
        # The path to which the system sends an HTTP GET request for a health check.
        self.path = path  # type: str
        # The port to which the system sends an HTTP GET request for a health check.
        self.port = port  # type: int
        # The protocol type supported by the method. Valid values: HTTP and HTTPS.
        self.scheme = scheme  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket(TeaModel):
    def __init__(self, host=None, port=None):
        # The hostname.
        self.host = host  # type: str
        # The port number.
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe(TeaModel):
    def __init__(self, execs=None, failure_threshold=None, http_get=None, initial_delay_seconds=None,
                 period_seconds=None, success_threshold=None, tcp_socket=None, timeout_seconds=None):
        # The commands that are used to check the containers.
        self.execs = execs  # type: list[str]
        # The minimum number of consecutive failures that must occur for the check to be considered failed. Default value: 3.
        self.failure_threshold = failure_threshold  # type: int
        # The HTTP GET method used to check the container.
        self.http_get = http_get  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet
        # The number of seconds between the time when the startup of the container ends and the time when the probe starts.
        self.initial_delay_seconds = initial_delay_seconds  # type: int
        # The interval at which the health check is performed. Unit: seconds. Default value: 10. Minimum value: 1.
        self.period_seconds = period_seconds  # type: int
        # The minimum number of consecutive successes that must occur for the check to be considered successful. Default value: 1. Set the value to 1.
        self.success_threshold = success_threshold  # type: int
        # The TCP socket method that is used to check the container.
        self.tcp_socket = tcp_socket  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket
        # The timeout period of the check. Default value: 1. Minimum value: 1. Unit: seconds.
        self.timeout_seconds = timeout_seconds  # type: int

    def validate(self):
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execs is not None:
            result['Execs'] = self.execs
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Execs') is not None:
            self.execs = m.get('Execs')
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts(TeaModel):
    def __init__(self, port=None, protocol=None):
        # The port number. Valid values: 1 to 65535.
        self.port = port  # type: int
        # The protocol type.
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState(TeaModel):
    def __init__(self, detail_status=None, exit_code=None, finish_time=None, message=None, reason=None, signal=None,
                 start_time=None, state=None):
        # The details of the container status.
        self.detail_status = detail_status  # type: str
        # The exit code of the container.
        self.exit_code = exit_code  # type: int
        # The time when the container stopped running.
        self.finish_time = finish_time  # type: str
        # The message about the container status.
        self.message = message  # type: str
        # The reason why the container is in this state.
        self.reason = reason  # type: str
        # The code of the container status.
        self.signal = signal  # type: int
        # The time when the container started to run.
        self.start_time = start_time  # type: str
        # The container status. Valid values:
        # 
        # *   Waiting: The container is being started.
        # *   Running: The container is running.
        # *   Terminated: The container stops running.
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet(TeaModel):
    def __init__(self, path=None, port=None, scheme=None):
        # The path to which the system sends an HTTP GET request for a health check.
        self.path = path  # type: str
        # The port to which the system sends an HTTP GET request for a health check.
        self.port = port  # type: int
        # The protocol type supported by the method. Valid values: HTTP and HTTPS.
        self.scheme = scheme  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket(TeaModel):
    def __init__(self, host=None, port=None):
        # The hostname.
        self.host = host  # type: str
        # The port number.
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe(TeaModel):
    def __init__(self, execs=None, failure_threshold=None, http_get=None, initial_delay_seconds=None,
                 period_seconds=None, success_threshold=None, tcp_socket=None, timeout_seconds=None):
        # The commands that are run in the container when you use a CLI to perform health checks.
        self.execs = execs  # type: list[str]
        # The minimum number of consecutive failures that must occur for the check to be considered failed. Default value: 3.
        self.failure_threshold = failure_threshold  # type: int
        # The HTTP GET method that is used to check the container.
        self.http_get = http_get  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet
        # The number of seconds between the time when the startup of the container ends and the time when the probe starts.
        self.initial_delay_seconds = initial_delay_seconds  # type: int
        # The interval at which the health check is performed. Unit: seconds. Default value: 10. Minimum value: 1.
        self.period_seconds = period_seconds  # type: int
        # The minimum number of consecutive successes that must occur for the check to be considered successful. Default value: 1. Set the value to 1.
        self.success_threshold = success_threshold  # type: int
        # The TCP socket method that is used to check the container.
        self.tcp_socket = tcp_socket  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket
        # The timeout period of the check. Default value: 1. Minimum value: 1. Unit: seconds.
        self.timeout_seconds = timeout_seconds  # type: int

    def validate(self):
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execs is not None:
            result['Execs'] = self.execs
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Execs') is not None:
            self.execs = m.get('Execs')
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability(TeaModel):
    def __init__(self, adds=None):
        # The permissions specific to the processes in the container.
        self.adds = adds  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext(TeaModel):
    def __init__(self, capability=None, read_only_root_filesystem=None, run_as_user=None):
        # The permissions specific to the processes in the container.
        self.capability = capability  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability
        # Indicates whether permissions on the root file system are read-only.
        self.read_only_root_filesystem = read_only_root_filesystem  # type: bool
        # The user ID (UID) that is used to run the container.
        self.run_as_user = run_as_user  # type: long

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts(TeaModel):
    def __init__(self, mount_path=None, mount_propagation=None, name=None, read_only=None, sub_path=None):
        # The directory of the volume that is mounted to the container. The data in this directory is overwritten by the data on the volume.
        self.mount_path = mount_path  # type: str
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on the volume or on the subdirectories of the volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume.
        # *   Bidirectional: The volume mount behaves the same as the HostToContainer mount. The volume mount receives subsequent mounts that are performed on the volume or on the subdirectories of the volume. In addition, all volume mounts that are performed on the container are propagated back to the host and all containers of all pods that use the same volume.
        self.mount_propagation = mount_propagation  # type: str
        # The volume name.
        self.name = name  # type: str
        # Indicates whether the volume is read-only.
        self.read_only = read_only  # type: bool
        # The subdirectory of the volume. You can use this parameter to mount the same volume to different subdirectories of the container.
        self.sub_path = sub_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsContainers(TeaModel):
    def __init__(self, args=None, commands=None, cpu=None, current_state=None, environment_vars=None, gpu=None,
                 image=None, image_pull_policy=None, liveness_probe=None, memory=None, name=None, ports=None,
                 previous_state=None, readiness_probe=None, ready=None, restart_count=None, security_context=None, stdin=None,
                 stdin_once=None, tty=None, volume_mounts=None, working_dir=None):
        # The arguments that are passed to the startup commands of the container.
        self.args = args  # type: list[str]
        # The startup commands of the container.
        self.commands = commands  # type: list[str]
        # The number of vCPUs that are allocated to the container.
        self.cpu = cpu  # type: float
        # The current container status.
        self.current_state = current_state  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState
        # The environment variables of the container.
        self.environment_vars = environment_vars  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars]
        # The number of GPUs.
        self.gpu = gpu  # type: int
        # The image in the container.
        self.image = image  # type: str
        # The image pulling policy. Valid values:
        # 
        # *   Always: Each time the instance is updated, image pulling is performed.
        # *   IfNotPresent: On-premises images are used first. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy  # type: str
        # The liveness probe of the container.
        self.liveness_probe = liveness_probe  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe
        # The memory size of the container. Unit: GiB.
        self.memory = memory  # type: float
        # The name of the container.
        self.name = name  # type: str
        # The exposed ports and protocols of the container.
        self.ports = ports  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts]
        # The previous status of the container.
        self.previous_state = previous_state  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState
        # The readiness probe that is used to check whether the container is ready to serve a request.
        self.readiness_probe = readiness_probe  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe
        # Indicates whether the container passed the readiness probe.
        self.ready = ready  # type: bool
        # The number of times that the container restarted.
        self.restart_count = restart_count  # type: int
        # The security context of the elastic container instance.
        self.security_context = security_context  # type: DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext
        # Indicates whether the container allocates buffer resources to standard input streams when the container is running. If you do not specify this parameter, an end-of-file (EOF) error may occur when standard input streams in the container are read. Default value: false.
        self.stdin = stdin  # type: bool
        # Indicates whether standard input streams are disconnected after a client is disconnected. If Stdin is set to true, standard input streams remain connected among multiple sessions. If StdinOnce is set to true, standard input streams are connected after the container is started, and remain idle until a client is connected to receive data. After the client is disconnected, streams are also disconnected, and remain disconnected until the container restarts.
        self.stdin_once = stdin_once  # type: bool
        # Indicates whether interaction is enabled. Default value: false. If the value of the Command parameter is `/bin/bash`, the value of this parameter is true.
        self.tty = tty  # type: bool
        # Information about the mounted volumes.
        self.volume_mounts = volume_mounts  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts]
        # The working directory of the container.
        self.working_dir = working_dir  # type: str

    def validate(self):
        if self.current_state:
            self.current_state.validate()
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.previous_state:
            self.previous_state.validate()
        if self.readiness_probe:
            self.readiness_probe.validate()
        if self.security_context:
            self.security_context.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsContainers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.current_state is not None:
            result['CurrentState'] = self.current_state.to_map()
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.previous_state is not None:
            result['PreviousState'] = self.previous_state.to_map()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CurrentState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersCurrentState()
            self.current_state = temp_model.from_map(m['CurrentState'])
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('LivenessProbe') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('PreviousState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersPreviousState()
            self.previous_state = temp_model.from_map(m['PreviousState'])
        if m.get('ReadinessProbe') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('SecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions(TeaModel):
    def __init__(self, name=None, value=None):
        # The variable name of the option.
        self.name = name  # type: str
        # The variable value of the option.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions, self).to_map()
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


class DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig(TeaModel):
    def __init__(self, name_servers=None, options=None, searches=None):
        # The IP addresses of DNS servers.
        self.name_servers = name_servers  # type: list[str]
        # The options. Each option is a name-value pair. The value in the name-value pair is optional.
        self.options = options  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions]
        # The search domain of the DNS server.
        self.searches = searches  # type: list[str]

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_servers is not None:
            result['NameServers'] = self.name_servers
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.searches is not None:
            result['Searches'] = self.searches
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NameServers') is not None:
            self.name_servers = m.get('NameServers')
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsDnsConfigOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('Searches') is not None:
            self.searches = m.get('Searches')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls(TeaModel):
    def __init__(self, name=None, value=None):
        # The name of the Sysctl parameter.
        self.name = name  # type: str
        # The value of the Sysctl parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls, self).to_map()
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


class DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext(TeaModel):
    def __init__(self, sysctls=None):
        # sysctl parameters.
        self.sysctls = sysctls  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls]

    def validate(self):
        if self.sysctls:
            for k in self.sysctls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sysctls'] = []
        if self.sysctls is not None:
            for k in self.sysctls:
                result['Sysctls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sysctls = []
        if m.get('Sysctls') is not None:
            for k in m.get('Sysctls'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContextSysctls()
                self.sysctls.append(temp_model.from_map(k))
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsEvents(TeaModel):
    def __init__(self, count=None, first_timestamp=None, last_timestamp=None, message=None, name=None, reason=None,
                 type=None):
        # The number of the events.
        self.count = count  # type: int
        # The start time of the event.
        self.first_timestamp = first_timestamp  # type: str
        # The end time of the event.
        self.last_timestamp = last_timestamp  # type: str
        # The event message.
        self.message = message  # type: str
        # The category to which the event belongs.
        self.name = name  # type: str
        # The event name.
        self.reason = reason  # type: str
        # The type of the event. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsHostAliases(TeaModel):
    def __init__(self, hostnames=None, ip=None):
        # The information about the hosts.
        self.hostnames = hostnames  # type: list[str]
        # The IP address of the instance.
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsHostAliases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState(TeaModel):
    def __init__(self, detail_status=None, exit_code=None, finish_time=None, message=None, reason=None, signal=None,
                 start_time=None, state=None):
        # The details of the container status.
        self.detail_status = detail_status  # type: str
        # The exit code of the container.
        self.exit_code = exit_code  # type: int
        # The time when the container stopped running.
        self.finish_time = finish_time  # type: str
        # The event message.
        self.message = message  # type: str
        # The reason why the container is in this state.
        self.reason = reason  # type: str
        # The code of the container status.
        self.signal = signal  # type: int
        # The time when the container started to run.
        self.start_time = start_time  # type: str
        # The container status. Valid values:
        # 
        # *   Waiting
        # *   Running
        # *   Terminated
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef(TeaModel):
    def __init__(self, field_path=None):
        # The path of the field. Only `status.podIP` is supported.
        self.field_path = field_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom(TeaModel):
    def __init__(self, field_ref=None):
        # The specified fields.
        self.field_ref = field_ref  # type: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFromFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars(TeaModel):
    def __init__(self, key=None, value=None, value_from=None):
        # The name of the environment variable.
        self.key = key  # type: str
        # The value of the environment variable.
        self.value = value  # type: str
        # The source of the environment variable value. This parameter has a value only when the Value parameter is not empty.
        self.value_from = value_from  # type: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom

    def validate(self):
        if self.value_from:
            self.value_from.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.value_from is not None:
            result['ValueFrom'] = self.value_from.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueFrom') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVarsValueFrom()
            self.value_from = temp_model.from_map(m['ValueFrom'])
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts(TeaModel):
    def __init__(self, port=None, protocol=None):
        # The port number. Valid values: 1 to 65535.
        self.port = port  # type: int
        # The protocol type.
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState(TeaModel):
    def __init__(self, detail_status=None, exit_code=None, finish_time=None, message=None, reason=None, signal=None,
                 start_time=None, state=None):
        # The details of the container status.
        self.detail_status = detail_status  # type: str
        # The exit code of the container.
        self.exit_code = exit_code  # type: int
        # The time when the container stopped running.
        self.finish_time = finish_time  # type: str
        # The message about the container status.
        self.message = message  # type: str
        # The reason why the container is in this state.
        self.reason = reason  # type: str
        # The code of the container status.
        self.signal = signal  # type: int
        # The time when the container started to run.
        self.start_time = start_time  # type: str
        # The container status. Valid values: Waiting, Running, and Terminated.
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_status is not None:
            result['DetailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signal is not None:
            result['Signal'] = self.signal
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailStatus') is not None:
            self.detail_status = m.get('DetailStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Signal') is not None:
            self.signal = m.get('Signal')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability(TeaModel):
    def __init__(self, adds=None):
        # The permissions specific to the processes in the container.
        self.adds = adds  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext(TeaModel):
    def __init__(self, capability=None, read_only_root_filesystem=None, run_as_user=None):
        # The permissions specific to the processes in the container.
        self.capability = capability  # type: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability
        # Indicates whether permissions on the root file system are read-only.
        self.read_only_root_filesystem = read_only_root_filesystem  # type: bool
        # The UID this is used to run the entry point of the container process.
        self.run_as_user = run_as_user  # type: long

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts(TeaModel):
    def __init__(self, mount_path=None, mount_propagation=None, name=None, read_only=None):
        # The directory of the volume that is mounted to the container. The data in this directory is overwritten by the data on the volume.
        self.mount_path = mount_path  # type: str
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on the volume or on the subdirectories of the volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume.
        # *   Bidirectional: The volume mount behaves the same as the HostToContainer mount. The volume mount receives subsequent mounts that are performed on the volume or on the subdirectories of the volume. In addition, all volume mounts that are performed on the container are propagated back to the host and all containers of all pods that use the same volume.
        self.mount_propagation = mount_propagation  # type: str
        # The name of the volume. The value of this parameter is the same as the name of the volume that you selected when you purchased the container.
        self.name = name  # type: str
        # Default value: false.
        self.read_only = read_only  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsInitContainers(TeaModel):
    def __init__(self, args=None, command=None, cpu=None, current_state=None, environment_vars=None, gpu=None,
                 image=None, image_pull_policy=None, memory=None, name=None, ports=None, previous_state=None, ready=None,
                 restart_count=None, security_context=None, volume_mounts=None, working_dir=None):
        # The arguments that are passed to the startup commands of the container.
        self.args = args  # type: list[str]
        # The startup commands of the containers.
        self.command = command  # type: list[str]
        # The number of vCPUs that are allocated to the container.
        self.cpu = cpu  # type: float
        # The current container status.
        self.current_state = current_state  # type: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState
        # The environment variables of the container.
        self.environment_vars = environment_vars  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars]
        # The number of GPUs.
        self.gpu = gpu  # type: int
        # The image of the container.
        self.image = image  # type: str
        # The image pulling policy. Valid values:
        # 
        # *   Always: Each time the instance is updated, image pulling is performed.
        # *   IfNotPresent: On-premises images are used first. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy  # type: str
        # The memory size of the init container. Unit: GiB.
        self.memory = memory  # type: float
        # The name of the init container.
        self.name = name  # type: str
        # The exposed ports and protocols of the container.
        self.ports = ports  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts]
        # The previous state of the container.
        self.previous_state = previous_state  # type: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState
        # Indicates whether the container passed the readiness probe.
        self.ready = ready  # type: bool
        # The number of times the container restarted.
        self.restart_count = restart_count  # type: int
        # The security context of the container.
        self.security_context = security_context  # type: DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext
        # The information about the volumes that are mounted to the init container.
        self.volume_mounts = volume_mounts  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts]
        # The working directory of the container.
        self.working_dir = working_dir  # type: str

    def validate(self):
        if self.current_state:
            self.current_state.validate()
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.previous_state:
            self.previous_state.validate()
        if self.security_context:
            self.security_context.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsInitContainers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.current_state is not None:
            result['CurrentState'] = self.current_state.to_map()
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.previous_state is not None:
            result['PreviousState'] = self.previous_state.to_map()
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CurrentState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersCurrentState()
            self.current_state = temp_model.from_map(m['CurrentState'])
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('PreviousState') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersPreviousState()
            self.previous_state = temp_model.from_map(m['PreviousState'])
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('SecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsTags, self).to_map()
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


class DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths(TeaModel):
    def __init__(self, content=None, path=None):
        # The content of the ConfigFile volume. Maximum size: 32 KB.
        self.content = content  # type: str
        # The relative path of the ConfigFile volume.
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeContainerGroupsResponseBodyContainerGroupsVolumes(TeaModel):
    def __init__(self, config_file_volume_config_file_to_paths=None, disk_volume_disk_id=None,
                 disk_volume_fs_type=None, empty_dir_volume_medium=None, empty_dir_volume_size_limit=None, flex_volume_driver=None,
                 flex_volume_fs_type=None, flex_volume_options=None, nfsvolume_path=None, nfsvolume_read_only=None,
                 nfsvolume_server=None, name=None, type=None):
        # The path of the ConfigFile volume.
        self.config_file_volume_config_file_to_paths = config_file_volume_config_file_to_paths  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths]
        # The ID of the disk when you set the Type parameter to DiskVolume.
        self.disk_volume_disk_id = disk_volume_disk_id  # type: str
        # The file system type of the disk volume.
        self.disk_volume_fs_type = disk_volume_fs_type  # type: str
        # The storage media for the emptyDir volume. This parameter is empty by default, indicating that the node file system is used as the storage media. Valid values:
        # 
        # *   Memory: Memory is used as the storage media.
        # *   LocalRaid0: Local disks are formed into RAID 0. This value is valid only if an elastic container instance that has local disks mounted is created. For more information, see [Create an elastic container instance that has local disks mounted](~~114664~~).
        self.empty_dir_volume_medium = empty_dir_volume_medium  # type: str
        # The storage size of the emptyDir volume.
        self.empty_dir_volume_size_limit = empty_dir_volume_size_limit  # type: str
        # The name of the driver when you set the Type parameter to FlexVolume.
        self.flex_volume_driver = flex_volume_driver  # type: str
        # The file system type when you set the Type parameter to FlexVolume. The default value varies based on the script of the FlexVolume plug-in.
        self.flex_volume_fs_type = flex_volume_fs_type  # type: str
        # The options when you set the Type parameter to FlexVolume.
        self.flex_volume_options = flex_volume_options  # type: str
        # The path of the NFS volume.
        self.nfsvolume_path = nfsvolume_path  # type: str
        # Indicates whether the NFS volume is read-only.
        self.nfsvolume_read_only = nfsvolume_read_only  # type: bool
        # The endpoint of the server when you set the Type parameter to NFSVolume.
        self.nfsvolume_server = nfsvolume_server  # type: str
        # The volume name.
        self.name = name  # type: str
        # The type of the volume. Valid values:
        # 
        # *   EmptyDirVolume
        # *   NFSVolume
        # *   ConfigFileVolume
        # *   FlexVolume
        self.type = type  # type: str

    def validate(self):
        if self.config_file_volume_config_file_to_paths:
            for k in self.config_file_volume_config_file_to_paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroupsVolumes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigFileVolumeConfigFileToPaths'] = []
        if self.config_file_volume_config_file_to_paths is not None:
            for k in self.config_file_volume_config_file_to_paths:
                result['ConfigFileVolumeConfigFileToPaths'].append(k.to_map() if k else None)
        if self.disk_volume_disk_id is not None:
            result['DiskVolumeDiskId'] = self.disk_volume_disk_id
        if self.disk_volume_fs_type is not None:
            result['DiskVolumeFsType'] = self.disk_volume_fs_type
        if self.empty_dir_volume_medium is not None:
            result['EmptyDirVolumeMedium'] = self.empty_dir_volume_medium
        if self.empty_dir_volume_size_limit is not None:
            result['EmptyDirVolumeSizeLimit'] = self.empty_dir_volume_size_limit
        if self.flex_volume_driver is not None:
            result['FlexVolumeDriver'] = self.flex_volume_driver
        if self.flex_volume_fs_type is not None:
            result['FlexVolumeFsType'] = self.flex_volume_fs_type
        if self.flex_volume_options is not None:
            result['FlexVolumeOptions'] = self.flex_volume_options
        if self.nfsvolume_path is not None:
            result['NFSVolumePath'] = self.nfsvolume_path
        if self.nfsvolume_read_only is not None:
            result['NFSVolumeReadOnly'] = self.nfsvolume_read_only
        if self.nfsvolume_server is not None:
            result['NFSVolumeServer'] = self.nfsvolume_server
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_file_volume_config_file_to_paths = []
        if m.get('ConfigFileVolumeConfigFileToPaths') is not None:
            for k in m.get('ConfigFileVolumeConfigFileToPaths'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsVolumesConfigFileVolumeConfigFileToPaths()
                self.config_file_volume_config_file_to_paths.append(temp_model.from_map(k))
        if m.get('DiskVolumeDiskId') is not None:
            self.disk_volume_disk_id = m.get('DiskVolumeDiskId')
        if m.get('DiskVolumeFsType') is not None:
            self.disk_volume_fs_type = m.get('DiskVolumeFsType')
        if m.get('EmptyDirVolumeMedium') is not None:
            self.empty_dir_volume_medium = m.get('EmptyDirVolumeMedium')
        if m.get('EmptyDirVolumeSizeLimit') is not None:
            self.empty_dir_volume_size_limit = m.get('EmptyDirVolumeSizeLimit')
        if m.get('FlexVolumeDriver') is not None:
            self.flex_volume_driver = m.get('FlexVolumeDriver')
        if m.get('FlexVolumeFsType') is not None:
            self.flex_volume_fs_type = m.get('FlexVolumeFsType')
        if m.get('FlexVolumeOptions') is not None:
            self.flex_volume_options = m.get('FlexVolumeOptions')
        if m.get('NFSVolumePath') is not None:
            self.nfsvolume_path = m.get('NFSVolumePath')
        if m.get('NFSVolumeReadOnly') is not None:
            self.nfsvolume_read_only = m.get('NFSVolumeReadOnly')
        if m.get('NFSVolumeServer') is not None:
            self.nfsvolume_server = m.get('NFSVolumeServer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeContainerGroupsResponseBodyContainerGroups(TeaModel):
    def __init__(self, compute_category=None, container_group_id=None, container_group_name=None, containers=None,
                 cpu=None, creation_time=None, discount=None, dns_config=None, eci_security_context=None,
                 eni_instance_id=None, ephemeral_storage=None, events=None, expired_time=None, failed_time=None, host_aliases=None,
                 init_containers=None, instance_type=None, internet_ip=None, intranet_ip=None, ipv_6address=None, memory=None,
                 ram_role_name=None, region_id=None, resource_group_id=None, restart_policy=None, security_group_id=None,
                 spot_price_limit=None, spot_strategy=None, status=None, succeeded_time=None, tags=None, tenant_eni_instance_id=None,
                 tenant_eni_ip=None, tenant_security_group_id=None, tenant_vswitch_id=None, v_switch_id=None, volumes=None,
                 vpc_id=None, zone_id=None):
        # The computing power type of the elastic container instance. A value of economy indicates economic instances.
        self.compute_category = compute_category  # type: str
        # The instance ID.
        self.container_group_id = container_group_id  # type: str
        # The instance name.
        self.container_group_name = container_group_name  # type: str
        # The information about containers in the elastic container instance.
        self.containers = containers  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsContainers]
        # The number of vCPUs that are allocated to the elastic container instance.
        self.cpu = cpu  # type: float
        # The time when the system created the elastic container instance after the system received the request. The time follows the RFC 3339 standard. The time is displayed in UTC.
        self.creation_time = creation_time  # type: str
        # The discount.
        self.discount = discount  # type: int
        # The Domain Name System (DNS) settings.
        self.dns_config = dns_config  # type: DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig
        # The security context of the elastic container instance.
        self.eci_security_context = eci_security_context  # type: DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext
        # The ID of the elastic network interface (ENI).
        self.eni_instance_id = eni_instance_id  # type: str
        # The size of the temporary storage space. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage  # type: int
        # The events of the elastic container instance. A maximum of 50 events can be returned.
        self.events = events  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsEvents]
        # The time when the elastic container instance failed to run due to overdue payments. The time follows the RFC 3339 standard. The time is displayed in UTC.
        self.expired_time = expired_time  # type: str
        # The time when the instance failed to run. The time follows the RFC 3339 standard. The time is displayed in UTC.
        self.failed_time = failed_time  # type: str
        # The hostnames and IP addresses for a container that are added to the hosts file of the elastic container instance.
        self.host_aliases = host_aliases  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsHostAliases]
        # The information about the init containers.
        self.init_containers = init_containers  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsInitContainers]
        # The instance type of the specified Elastic Compute Service (ECS) instance.
        self.instance_type = instance_type  # type: str
        # The public IP address.
        self.internet_ip = internet_ip  # type: str
        # The private IP address.
        self.intranet_ip = intranet_ip  # type: str
        # The IPv6 address of the instance.
        self.ipv_6address = ipv_6address  # type: str
        # The memory size of the instance. Unit: GiB.
        self.memory = memory  # type: float
        # The name of the instance RAM role. The elastic container instance and the ECS instance share a RAM role. For more information, see [Use an instance RAM role by calling API operations](~~61178~~).
        self.ram_role_name = ram_role_name  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The restart policy of the elastic container instance. Valid values:
        # 
        # *   Never: Never restarts the instance if a container in the instance exits.
        # *   Always: Always restarts the instance if a container in the instance exits.
        # *   OnFailure: Restarts the instance only if a container in the instance exists upon failure with a status code of non-zero.
        self.restart_policy = restart_policy  # type: str
        # The security group ID.
        self.security_group_id = security_group_id  # type: str
        # The maximum hourly price for the preemptible elastic container instance.
        # 
        # This parameter is returned only when SpotStrategy is set to SpotWithPriceLimit.
        self.spot_price_limit = spot_price_limit  # type: float
        # The bid policy for the instance. Default value: NoSpot. Valid values:
        # 
        # *   NoSpot: The instance is a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is a preemptible instance that has a maximum price.
        # *   SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is used as the bid price.
        self.spot_strategy = spot_strategy  # type: str
        # The state of the instance. Valid values:
        # 
        # *   Pending: The instance is being started.
        # *   Running: The instance is running.
        # *   Succeeded: The instance successfully runs.
        # *   Failed: The instance fails to run.
        # *   Scheduling: The instance is being created.
        # *   ScheduleFailed: The instance fails to be created.
        # *   Restarting: The instance is being restarted.
        # *   Updating: The instance is being updated.
        # *   Terminating: The instance is being terminated.
        # *   Expired: The instance is expired.
        self.status = status  # type: str
        # The time when all containers exited on success. The time follows the RFC 3339 standard. The time is displayed in UTC.
        self.succeeded_time = succeeded_time  # type: str
        # The tags of the instance.
        self.tags = tags  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsTags]
        # This parameter is not publicly available.
        self.tenant_eni_instance_id = tenant_eni_instance_id  # type: str
        # This parameter is not publicly available.
        self.tenant_eni_ip = tenant_eni_ip  # type: str
        # This parameter is not publicly available.
        self.tenant_security_group_id = tenant_security_group_id  # type: str
        # This parameter is not publicly available.
        self.tenant_vswitch_id = tenant_vswitch_id  # type: str
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id  # type: str
        # Information about the volumes.
        self.volumes = volumes  # type: list[DescribeContainerGroupsResponseBodyContainerGroupsVolumes]
        # The ID of the VPC to which the instance belongs.
        self.vpc_id = vpc_id  # type: str
        # The zone to which the instance belongs.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.dns_config:
            self.dns_config.validate()
        if self.eci_security_context:
            self.eci_security_context.validate()
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.host_aliases:
            for k in self.host_aliases:
                if k:
                    k.validate()
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBodyContainerGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_category is not None:
            result['ComputeCategory'] = self.compute_category
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.discount is not None:
            result['Discount'] = self.discount
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        if self.eci_security_context is not None:
            result['EciSecurityContext'] = self.eci_security_context.to_map()
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k in self.host_aliases:
                result['HostAliases'].append(k.to_map() if k else None)
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.status is not None:
            result['Status'] = self.status
        if self.succeeded_time is not None:
            result['SucceededTime'] = self.succeeded_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_eni_instance_id is not None:
            result['TenantEniInstanceId'] = self.tenant_eni_instance_id
        if self.tenant_eni_ip is not None:
            result['TenantEniIp'] = self.tenant_eni_ip
        if self.tenant_security_group_id is not None:
            result['TenantSecurityGroupId'] = self.tenant_security_group_id
        if self.tenant_vswitch_id is not None:
            result['TenantVSwitchId'] = self.tenant_vswitch_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComputeCategory') is not None:
            self.compute_category = m.get('ComputeCategory')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsContainers()
                self.containers.append(temp_model.from_map(k))
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Discount') is not None:
            self.discount = m.get('Discount')
        if m.get('DnsConfig') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        if m.get('EciSecurityContext') is not None:
            temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEciSecurityContext()
            self.eci_security_context = temp_model.from_map(m['EciSecurityContext'])
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k in m.get('HostAliases'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsHostAliases()
                self.host_aliases.append(temp_model.from_map(k))
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsInitContainers()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SucceededTime') is not None:
            self.succeeded_time = m.get('SucceededTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantEniInstanceId') is not None:
            self.tenant_eni_instance_id = m.get('TenantEniInstanceId')
        if m.get('TenantEniIp') is not None:
            self.tenant_eni_ip = m.get('TenantEniIp')
        if m.get('TenantSecurityGroupId') is not None:
            self.tenant_security_group_id = m.get('TenantSecurityGroupId')
        if m.get('TenantVSwitchId') is not None:
            self.tenant_vswitch_id = m.get('TenantVSwitchId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroupsVolumes()
                self.volumes.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeContainerGroupsResponseBody(TeaModel):
    def __init__(self, container_groups=None, next_token=None, request_id=None, total_count=None):
        # Details about the elastic container instances.
        self.container_groups = container_groups  # type: list[DescribeContainerGroupsResponseBodyContainerGroups]
        # The token that determines the start point of the query.
        self.next_token = next_token  # type: str
        # The ID of the request. The value is unique.
        self.request_id = request_id  # type: str
        # The number of queried instances.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.container_groups:
            for k in self.container_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerGroups'] = []
        if self.container_groups is not None:
            for k in self.container_groups:
                result['ContainerGroups'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.container_groups = []
        if m.get('ContainerGroups') is not None:
            for k in m.get('ContainerGroups'):
                temp_model = DescribeContainerGroupsResponseBodyContainerGroups()
                self.container_groups.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeContainerGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContainerGroupsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerGroupsResponse, self).to_map()
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
            temp_model = DescribeContainerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerLogRequest(TeaModel):
    def __init__(self, container_group_id=None, container_name=None, last_time=None, limit_bytes=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 since_seconds=None, start_time=None, tail=None, timestamps=None):
        # The instance ID.
        self.container_group_id = container_group_id  # type: str
        # The name of the container.
        self.container_name = container_name  # type: str
        # Specifies whether to query the logs of the previous container if the container exits and restarts. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.last_time = last_time  # type: bool
        # The limit on the total size of logs. Unit: bytes. Valid values: 1 to 1048576(1 MB).
        self.limit_bytes = limit_bytes  # type: long
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the elastic container instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # A relative time in seconds before the current time from which to show logs. Examples: 10, 20, and 30.
        self.since_seconds = since_seconds  # type: int
        # The beginning of the time range to query. Specify the time in the RFC 3339 standard. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The number of log entries that you want to query. Default value: 500. Maximum value: 2000. A maximum of 1 MB of logs can be returned.
        self.tail = tail  # type: int
        # Specifies whether to return the timestamps of logs. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.timestamps = timestamps  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.limit_bytes is not None:
            result['LimitBytes'] = self.limit_bytes
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.since_seconds is not None:
            result['SinceSeconds'] = self.since_seconds
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tail is not None:
            result['Tail'] = self.tail
        if self.timestamps is not None:
            result['Timestamps'] = self.timestamps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('LimitBytes') is not None:
            self.limit_bytes = m.get('LimitBytes')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SinceSeconds') is not None:
            self.since_seconds = m.get('SinceSeconds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tail') is not None:
            self.tail = m.get('Tail')
        if m.get('Timestamps') is not None:
            self.timestamps = m.get('Timestamps')
        return self


class DescribeContainerLogResponseBody(TeaModel):
    def __init__(self, container_name=None, content=None, request_id=None):
        # The container name.
        self.container_name = container_name  # type: str
        # The content of the log.
        self.content = content  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContainerLogResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerLogResponse, self).to_map()
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
            temp_model = DescribeContainerLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCachesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCachesRequestTag, self).to_map()
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


class DescribeDataCachesRequest(TeaModel):
    def __init__(self, bucket=None, data_cache_id=None, limit=None, next_token=None, owner_account=None,
                 owner_id=None, path=None, region_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, tag=None):
        # The bucket that stores the data cache. Default value: default.
        self.bucket = bucket  # type: str
        # The data cache IDs.
        self.data_cache_id = data_cache_id  # type: list[str]
        # The maximum entries of query results that are allowed to be displayed. Valid values: 1 to 20. Default value: 20.
        self.limit = limit  # type: int
        # The query token. Set the value to the NextToken value that is returned in the previous call.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The virtual host (vHost) directory in which the data cache resides.
        self.path = path  # type: str
        # The region ID of the data caches that you want to query.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the data cache belongs.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The tags that are attached to the data cache.
        self.tag = tag  # type: list[DescribeDataCachesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataCachesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDataCachesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDataCachesResponseBodyDataCachesDataSource(TeaModel):
    def __init__(self, options=None, type=None):
        # The parameters that are configured for the data source.
        self.options = options  # type: str
        # The type of the data source. Valid values:
        # 
        # *   NAS
        # *   OSS
        # *   URL
        # *   SNAPSHOT
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCachesResponseBodyDataCachesDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['Options'] = self.options
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDataCachesResponseBodyDataCachesEvents(TeaModel):
    def __init__(self, count=None, first_timestamp=None, last_timestamp=None, message=None, name=None, reason=None,
                 type=None):
        # The number of times that the event occurred.
        self.count = count  # type: int
        # The time when the event started.
        self.first_timestamp = first_timestamp  # type: str
        # The time when the event ended.
        self.last_timestamp = last_timestamp  # type: str
        # The message about the event.
        self.message = message  # type: str
        # The event name.
        self.name = name  # type: str
        # The reason for the transition into the current status of the event.
        self.reason = reason  # type: str
        # The type of the event. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCachesResponseBodyDataCachesEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDataCachesResponseBodyDataCachesTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCachesResponseBodyDataCachesTags, self).to_map()
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


class DescribeDataCachesResponseBodyDataCaches(TeaModel):
    def __init__(self, bucket=None, container_group_id=None, creation_time=None, data_cache_id=None,
                 data_source=None, events=None, expire_date_time=None, flash_snapshot_id=None, last_matched_time=None,
                 name=None, path=None, progress=None, region_id=None, resource_group_id=None, size=None, snapshot_id=None,
                 status=None, tags=None):
        # The bucket that stores the data cache.
        self.bucket = bucket  # type: str
        # The ID of the elastic container instance that was generated when the data cache was created.
        self.container_group_id = container_group_id  # type: str
        # The time when the data cache was created.
        self.creation_time = creation_time  # type: str
        # The ID of the data cache.
        self.data_cache_id = data_cache_id  # type: str
        # The information about the data source.
        self.data_source = data_source  # type: DescribeDataCachesResponseBodyDataCachesDataSource
        # The events.
        self.events = events  # type: list[DescribeDataCachesResponseBodyDataCachesEvents]
        # The time when the data cache expires.
        self.expire_date_time = expire_date_time  # type: str
        # The ID of the on-premises snapshot.
        self.flash_snapshot_id = flash_snapshot_id  # type: str
        # The time when the data cache was last matched.
        self.last_matched_time = last_matched_time  # type: str
        # The name of the data cache.
        self.name = name  # type: str
        # The directory in which the virtual host of the data cache resides.
        self.path = path  # type: str
        # The creation progress of the data cache.
        self.progress = progress  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The size of the data cache. Unit: GiB.
        self.size = size  # type: int
        # The snapshot ID.
        self.snapshot_id = snapshot_id  # type: str
        # The status of the data cache. Valid values:
        # 
        # *   Loading: The data cache is loading data.
        # *   Creating: The data cache is being created.
        # *   Available: The data cache is created.
        # *   Failed: The data cache failed to be created.
        # *   Updating: The data cache is being updated.
        # *   UpdateFailed: The data cache failed to be updated.
        # 
        # If the data cache is in the Available state, the data cache can be used.
        self.status = status  # type: str
        # The tags that are attached to the data cache.
        self.tags = tags  # type: list[DescribeDataCachesResponseBodyDataCachesTags]

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataCachesResponseBodyDataCaches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.expire_date_time is not None:
            result['ExpireDateTime'] = self.expire_date_time
        if self.flash_snapshot_id is not None:
            result['FlashSnapshotId'] = self.flash_snapshot_id
        if self.last_matched_time is not None:
            result['LastMatchedTime'] = self.last_matched_time
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('DataSource') is not None:
            temp_model = DescribeDataCachesResponseBodyDataCachesDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDataCachesResponseBodyDataCachesEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('ExpireDateTime') is not None:
            self.expire_date_time = m.get('ExpireDateTime')
        if m.get('FlashSnapshotId') is not None:
            self.flash_snapshot_id = m.get('FlashSnapshotId')
        if m.get('LastMatchedTime') is not None:
            self.last_matched_time = m.get('LastMatchedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDataCachesResponseBodyDataCachesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeDataCachesResponseBody(TeaModel):
    def __init__(self, data_caches=None, next_token=None, request_id=None, total_count=None):
        # The information about the data caches.
        self.data_caches = data_caches  # type: list[DescribeDataCachesResponseBodyDataCaches]
        # The query token. Set the value to the NextToken value that is returned in the previous call.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data_caches:
            for k in self.data_caches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataCachesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataCaches'] = []
        if self.data_caches is not None:
            for k in self.data_caches:
                result['DataCaches'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_caches = []
        if m.get('DataCaches') is not None:
            for k in m.get('DataCaches'):
                temp_model = DescribeDataCachesResponseBodyDataCaches()
                self.data_caches.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataCachesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataCachesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataCachesResponse, self).to_map()
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
            temp_model = DescribeDataCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageCachesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N of the image cache.
        self.key = key  # type: str
        # The value of tag N of the image cache.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageCachesRequestTag, self).to_map()
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


class DescribeImageCachesRequest(TeaModel):
    def __init__(self, image=None, image_cache_id=None, image_cache_name=None, image_full_match=None,
                 image_match_count_request=None, limit=None, match_image=None, next_token=None, owner_account=None, owner_id=None,
                 region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None,
                 snapshot_id=None, tag=None):
        # The container images.
        self.image = image  # type: str
        # The IDs of the image caches.
        self.image_cache_id = image_cache_id  # type: str
        # The names of the image caches.
        self.image_cache_name = image_cache_name  # type: str
        # Specifies whether the image layers of the image caches must contain all image layers of the container image.\
        # If you configure MatchImage, you can configure this parameter to further filter query results.
        self.image_full_match = image_full_match  # type: bool
        # The quantity of image caches whose image layers contain all image layers of the container image.\
        # If you configure MatchImage, you can configure this parameter to further filter query results.
        self.image_match_count_request = image_match_count_request  # type: int
        # The maximum entries of query results that are allowed to be displayed.
        self.limit = limit  # type: int
        # The container images used to match the image caches that you want to query. You can specify a maximum of 100 container images.
        self.match_image = match_image  # type: list[str]
        # The pagination token that is used in the next request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the image caches.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the image caches belong.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The IDs of the snapshots that correspond to the image caches.
        self.snapshot_id = snapshot_id  # type: str
        # The tags to add to the image caches.
        self.tag = tag  # type: list[DescribeImageCachesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImageCachesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.image_full_match is not None:
            result['ImageFullMatch'] = self.image_full_match
        if self.image_match_count_request is not None:
            result['ImageMatchCountRequest'] = self.image_match_count_request
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.match_image is not None:
            result['MatchImage'] = self.match_image
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('ImageFullMatch') is not None:
            self.image_full_match = m.get('ImageFullMatch')
        if m.get('ImageMatchCountRequest') is not None:
            self.image_match_count_request = m.get('ImageMatchCountRequest')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MatchImage') is not None:
            self.match_image = m.get('MatchImage')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeImageCachesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeImageCachesResponseBodyImageCachesEvents(TeaModel):
    def __init__(self, count=None, first_timestamp=None, last_timestamp=None, message=None, name=None, reason=None,
                 type=None):
        # The number of events.
        self.count = count  # type: int
        # The time when the event started.
        self.first_timestamp = first_timestamp  # type: str
        # The time when the event ended.
        self.last_timestamp = last_timestamp  # type: str
        # The message about the event.
        self.message = message  # type: str
        # The name of the event.
        self.name = name  # type: str
        # The cause of the event.
        self.reason = reason  # type: str
        # The type of the event. Valid values:
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageCachesResponseBodyImageCachesEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeImageCachesResponseBodyImageCachesTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageCachesResponseBodyImageCachesTags, self).to_map()
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


class DescribeImageCachesResponseBodyImageCaches(TeaModel):
    def __init__(self, container_group_id=None, creation_time=None, elimination_strategy=None, events=None,
                 expire_date_time=None, flash_snapshot_id=None, image_cache_id=None, image_cache_name=None, image_cache_size=None,
                 images=None, last_matched_time=None, progress=None, region_id=None, resource_group_id=None,
                 snapshot_id=None, status=None, tags=None):
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id  # type: str
        # The time when the image cache was created.
        self.creation_time = creation_time  # type: str
        # The elimination policy of the image cache. This parameter is empty by default, which indicates that the image cache is always retained.
        # 
        # You can set this parameter to LRU, which indicates that the image cache can be automatically deleted. When the number of image caches reaches the quota, the system automatically deletes the image caches whose EliminationStrategy parameter is set to LRU and that are least regularly used.
        self.elimination_strategy = elimination_strategy  # type: str
        # The events of pulling an image to create the image cache.
        self.events = events  # type: list[DescribeImageCachesResponseBodyImageCachesEvents]
        # The time when the image cache expires.
        self.expire_date_time = expire_date_time  # type: str
        # The ID of the local snapshot. A temporary local snapshot is created if the instant image cache feature is enabled.
        self.flash_snapshot_id = flash_snapshot_id  # type: str
        # The ID of the image cache.
        self.image_cache_id = image_cache_id  # type: str
        # The name of the image cache.
        self.image_cache_name = image_cache_name  # type: str
        # The size of the image cache. Unit: GiB.
        self.image_cache_size = image_cache_size  # type: int
        # The images contained in the image cache.
        self.images = images  # type: list[str]
        # The time when the image cache was last matched.
        self.last_matched_time = last_matched_time  # type: str
        # The progress of creating the snapshot that is used to create the image cache.
        # 
        # >  If the instant image cache feature is enabled, the system creates a temporary local snapshot and then a regular snapshot. In this case, this parameter indicates the progress of creating the regular snapshot.
        self.progress = progress  # type: str
        # The region ID of the image cache.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the image cache belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the snapshot that corresponds to the image cache.
        self.snapshot_id = snapshot_id  # type: str
        # The status of the image cache. Valid values:
        # 
        # *   Preparing: The image cache is being prepared.
        # *   Creating: The image is being created.
        # *   Ready: The image cache is created.
        # *   Failed: The image cache failed to be created.
        # *   Updating: The image cache is being updated.
        # *   UpdateFailed: The image cache failed to be updated.
        # 
        # The image cache is ready for use when it is in the Ready state.
        self.status = status  # type: str
        # The tags of the image cache.
        self.tags = tags  # type: list[DescribeImageCachesResponseBodyImageCachesTags]

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImageCachesResponseBodyImageCaches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.elimination_strategy is not None:
            result['EliminationStrategy'] = self.elimination_strategy
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.expire_date_time is not None:
            result['ExpireDateTime'] = self.expire_date_time
        if self.flash_snapshot_id is not None:
            result['FlashSnapshotId'] = self.flash_snapshot_id
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.image_cache_size is not None:
            result['ImageCacheSize'] = self.image_cache_size
        if self.images is not None:
            result['Images'] = self.images
        if self.last_matched_time is not None:
            result['LastMatchedTime'] = self.last_matched_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EliminationStrategy') is not None:
            self.elimination_strategy = m.get('EliminationStrategy')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeImageCachesResponseBodyImageCachesEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('ExpireDateTime') is not None:
            self.expire_date_time = m.get('ExpireDateTime')
        if m.get('FlashSnapshotId') is not None:
            self.flash_snapshot_id = m.get('FlashSnapshotId')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('ImageCacheSize') is not None:
            self.image_cache_size = m.get('ImageCacheSize')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('LastMatchedTime') is not None:
            self.last_matched_time = m.get('LastMatchedTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeImageCachesResponseBodyImageCachesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeImageCachesResponseBody(TeaModel):
    def __init__(self, image_caches=None, next_token=None, request_id=None, total_count=None):
        # The information about image caches.
        self.image_caches = image_caches  # type: list[DescribeImageCachesResponseBodyImageCaches]
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.image_caches:
            for k in self.image_caches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImageCachesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageCaches'] = []
        if self.image_caches is not None:
            for k in self.image_caches:
                result['ImageCaches'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.image_caches = []
        if m.get('ImageCaches') is not None:
            for k in m.get('ImageCaches'):
                temp_model = DescribeImageCachesResponseBodyImageCaches()
                self.image_caches.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageCachesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeImageCachesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImageCachesResponse, self).to_map()
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
            temp_model = DescribeImageCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceOpsRecordsRequest(TeaModel):
    def __init__(self, container_group_id=None, ops_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id  # type: str
        # The type of the O\&M task. Valid values:
        # 
        # *   coredump
        # *   tcpdump
        self.ops_type = ops_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceOpsRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.ops_type is not None:
            result['OpsType'] = self.ops_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeInstanceOpsRecordsResponseBodyRecords(TeaModel):
    def __init__(self, create_time=None, expire_time=None, ops_status=None, ops_type=None, result_content=None,
                 result_type=None):
        # The time when the O\&M task was created.
        self.create_time = create_time  # type: str
        # The time when the O\&M task expires.
        self.expire_time = expire_time  # type: str
        # The status of the O\&M task.
        self.ops_status = ops_status  # type: str
        # The type of the O\&M task.
        self.ops_type = ops_type  # type: str
        # The content of the O\&M result. The content is the download URL of the files that are generated for the O\&M task.
        self.result_content = result_content  # type: str
        # The type of the O\&M result. Valid value: OSS. This value indicates that the files generated for the O\&M task are saved to Object Storage Service (OSS) buckets.
        self.result_type = result_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceOpsRecordsResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ops_status is not None:
            result['OpsStatus'] = self.ops_status
        if self.ops_type is not None:
            result['OpsType'] = self.ops_type
        if self.result_content is not None:
            result['ResultContent'] = self.result_content
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('OpsStatus') is not None:
            self.ops_status = m.get('OpsStatus')
        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')
        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        return self


class DescribeInstanceOpsRecordsResponseBody(TeaModel):
    def __init__(self, records=None, request_id=None):
        # The details of the O\&M tasks.
        self.records = records  # type: list[DescribeInstanceOpsRecordsResponseBodyRecords]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceOpsRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeInstanceOpsRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceOpsRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceOpsRecordsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceOpsRecordsResponse, self).to_map()
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
            temp_model = DescribeInstanceOpsRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiContainerGroupMetricRequest(TeaModel):
    def __init__(self, container_group_ids=None, metric_type=None, owner_account=None, owner_id=None,
                 region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None):
        # The instance ID. The value is a JSON array. You can specify up to 20 instance IDs at a time.
        self.container_group_ids = container_group_ids  # type: str
        # The type of the monitoring data. Set the value to summary. This value indicates that records are returned.
        self.metric_type = metric_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the elastic container instances belong.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_ids is not None:
            result['ContainerGroupIds'] = self.container_group_ids
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupIds') is not None:
            self.container_group_ids = m.get('ContainerGroupIds')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU(TeaModel):
    def __init__(self, limit=None, load=None, usage_core_nano_seconds=None, usage_nano_cores=None):
        # The upper limit of vCPU usage. The calculation formula for this parameter: The number of vCPUs × 1000.
        self.limit = limit  # type: long
        # The average load in the last 10 seconds.
        self.load = load  # type: long
        # The cumulative usage of vCPUs.
        self.usage_core_nano_seconds = usage_core_nano_seconds  # type: long
        # The vCPU usage in the sampling window. Unit for the sampling window: nanoseconds.
        self.usage_nano_cores = usage_nano_cores  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.load is not None:
            result['Load'] = self.load
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU(TeaModel):
    def __init__(self, limit=None, load=None, usage_core_nano_seconds=None, usage_nano_cores=None):
        # The upper limit of vCPU usage. The calculation formula for this parameter: The number of vCPUs × 1000.
        self.limit = limit  # type: long
        # The average load in the last 10 seconds.
        self.load = load  # type: long
        # The cumulative usage of vCPUs.
        self.usage_core_nano_seconds = usage_core_nano_seconds  # type: long
        # The vCPU usage in the sampling window. Unit for the sampling window: nanoseconds.
        self.usage_nano_cores = usage_nano_cores  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.load is not None:
            result['Load'] = self.load
        if self.usage_core_nano_seconds is not None:
            result['UsageCoreNanoSeconds'] = self.usage_core_nano_seconds
        if self.usage_nano_cores is not None:
            result['UsageNanoCores'] = self.usage_nano_cores
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('UsageCoreNanoSeconds') is not None:
            self.usage_core_nano_seconds = m.get('UsageCoreNanoSeconds')
        if m.get('UsageNanoCores') is not None:
            self.usage_nano_cores = m.get('UsageNanoCores')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory(TeaModel):
    def __init__(self, available_bytes=None, cache=None, rss=None, usage_bytes=None, working_set=None):
        # The size of the available memory. Unit: bytes.
        self.available_bytes = available_bytes  # type: long
        # The size of the cache. Unit: bytes.
        self.cache = cache  # type: long
        # The size of the resident memory set, which indicates the size of the physical memory that is actually used. Unit: bytes.
        self.rss = rss  # type: long
        # The size of the used memory. Unit: bytes.
        self.usage_bytes = usage_bytes  # type: long
        # The usage of the working set. Unit: bytes.
        self.working_set = working_set  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers(TeaModel):
    def __init__(self, cpu=None, memory=None, name=None):
        # The vCPU monitoring data of the container.
        self.cpu = cpu  # type: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU
        # The memory monitoring data of the container.
        self.memory = memory  # type: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory
        # The name.
        self.name = name  # type: str

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        if m.get('Memory') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainersMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsDisk(TeaModel):
    def __init__(self, device=None, read_bytes=None, read_io=None, write_bytes=None, write_io=None):
        # The name of the disk.
        self.device = device  # type: str
        # The amount of data that was read from the disk. Unit: bytes.
        self.read_bytes = read_bytes  # type: long
        # This parameter is unavailable for public use.
        self.read_io = read_io  # type: long
        # The amount of data that was written to the disk. Unit: bytes.
        self.write_bytes = write_bytes  # type: long
        # This parameter is unavailable for public use.
        self.write_io = write_io  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device
        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes
        if self.read_io is not None:
            result['ReadIo'] = self.read_io
        if self.write_bytes is not None:
            result['WriteBytes'] = self.write_bytes
        if self.write_io is not None:
            result['WriteIo'] = self.write_io
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')
        if m.get('ReadIo') is not None:
            self.read_io = m.get('ReadIo')
        if m.get('WriteBytes') is not None:
            self.write_bytes = m.get('WriteBytes')
        if m.get('WriteIo') is not None:
            self.write_io = m.get('WriteIo')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsFilesystem(TeaModel):
    def __init__(self, available=None, capacity=None, fs_name=None, usage=None):
        # The size of the available space.
        self.available = available  # type: long
        # The total file system space.
        self.capacity = capacity  # type: long
        # The name of the partition.
        self.fs_name = fs_name  # type: str
        # The size of used space.
        self.usage = usage  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsFilesystem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory(TeaModel):
    def __init__(self, available_bytes=None, cache=None, rss=None, usage_bytes=None, working_set=None):
        # The size of the available memory. Unit: bytes.
        self.available_bytes = available_bytes  # type: long
        # The size of the cache. Unit: bytes.
        self.cache = cache  # type: long
        # The size of the resident memory set, which indicates the size of the physical memory that is actually used. Unit: bytes.
        self.rss = rss  # type: long
        # The size of the used memory. Unit: bytes.
        self.usage_bytes = usage_bytes  # type: long
        # The usage of the working set. Unit: bytes.
        self.working_set = working_set  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_bytes is not None:
            result['AvailableBytes'] = self.available_bytes
        if self.cache is not None:
            result['Cache'] = self.cache
        if self.rss is not None:
            result['Rss'] = self.rss
        if self.usage_bytes is not None:
            result['UsageBytes'] = self.usage_bytes
        if self.working_set is not None:
            result['WorkingSet'] = self.working_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableBytes') is not None:
            self.available_bytes = m.get('AvailableBytes')
        if m.get('Cache') is not None:
            self.cache = m.get('Cache')
        if m.get('Rss') is not None:
            self.rss = m.get('Rss')
        if m.get('UsageBytes') is not None:
            self.usage_bytes = m.get('UsageBytes')
        if m.get('WorkingSet') is not None:
            self.working_set = m.get('WorkingSet')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces(TeaModel):
    def __init__(self, name=None, rx_bytes=None, rx_drops=None, rx_errors=None, rx_packets=None, tx_bytes=None,
                 tx_drops=None, tx_errors=None, tx_packets=None):
        # The name of the NIC.
        self.name = name  # type: str
        # The total number of bytes received.
        self.rx_bytes = rx_bytes  # type: long
        # The number of packets that fail to be received.
        self.rx_drops = rx_drops  # type: long
        # The number of receipt errors.
        self.rx_errors = rx_errors  # type: long
        # The total number of packets received.
        self.rx_packets = rx_packets  # type: long
        # The total number of bytes sent.
        self.tx_bytes = tx_bytes  # type: long
        # The number of packets that fail to arrive at their destination.
        self.tx_drops = tx_drops  # type: long
        # The total number of sending errors.
        self.tx_errors = tx_errors  # type: long
        # The total number of packets sent.
        self.tx_packets = tx_packets  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rx_bytes is not None:
            result['RxBytes'] = self.rx_bytes
        if self.rx_drops is not None:
            result['RxDrops'] = self.rx_drops
        if self.rx_errors is not None:
            result['RxErrors'] = self.rx_errors
        if self.rx_packets is not None:
            result['RxPackets'] = self.rx_packets
        if self.tx_bytes is not None:
            result['TxBytes'] = self.tx_bytes
        if self.tx_drops is not None:
            result['TxDrops'] = self.tx_drops
        if self.tx_errors is not None:
            result['TxErrors'] = self.tx_errors
        if self.tx_packets is not None:
            result['TxPackets'] = self.tx_packets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RxBytes') is not None:
            self.rx_bytes = m.get('RxBytes')
        if m.get('RxDrops') is not None:
            self.rx_drops = m.get('RxDrops')
        if m.get('RxErrors') is not None:
            self.rx_errors = m.get('RxErrors')
        if m.get('RxPackets') is not None:
            self.rx_packets = m.get('RxPackets')
        if m.get('TxBytes') is not None:
            self.tx_bytes = m.get('TxBytes')
        if m.get('TxDrops') is not None:
            self.tx_drops = m.get('TxDrops')
        if m.get('TxErrors') is not None:
            self.tx_errors = m.get('TxErrors')
        if m.get('TxPackets') is not None:
            self.tx_packets = m.get('TxPackets')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork(TeaModel):
    def __init__(self, interfaces=None):
        # The monitoring data of network interface controllers (NICs).
        self.interfaces = interfaces  # type: list[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces]

    def validate(self):
        if self.interfaces:
            for k in self.interfaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Interfaces'] = []
        if self.interfaces is not None:
            for k in self.interfaces:
                result['Interfaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.interfaces = []
        if m.get('Interfaces') is not None:
            for k in m.get('Interfaces'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetworkInterfaces()
                self.interfaces.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords(TeaModel):
    def __init__(self, cpu=None, containers=None, disk=None, filesystem=None, memory=None, network=None,
                 timestamp=None):
        # The monitoring data of vCPUs.
        self.cpu = cpu  # type: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU
        # The monitoring data of containers.
        self.containers = containers  # type: list[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers]
        # The monitoring data of disks.
        self.disk = disk  # type: list[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsDisk]
        # The monitoring data of file system partitions.
        self.filesystem = filesystem  # type: list[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsFilesystem]
        # The monitoring data of the memory.
        self.memory = memory  # type: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory
        # The monitoring data of the network.
        self.network = network  # type: DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork
        # The time when the entry of monitoring data was collected. The time follows the RFC 3339 format.
        self.timestamp = timestamp  # type: str

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()
        if self.filesystem:
            for k in self.filesystem:
                if k:
                    k.validate()
        if self.memory:
            self.memory.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu.to_map()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        result['Filesystem'] = []
        if self.filesystem is not None:
            for k in self.filesystem:
                result['Filesystem'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsCPU()
            self.cpu = temp_model.from_map(m['CPU'])
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsContainers()
                self.containers.append(temp_model.from_map(k))
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsDisk()
                self.disk.append(temp_model.from_map(k))
        self.filesystem = []
        if m.get('Filesystem') is not None:
            for k in m.get('Filesystem'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsFilesystem()
                self.filesystem.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('Network') is not None:
            temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecordsNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMultiContainerGroupMetricResponseBodyMonitorDatas(TeaModel):
    def __init__(self, container_group_id=None, records=None):
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id  # type: str
        # The details about monitoring data.
        self.records = records  # type: list[DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords]

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBodyMonitorDatas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatasRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeMultiContainerGroupMetricResponseBody(TeaModel):
    def __init__(self, monitor_datas=None, request_id=None):
        # The monitoring data of the elastic container instances.
        self.monitor_datas = monitor_datas  # type: list[DescribeMultiContainerGroupMetricResponseBodyMonitorDatas]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.monitor_datas:
            for k in self.monitor_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorDatas'] = []
        if self.monitor_datas is not None:
            for k in self.monitor_datas:
                result['MonitorDatas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.monitor_datas = []
        if m.get('MonitorDatas') is not None:
            for k in m.get('MonitorDatas'):
                temp_model = DescribeMultiContainerGroupMetricResponseBodyMonitorDatas()
                self.monitor_datas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMultiContainerGroupMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMultiContainerGroupMetricResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMultiContainerGroupMetricResponse, self).to_map()
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
            temp_model = DescribeMultiContainerGroupMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, recommend_zones=None, region_endpoint=None, region_id=None, zones=None):
        # The recommended zones. Recommended zones are zones that have relatively sufficient resources in the current region.
        self.recommend_zones = recommend_zones  # type: list[str]
        # The endpoint for the region.
        self.region_endpoint = region_endpoint  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The queried zones.
        self.zones = zones  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend_zones is not None:
            result['RecommendZones'] = self.recommend_zones
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecommendZones') is not None:
            self.recommend_zones = m.get('RecommendZones')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # The queried regions.
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
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
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualNodesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        self.key = key  # type: str
        # The value of tag N.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVirtualNodesRequestTag, self).to_map()
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


class DescribeVirtualNodesRequest(TeaModel):
    def __init__(self, client_token=None, limit=None, next_token=None, owner_account=None, owner_id=None,
                 region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None, status=None,
                 tag=None, virtual_node_ids=None, virtual_node_name=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency of requests?](~~25693~~)
        self.client_token = client_token  # type: str
        # The maximum number of resources that are allowed to return for this request. Default value: 20. Maximum value: 20.
        # 
        # >  The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: long
        # The token that determines the start point of the next query. If this parameter is empty, all results have been returned.
        # 
        # You do not need to specify this parameter in the first request. From the second request, you can obtain the token from the result returned by the previous request.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the virtual nodes.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The status of the virtual node. Valid values:
        # 
        # *   Pending
        # *   Ready
        # *   Failed
        self.status = status  # type: str
        # The tags that are bound to the virtual node.
        self.tag = tag  # type: list[DescribeVirtualNodesRequestTag]
        # The IDs of the virtual nodes. You can specify up to 20 IDs. Each ID must be a string in the JSON format.
        self.virtual_node_ids = virtual_node_ids  # type: str
        # The names of the virtual nodes.
        self.virtual_node_name = virtual_node_name  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVirtualNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.virtual_node_ids is not None:
            result['VirtualNodeIds'] = self.virtual_node_ids
        if self.virtual_node_name is not None:
            result['VirtualNodeName'] = self.virtual_node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVirtualNodesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VirtualNodeIds') is not None:
            self.virtual_node_ids = m.get('VirtualNodeIds')
        if m.get('VirtualNodeName') is not None:
            self.virtual_node_name = m.get('VirtualNodeName')
        return self


class DescribeVirtualNodesResponseBodyVirtualNodesEvents(TeaModel):
    def __init__(self, count=None, first_timestamp=None, last_timestamp=None, message=None, name=None, reason=None,
                 type=None):
        # The number of events.
        self.count = count  # type: int
        # The time when the event started.
        self.first_timestamp = first_timestamp  # type: str
        # The time when the event ended.
        self.last_timestamp = last_timestamp  # type: str
        # The message of the event.
        self.message = message  # type: str
        # The name of the object to which the event belongs.
        self.name = name  # type: str
        # The name of the event.
        self.reason = reason  # type: str
        # The type of the event. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVirtualNodesResponseBodyVirtualNodesEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeVirtualNodesResponseBodyVirtualNodesTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVirtualNodesResponseBodyVirtualNodesTags, self).to_map()
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


class DescribeVirtualNodesResponseBodyVirtualNodes(TeaModel):
    def __init__(self, creation_time=None, events=None, internet_ip=None, intranet_ip=None, region_id=None,
                 resource_group_id=None, status=None, tags=None, virtual_node_id=None, virtual_node_name=None,
                 virtual_node_security_group_id=None, virtual_node_vswitch_id=None, vpc_id=None):
        # The time when the virtual node was created. The time follows the RFC 3339 standard and is displayed in UTC.
        self.creation_time = creation_time  # type: str
        # The events about the virtual node.
        self.events = events  # type: list[DescribeVirtualNodesResponseBodyVirtualNodesEvents]
        # The public IP address of the virtual node.
        self.internet_ip = internet_ip  # type: str
        # The private IP address of the virtual node.
        self.intranet_ip = intranet_ip  # type: str
        # The ID of the region in which the virtual node resides.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the virtual node belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the virtual node. Valid values:
        # 
        # *   Pending
        # *   Ready
        # *   Failed
        self.status = status  # type: str
        # The tags that are bound to the virtual node.
        self.tags = tags  # type: list[DescribeVirtualNodesResponseBodyVirtualNodesTags]
        # The ID of the virtual node.
        self.virtual_node_id = virtual_node_id  # type: str
        # The name of the virtual node.
        self.virtual_node_name = virtual_node_name  # type: str
        # The ID of the security group to which the virtual node belongs.
        self.virtual_node_security_group_id = virtual_node_security_group_id  # type: str
        # The ID of the vSwitch with which the virtual node is associated.
        self.virtual_node_vswitch_id = virtual_node_vswitch_id  # type: str
        # The ID of the VPC to which the virtual node belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVirtualNodesResponseBodyVirtualNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.virtual_node_id is not None:
            result['VirtualNodeId'] = self.virtual_node_id
        if self.virtual_node_name is not None:
            result['VirtualNodeName'] = self.virtual_node_name
        if self.virtual_node_security_group_id is not None:
            result['VirtualNodeSecurityGroupId'] = self.virtual_node_security_group_id
        if self.virtual_node_vswitch_id is not None:
            result['VirtualNodeVSwitchId'] = self.virtual_node_vswitch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeVirtualNodesResponseBodyVirtualNodesEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeVirtualNodesResponseBodyVirtualNodesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VirtualNodeId') is not None:
            self.virtual_node_id = m.get('VirtualNodeId')
        if m.get('VirtualNodeName') is not None:
            self.virtual_node_name = m.get('VirtualNodeName')
        if m.get('VirtualNodeSecurityGroupId') is not None:
            self.virtual_node_security_group_id = m.get('VirtualNodeSecurityGroupId')
        if m.get('VirtualNodeVSwitchId') is not None:
            self.virtual_node_vswitch_id = m.get('VirtualNodeVSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVirtualNodesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, total_count=None, virtual_nodes=None):
        # The token that determines the start point of the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of virtual nodes that were queried.
        self.total_count = total_count  # type: int
        # The virtual nodes that were queried.
        self.virtual_nodes = virtual_nodes  # type: list[DescribeVirtualNodesResponseBodyVirtualNodes]

    def validate(self):
        if self.virtual_nodes:
            for k in self.virtual_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVirtualNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VirtualNodes'] = []
        if self.virtual_nodes is not None:
            for k in self.virtual_nodes:
                result['VirtualNodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.virtual_nodes = []
        if m.get('VirtualNodes') is not None:
            for k in m.get('VirtualNodes'):
                temp_model = DescribeVirtualNodesResponseBodyVirtualNodes()
                self.virtual_nodes.append(temp_model.from_map(k))
        return self


class DescribeVirtualNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVirtualNodesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVirtualNodesResponse, self).to_map()
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
            temp_model = DescribeVirtualNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecContainerCommandRequest(TeaModel):
    def __init__(self, command=None, container_group_id=None, container_name=None, owner_account=None,
                 owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None, stdin=None, sync=None,
                 tty=None):
        # The commands to run in the container. You can specify up to 20 commands. Each command can be up to 256 characters in length.\
        # The strings must be in the JSON format. Example: `["/bin/sh", "-c", "ls -a"]`.
        self.command = command  # type: str
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id  # type: str
        # The name of the container.
        self.container_name = container_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # Specifies whether to read the commands from standard input (stdin). Default value: true.
        self.stdin = stdin  # type: bool
        # Specifies whether to run the command immediately and return the result. Default value: false.\
        # If you set this parameter to true, set the value of TTY to false.
        self.sync = sync  # type: bool
        # Specifies whether to enable interaction. Default value: false.\
        # If the command is a /bin/bash command, set the value to true.
        self.tty = tty  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecContainerCommandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.sync is not None:
            result['Sync'] = self.sync
        if self.tty is not None:
            result['TTY'] = self.tty
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
        if m.get('TTY') is not None:
            self.tty = m.get('TTY')
        return self


class ExecContainerCommandResponseBody(TeaModel):
    def __init__(self, http_url=None, request_id=None, sync_response=None, web_socket_uri=None):
        # The HTTP URL. You can use this URL to enter the container within 30 seconds after this operation is called. For more information, see [Use and integrate the Elastic Container Instance terminal](~~202846~~).
        self.http_url = http_url  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The output of the command. This parameter is returned only if Sync is set to true.
        self.sync_response = sync_response  # type: str
        # The WebSocket URL. You can use this URL to establish a WebSocket connection with the container.
        self.web_socket_uri = web_socket_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecContainerCommandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_url is not None:
            result['HttpUrl'] = self.http_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_response is not None:
            result['SyncResponse'] = self.sync_response
        if self.web_socket_uri is not None:
            result['WebSocketUri'] = self.web_socket_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncResponse') is not None:
            self.sync_response = m.get('SyncResponse')
        if m.get('WebSocketUri') is not None:
            self.web_socket_uri = m.get('WebSocketUri')
        return self


class ExecContainerCommandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecContainerCommandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecContainerCommandResponse, self).to_map()
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
            temp_model = ExecContainerCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsageRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListUsageResponseBody(TeaModel):
    def __init__(self, attributes=None, request_id=None):
        # The information about the used amounts and upper limits of privileges and quotas that you have in the specified region. The information contains the following items:
        # 
        # *   UsedCpu: the number of existing vCPUs.
        # *   MaxCpu: the upper limit of vCPUs.
        # *   MaxImageCacheCount: the upper limit of manually created image caches.
        # *   UsedImageCacheCount: the number of existing image caches that are manually created.
        # *   MaxAutoImageCacheCount: the upper limit of automatically created image caches.
        # *   UsedAutoImageCacheCount: the number of existing image caches that are automatically created.
        # *   MaxDataCacheCount: the upper limit of DataCaches.
        # *   UsedDataCacheCount: the number of existing DataCaches.
        self.attributes = attributes  # type: dict[str, any]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsageResponse, self).to_map()
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
            temp_model = ListUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeContainerGroupVolumeRequest(TeaModel):
    def __init__(self, client_token=None, container_group_id=None, new_size=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, volume_name=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id  # type: str
        # The size of the volume after the volume is scaled up. Unit: GiB. Valid values:
        # 
        # *   Ultra disk (cloud_efficiency): 20 to 32768
        # *   Standard SSD (cloud_ssd): 20 to 32768
        # *   Enhanced SSD (cloud_essd): 20 to 32768
        # *   Basic disk (cloud): 5 to 2000
        # 
        # >  The capacity of the volume after the volume is scaled up must be greater than the original capacity of the volume. If the new capacity is equal to the original capacity of the volume, only the file system is scaled up.
        self.new_size = new_size  # type: long
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The name of the volume that you want to scale up. The volume must be an Alibaba Cloud disk.
        self.volume_name = volume_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeContainerGroupVolumeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.new_size is not None:
            result['NewSize'] = self.new_size
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.volume_name is not None:
            result['VolumeName'] = self.volume_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('NewSize') is not None:
            self.new_size = m.get('NewSize')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VolumeName') is not None:
            self.volume_name = m.get('VolumeName')
        return self


class ResizeContainerGroupVolumeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeContainerGroupVolumeResponseBody, self).to_map()
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


class ResizeContainerGroupVolumeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResizeContainerGroupVolumeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeContainerGroupVolumeResponse, self).to_map()
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
            temp_model = ResizeContainerGroupVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartContainerGroupRequest(TeaModel):
    def __init__(self, client_token=None, container_group_id=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request?](~~25693~~)
        self.client_token = client_token  # type: str
        # The instance ID.
        self.container_group_id = container_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartContainerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RestartContainerGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartContainerGroupResponseBody, self).to_map()
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


class RestartContainerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartContainerGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartContainerGroupResponse, self).to_map()
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
            temp_model = RestartContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateContainerGroupRequestDnsConfigOption(TeaModel):
    def __init__(self, name=None, value=None):
        # The option name of DNS configurations.
        self.name = name  # type: str
        # The option value of DNS configurations.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestDnsConfigOption, self).to_map()
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


class UpdateContainerGroupRequestDnsConfig(TeaModel):
    def __init__(self, name_server=None, option=None, search=None):
        # The IP addresses of DNS servers.
        self.name_server = name_server  # type: list[str]
        # The configurations of DNS.
        self.option = option  # type: list[UpdateContainerGroupRequestDnsConfigOption]
        # The search domains of the Domain Name System (DNS) server.
        self.search = search  # type: list[str]

    def validate(self):
        if self.option:
            for k in self.option:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestDnsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_server is not None:
            result['NameServer'] = self.name_server
        result['Option'] = []
        if self.option is not None:
            for k in self.option:
                result['Option'].append(k.to_map() if k else None)
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NameServer') is not None:
            self.name_server = m.get('NameServer')
        self.option = []
        if m.get('Option') is not None:
            for k in m.get('Option'):
                temp_model = UpdateContainerGroupRequestDnsConfigOption()
                self.option.append(temp_model.from_map(k))
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class UpdateContainerGroupRequestAcrRegistryInfo(TeaModel):
    def __init__(self, domain=None, instance_id=None, instance_name=None, region_id=None):
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. You can specify specific domain names. Separate multiple domain names with commas (,).
        self.domain = domain  # type: list[str]
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id  # type: str
        # The name of the Container Registry Enterprise Edition instance.
        self.instance_name = instance_name  # type: str
        # The ID of the region where the Container Registry Enterprise Edition instance resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestAcrRegistryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeExec(TeaModel):
    def __init__(self, command=None):
        self.command = command  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerLivenessProbeExec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeHttpGet(TeaModel):
    def __init__(self, path=None, port=None, scheme=None):
        self.path = path  # type: str
        self.port = port  # type: int
        self.scheme = scheme  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerLivenessProbeHttpGet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class UpdateContainerGroupRequestContainerLivenessProbeTcpSocket(TeaModel):
    def __init__(self, port=None):
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerLivenessProbeTcpSocket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestContainerLivenessProbe(TeaModel):
    def __init__(self, exec_=None, failure_threshold=None, http_get=None, initial_delay_seconds=None,
                 period_seconds=None, success_threshold=None, tcp_socket=None, timeout_seconds=None):
        self.exec_ = exec_  # type: UpdateContainerGroupRequestContainerLivenessProbeExec
        self.failure_threshold = failure_threshold  # type: int
        self.http_get = http_get  # type: UpdateContainerGroupRequestContainerLivenessProbeHttpGet
        self.initial_delay_seconds = initial_delay_seconds  # type: int
        self.period_seconds = period_seconds  # type: int
        self.success_threshold = success_threshold  # type: int
        self.tcp_socket = tcp_socket  # type: UpdateContainerGroupRequestContainerLivenessProbeTcpSocket
        self.timeout_seconds = timeout_seconds  # type: int

    def validate(self):
        if self.exec_:
            self.exec_.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerLivenessProbe, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_ is not None:
            result['Exec'] = self.exec_.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeExec()
            self.exec_ = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeExec(TeaModel):
    def __init__(self, command=None):
        self.command = command  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerReadinessProbeExec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeHttpGet(TeaModel):
    def __init__(self, path=None, port=None, scheme=None):
        self.path = path  # type: str
        self.port = port  # type: int
        self.scheme = scheme  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerReadinessProbeHttpGet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class UpdateContainerGroupRequestContainerReadinessProbeTcpSocket(TeaModel):
    def __init__(self, port=None):
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerReadinessProbeTcpSocket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class UpdateContainerGroupRequestContainerReadinessProbe(TeaModel):
    def __init__(self, exec_=None, failure_threshold=None, http_get=None, initial_delay_seconds=None,
                 period_seconds=None, success_threshold=None, tcp_socket=None, timeout_seconds=None):
        self.exec_ = exec_  # type: UpdateContainerGroupRequestContainerReadinessProbeExec
        self.failure_threshold = failure_threshold  # type: int
        self.http_get = http_get  # type: UpdateContainerGroupRequestContainerReadinessProbeHttpGet
        self.initial_delay_seconds = initial_delay_seconds  # type: int
        self.period_seconds = period_seconds  # type: int
        self.success_threshold = success_threshold  # type: int
        self.tcp_socket = tcp_socket  # type: UpdateContainerGroupRequestContainerReadinessProbeTcpSocket
        self.timeout_seconds = timeout_seconds  # type: int

    def validate(self):
        if self.exec_:
            self.exec_.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerReadinessProbe, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_ is not None:
            result['Exec'] = self.exec_.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeExec()
            self.exec_ = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class UpdateContainerGroupRequestContainerSecurityContextCapability(TeaModel):
    def __init__(self, add=None):
        self.add = add  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerSecurityContextCapability, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class UpdateContainerGroupRequestContainerSecurityContext(TeaModel):
    def __init__(self, capability=None, read_only_root_filesystem=None, run_as_user=None):
        self.capability = capability  # type: UpdateContainerGroupRequestContainerSecurityContextCapability
        self.read_only_root_filesystem = read_only_root_filesystem  # type: bool
        self.run_as_user = run_as_user  # type: long

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = UpdateContainerGroupRequestContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class UpdateContainerGroupRequestContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(self, field_path=None):
        self.field_path = field_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerEnvironmentVarFieldRef, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class UpdateContainerGroupRequestContainerEnvironmentVar(TeaModel):
    def __init__(self, field_ref=None, key=None, value=None):
        self.field_ref = field_ref  # type: UpdateContainerGroupRequestContainerEnvironmentVarFieldRef
        # The name of the environment variable for the container.
        self.key = key  # type: str
        # The value of the environment variable for the container.
        self.value = value  # type: str

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerEnvironmentVar, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = UpdateContainerGroupRequestContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders(TeaModel):
    def __init__(self, name=None, value=None):
        # The request parameter of the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.name = name  # type: str
        # The request parameter value of the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders, self).to_map()
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


class UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader(TeaModel):
    def __init__(self, name=None, value=None):
        # The request parameter of the HTTP GET request when you use an HTTP request to specify the preStop callback function.
        self.name = name  # type: str
        # The request parameter value of the HTTP GET request when you use an HTTP request to specify the preStop callback function.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader, self).to_map()
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


class UpdateContainerGroupRequestContainerPort(TeaModel):
    def __init__(self, port=None, protocol=None):
        # The port number. Valid values: 1 to 65535.
        self.port = port  # type: int
        # The protocol of the container. Valid values: TCP and UDP.
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerPort, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class UpdateContainerGroupRequestContainerVolumeMount(TeaModel):
    def __init__(self, mount_path=None, mount_propagation=None, name=None, read_only=None, sub_path=None):
        # The directory of the volume that is mounted to the container. The data in this directory is overwritten by the data on the volume. Specify this parameter with caution.
        self.mount_path = mount_path  # type: str
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: This volume mount does not receive subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   HostToCotainer: The volume mount receives subsequent mounts that are performed on this volume or the subdirectories of this volume.
        # *   Bidirectional: The volume mount behaves the same as the HostToContainer mount. The volume mount receives subsequent mounts that are performed on the volume or the subdirectories of the volume. In addition, all volume mounts that are mounted on the container are propagated back to the host and all containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation  # type: str
        # The name of the volume that is mounted to the container. Valid values: the values of Volume.N.Name, which are the names of volumes that are mounted to the elastic container instance.
        self.name = name  # type: str
        # Specifies whether the volume is read-only. Default value: false.
        self.read_only = read_only  # type: bool
        # The subdirectory of the volume that is mounted to the container. You can use this parameter to mount the same volume to different subdirectories of the container.
        self.sub_path = sub_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainerVolumeMount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class UpdateContainerGroupRequestContainer(TeaModel):
    def __init__(self, liveness_probe=None, readiness_probe=None, security_context=None, arg=None, command=None,
                 cpu=None, environment_var=None, gpu=None, image=None, image_pull_policy=None,
                 lifecycle_post_start_handler_exec=None, lifecycle_post_start_handler_http_get_host=None,
                 lifecycle_post_start_handler_http_get_http_headers=None, lifecycle_post_start_handler_http_get_path=None,
                 lifecycle_post_start_handler_http_get_port=None, lifecycle_post_start_handler_http_get_scheme=None,
                 lifecycle_post_start_handler_tcp_socket_host=None, lifecycle_post_start_handler_tcp_socket_port=None, lifecycle_pre_stop_handler_exec=None,
                 lifecycle_pre_stop_handler_http_get_host=None, lifecycle_pre_stop_handler_http_get_http_header=None,
                 lifecycle_pre_stop_handler_http_get_path=None, lifecycle_pre_stop_handler_http_get_port=None,
                 lifecycle_pre_stop_handler_http_get_scheme=None, lifecycle_pre_stop_handler_tcp_socket_host=None,
                 lifecycle_pre_stop_handler_tcp_socket_port=None, memory=None, name=None, port=None, stdin=None, stdin_once=None, tty=None, volume_mount=None,
                 working_dir=None):
        self.liveness_probe = liveness_probe  # type: UpdateContainerGroupRequestContainerLivenessProbe
        self.readiness_probe = readiness_probe  # type: UpdateContainerGroupRequestContainerReadinessProbe
        self.security_context = security_context  # type: UpdateContainerGroupRequestContainerSecurityContext
        # The arguments that you want to pass to the startup command of the container. You can specify up to 10 arguments.
        self.arg = arg  # type: list[str]
        # The commands that you want to run to perform the health check.
        self.command = command  # type: list[str]
        # The number of vCPUs that you want to allocate to the container
        self.cpu = cpu  # type: float
        # The environment variables for the container.
        self.environment_var = environment_var  # type: list[UpdateContainerGroupRequestContainerEnvironmentVar]
        # The number of GPUs that you want to allocate to the container.
        self.gpu = gpu  # type: int
        # The image of the container.
        self.image = image  # type: str
        # The image pulling policy. Valid values:
        # 
        # *   Always: Each time the instance is updated, image pulling is performed.
        # *   IfNotPresent: On-premises images are used first. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy  # type: str
        # The commands to be executed in the container when you use the CLI to specify the postStart callback function.
        self.lifecycle_post_start_handler_exec = lifecycle_post_start_handler_exec  # type: list[str]
        # The IP address of the host that receives the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host  # type: str
        # The information about the valid HTTP request headers among the generated HTTP request headers.
        self.lifecycle_post_start_handler_http_get_http_headers = lifecycle_post_start_handler_http_get_http_headers  # type: list[UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders]
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path  # type: str
        # The port to which the system sends the HTTP GET request when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port  # type: int
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify the postStart callback function.
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme  # type: str
        # The IP address of the host that receives the TCP socket request when you use a TCP socket request to specify the postStart callback function.
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host  # type: str
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify the postStart callback function.
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port  # type: int
        # The commands to be executed in the container when you use the CLI to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_exec = lifecycle_pre_stop_handler_exec  # type: list[str]
        # The IP address of the host that receives the HTTP GET request when you use an HTTP request to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host  # type: str
        # The information about the generated HTTP request header.
        self.lifecycle_pre_stop_handler_http_get_http_header = lifecycle_pre_stop_handler_http_get_http_header  # type: list[UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader]
        # The path to which the system sends an HTTP GET request for a health check when you use an HTTP request to specify the preSop callback function.
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path  # type: str
        # The port to which the system sends the HTTP GET request for a health check when you use an HTTP request to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port  # type: int
        # The protocol type of the HTTP GET request when you use an HTTP request to specify the preStop callback function. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme  # type: str
        # The IP address of the host that receives the TCP socket request when you use a TCP socket request to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host  # type: str
        # The port to which the system sends a TCP socket request for a health check when you use TCP sockets to specify the preStop callback function.
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port  # type: int
        # The memory size of the container.
        self.memory = memory  # type: float
        # The name of the container.
        self.name = name  # type: str
        # The port to which the system sends an HTTP GET request for a health check.
        self.port = port  # type: list[UpdateContainerGroupRequestContainerPort]
        # Specifies whether the container allocates buffer resources to standard input streams when the container is running. If you do not specify this parameter, an end-of-file (EOF) error may occur when standard input streams in the container are read. Default value: false.
        self.stdin = stdin  # type: bool
        # Specifies whether standard input streams are disconnected after a client is disconnected. If Stdin is set to true, standard input streams remain connected among multiple sessions. If StdinOnce is set to true, standard input streams are connected after the container is started, and remain idle until a client is connected to receive data. After the client is disconnected, streams are also disconnected, and remain disconnected until the container restarts.
        self.stdin_once = stdin_once  # type: bool
        # Specifies whether to enable interaction. Default value: false. If the command is a /bin/bash command, set the value to true.
        self.tty = tty  # type: bool
        # Pod volumes that you want to mount into the filesystem of the container.
        self.volume_mount = volume_mount  # type: list[UpdateContainerGroupRequestContainerVolumeMount]
        # The working directory of the container.
        self.working_dir = working_dir  # type: str

    def validate(self):
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.readiness_probe:
            self.readiness_probe.validate()
        if self.security_context:
            self.security_context.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.lifecycle_post_start_handler_http_get_http_headers:
            for k in self.lifecycle_post_start_handler_http_get_http_headers:
                if k:
                    k.validate()
        if self.lifecycle_pre_stop_handler_http_get_http_header:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestContainer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.lifecycle_post_start_handler_exec is not None:
            result['LifecyclePostStartHandlerExec'] = self.lifecycle_post_start_handler_exec
        if self.lifecycle_post_start_handler_http_get_host is not None:
            result['LifecyclePostStartHandlerHttpGetHost'] = self.lifecycle_post_start_handler_http_get_host
        result['LifecyclePostStartHandlerHttpGetHttpHeaders'] = []
        if self.lifecycle_post_start_handler_http_get_http_headers is not None:
            for k in self.lifecycle_post_start_handler_http_get_http_headers:
                result['LifecyclePostStartHandlerHttpGetHttpHeaders'].append(k.to_map() if k else None)
        if self.lifecycle_post_start_handler_http_get_path is not None:
            result['LifecyclePostStartHandlerHttpGetPath'] = self.lifecycle_post_start_handler_http_get_path
        if self.lifecycle_post_start_handler_http_get_port is not None:
            result['LifecyclePostStartHandlerHttpGetPort'] = self.lifecycle_post_start_handler_http_get_port
        if self.lifecycle_post_start_handler_http_get_scheme is not None:
            result['LifecyclePostStartHandlerHttpGetScheme'] = self.lifecycle_post_start_handler_http_get_scheme
        if self.lifecycle_post_start_handler_tcp_socket_host is not None:
            result['LifecyclePostStartHandlerTcpSocketHost'] = self.lifecycle_post_start_handler_tcp_socket_host
        if self.lifecycle_post_start_handler_tcp_socket_port is not None:
            result['LifecyclePostStartHandlerTcpSocketPort'] = self.lifecycle_post_start_handler_tcp_socket_port
        if self.lifecycle_pre_stop_handler_exec is not None:
            result['LifecyclePreStopHandlerExec'] = self.lifecycle_pre_stop_handler_exec
        if self.lifecycle_pre_stop_handler_http_get_host is not None:
            result['LifecyclePreStopHandlerHttpGetHost'] = self.lifecycle_pre_stop_handler_http_get_host
        result['LifecyclePreStopHandlerHttpGetHttpHeader'] = []
        if self.lifecycle_pre_stop_handler_http_get_http_header is not None:
            for k in self.lifecycle_pre_stop_handler_http_get_http_header:
                result['LifecyclePreStopHandlerHttpGetHttpHeader'].append(k.to_map() if k else None)
        if self.lifecycle_pre_stop_handler_http_get_path is not None:
            result['LifecyclePreStopHandlerHttpGetPath'] = self.lifecycle_pre_stop_handler_http_get_path
        if self.lifecycle_pre_stop_handler_http_get_port is not None:
            result['LifecyclePreStopHandlerHttpGetPort'] = self.lifecycle_pre_stop_handler_http_get_port
        if self.lifecycle_pre_stop_handler_http_get_scheme is not None:
            result['LifecyclePreStopHandlerHttpGetScheme'] = self.lifecycle_pre_stop_handler_http_get_scheme
        if self.lifecycle_pre_stop_handler_tcp_socket_host is not None:
            result['LifecyclePreStopHandlerTcpSocketHost'] = self.lifecycle_pre_stop_handler_tcp_socket_host
        if self.lifecycle_pre_stop_handler_tcp_socket_port is not None:
            result['LifecyclePreStopHandlerTcpSocketPort'] = self.lifecycle_pre_stop_handler_tcp_socket_port
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LivenessProbe') is not None:
            temp_model = UpdateContainerGroupRequestContainerLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('ReadinessProbe') is not None:
            temp_model = UpdateContainerGroupRequestContainerReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('SecurityContext') is not None:
            temp_model = UpdateContainerGroupRequestContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = UpdateContainerGroupRequestContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('LifecyclePostStartHandlerExec') is not None:
            self.lifecycle_post_start_handler_exec = m.get('LifecyclePostStartHandlerExec')
        if m.get('LifecyclePostStartHandlerHttpGetHost') is not None:
            self.lifecycle_post_start_handler_http_get_host = m.get('LifecyclePostStartHandlerHttpGetHost')
        self.lifecycle_post_start_handler_http_get_http_headers = []
        if m.get('LifecyclePostStartHandlerHttpGetHttpHeaders') is not None:
            for k in m.get('LifecyclePostStartHandlerHttpGetHttpHeaders'):
                temp_model = UpdateContainerGroupRequestContainerLifecyclePostStartHandlerHttpGetHttpHeaders()
                self.lifecycle_post_start_handler_http_get_http_headers.append(temp_model.from_map(k))
        if m.get('LifecyclePostStartHandlerHttpGetPath') is not None:
            self.lifecycle_post_start_handler_http_get_path = m.get('LifecyclePostStartHandlerHttpGetPath')
        if m.get('LifecyclePostStartHandlerHttpGetPort') is not None:
            self.lifecycle_post_start_handler_http_get_port = m.get('LifecyclePostStartHandlerHttpGetPort')
        if m.get('LifecyclePostStartHandlerHttpGetScheme') is not None:
            self.lifecycle_post_start_handler_http_get_scheme = m.get('LifecyclePostStartHandlerHttpGetScheme')
        if m.get('LifecyclePostStartHandlerTcpSocketHost') is not None:
            self.lifecycle_post_start_handler_tcp_socket_host = m.get('LifecyclePostStartHandlerTcpSocketHost')
        if m.get('LifecyclePostStartHandlerTcpSocketPort') is not None:
            self.lifecycle_post_start_handler_tcp_socket_port = m.get('LifecyclePostStartHandlerTcpSocketPort')
        if m.get('LifecyclePreStopHandlerExec') is not None:
            self.lifecycle_pre_stop_handler_exec = m.get('LifecyclePreStopHandlerExec')
        if m.get('LifecyclePreStopHandlerHttpGetHost') is not None:
            self.lifecycle_pre_stop_handler_http_get_host = m.get('LifecyclePreStopHandlerHttpGetHost')
        self.lifecycle_pre_stop_handler_http_get_http_header = []
        if m.get('LifecyclePreStopHandlerHttpGetHttpHeader') is not None:
            for k in m.get('LifecyclePreStopHandlerHttpGetHttpHeader'):
                temp_model = UpdateContainerGroupRequestContainerLifecyclePreStopHandlerHttpGetHttpHeader()
                self.lifecycle_pre_stop_handler_http_get_http_header.append(temp_model.from_map(k))
        if m.get('LifecyclePreStopHandlerHttpGetPath') is not None:
            self.lifecycle_pre_stop_handler_http_get_path = m.get('LifecyclePreStopHandlerHttpGetPath')
        if m.get('LifecyclePreStopHandlerHttpGetPort') is not None:
            self.lifecycle_pre_stop_handler_http_get_port = m.get('LifecyclePreStopHandlerHttpGetPort')
        if m.get('LifecyclePreStopHandlerHttpGetScheme') is not None:
            self.lifecycle_pre_stop_handler_http_get_scheme = m.get('LifecyclePreStopHandlerHttpGetScheme')
        if m.get('LifecyclePreStopHandlerTcpSocketHost') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_host = m.get('LifecyclePreStopHandlerTcpSocketHost')
        if m.get('LifecyclePreStopHandlerTcpSocketPort') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_port = m.get('LifecyclePreStopHandlerTcpSocketPort')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = UpdateContainerGroupRequestContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = UpdateContainerGroupRequestContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class UpdateContainerGroupRequestImageRegistryCredential(TeaModel):
    def __init__(self, password=None, server=None, user_name=None):
        # The password that you use to access the image repository.
        self.password = password  # type: str
        # The address of the image repository. This address does not contain `http://` or `https://`.
        self.server = server  # type: str
        # The username that you use to access the image repository.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestImageRegistryCredential, self).to_map()
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


class UpdateContainerGroupRequestInitContainerSecurityContextCapability(TeaModel):
    def __init__(self, add=None):
        self.add = add  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestInitContainerSecurityContextCapability, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class UpdateContainerGroupRequestInitContainerSecurityContext(TeaModel):
    def __init__(self, capability=None, read_only_root_filesystem=None, run_as_user=None):
        self.capability = capability  # type: UpdateContainerGroupRequestInitContainerSecurityContextCapability
        self.read_only_root_filesystem = read_only_root_filesystem  # type: bool
        self.run_as_user = run_as_user  # type: long

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestInitContainerSecurityContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef(TeaModel):
    def __init__(self, field_path=None):
        self.field_path = field_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class UpdateContainerGroupRequestInitContainerEnvironmentVar(TeaModel):
    def __init__(self, field_ref=None, key=None, value=None):
        self.field_ref = field_ref  # type: UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef
        # The name of the environment variable for the init container.
        self.key = key  # type: str
        # The value of the environment variable for the init container.
        self.value = value  # type: str

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestInitContainerEnvironmentVar, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerEnvironmentVarFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateContainerGroupRequestInitContainerPort(TeaModel):
    def __init__(self, port=None, protocol=None):
        # The port number of the init container. Valid values: 1 to 65535.
        self.port = port  # type: int
        # The protocol of the init container. Valid values: TCP and UDP.
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestInitContainerPort, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class UpdateContainerGroupRequestInitContainerVolumeMount(TeaModel):
    def __init__(self, mount_path=None, mount_propagation=None, name=None, read_only=None, sub_path=None):
        # The mount directory of the init container. The data in this directory is overwritten by the data on the volume. Specify this parameter with caution.
        self.mount_path = mount_path  # type: str
        # The mount propagation settings of the volume. Mount propagation allows volumes that are mounted on one container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # *   None: The volume mount does not receive subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   HostToContainer: The volume mount receives all subsequent mounts that are performed on this volume or subdirectories of this volume.
        # *   Bidirectional: The volume mount behaves the same as the HostToContainer mount. The volume mount receives subsequent mounts that are performed on the volume or the subdirectories of the volume. In addition, all volume mounts that are mounted on the container are propagated back to the host and all containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation  # type: str
        # The name of the volume that is mounted to the init container. Valid values: the values of Volume.N.Name, which are the names of volumes that are mounted to the elastic container instance.
        self.name = name  # type: str
        # Specifies whether the volume is read-only. Default value: false.
        self.read_only = read_only  # type: bool
        # The subdirectory of the volume that is mounted to the init container. You can use this parameter to mount the same volume to different subdirectories of the init container.
        self.sub_path = sub_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestInitContainerVolumeMount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class UpdateContainerGroupRequestInitContainer(TeaModel):
    def __init__(self, security_context=None, arg=None, command=None, cpu=None, environment_var=None, gpu=None,
                 image=None, image_pull_policy=None, memory=None, name=None, port=None, stdin=None, stdin_once=None,
                 tty=None, volume_mount=None, working_dir=None):
        self.security_context = security_context  # type: UpdateContainerGroupRequestInitContainerSecurityContext
        # The arguments that you want to pass to the startup command of the init container.
        self.arg = arg  # type: list[str]
        # The commands that are used to start the init container.
        self.command = command  # type: list[str]
        # The number of vCPUs that you want to allocate to the init container.
        self.cpu = cpu  # type: float
        # The environment variable of the init container.
        self.environment_var = environment_var  # type: list[UpdateContainerGroupRequestInitContainerEnvironmentVar]
        # The number of GPUs you want to allocate to the init container.
        self.gpu = gpu  # type: int
        # The image of the init container.
        self.image = image  # type: str
        # The image pulling policy. Valid values:
        # 
        # *   Always: Each time the instance is updated, image pulling is performed.
        # *   IfNotPresent: On-premises images are used first. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy  # type: str
        # The memory size of the init container.
        self.memory = memory  # type: float
        # The name of the init container.
        self.name = name  # type: str
        # The port number. Valid values: 1 to 65535.
        self.port = port  # type: list[UpdateContainerGroupRequestInitContainerPort]
        # Specifies whether the init container allocates buffer resources to standard input streams when the init container is running. If you do not specify this parameter, an EOF error may occur when standard input streams in the init container are read. Default value: false.
        self.stdin = stdin  # type: bool
        # Specifies whether standard input streams are disconnected after a client is disconnected. If Stdin is set to true, standard input streams remain connected among multiple sessions. If StdinOnce is set to true, standard input streams are connected after the init container is started, and remain idle until a client is connected to receive data. After the client is disconnected, streams are also disconnected, and remain disconnected until the init container restarts.
        self.stdin_once = stdin_once  # type: bool
        # Specifies whether to enable interaction. Default value: false. If the command is a /bin/bash command, set the value to true.
        self.tty = tty  # type: bool
        # The information about the volume that you want to mount on the init container.
        self.volume_mount = volume_mount  # type: list[UpdateContainerGroupRequestInitContainerVolumeMount]
        # The working directory of the init container.
        self.working_dir = working_dir  # type: str

    def validate(self):
        if self.security_context:
            self.security_context.validate()
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()
        if self.port:
            for k in self.port:
                if k:
                    k.validate()
        if self.volume_mount:
            for k in self.volume_mount:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestInitContainer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.command is not None:
            result['Command'] = self.command
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Port'] = []
        if self.port is not None:
            for k in self.port:
                result['Port'].append(k.to_map() if k else None)
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k in self.volume_mount:
                result['VolumeMount'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = UpdateContainerGroupRequestInitContainerSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = UpdateContainerGroupRequestInitContainerEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port = []
        if m.get('Port') is not None:
            for k in m.get('Port'):
                temp_model = UpdateContainerGroupRequestInitContainerPort()
                self.port.append(temp_model.from_map(k))
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k in m.get('VolumeMount'):
                temp_model = UpdateContainerGroupRequestInitContainerVolumeMount()
                self.volume_mount.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class UpdateContainerGroupRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestTag, self).to_map()
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


class UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath(TeaModel):
    def __init__(self, content=None, path=None):
        self.content = content  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class UpdateContainerGroupRequestVolumeConfigFileVolume(TeaModel):
    def __init__(self, config_file_to_path=None):
        self.config_file_to_path = config_file_to_path  # type: list[UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath]

    def validate(self):
        if self.config_file_to_path:
            for k in self.config_file_to_path:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestVolumeConfigFileVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigFileToPath'] = []
        if self.config_file_to_path is not None:
            for k in self.config_file_to_path:
                result['ConfigFileToPath'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_file_to_path = []
        if m.get('ConfigFileToPath') is not None:
            for k in m.get('ConfigFileToPath'):
                temp_model = UpdateContainerGroupRequestVolumeConfigFileVolumeConfigFileToPath()
                self.config_file_to_path.append(temp_model.from_map(k))
        return self


class UpdateContainerGroupRequestVolumeEmptyDirVolume(TeaModel):
    def __init__(self, medium=None, size_limit=None):
        self.medium = medium  # type: str
        self.size_limit = size_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestVolumeEmptyDirVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        return self


class UpdateContainerGroupRequestVolumeFlexVolume(TeaModel):
    def __init__(self, driver=None, fs_type=None, options=None):
        self.driver = driver  # type: str
        self.fs_type = fs_type  # type: str
        self.options = options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestVolumeFlexVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class UpdateContainerGroupRequestVolumeHostPathVolume(TeaModel):
    def __init__(self, path=None, type=None):
        self.path = path  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestVolumeHostPathVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateContainerGroupRequestVolumeNFSVolume(TeaModel):
    def __init__(self, path=None, read_only=None, server=None):
        self.path = path  # type: str
        self.read_only = read_only  # type: bool
        self.server = server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupRequestVolumeNFSVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class UpdateContainerGroupRequestVolume(TeaModel):
    def __init__(self, config_file_volume=None, empty_dir_volume=None, flex_volume=None, host_path_volume=None,
                 nfsvolume=None, name=None, type=None):
        self.config_file_volume = config_file_volume  # type: UpdateContainerGroupRequestVolumeConfigFileVolume
        self.empty_dir_volume = empty_dir_volume  # type: UpdateContainerGroupRequestVolumeEmptyDirVolume
        self.flex_volume = flex_volume  # type: UpdateContainerGroupRequestVolumeFlexVolume
        self.host_path_volume = host_path_volume  # type: UpdateContainerGroupRequestVolumeHostPathVolume
        self.nfsvolume = nfsvolume  # type: UpdateContainerGroupRequestVolumeNFSVolume
        # The volume name.
        self.name = name  # type: str
        # The type of the HostPath volume. Valid values:
        # 
        # *   Directory
        # *   File
        # 
        # >  This parameter is not publicly available.
        self.type = type  # type: str

    def validate(self):
        if self.config_file_volume:
            self.config_file_volume.validate()
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()
        if self.flex_volume:
            self.flex_volume.validate()
        if self.host_path_volume:
            self.host_path_volume.validate()
        if self.nfsvolume:
            self.nfsvolume.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequestVolume, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_volume is not None:
            result['ConfigFileVolume'] = self.config_file_volume.to_map()
        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()
        if self.flex_volume is not None:
            result['FlexVolume'] = self.flex_volume.to_map()
        if self.host_path_volume is not None:
            result['HostPathVolume'] = self.host_path_volume.to_map()
        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigFileVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeConfigFileVolume()
            self.config_file_volume = temp_model.from_map(m['ConfigFileVolume'])
        if m.get('EmptyDirVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m['EmptyDirVolume'])
        if m.get('FlexVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeFlexVolume()
            self.flex_volume = temp_model.from_map(m['FlexVolume'])
        if m.get('HostPathVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeHostPathVolume()
            self.host_path_volume = temp_model.from_map(m['HostPathVolume'])
        if m.get('NFSVolume') is not None:
            temp_model = UpdateContainerGroupRequestVolumeNFSVolume()
            self.nfsvolume = temp_model.from_map(m['NFSVolume'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateContainerGroupRequest(TeaModel):
    def __init__(self, dns_config=None, acr_registry_info=None, client_token=None, container=None,
                 container_group_id=None, cpu=None, image_registry_credential=None, init_container=None, memory=None,
                 owner_account=None, owner_id=None, region_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, restart_policy=None, tag=None, update_type=None, volume=None):
        self.dns_config = dns_config  # type: UpdateContainerGroupRequestDnsConfig
        # Details of the Container Registry Enterprise Edition instance that hosts the image of the init container.
        self.acr_registry_info = acr_registry_info  # type: list[UpdateContainerGroupRequestAcrRegistryInfo]
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency](~~25693~~).
        self.client_token = client_token  # type: str
        # The new configurations of the container group.
        self.container = container  # type: list[UpdateContainerGroupRequestContainer]
        # The ID of the elastic container instance that you want to update.
        self.container_group_id = container_group_id  # type: str
        # The number of vCPUs that are allocated to the elastic container instance.
        self.cpu = cpu  # type: float
        # The information about the credentials of the image repository.
        self.image_registry_credential = image_registry_credential  # type: list[UpdateContainerGroupRequestImageRegistryCredential]
        # The information about the new init container.
        self.init_container = init_container  # type: list[UpdateContainerGroupRequestInitContainer]
        # The size of the memory that is allocated to the elastic container instance. Unit: GiB.
        self.memory = memory  # type: float
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The restart policy of the elastic container instance. Valid values:
        # 
        # *   Always: Always restarts the instance if a container in the instance exits upon termination.
        # *   Never: Never restarts the instance if a container in the instance exits upon termination.
        # *   OnFailure: Restarts the instance only if a container in the instance exists upon failure with a status code of non-zero.
        self.restart_policy = restart_policy  # type: str
        # The tags that are bound to the instance.
        self.tag = tag  # type: list[UpdateContainerGroupRequestTag]
        # The update type. Valid values:
        # 
        # *   RenewUpdate: full updates. You must specify all relevant parameters to update the elastic container instance. For a parameter of the list type, you must specify all the items contained in the parameter even if you want to update only some of the items. For a parameter of the struct type, you must specify all the members even if you want to update only some of the members.
        # *   IncrementalUpdate: incremental updates. You may specify only the parameter that you want to update. Other related parameters remain unchanged.
        # 
        # Default value: RenewUpdate.
        self.update_type = update_type  # type: str
        # The volumes that are mounted to the instance.
        self.volume = volume  # type: list[UpdateContainerGroupRequestVolume]

    def validate(self):
        if self.dns_config:
            self.dns_config.validate()
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()
        if self.container:
            for k in self.container:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.init_container:
            for k in self.init_container:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.volume:
            for k in self.volume:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Container'] = []
        if self.container is not None:
            for k in self.container:
                result['Container'].append(k.to_map() if k else None)
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        result['InitContainer'] = []
        if self.init_container is not None:
            for k in self.init_container:
                result['InitContainer'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.update_type is not None:
            result['UpdateType'] = self.update_type
        result['Volume'] = []
        if self.volume is not None:
            for k in self.volume:
                result['Volume'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsConfig') is not None:
            temp_model = UpdateContainerGroupRequestDnsConfig()
            self.dns_config = temp_model.from_map(m['DnsConfig'])
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = UpdateContainerGroupRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.container = []
        if m.get('Container') is not None:
            for k in m.get('Container'):
                temp_model = UpdateContainerGroupRequestContainer()
                self.container.append(temp_model.from_map(k))
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = UpdateContainerGroupRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        self.init_container = []
        if m.get('InitContainer') is not None:
            for k in m.get('InitContainer'):
                temp_model = UpdateContainerGroupRequestInitContainer()
                self.init_container.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateContainerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')
        self.volume = []
        if m.get('Volume') is not None:
            for k in m.get('Volume'):
                temp_model = UpdateContainerGroupRequestVolume()
                self.volume.append(temp_model.from_map(k))
        return self


class UpdateContainerGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContainerGroupResponseBody, self).to_map()
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


class UpdateContainerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateContainerGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateContainerGroupResponse, self).to_map()
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
            temp_model = UpdateContainerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataCacheRequestDataSource(TeaModel):
    def __init__(self, options=None, type=None):
        # The parameters that are configured for the data source.
        self.options = options  # type: dict[str, str]
        # The type of the data source. Valid values:
        # 
        # *   URL
        # *   NAS
        # *   OSS
        # *   SNAPSHOT
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDataCacheRequestDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['Options'] = self.options
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateDataCacheRequestEipCreateParam(TeaModel):
    def __init__(self, bandwidth=None, common_bandwidth_package=None, isp=None, internet_charge_type=None,
                 public_ip_address_pool_id=None):
        # The bandwidth of the EIP. Unit: Mbit/s. Default value: 5.
        self.bandwidth = bandwidth  # type: int
        # The EIP bandwidth plan to be associated.
        self.common_bandwidth_package = common_bandwidth_package  # type: str
        # The line type of the EIP. Valid values:
        # 
        # *   BGP (default): BGP (Multi-ISP) line
        # *   BGP_PRO: BGP (Multi-ISP) Pro line
        self.isp = isp  # type: str
        # The metering method of the EIP. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth
        # *   PayByTraffic: pay-by-data-transfer
        self.internet_charge_type = internet_charge_type  # type: str
        # The ID of the IP address pool. The EIP is allocated from the IP address pool. You cannot use the IP address pool feature by default. To use this feature, you must apply for the privilege in the Quota Center console.
        self.public_ip_address_pool_id = public_ip_address_pool_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDataCacheRequestEipCreateParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.common_bandwidth_package is not None:
            result['CommonBandwidthPackage'] = self.common_bandwidth_package
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CommonBandwidthPackage') is not None:
            self.common_bandwidth_package = m.get('CommonBandwidthPackage')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')
        return self


class UpdateDataCacheRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDataCacheRequestTag, self).to_map()
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


class UpdateDataCacheRequest(TeaModel):
    def __init__(self, bucket=None, client_token=None, data_cache_id=None, data_source=None, eip_create_param=None,
                 eip_instance_id=None, name=None, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, retention_days=None, security_group_id=None, size=None, tag=None,
                 v_switch_id=None):
        # The bucket in which the data cache is stored. Default value: default.
        self.bucket = bucket  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The data cache ID.
        self.data_cache_id = data_cache_id  # type: str
        # The information about the data source.
        self.data_source = data_source  # type: UpdateDataCacheRequestDataSource
        # The elastic IP address (EIP) to be created and associated. If no NAT gateway is configured for the virtual private cloud (VPC), you can associate an EIP to pull data from the Internet.
        self.eip_create_param = eip_create_param  # type: UpdateDataCacheRequestEipCreateParam
        # The ID of the elastic IP address (EIP). If no NAT gateway is configured for the virtual private cloud (VPC), you can bind an EIP to the elastic container instance to pull data from the Internet.
        self.eip_instance_id = eip_instance_id  # type: str
        # The data cache name.
        self.name = name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        self.region_id = region_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The retention period for the data cache. The data cache is deleted after the retention period expires. By default, the data cache does not expire.
        self.retention_days = retention_days  # type: int
        # The ID of the security group.
        self.security_group_id = security_group_id  # type: str
        # The data cache size.
        self.size = size  # type: int
        # The tags that are added to the data cache.
        self.tag = tag  # type: list[UpdateDataCacheRequestTag]
        # The vSwitch ID.
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.eip_create_param:
            self.eip_create_param.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateDataCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_cache_id is not None:
            result['DataCacheId'] = self.data_cache_id
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.eip_create_param is not None:
            result['EipCreateParam'] = self.eip_create_param.to_map()
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.size is not None:
            result['Size'] = self.size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataCacheId') is not None:
            self.data_cache_id = m.get('DataCacheId')
        if m.get('DataSource') is not None:
            temp_model = UpdateDataCacheRequestDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('EipCreateParam') is not None:
            temp_model = UpdateDataCacheRequestEipCreateParam()
            self.eip_create_param = temp_model.from_map(m['EipCreateParam'])
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateDataCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class UpdateDataCacheResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDataCacheResponseBody, self).to_map()
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


class UpdateDataCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDataCacheResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDataCacheResponse, self).to_map()
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
            temp_model = UpdateDataCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageCacheRequestAcrRegistryInfo(TeaModel):
    def __init__(self, domain=None, instance_id=None, instance_name=None, region_id=None):
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. You can specify multiple domain names. Separate multiple domain names with commas (,).
        self.domain = domain  # type: list[str]
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id  # type: str
        # The name of the Container Registry Enterprise Edition instance.
        self.instance_name = instance_name  # type: str
        # The region ID of the Container Registry Enterprise Edition instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageCacheRequestAcrRegistryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateImageCacheRequestImageRegistryCredential(TeaModel):
    def __init__(self, password=None, server=None, user_name=None):
        # The password that is used to access the image repository.
        self.password = password  # type: str
        # The image repository address without `http://` or `https://` as a prefix.
        self.server = server  # type: str
        # The username that is used to access the image repository.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageCacheRequestImageRegistryCredential, self).to_map()
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


class UpdateImageCacheRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to add to the image cache.
        self.key = key  # type: str
        # The value of tag N to add to the image cache.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageCacheRequestTag, self).to_map()
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


class UpdateImageCacheRequest(TeaModel):
    def __init__(self, acr_registry_info=None, auto_match_image_cache=None, client_token=None,
                 eip_instance_id=None, elimination_strategy=None, flash=None, flash_copy_count=None, image=None,
                 image_cache_id=None, image_cache_name=None, image_cache_size=None, image_registry_credential=None,
                 owner_account=None, owner_id=None, region_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, retention_days=None, security_group_id=None, standard_copy_count=None, tag=None,
                 v_switch_id=None):
        # The information about the Container Registry Enterprise Edition instance.
        self.acr_registry_info = acr_registry_info  # type: list[UpdateImageCacheRequestAcrRegistryInfo]
        # Specifies whether to enable reuse of image cache layers. If you enable this feature and the image cache that you want to create and an existing image cache contain duplicate image layers, the system reuses the duplicate image layers to create the new image cache. This accelerates the creation of the image cache. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.auto_match_image_cache = auto_match_image_cache  # type: bool
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request?](~~25693~~)
        self.client_token = client_token  # type: str
        # The ID of the elastic IP address (EIP). If you want to pull public images, you must make sure that the elastic container instance can access the Internet. To enable Internet access, you can configure an EIP or a NAT gateway for the instance.
        self.eip_instance_id = eip_instance_id  # type: str
        # The elimination policy for the image cache. This parameter is empty by default, which indicates that the image cache is always retained.
        # 
        # You can set this parameter to LRU, which indicates that the image cache can be automatically deleted. When the number of image caches reaches the quota, the system automatically deletes the image caches whose EliminationStrategy parameter is set to LRU and that are least recently used.
        self.elimination_strategy = elimination_strategy  # type: str
        # Specifies whether to enable the instant image cache feature. The feature can accelerate the creation of image caches. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.flash = flash  # type: bool
        # The number of duplicates of temporary local snapshots. By default, the system creates one snapshot for each image cache. If you use the image cache to create multiple elastic container instances at a time, we recommend that you configure this parameter to create multiple snapshot duplicates for the image cache. We recommend that you create one snapshot duplicate for creation of every 1,000 elastic container instances.
        # 
        # > If you enable the instant image cache feature by setting Flash to true, a local snapshot is first created during the creation of the image cache. After the local snapshot is created, regular snapshots start to be created. After the regular snapshots are created, the local snapshot is automatically deleted.
        self.flash_copy_count = flash_copy_count  # type: int
        # Container images that are used to create the image cache.
        self.image = image  # type: list[str]
        # The ID of the image cache.
        self.image_cache_id = image_cache_id  # type: str
        # The name of the image cache.
        self.image_cache_name = image_cache_name  # type: str
        # The size of the image cache. Unit: GiB. Default value: 20.
        self.image_cache_size = image_cache_size  # type: int
        # The information about the image repository.
        self.image_registry_credential = image_registry_credential  # type: list[UpdateImageCacheRequestImageRegistryCredential]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the image cache.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the image cache belongs.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The retention period of the image cache. Unit: days. When the retention period elapses, the image cache expires and is deleted. By default, image caches never expire.
        # 
        # > The image caches that fail to be created are retained for only 1 day.
        self.retention_days = retention_days  # type: int
        # The ID of the security group to which the image cache belongs.
        self.security_group_id = security_group_id  # type: str
        # The number of duplicates of regular snapshots. By default, the system creates one snapshot for each image cache. If you use the image cache to create multiple elastic container instances at a time, we recommend that you configure this parameter to create multiple snapshot duplicates for the image cache. We recommend that you create one snapshot duplicate for creation of every 1,000 elastic container instances.
        # 
        # > If you disable the instant image cache feature by setting Flash to false, only regular snapshots are generated when you create an image cache.
        self.standard_copy_count = standard_copy_count  # type: int
        # The tags to add to the image cache. A maximum of 20 tags can be added to the image cache.
        self.tag = tag  # type: list[UpdateImageCacheRequestTag]
        # The ID of the vSwitch to which the image cache is connected.
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        if self.acr_registry_info:
            for k in self.acr_registry_info:
                if k:
                    k.validate()
        if self.image_registry_credential:
            for k in self.image_registry_credential:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateImageCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcrRegistryInfo'] = []
        if self.acr_registry_info is not None:
            for k in self.acr_registry_info:
                result['AcrRegistryInfo'].append(k.to_map() if k else None)
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id
        if self.elimination_strategy is not None:
            result['EliminationStrategy'] = self.elimination_strategy
        if self.flash is not None:
            result['Flash'] = self.flash
        if self.flash_copy_count is not None:
            result['FlashCopyCount'] = self.flash_copy_count
        if self.image is not None:
            result['Image'] = self.image
        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id
        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name
        if self.image_cache_size is not None:
            result['ImageCacheSize'] = self.image_cache_size
        result['ImageRegistryCredential'] = []
        if self.image_registry_credential is not None:
            for k in self.image_registry_credential:
                result['ImageRegistryCredential'].append(k.to_map() if k else None)
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.standard_copy_count is not None:
            result['StandardCopyCount'] = self.standard_copy_count
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acr_registry_info = []
        if m.get('AcrRegistryInfo') is not None:
            for k in m.get('AcrRegistryInfo'):
                temp_model = UpdateImageCacheRequestAcrRegistryInfo()
                self.acr_registry_info.append(temp_model.from_map(k))
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')
        if m.get('EliminationStrategy') is not None:
            self.elimination_strategy = m.get('EliminationStrategy')
        if m.get('Flash') is not None:
            self.flash = m.get('Flash')
        if m.get('FlashCopyCount') is not None:
            self.flash_copy_count = m.get('FlashCopyCount')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')
        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')
        if m.get('ImageCacheSize') is not None:
            self.image_cache_size = m.get('ImageCacheSize')
        self.image_registry_credential = []
        if m.get('ImageRegistryCredential') is not None:
            for k in m.get('ImageRegistryCredential'):
                temp_model = UpdateImageCacheRequestImageRegistryCredential()
                self.image_registry_credential.append(temp_model.from_map(k))
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StandardCopyCount') is not None:
            self.standard_copy_count = m.get('StandardCopyCount')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateImageCacheRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class UpdateImageCacheResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageCacheResponseBody, self).to_map()
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


class UpdateImageCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateImageCacheResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateImageCacheResponse, self).to_map()
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
            temp_model = UpdateImageCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVirtualNodeRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to add to the virtual node.
        self.key = key  # type: str
        # The value of tag N to add to the virtual node.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVirtualNodeRequestTag, self).to_map()
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


class UpdateVirtualNodeRequest(TeaModel):
    def __init__(self, client_token=None, cluster_dns=None, cluster_domain=None, custom_resources=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None, tag=None,
                 virtual_node_id=None, virtual_node_name=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotency of requests?](~~25693~~)
        self.client_token = client_token  # type: str
        # The IP address of the DNS server. If `dnsPolicy=ClusterFirst` is configured for the Elastic Container Instance pod, Elastic Container Instance uses the configuration to provide DNS services to containers. You can configure multiple IP addresses. Separate multiple IP addresses with commas (,).
        self.cluster_dns = cluster_dns  # type: str
        # The domain name of the cluster. If this parameter is specified, in addition to the search domain of the host, Kubelet configures all containers to search for the specified domain name.
        self.cluster_domain = cluster_domain  # type: str
        # The custom resources that are supported by the virtual node. If a custom resource is specified in the request of an Elastic Container Instance pod, the pod is scheduled to run on the virtual node that supports the custom resource. You can use the `Resource name = Number of resources` format to specify custom resources. Separate multiple resources with commas (,).
        self.custom_resources = custom_resources  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the virtual node.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The tags to add to the virtual node.
        self.tag = tag  # type: list[UpdateVirtualNodeRequestTag]
        # The ID of the virtual node.
        self.virtual_node_id = virtual_node_id  # type: str
        # The name of the virtual node.
        self.virtual_node_name = virtual_node_name  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateVirtualNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_dns is not None:
            result['ClusterDNS'] = self.cluster_dns
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.custom_resources is not None:
            result['CustomResources'] = self.custom_resources
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.virtual_node_id is not None:
            result['VirtualNodeId'] = self.virtual_node_id
        if self.virtual_node_name is not None:
            result['VirtualNodeName'] = self.virtual_node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterDNS') is not None:
            self.cluster_dns = m.get('ClusterDNS')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('CustomResources') is not None:
            self.custom_resources = m.get('CustomResources')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = UpdateVirtualNodeRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VirtualNodeId') is not None:
            self.virtual_node_id = m.get('VirtualNodeId')
        if m.get('VirtualNodeName') is not None:
            self.virtual_node_name = m.get('VirtualNodeName')
        return self


class UpdateVirtualNodeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVirtualNodeResponseBody, self).to_map()
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


class UpdateVirtualNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVirtualNodeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVirtualNodeResponse, self).to_map()
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
            temp_model = UpdateVirtualNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


