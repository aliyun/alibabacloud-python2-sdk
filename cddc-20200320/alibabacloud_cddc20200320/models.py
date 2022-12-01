# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateDedicatedHostRequest(TeaModel):
    def __init__(self, auto_renew=None, client_token=None, dedicated_host_group_id=None, host_class=None,
                 host_storage=None, host_storage_type=None, image_category=None, os_password=None, owner_id=None, pay_type=None,
                 period=None, region_id=None, resource_owner_account=None, resource_owner_id=None, used_time=None,
                 v_switch_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: str
        self.client_token = client_token  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.host_class = host_class  # type: str
        self.host_storage = host_storage  # type: str
        self.host_storage_type = host_storage_type  # type: str
        self.image_category = image_category  # type: str
        self.os_password = os_password  # type: str
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.used_time = used_time  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDedicatedHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_storage_type is not None:
            result['HostStorageType'] = self.host_storage_type
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostStorageType') is not None:
            self.host_storage_type = m.get('HostStorageType')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList(TeaModel):
    def __init__(self, dedicated_host_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        return self


class CreateDedicatedHostResponseBodyDedicateHostList(TeaModel):
    def __init__(self, dedicate_host_list=None):
        self.dedicate_host_list = dedicate_host_list  # type: list[CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList]

    def validate(self):
        if self.dedicate_host_list:
            for k in self.dedicate_host_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDedicatedHostResponseBodyDedicateHostList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicateHostList'] = []
        if self.dedicate_host_list is not None:
            for k in self.dedicate_host_list:
                result['DedicateHostList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dedicate_host_list = []
        if m.get('DedicateHostList') is not None:
            for k in m.get('DedicateHostList'):
                temp_model = CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList()
                self.dedicate_host_list.append(temp_model.from_map(k))
        return self


class CreateDedicatedHostResponseBody(TeaModel):
    def __init__(self, dedicate_host_list=None, order_id=None, request_id=None):
        self.dedicate_host_list = dedicate_host_list  # type: CreateDedicatedHostResponseBodyDedicateHostList
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dedicate_host_list:
            self.dedicate_host_list.validate()

    def to_map(self):
        _map = super(CreateDedicatedHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicate_host_list is not None:
            result['DedicateHostList'] = self.dedicate_host_list.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicateHostList') is not None:
            temp_model = CreateDedicatedHostResponseBodyDedicateHostList()
            self.dedicate_host_list = temp_model.from_map(m['DedicateHostList'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDedicatedHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDedicatedHostResponse, self).to_map()
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
            temp_model = CreateDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostAccountRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, account_type=None, bastion_instance_id=None,
                 client_token=None, dedicated_host_id=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.account_type = account_type  # type: str
        self.bastion_instance_id = bastion_instance_id  # type: str
        self.client_token = client_token  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDedicatedHostAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDedicatedHostAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDedicatedHostAccountResponseBody, self).to_map()
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


class CreateDedicatedHostAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDedicatedHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDedicatedHostAccountResponse, self).to_map()
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
            temp_model = CreateDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostGroupRequest(TeaModel):
    def __init__(self, allocation_policy=None, client_token=None, cpu_allocation_ratio=None,
                 dedicated_host_group_desc=None, disk_allocation_ratio=None, engine=None, host_replace_policy=None,
                 mem_allocation_ratio=None, open_permission=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, vpcid=None):
        self.allocation_policy = allocation_policy  # type: str
        self.client_token = client_token  # type: str
        self.cpu_allocation_ratio = cpu_allocation_ratio  # type: int
        self.dedicated_host_group_desc = dedicated_host_group_desc  # type: str
        self.disk_allocation_ratio = disk_allocation_ratio  # type: int
        self.engine = engine  # type: str
        self.host_replace_policy = host_replace_policy  # type: str
        self.mem_allocation_ratio = mem_allocation_ratio  # type: int
        self.open_permission = open_permission  # type: int
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.vpcid = vpcid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDedicatedHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        return self


class CreateDedicatedHostGroupResponseBody(TeaModel):
    def __init__(self, dedicated_host_group_id=None, request_id=None):
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDedicatedHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedHostGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDedicatedHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDedicatedHostGroupResponse, self).to_map()
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
            temp_model = CreateDedicatedHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMyBaseRequestECSClassList(TeaModel):
    def __init__(self, data_disk_performance_level=None, disk_capacity=None, disk_count=None, disk_type=None,
                 instance_type=None, node_count=None, sys_disk_capacity=None, sys_disk_type=None,
                 system_disk_performance_level=None):
        self.data_disk_performance_level = data_disk_performance_level  # type: str
        self.disk_capacity = disk_capacity  # type: int
        self.disk_count = disk_count  # type: int
        self.disk_type = disk_type  # type: str
        self.instance_type = instance_type  # type: str
        self.node_count = node_count  # type: int
        self.sys_disk_capacity = sys_disk_capacity  # type: int
        self.sys_disk_type = sys_disk_type  # type: str
        self.system_disk_performance_level = system_disk_performance_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMyBaseRequestECSClassList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_performance_level is not None:
            result['dataDiskPerformanceLevel'] = self.data_disk_performance_level
        if self.disk_capacity is not None:
            result['diskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['diskCount'] = self.disk_count
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        if self.sys_disk_capacity is not None:
            result['sysDiskCapacity'] = self.sys_disk_capacity
        if self.sys_disk_type is not None:
            result['sysDiskType'] = self.sys_disk_type
        if self.system_disk_performance_level is not None:
            result['systemDiskPerformanceLevel'] = self.system_disk_performance_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('dataDiskPerformanceLevel')
        if m.get('diskCapacity') is not None:
            self.disk_capacity = m.get('diskCapacity')
        if m.get('diskCount') is not None:
            self.disk_count = m.get('diskCount')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        if m.get('sysDiskCapacity') is not None:
            self.sys_disk_capacity = m.get('sysDiskCapacity')
        if m.get('sysDiskType') is not None:
            self.sys_disk_type = m.get('sysDiskType')
        if m.get('systemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('systemDiskPerformanceLevel')
        return self


class CreateMyBaseRequest(TeaModel):
    def __init__(self, auto_renew=None, client_token=None, dedicated_host_group_description=None,
                 dedicated_host_group_id=None, ecsclass_list=None, engine=None, image_id=None, key_pair_name=None, os_password=None,
                 owner_id=None, password_inherit=None, pay_type=None, period=None, period_type=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_group_id=None, v_switch_id=None, vpc_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: str
        self.client_token = client_token  # type: str
        self.dedicated_host_group_description = dedicated_host_group_description  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.ecsclass_list = ecsclass_list  # type: list[CreateMyBaseRequestECSClassList]
        self.engine = engine  # type: str
        self.image_id = image_id  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.os_password = os_password  # type: str
        self.owner_id = owner_id  # type: long
        self.password_inherit = password_inherit  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.period_type = period_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.ecsclass_list:
            for k in self.ecsclass_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateMyBaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_group_description is not None:
            result['DedicatedHostGroupDescription'] = self.dedicated_host_group_description
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['ECSClassList'] = []
        if self.ecsclass_list is not None:
            for k in self.ecsclass_list:
                result['ECSClassList'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostGroupDescription') is not None:
            self.dedicated_host_group_description = m.get('DedicatedHostGroupDescription')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.ecsclass_list = []
        if m.get('ECSClassList') is not None:
            for k in m.get('ECSClassList'):
                temp_model = CreateMyBaseRequestECSClassList()
                self.ecsclass_list.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateMyBaseShrinkRequest(TeaModel):
    def __init__(self, auto_renew=None, client_token=None, dedicated_host_group_description=None,
                 dedicated_host_group_id=None, ecsclass_list_shrink=None, engine=None, image_id=None, key_pair_name=None, os_password=None,
                 owner_id=None, password_inherit=None, pay_type=None, period=None, period_type=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_group_id=None, v_switch_id=None, vpc_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: str
        self.client_token = client_token  # type: str
        self.dedicated_host_group_description = dedicated_host_group_description  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.ecsclass_list_shrink = ecsclass_list_shrink  # type: str
        self.engine = engine  # type: str
        self.image_id = image_id  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.os_password = os_password  # type: str
        self.owner_id = owner_id  # type: long
        self.password_inherit = password_inherit  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.period_type = period_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMyBaseShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_group_description is not None:
            result['DedicatedHostGroupDescription'] = self.dedicated_host_group_description
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.ecsclass_list_shrink is not None:
            result['ECSClassList'] = self.ecsclass_list_shrink
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostGroupDescription') is not None:
            self.dedicated_host_group_description = m.get('DedicatedHostGroupDescription')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ECSClassList') is not None:
            self.ecsclass_list_shrink = m.get('ECSClassList')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateMyBaseResponseBodyOrderListOrderList(TeaModel):
    def __init__(self, create_timestamp=None, ecsinstance_ids=None, order_id=None):
        self.create_timestamp = create_timestamp  # type: long
        self.ecsinstance_ids = ecsinstance_ids  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMyBaseResponseBodyOrderListOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.ecsinstance_ids is not None:
            result['ECSInstanceIds'] = self.ecsinstance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ECSInstanceIds') is not None:
            self.ecsinstance_ids = m.get('ECSInstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateMyBaseResponseBodyOrderList(TeaModel):
    def __init__(self, order_list=None):
        self.order_list = order_list  # type: list[CreateMyBaseResponseBodyOrderListOrderList]

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateMyBaseResponseBodyOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['OrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.order_list = []
        if m.get('OrderList') is not None:
            for k in m.get('OrderList'):
                temp_model = CreateMyBaseResponseBodyOrderListOrderList()
                self.order_list.append(temp_model.from_map(k))
        return self


class CreateMyBaseResponseBody(TeaModel):
    def __init__(self, order_list=None, request_id=None):
        self.order_list = order_list  # type: CreateMyBaseResponseBodyOrderList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        _map = super(CreateMyBaseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderList') is not None:
            temp_model = CreateMyBaseResponseBodyOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMyBaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMyBaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMyBaseResponse, self).to_map()
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
            temp_model = CreateMyBaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedHostAccountRequest(TeaModel):
    def __init__(self, account_name=None, dedicated_host_id=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDedicatedHostAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDedicatedHostAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDedicatedHostAccountResponseBody, self).to_map()
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


class DeleteDedicatedHostAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDedicatedHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDedicatedHostAccountResponse, self).to_map()
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
            temp_model = DeleteDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedHostGroupRequest(TeaModel):
    def __init__(self, dedicated_host_group_id=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDedicatedHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
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
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDedicatedHostGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDedicatedHostGroupResponseBody, self).to_map()
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


class DeleteDedicatedHostGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDedicatedHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDedicatedHostGroupResponse, self).to_map()
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
            temp_model = DeleteDedicatedHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostAttributeRequest(TeaModel):
    def __init__(self, dedicated_host_group_id=None, dedicated_host_id=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedHostAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDedicatedHostAttributeResponseBody(TeaModel):
    def __init__(self, account_name=None, account_type=None, allocation_status=None, auto_renew=None,
                 cpuallocation_ratio=None, cpu_used=None, created_time=None, dedicated_host_group_id=None, dedicated_host_id=None,
                 disk_allocation_ratio=None, distribution_tag=None, ecs_class_code=None, expired_time=None, host_cpu=None,
                 host_class=None, host_mem=None, host_name=None, host_status=None, host_storage=None, host_type=None,
                 ipaddress=None, image_category=None, instance_number=None, instance_number_master=None,
                 instance_number_romaster=None, instance_number_roslave=None, instance_number_slave=None, mem_allocation_ratio=None,
                 memory_used=None, open_permission=None, region_id=None, request_id=None, storage_used=None, vpcid=None,
                 v_switch_id=None, zone_id=None):
        self.account_name = account_name  # type: str
        self.account_type = account_type  # type: str
        self.allocation_status = allocation_status  # type: str
        self.auto_renew = auto_renew  # type: str
        self.cpuallocation_ratio = cpuallocation_ratio  # type: str
        self.cpu_used = cpu_used  # type: str
        self.created_time = created_time  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.disk_allocation_ratio = disk_allocation_ratio  # type: str
        self.distribution_tag = distribution_tag  # type: str
        self.ecs_class_code = ecs_class_code  # type: str
        self.expired_time = expired_time  # type: str
        self.host_cpu = host_cpu  # type: int
        self.host_class = host_class  # type: str
        self.host_mem = host_mem  # type: int
        self.host_name = host_name  # type: str
        self.host_status = host_status  # type: str
        self.host_storage = host_storage  # type: int
        self.host_type = host_type  # type: str
        self.ipaddress = ipaddress  # type: str
        self.image_category = image_category  # type: str
        self.instance_number = instance_number  # type: int
        self.instance_number_master = instance_number_master  # type: int
        self.instance_number_romaster = instance_number_romaster  # type: int
        self.instance_number_roslave = instance_number_roslave  # type: int
        self.instance_number_slave = instance_number_slave  # type: int
        self.mem_allocation_ratio = mem_allocation_ratio  # type: str
        self.memory_used = memory_used  # type: str
        self.open_permission = open_permission  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.storage_used = storage_used  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedHostAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio
        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.distribution_tag is not None:
            result['DistributionTag'] = self.distribution_tag
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.instance_number_master is not None:
            result['InstanceNumberMaster'] = self.instance_number_master
        if self.instance_number_romaster is not None:
            result['InstanceNumberROMaster'] = self.instance_number_romaster
        if self.instance_number_roslave is not None:
            result['InstanceNumberROSlave'] = self.instance_number_roslave
        if self.instance_number_slave is not None:
            result['InstanceNumberSlave'] = self.instance_number_slave
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')
        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DistributionTag') is not None:
            self.distribution_tag = m.get('DistributionTag')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('InstanceNumberMaster') is not None:
            self.instance_number_master = m.get('InstanceNumberMaster')
        if m.get('InstanceNumberROMaster') is not None:
            self.instance_number_romaster = m.get('InstanceNumberROMaster')
        if m.get('InstanceNumberROSlave') is not None:
            self.instance_number_roslave = m.get('InstanceNumberROSlave')
        if m.get('InstanceNumberSlave') is not None:
            self.instance_number_slave = m.get('InstanceNumberSlave')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDedicatedHostAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostAttributeResponse, self).to_map()
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
            temp_model = DescribeDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostDisksRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedHostDisksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDedicatedHostDisksResponseBodyDisks(TeaModel):
    def __init__(self, category=None, dbinstance_id=None, device=None, disk_id=None, has_dbinstance=None,
                 max_iops=None, max_throughput=None, performance_level=None, size=None, status=None, type=None, zone_id=None):
        self.category = category  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.device = device  # type: str
        self.disk_id = disk_id  # type: str
        self.has_dbinstance = has_dbinstance  # type: bool
        self.max_iops = max_iops  # type: int
        self.max_throughput = max_throughput  # type: int
        self.performance_level = performance_level  # type: str
        self.size = size  # type: int
        self.status = status  # type: str
        self.type = type  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedHostDisksResponseBodyDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.has_dbinstance is not None:
            result['HasDBInstance'] = self.has_dbinstance
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.max_throughput is not None:
            result['MaxThroughput'] = self.max_throughput
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('HasDBInstance') is not None:
            self.has_dbinstance = m.get('HasDBInstance')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('MaxThroughput') is not None:
            self.max_throughput = m.get('MaxThroughput')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostDisksResponseBody(TeaModel):
    def __init__(self, dedicated_host_id=None, disks=None, request_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.disks = disks  # type: list[DescribeDedicatedHostDisksResponseBodyDisks]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostDisksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDedicatedHostDisksResponseBodyDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDedicatedHostDisksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDedicatedHostDisksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostDisksResponse, self).to_map()
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
            temp_model = DescribeDedicatedHostDisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostGroupsRequest(TeaModel):
    def __init__(self, dedicated_host_group_id=None, engine=None, image_category=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.engine = engine  # type: str
        self.image_category = image_category  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedHostGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
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
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList(TeaModel):
    def __init__(self, zone_idlist=None):
        self.zone_idlist = zone_idlist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZoneIDList') is not None:
            self.zone_idlist = m.get('ZoneIDList')
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups(TeaModel):
    def __init__(self, allocation_policy=None, bastion_instance_id=None, category=None, cpu_allocate_ration=None,
                 cpu_allocated_amount=None, cpu_allocation_ratio=None, create_time=None, dedicated_host_count_group_by_host_type=None,
                 dedicated_host_group_desc=None, dedicated_host_group_id=None, deploy_type=None, disk_allocate_ration=None,
                 disk_allocated_amount=None, disk_allocation_ratio=None, disk_used_amount=None, disk_utility=None, engine=None,
                 host_number=None, host_replace_policy=None, instance_number=None, mem_allocate_ration=None,
                 mem_allocated_amount=None, mem_allocation_ratio=None, mem_used_amount=None, mem_utility=None, open_permission=None,
                 text=None, vpcid=None, zone_idlist=None):
        self.allocation_policy = allocation_policy  # type: str
        self.bastion_instance_id = bastion_instance_id  # type: str
        self.category = category  # type: str
        self.cpu_allocate_ration = cpu_allocate_ration  # type: float
        self.cpu_allocated_amount = cpu_allocated_amount  # type: float
        self.cpu_allocation_ratio = cpu_allocation_ratio  # type: int
        self.create_time = create_time  # type: str
        self.dedicated_host_count_group_by_host_type = dedicated_host_count_group_by_host_type  # type: dict[str, any]
        self.dedicated_host_group_desc = dedicated_host_group_desc  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.deploy_type = deploy_type  # type: str
        self.disk_allocate_ration = disk_allocate_ration  # type: float
        self.disk_allocated_amount = disk_allocated_amount  # type: float
        self.disk_allocation_ratio = disk_allocation_ratio  # type: int
        self.disk_used_amount = disk_used_amount  # type: float
        self.disk_utility = disk_utility  # type: float
        self.engine = engine  # type: str
        self.host_number = host_number  # type: int
        self.host_replace_policy = host_replace_policy  # type: str
        self.instance_number = instance_number  # type: int
        self.mem_allocate_ration = mem_allocate_ration  # type: float
        self.mem_allocated_amount = mem_allocated_amount  # type: float
        self.mem_allocation_ratio = mem_allocation_ratio  # type: int
        self.mem_used_amount = mem_used_amount  # type: float
        self.mem_utility = mem_utility  # type: float
        self.open_permission = open_permission  # type: str
        self.text = text  # type: str
        self.vpcid = vpcid  # type: str
        self.zone_idlist = zone_idlist  # type: DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList

    def validate(self):
        if self.zone_idlist:
            self.zone_idlist.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.category is not None:
            result['Category'] = self.category
        if self.cpu_allocate_ration is not None:
            result['CpuAllocateRation'] = self.cpu_allocate_ration
        if self.cpu_allocated_amount is not None:
            result['CpuAllocatedAmount'] = self.cpu_allocated_amount
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dedicated_host_count_group_by_host_type is not None:
            result['DedicatedHostCountGroupByHostType'] = self.dedicated_host_count_group_by_host_type
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_allocate_ration is not None:
            result['DiskAllocateRation'] = self.disk_allocate_ration
        if self.disk_allocated_amount is not None:
            result['DiskAllocatedAmount'] = self.disk_allocated_amount
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.disk_used_amount is not None:
            result['DiskUsedAmount'] = self.disk_used_amount
        if self.disk_utility is not None:
            result['DiskUtility'] = self.disk_utility
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_number is not None:
            result['HostNumber'] = self.host_number
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.mem_allocate_ration is not None:
            result['MemAllocateRation'] = self.mem_allocate_ration
        if self.mem_allocated_amount is not None:
            result['MemAllocatedAmount'] = self.mem_allocated_amount
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.mem_used_amount is not None:
            result['MemUsedAmount'] = self.mem_used_amount
        if self.mem_utility is not None:
            result['MemUtility'] = self.mem_utility
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.text is not None:
            result['Text'] = self.text
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CpuAllocateRation') is not None:
            self.cpu_allocate_ration = m.get('CpuAllocateRation')
        if m.get('CpuAllocatedAmount') is not None:
            self.cpu_allocated_amount = m.get('CpuAllocatedAmount')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DedicatedHostCountGroupByHostType') is not None:
            self.dedicated_host_count_group_by_host_type = m.get('DedicatedHostCountGroupByHostType')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskAllocateRation') is not None:
            self.disk_allocate_ration = m.get('DiskAllocateRation')
        if m.get('DiskAllocatedAmount') is not None:
            self.disk_allocated_amount = m.get('DiskAllocatedAmount')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DiskUsedAmount') is not None:
            self.disk_used_amount = m.get('DiskUsedAmount')
        if m.get('DiskUtility') is not None:
            self.disk_utility = m.get('DiskUtility')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostNumber') is not None:
            self.host_number = m.get('HostNumber')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('MemAllocateRation') is not None:
            self.mem_allocate_ration = m.get('MemAllocateRation')
        if m.get('MemAllocatedAmount') is not None:
            self.mem_allocated_amount = m.get('MemAllocatedAmount')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemUsedAmount') is not None:
            self.mem_used_amount = m.get('MemUsedAmount')
        if m.get('MemUtility') is not None:
            self.mem_utility = m.get('MemUtility')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('ZoneIDList') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList()
            self.zone_idlist = temp_model.from_map(m['ZoneIDList'])
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups(TeaModel):
    def __init__(self, dedicated_host_groups=None):
        self.dedicated_host_groups = dedicated_host_groups  # type: list[DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups]

    def validate(self):
        if self.dedicated_host_groups:
            for k in self.dedicated_host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedHostGroups'] = []
        if self.dedicated_host_groups is not None:
            for k in self.dedicated_host_groups:
                result['DedicatedHostGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dedicated_host_groups = []
        if m.get('DedicatedHostGroups') is not None:
            for k in m.get('DedicatedHostGroups'):
                temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups()
                self.dedicated_host_groups.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostGroupsResponseBody(TeaModel):
    def __init__(self, dedicated_host_groups=None, request_id=None):
        self.dedicated_host_groups = dedicated_host_groups  # type: DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dedicated_host_groups:
            self.dedicated_host_groups.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_groups is not None:
            result['DedicatedHostGroups'] = self.dedicated_host_groups.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostGroups') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups()
            self.dedicated_host_groups = temp_model.from_map(m['DedicatedHostGroups'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDedicatedHostGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDedicatedHostGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostGroupsResponse, self).to_map()
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
            temp_model = DescribeDedicatedHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostsRequest(TeaModel):
    def __init__(self, allocation_status=None, dedicated_host_group_id=None, dedicated_host_id=None,
                 host_status=None, host_type=None, order_id=None, owner_id=None, page_numbers=None, page_size=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, tags=None, zone_id=None):
        self.allocation_status = allocation_status  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.host_status = host_status  # type: str
        self.host_type = host_type  # type: str
        self.order_id = order_id  # type: long
        self.owner_id = owner_id  # type: long
        self.page_numbers = page_numbers  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tags = tags  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedHostsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts(TeaModel):
    def __init__(self, account_name=None, account_type=None, allocation_status=None, bastion_instance_id=None,
                 cpuallocation_ratio=None, category=None, charge_type=None, cpu_used=None, created_time=None,
                 dedicated_host_group_id=None, dedicated_host_id=None, disk_allocation_ratio=None, disk_info=None,
                 distribution_symbol=None, distribution_tag=None, ecs_class_code=None, ecs_id=None, end_time=None, engine=None,
                 host_cpu=None, host_class=None, host_mem=None, host_name=None, host_status=None, host_storage=None,
                 host_type=None, ipaddress=None, image_category=None, instance_number=None, mem_allocation_ratio=None,
                 memory_used=None, mssql_support_version=None, open_permission=None, storage_used=None, vpcid=None,
                 v_switch_id=None, zone_id=None):
        self.account_name = account_name  # type: str
        self.account_type = account_type  # type: str
        self.allocation_status = allocation_status  # type: str
        self.bastion_instance_id = bastion_instance_id  # type: str
        self.cpuallocation_ratio = cpuallocation_ratio  # type: str
        self.category = category  # type: str
        self.charge_type = charge_type  # type: str
        self.cpu_used = cpu_used  # type: str
        self.created_time = created_time  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.disk_allocation_ratio = disk_allocation_ratio  # type: str
        self.disk_info = disk_info  # type: str
        self.distribution_symbol = distribution_symbol  # type: str
        self.distribution_tag = distribution_tag  # type: str
        self.ecs_class_code = ecs_class_code  # type: str
        self.ecs_id = ecs_id  # type: str
        self.end_time = end_time  # type: str
        self.engine = engine  # type: str
        self.host_cpu = host_cpu  # type: str
        self.host_class = host_class  # type: str
        self.host_mem = host_mem  # type: str
        self.host_name = host_name  # type: str
        self.host_status = host_status  # type: str
        self.host_storage = host_storage  # type: str
        self.host_type = host_type  # type: str
        self.ipaddress = ipaddress  # type: str
        self.image_category = image_category  # type: str
        self.instance_number = instance_number  # type: str
        self.mem_allocation_ratio = mem_allocation_ratio  # type: str
        self.memory_used = memory_used  # type: str
        self.mssql_support_version = mssql_support_version  # type: str
        self.open_permission = open_permission  # type: str
        self.storage_used = storage_used  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio
        if self.category is not None:
            result['Category'] = self.category
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info
        if self.distribution_symbol is not None:
            result['DistributionSymbol'] = self.distribution_symbol
        if self.distribution_tag is not None:
            result['DistributionTag'] = self.distribution_tag
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        if self.mssql_support_version is not None:
            result['MssqlSupportVersion'] = self.mssql_support_version
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')
        if m.get('DistributionSymbol') is not None:
            self.distribution_symbol = m.get('DistributionSymbol')
        if m.get('DistributionTag') is not None:
            self.distribution_tag = m.get('DistributionTag')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        if m.get('MssqlSupportVersion') is not None:
            self.mssql_support_version = m.get('MssqlSupportVersion')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostsResponseBodyDedicatedHosts(TeaModel):
    def __init__(self, dedicated_hosts=None):
        self.dedicated_hosts = dedicated_hosts  # type: list[DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts]

    def validate(self):
        if self.dedicated_hosts:
            for k in self.dedicated_hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostsResponseBodyDedicatedHosts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedHosts'] = []
        if self.dedicated_hosts is not None:
            for k in self.dedicated_hosts:
                result['DedicatedHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dedicated_hosts = []
        if m.get('DedicatedHosts') is not None:
            for k in m.get('DedicatedHosts'):
                temp_model = DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts()
                self.dedicated_hosts.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostsResponseBody(TeaModel):
    def __init__(self, dedicated_host_group_id=None, dedicated_hosts=None, max_auto_scale_host_storage=None,
                 page_numbers=None, page_size=None, request_id=None, total_records=None):
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_hosts = dedicated_hosts  # type: DescribeDedicatedHostsResponseBodyDedicatedHosts
        self.max_auto_scale_host_storage = max_auto_scale_host_storage  # type: long
        self.page_numbers = page_numbers  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_records = total_records  # type: int

    def validate(self):
        if self.dedicated_hosts:
            self.dedicated_hosts.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_hosts is not None:
            result['DedicatedHosts'] = self.dedicated_hosts.to_map()
        if self.max_auto_scale_host_storage is not None:
            result['MaxAutoScaleHostStorage'] = self.max_auto_scale_host_storage
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_records is not None:
            result['TotalRecords'] = self.total_records
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHosts') is not None:
            temp_model = DescribeDedicatedHostsResponseBodyDedicatedHosts()
            self.dedicated_hosts = temp_model.from_map(m['DedicatedHosts'])
        if m.get('MaxAutoScaleHostStorage') is not None:
            self.max_auto_scale_host_storage = m.get('MaxAutoScaleHostStorage')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')
        return self


class DescribeDedicatedHostsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDedicatedHostsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDedicatedHostsResponse, self).to_map()
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
            temp_model = DescribeDedicatedHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostEcsLevelInfoRequest(TeaModel):
    def __init__(self, db_type=None, image_category=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, storage_type=None, zone_id=None):
        self.db_type = db_type  # type: str
        self.image_category = image_category  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.storage_type = storage_type  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHostEcsLevelInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems(TeaModel):
    def __init__(self, cloud_storage_bandwidth=None, cpu=None, cpu_frequency=None, cpu_version=None,
                 description=None, ecs_class=None, ecs_class_code=None, is_cloud_disk=None, local_storage=None, memory=None,
                 net_band_width=None, net_package=None, rds_class_code=None, storage_iops=None):
        self.cloud_storage_bandwidth = cloud_storage_bandwidth  # type: float
        self.cpu = cpu  # type: int
        self.cpu_frequency = cpu_frequency  # type: str
        self.cpu_version = cpu_version  # type: str
        self.description = description  # type: str
        self.ecs_class = ecs_class  # type: str
        self.ecs_class_code = ecs_class_code  # type: str
        self.is_cloud_disk = is_cloud_disk  # type: int
        self.local_storage = local_storage  # type: str
        self.memory = memory  # type: int
        self.net_band_width = net_band_width  # type: float
        self.net_package = net_package  # type: int
        self.rds_class_code = rds_class_code  # type: str
        self.storage_iops = storage_iops  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_storage_bandwidth is not None:
            result['CloudStorageBandwidth'] = self.cloud_storage_bandwidth
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_frequency is not None:
            result['CpuFrequency'] = self.cpu_frequency
        if self.cpu_version is not None:
            result['CpuVersion'] = self.cpu_version
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_class is not None:
            result['EcsClass'] = self.ecs_class
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.is_cloud_disk is not None:
            result['IsCloudDisk'] = self.is_cloud_disk
        if self.local_storage is not None:
            result['LocalStorage'] = self.local_storage
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.net_band_width is not None:
            result['NetBandWidth'] = self.net_band_width
        if self.net_package is not None:
            result['NetPackage'] = self.net_package
        if self.rds_class_code is not None:
            result['RdsClassCode'] = self.rds_class_code
        if self.storage_iops is not None:
            result['StorageIops'] = self.storage_iops
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudStorageBandwidth') is not None:
            self.cloud_storage_bandwidth = m.get('CloudStorageBandwidth')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuFrequency') is not None:
            self.cpu_frequency = m.get('CpuFrequency')
        if m.get('CpuVersion') is not None:
            self.cpu_version = m.get('CpuVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsClass') is not None:
            self.ecs_class = m.get('EcsClass')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('IsCloudDisk') is not None:
            self.is_cloud_disk = m.get('IsCloudDisk')
        if m.get('LocalStorage') is not None:
            self.local_storage = m.get('LocalStorage')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetBandWidth') is not None:
            self.net_band_width = m.get('NetBandWidth')
        if m.get('NetPackage') is not None:
            self.net_package = m.get('NetPackage')
        if m.get('RdsClassCode') is not None:
            self.rds_class_code = m.get('RdsClassCode')
        if m.get('StorageIops') is not None:
            self.storage_iops = m.get('StorageIops')
        return self


class DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos(TeaModel):
    def __init__(self, cddc_host_type=None, items=None):
        self.cddc_host_type = cddc_host_type  # type: str
        self.items = items  # type: list[DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cddc_host_type is not None:
            result['CddcHostType'] = self.cddc_host_type
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CddcHostType') is not None:
            self.cddc_host_type = m.get('CddcHostType')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeHostEcsLevelInfoResponseBody(TeaModel):
    def __init__(self, host_ecs_level_infos=None, request_id=None):
        self.host_ecs_level_infos = host_ecs_level_infos  # type: list[DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host_ecs_level_infos:
            for k in self.host_ecs_level_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHostEcsLevelInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostEcsLevelInfos'] = []
        if self.host_ecs_level_infos is not None:
            for k in self.host_ecs_level_infos:
                result['HostEcsLevelInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_ecs_level_infos = []
        if m.get('HostEcsLevelInfos') is not None:
            for k in m.get('HostEcsLevelInfos'):
                temp_model = DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos()
                self.host_ecs_level_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHostEcsLevelInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHostEcsLevelInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHostEcsLevelInfoResponse, self).to_map()
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
            temp_model = DescribeHostEcsLevelInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostWebShellRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, zone_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHostWebShellRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHostWebShellResponseBody(TeaModel):
    def __init__(self, login_url=None, request_id=None):
        self.login_url = login_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHostWebShellResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHostWebShellResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHostWebShellResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHostWebShellResponse, self).to_map()
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
            temp_model = DescribeHostWebShellResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, resource_owner_id=None):
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRDSRegion(TeaModel):
    def __init__(self, region_id=None, zone_id=None):
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRDSRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, rdsregion=None):
        self.rdsregion = rdsregion  # type: list[DescribeRegionsResponseBodyRegionsRDSRegion]

    def validate(self):
        if self.rdsregion:
            for k in self.rdsregion:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RDSRegion'] = []
        if self.rdsregion is not None:
            for k in self.rdsregion:
                result['RDSRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rdsregion = []
        if m.get('RDSRegion') is not None:
            for k in m.get('RDSRegion'):
                temp_model = DescribeRegionsResponseBodyRegionsRDSRegion()
                self.rdsregion.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
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
    def __init__(self, owner_id=None, region_id=None, resource_id=None, resource_owner_account=None,
                 resource_owner_id=None, resource_type=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_resources=None):
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
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


class ModifyDedicatedHostAccountRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, dedicated_host_id=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDedicatedHostAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostAccountResponseBody, self).to_map()
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


class ModifyDedicatedHostAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDedicatedHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDedicatedHostAccountResponse, self).to_map()
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
            temp_model = ModifyDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAttributeRequest(TeaModel):
    def __init__(self, allocation_status=None, dedicated_host_id=None, host_name=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.allocation_status = allocation_status  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.host_name = host_name  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
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
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDedicatedHostAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostAttributeResponseBody, self).to_map()
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


class ModifyDedicatedHostAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDedicatedHostAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDedicatedHostAttributeResponse, self).to_map()
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
            temp_model = ModifyDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostClassRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, switch_time=None, switch_time_mode=None, target_class_code=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.switch_time = switch_time  # type: str
        self.switch_time_mode = switch_time_mode  # type: str
        self.target_class_code = target_class_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostClassRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        if self.target_class_code is not None:
            result['TargetClassCode'] = self.target_class_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        if m.get('TargetClassCode') is not None:
            self.target_class_code = m.get('TargetClassCode')
        return self


class ModifyDedicatedHostClassResponseBody(TeaModel):
    def __init__(self, dedicated_host_id=None, request_id=None, task_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostClassResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyDedicatedHostClassResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDedicatedHostClassResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDedicatedHostClassResponse, self).to_map()
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
            temp_model = ModifyDedicatedHostClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostGroupAttributeRequest(TeaModel):
    def __init__(self, allocation_policy=None, cpu_allocation_ratio=None, dedicated_host_group_desc=None,
                 dedicated_host_group_id=None, disk_allocation_ratio=None, host_replace_policy=None, mem_allocation_ratio=None,
                 open_permission=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.allocation_policy = allocation_policy  # type: str
        self.cpu_allocation_ratio = cpu_allocation_ratio  # type: int
        self.dedicated_host_group_desc = dedicated_host_group_desc  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.disk_allocation_ratio = disk_allocation_ratio  # type: int
        self.host_replace_policy = host_replace_policy  # type: str
        self.mem_allocation_ratio = mem_allocation_ratio  # type: int
        self.open_permission = open_permission  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostGroupAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
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
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDedicatedHostGroupAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostGroupAttributeResponseBody, self).to_map()
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


class ModifyDedicatedHostGroupAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDedicatedHostGroupAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDedicatedHostGroupAttributeResponse, self).to_map()
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
            temp_model = ModifyDedicatedHostGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostPasswordRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, new_password=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.new_password = new_password  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDedicatedHostPasswordResponseBody(TeaModel):
    def __init__(self, dedicated_host_name=None, request_id=None):
        self.dedicated_host_name = dedicated_host_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedHostPasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDedicatedHostPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDedicatedHostPasswordResponse, self).to_map()
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
            temp_model = ModifyDedicatedHostPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHostBaseInfoByInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHostBaseInfoByInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos(TeaModel):
    def __init__(self, cluster_name=None, engine=None, engine_version=None, expired_time=None, host_name=None,
                 ip=None, port=None, role=None, status=None, vpc_id=None):
        self.cluster_name = cluster_name  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.expired_time = expired_time  # type: str
        self.host_name = host_name  # type: str
        self.ip = ip  # type: str
        self.port = port  # type: str
        self.role = role  # type: str
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class QueryHostBaseInfoByInstanceResponseBody(TeaModel):
    def __init__(self, host_instance_console_infos=None, request_id=None):
        self.host_instance_console_infos = host_instance_console_infos  # type: list[QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host_instance_console_infos:
            for k in self.host_instance_console_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryHostBaseInfoByInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostInstanceConsoleInfos'] = []
        if self.host_instance_console_infos is not None:
            for k in self.host_instance_console_infos:
                result['HostInstanceConsoleInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_instance_console_infos = []
        if m.get('HostInstanceConsoleInfos') is not None:
            for k in m.get('HostInstanceConsoleInfos'):
                temp_model = QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos()
                self.host_instance_console_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryHostBaseInfoByInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryHostBaseInfoByInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryHostBaseInfoByInstanceResponse, self).to_map()
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
            temp_model = QueryHostBaseInfoByInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHostInstanceConsoleInfoRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHostInstanceConsoleInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo(TeaModel):
    def __init__(self, cpu_ratio=None, disk_curr=None, mem_ratio=None, perf_idb_pio=None):
        self.cpu_ratio = cpu_ratio  # type: float
        self.disk_curr = disk_curr  # type: float
        self.mem_ratio = mem_ratio  # type: float
        self.perf_idb_pio = perf_idb_pio  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_ratio is not None:
            result['CpuRatio'] = self.cpu_ratio
        if self.disk_curr is not None:
            result['DiskCurr'] = self.disk_curr
        if self.mem_ratio is not None:
            result['MemRatio'] = self.mem_ratio
        if self.perf_idb_pio is not None:
            result['PerfIdbPio'] = self.perf_idb_pio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuRatio') is not None:
            self.cpu_ratio = m.get('CpuRatio')
        if m.get('DiskCurr') is not None:
            self.disk_curr = m.get('DiskCurr')
        if m.get('MemRatio') is not None:
            self.mem_ratio = m.get('MemRatio')
        if m.get('PerfIdbPio') is not None:
            self.perf_idb_pio = m.get('PerfIdbPio')
        return self


class QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos(TeaModel):
    def __init__(self, cpu_cores=None, cpu_increase_ratio_value=None, dbinstance_description=None,
                 dbinstance_id=None, disk_size=None, engine=None, engine_version=None, ip=None, level_name=None,
                 max_conn_increase_ratio_value=None, mem_size=None, memory_increase_ratio_value=None, perf_info=None, port=None, role=None,
                 status=None):
        self.cpu_cores = cpu_cores  # type: int
        self.cpu_increase_ratio_value = cpu_increase_ratio_value  # type: int
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.disk_size = disk_size  # type: int
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.ip = ip  # type: str
        self.level_name = level_name  # type: str
        self.max_conn_increase_ratio_value = max_conn_increase_ratio_value  # type: int
        self.mem_size = mem_size  # type: int
        self.memory_increase_ratio_value = memory_increase_ratio_value  # type: int
        self.perf_info = perf_info  # type: QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo
        self.port = port  # type: str
        self.role = role  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.perf_info:
            self.perf_info.validate()

    def to_map(self):
        _map = super(QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.cpu_increase_ratio_value is not None:
            result['CpuIncreaseRatioValue'] = self.cpu_increase_ratio_value
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.level_name is not None:
            result['LevelName'] = self.level_name
        if self.max_conn_increase_ratio_value is not None:
            result['MaxConnIncreaseRatioValue'] = self.max_conn_increase_ratio_value
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.memory_increase_ratio_value is not None:
            result['MemoryIncreaseRatioValue'] = self.memory_increase_ratio_value
        if self.perf_info is not None:
            result['PerfInfo'] = self.perf_info.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('CpuIncreaseRatioValue') is not None:
            self.cpu_increase_ratio_value = m.get('CpuIncreaseRatioValue')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')
        if m.get('MaxConnIncreaseRatioValue') is not None:
            self.max_conn_increase_ratio_value = m.get('MaxConnIncreaseRatioValue')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('MemoryIncreaseRatioValue') is not None:
            self.memory_increase_ratio_value = m.get('MemoryIncreaseRatioValue')
        if m.get('PerfInfo') is not None:
            temp_model = QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo()
            self.perf_info = temp_model.from_map(m['PerfInfo'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryHostInstanceConsoleInfoResponseBody(TeaModel):
    def __init__(self, host_instance_console_infos=None, request_id=None):
        self.host_instance_console_infos = host_instance_console_infos  # type: list[QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host_instance_console_infos:
            for k in self.host_instance_console_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryHostInstanceConsoleInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostInstanceConsoleInfos'] = []
        if self.host_instance_console_infos is not None:
            for k in self.host_instance_console_infos:
                result['HostInstanceConsoleInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_instance_console_infos = []
        if m.get('HostInstanceConsoleInfos') is not None:
            for k in m.get('HostInstanceConsoleInfos'):
                temp_model = QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos()
                self.host_instance_console_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryHostInstanceConsoleInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryHostInstanceConsoleInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryHostInstanceConsoleInfoResponse, self).to_map()
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
            temp_model = QueryHostInstanceConsoleInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceDedicatedHostRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, failover_mode=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.failover_mode = failover_mode  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceDedicatedHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReplaceDedicatedHostResponseBody(TeaModel):
    def __init__(self, dedicated_host_id=None, request_id=None, task_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceDedicatedHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ReplaceDedicatedHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReplaceDedicatedHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplaceDedicatedHostResponse, self).to_map()
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
            temp_model = ReplaceDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDedicatedHostRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, failover_mode=None, force_stop=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.failover_mode = failover_mode  # type: str
        self.force_stop = force_stop  # type: bool
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDedicatedHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RestartDedicatedHostResponseBody(TeaModel):
    def __init__(self, dedicated_host_id=None, request_id=None, task_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDedicatedHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RestartDedicatedHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartDedicatedHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartDedicatedHostResponse, self).to_map()
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
            temp_model = RestartDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
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
    def __init__(self, owner_id=None, region_id=None, resource_id=None, resource_owner_account=None,
                 resource_owner_id=None, resource_type=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
    def __init__(self, all=None, owner_id=None, region_id=None, resource_id=None, resource_owner_account=None,
                 resource_owner_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
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


