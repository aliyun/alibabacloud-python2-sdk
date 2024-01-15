# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, dbinstance_id=None, net_type=None, region_id=None,
                 resource_owner_id=None):
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.net_type = net_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateInstancePublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
    def __init__(self, instance_name=None, request_id=None, task_id=None):
        self.instance_name = instance_name  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateInstancePublicConnectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AllocateInstancePublicConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllocateInstancePublicConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocateInstancePublicConnectionResponse, self).to_map()
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
            temp_model = AllocateInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCreateDBInstanceRequest(TeaModel):
    def __init__(self, cache_size=None, charge_type=None, client_token=None, connection_string=None,
                 dbinstance_class=None, dbinstance_description=None, engine=None, engine_version=None, period=None, region_id=None,
                 resource_group_id=None, resource_owner_id=None, security_iplist=None, used_time=None, v_switch_id=None, vpc_id=None,
                 zone_id=None):
        self.cache_size = cache_size  # type: int
        self.charge_type = charge_type  # type: str
        self.client_token = client_token  # type: str
        self.connection_string = connection_string  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_iplist = security_iplist  # type: str
        self.used_time = used_time  # type: int
        self.v_switch_id = v_switch_id  # type: str
        # VPC ID。
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCreateDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckCreateDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCreateDBInstanceResponseBody, self).to_map()
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


class CheckCreateDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckCreateDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckCreateDBInstanceResponse, self).to_map()
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
            temp_model = CheckCreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleRequest(TeaModel):
    def __init__(self, owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, has_service_linked_role=None, request_id=None):
        self.has_service_linked_role = has_service_linked_role  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_service_linked_role is not None:
            result['HasServiceLinkedRole'] = self.has_service_linked_role
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasServiceLinkedRole') is not None:
            self.has_service_linked_role = m.get('HasServiceLinkedRole')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckServiceLinkedRoleResponse, self).to_map()
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
            temp_model = CheckServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBClusterRequest(TeaModel):
    def __init__(self, cache_size=None, charge_type=None, dbcluster_class=None, dbcluster_description=None,
                 dbinstance_id=None, engine=None, engine_version=None, period=None, region_id=None, resource_group_id=None,
                 resource_owner_id=None, used_time=None, v_switch_id=None, vpc_id=None, zone_id=None):
        self.cache_size = cache_size  # type: str
        self.charge_type = charge_type  # type: str
        self.dbcluster_class = dbcluster_class  # type: str
        self.dbcluster_description = dbcluster_description  # type: str
        # 代表资源一级ID的资源属性字段
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        # 代表资源组的资源属性字段
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.used_time = used_time  # type: str
        self.v_switch_id = v_switch_id  # type: str
        # VPC ID。
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBClusterResponseBodyData(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDBClusterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateDBClusterResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateDBClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateDBClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBClusterResponse, self).to_map()
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
            temp_model = CreateDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(self, cache_size=None, charge_type=None, client_token=None, connection_string=None,
                 dbinstance_class=None, dbinstance_description=None, engine=None, engine_version=None, period=None, region_id=None,
                 resource_group_id=None, resource_owner_id=None, security_iplist=None, used_time=None, v_switch_id=None, vpc_id=None,
                 zone_id=None):
        self.cache_size = cache_size  # type: int
        self.charge_type = charge_type  # type: str
        self.client_token = client_token  # type: str
        self.connection_string = connection_string  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        # 代表资源组的资源属性字段
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_iplist = security_iplist  # type: str
        self.used_time = used_time  # type: int
        self.v_switch_id = v_switch_id  # type: str
        # VPC ID。
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBodyData(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateDBInstanceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateDBInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateDBInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBInstanceResponse, self).to_map()
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
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleForSelectDBRequest(TeaModel):
    def __init__(self, owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleForSelectDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateServiceLinkedRoleForSelectDBResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleForSelectDBResponseBody, self).to_map()
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


class CreateServiceLinkedRoleForSelectDBResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceLinkedRoleForSelectDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleForSelectDBResponse, self).to_map()
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
            temp_model = CreateServiceLinkedRoleForSelectDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBClusterRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbinstance_id=None, region_id=None, resource_group_id=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        # 代表资源一级ID的资源属性字段
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        # 代表资源组的资源属性字段
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBClusterResponseBodyData(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeleteDBClusterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DeleteDBClusterResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteDBClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDBClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDBClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBClusterResponse, self).to_map()
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
            temp_model = DeleteDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBInstanceResponseBody, self).to_map()
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


class DeleteDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBInstanceResponse, self).to_map()
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
            temp_model = DeleteDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBClusterList(TeaModel):
    def __init__(self, cache_storage_size_gb=None, cache_storage_type=None, charge_type=None, cpu_cores=None,
                 created_time=None, db_cluster_class=None, db_cluster_id=None, db_cluster_name=None, db_instance_name=None,
                 memory=None, performance_level=None, start_time=None, status=None):
        self.cache_storage_size_gb = cache_storage_size_gb  # type: str
        self.cache_storage_type = cache_storage_type  # type: str
        self.charge_type = charge_type  # type: str
        self.cpu_cores = cpu_cores  # type: long
        self.created_time = created_time  # type: str
        self.db_cluster_class = db_cluster_class  # type: str
        self.db_cluster_id = db_cluster_id  # type: str
        self.db_cluster_name = db_cluster_name  # type: str
        self.db_instance_name = db_instance_name  # type: str
        self.memory = memory  # type: long
        self.performance_level = performance_level  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBClusterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_storage_size_gb is not None:
            result['CacheStorageSizeGB'] = self.cache_storage_size_gb
        if self.cache_storage_type is not None:
            result['CacheStorageType'] = self.cache_storage_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.db_cluster_class is not None:
            result['DbClusterClass'] = self.db_cluster_class
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.db_cluster_name is not None:
            result['DbClusterName'] = self.db_cluster_name
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CacheStorageSizeGB') is not None:
            self.cache_storage_size_gb = m.get('CacheStorageSizeGB')
        if m.get('CacheStorageType') is not None:
            self.cache_storage_type = m.get('CacheStorageType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DbClusterClass') is not None:
            self.db_cluster_class = m.get('DbClusterClass')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('DbClusterName') is not None:
            self.db_cluster_name = m.get('DbClusterName')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(self, can_upgrade_versions=None, charge_type=None, create_time=None, dbcluster_list=None,
                 dbinstance_id=None, description=None, engine=None, engine_minor_version=None, engine_version=None,
                 expire_time=None, gmt_modified=None, lock_mode=None, lock_reason=None, maintain_endtime=None,
                 maintain_starttime=None, object_store_size=None, request_id=None, resource_cpu=None, status=None, storage_size=None,
                 sub_domain=None):
        self.can_upgrade_versions = can_upgrade_versions  # type: list[str]
        self.charge_type = charge_type  # type: str
        self.create_time = create_time  # type: str
        self.dbcluster_list = dbcluster_list  # type: list[DescribeDBInstanceAttributeResponseBodyDBClusterList]
        self.dbinstance_id = dbinstance_id  # type: str
        self.description = description  # type: str
        self.engine = engine  # type: str
        self.engine_minor_version = engine_minor_version  # type: str
        self.engine_version = engine_version  # type: str
        self.expire_time = expire_time  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.lock_mode = lock_mode  # type: long
        self.lock_reason = lock_reason  # type: str
        self.maintain_endtime = maintain_endtime  # type: str
        self.maintain_starttime = maintain_starttime  # type: str
        self.object_store_size = object_store_size  # type: long
        self.request_id = request_id  # type: str
        self.resource_cpu = resource_cpu  # type: long
        self.status = status  # type: str
        self.storage_size = storage_size  # type: long
        self.sub_domain = sub_domain  # type: str

    def validate(self):
        if self.dbcluster_list:
            for k in self.dbcluster_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_upgrade_versions is not None:
            result['CanUpgradeVersions'] = self.can_upgrade_versions
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DBClusterList'] = []
        if self.dbcluster_list is not None:
            for k in self.dbcluster_list:
                result['DBClusterList'].append(k.to_map() if k else None)
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_minor_version is not None:
            result['EngineMinorVersion'] = self.engine_minor_version
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_endtime is not None:
            result['MaintainEndtime'] = self.maintain_endtime
        if self.maintain_starttime is not None:
            result['MaintainStarttime'] = self.maintain_starttime
        if self.object_store_size is not None:
            result['ObjectStoreSize'] = self.object_store_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_cpu is not None:
            result['ResourceCpu'] = self.resource_cpu
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanUpgradeVersions') is not None:
            self.can_upgrade_versions = m.get('CanUpgradeVersions')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.dbcluster_list = []
        if m.get('DBClusterList') is not None:
            for k in m.get('DBClusterList'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBClusterList()
                self.dbcluster_list.append(temp_model.from_map(k))
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineMinorVersion') is not None:
            self.engine_minor_version = m.get('EngineMinorVersion')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndtime') is not None:
            self.maintain_endtime = m.get('MaintainEndtime')
        if m.get('MaintainStarttime') is not None:
            self.maintain_starttime = m.get('MaintainStarttime')
        if m.get('ObjectStoreSize') is not None:
            self.object_store_size = m.get('ObjectStoreSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceCpu') is not None:
            self.resource_cpu = m.get('ResourceCpu')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponse, self).to_map()
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
            temp_model = DescribeDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceNetInfoRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList(TeaModel):
    def __init__(self, port=None, protocol=None):
        self.port = port  # type: int
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList, self).to_map()
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


class DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos(TeaModel):
    def __init__(self, cluster_id=None, connection_string=None, ip=None, net_type=None, port_list=None,
                 user_visible=None, vpc_id=None, vpc_instance_id=None, vswitch_id=None):
        self.cluster_id = cluster_id  # type: str
        self.connection_string = connection_string  # type: str
        self.ip = ip  # type: str
        self.net_type = net_type  # type: str
        self.port_list = port_list  # type: list[DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList]
        self.user_visible = user_visible  # type: bool
        self.vpc_id = vpc_id  # type: str
        self.vpc_instance_id = vpc_instance_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        if self.port_list:
            for k in self.port_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.net_type is not None:
            result['NetType'] = self.net_type
        result['PortList'] = []
        if self.port_list is not None:
            for k in self.port_list:
                result['PortList'].append(k.to_map() if k else None)
        if self.user_visible is not None:
            result['UserVisible'] = self.user_visible
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        self.port_list = []
        if m.get('PortList') is not None:
            for k in m.get('PortList'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList()
                self.port_list.append(temp_model.from_map(k))
        if m.get('UserVisible') is not None:
            self.user_visible = m.get('UserVisible')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList(TeaModel):
    def __init__(self, port=None, protocol=None):
        self.port = port  # type: int
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList, self).to_map()
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


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos(TeaModel):
    def __init__(self, cluster_id=None, connection_string=None, ip=None, net_type=None, port_list=None,
                 user_visible=None, vpc_id=None, vpc_instance_id=None, vswitch_id=None):
        self.cluster_id = cluster_id  # type: str
        self.connection_string = connection_string  # type: str
        self.ip = ip  # type: str
        self.net_type = net_type  # type: str
        self.port_list = port_list  # type: list[DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList]
        self.user_visible = user_visible  # type: bool
        # VPC ID。
        self.vpc_id = vpc_id  # type: str
        self.vpc_instance_id = vpc_instance_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        if self.port_list:
            for k in self.port_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.net_type is not None:
            result['NetType'] = self.net_type
        result['PortList'] = []
        if self.port_list is not None:
            for k in self.port_list:
                result['PortList'].append(k.to_map() if k else None)
        if self.user_visible is not None:
            result['UserVisible'] = self.user_visible
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        self.port_list = []
        if m.get('PortList') is not None:
            for k in m.get('PortList'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList()
                self.port_list.append(temp_model.from_map(k))
        if m.get('UserVisible') is not None:
            self.user_visible = m.get('UserVisible')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeDBInstanceNetInfoResponseBody(TeaModel):
    def __init__(self, dbclusters_net_infos=None, dbinstance_net_infos=None, request_id=None):
        self.dbclusters_net_infos = dbclusters_net_infos  # type: list[DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos]
        self.dbinstance_net_infos = dbinstance_net_infos  # type: list[DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbclusters_net_infos:
            for k in self.dbclusters_net_infos:
                if k:
                    k.validate()
        if self.dbinstance_net_infos:
            for k in self.dbinstance_net_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBClustersNetInfos'] = []
        if self.dbclusters_net_infos is not None:
            for k in self.dbclusters_net_infos:
                result['DBClustersNetInfos'].append(k.to_map() if k else None)
        result['DBInstanceNetInfos'] = []
        if self.dbinstance_net_infos is not None:
            for k in self.dbinstance_net_infos:
                result['DBInstanceNetInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbclusters_net_infos = []
        if m.get('DBClustersNetInfos') is not None:
            for k in m.get('DBClustersNetInfos'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos()
                self.dbclusters_net_infos.append(temp_model.from_map(k))
        self.dbinstance_net_infos = []
        if m.get('DBInstanceNetInfos') is not None:
            for k in m.get('DBInstanceNetInfos'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos()
                self.dbinstance_net_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceNetInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceNetInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponse, self).to_map()
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
            temp_model = DescribeDBInstanceNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequest(TeaModel):
    def __init__(self, dbinstance_description=None, dbinstance_ids=None, dbinstance_status=None, page_number=None,
                 page_size=None, region_id=None, resource_group_id=None, resource_owner_id=None):
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_ids = dbinstance_ids  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBInstancesResponseBodyItemsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItemsTags, self).to_map()
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


class DescribeDBInstancesResponseBodyItems(TeaModel):
    def __init__(self, category=None, charge_type=None, cluster_count=None, dbinstance_id=None, description=None,
                 engine=None, engine_version=None, expire_time=None, gmt_created=None, gmt_modified=None,
                 instance_used_type=None, is_deleted=None, lock_mode=None, lock_reason=None, maintain_end_time_str=None,
                 maintain_endtime=None, maintain_start_time_str=None, maintain_starttime=None, object_store_size=None,
                 parent_instance=None, region_id=None, resource_cpu=None, resource_group_id=None, resource_memory=None,
                 scale_max=None, scale_min=None, scale_replica=None, status=None, storage_size=None, storage_type=None,
                 tags=None, tenant_cluster_id=None, tenant_token=None, tenant_user_id=None, vpc_id=None, vswitch_id=None,
                 zone_id=None, connection_string=None):
        self.category = category  # type: str
        self.charge_type = charge_type  # type: str
        self.cluster_count = cluster_count  # type: int
        self.dbinstance_id = dbinstance_id  # type: str
        self.description = description  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.expire_time = expire_time  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.instance_used_type = instance_used_type  # type: str
        self.is_deleted = is_deleted  # type: bool
        self.lock_mode = lock_mode  # type: long
        self.lock_reason = lock_reason  # type: str
        self.maintain_end_time_str = maintain_end_time_str  # type: str
        self.maintain_endtime = maintain_endtime  # type: str
        self.maintain_start_time_str = maintain_start_time_str  # type: str
        self.maintain_starttime = maintain_starttime  # type: str
        self.object_store_size = object_store_size  # type: long
        self.parent_instance = parent_instance  # type: str
        self.region_id = region_id  # type: str
        self.resource_cpu = resource_cpu  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.resource_memory = resource_memory  # type: long
        self.scale_max = scale_max  # type: long
        self.scale_min = scale_min  # type: long
        self.scale_replica = scale_replica  # type: long
        self.status = status  # type: str
        self.storage_size = storage_size  # type: long
        self.storage_type = storage_type  # type: str
        self.tags = tags  # type: list[DescribeDBInstancesResponseBodyItemsTags]
        self.tenant_cluster_id = tenant_cluster_id  # type: str
        self.tenant_token = tenant_token  # type: str
        self.tenant_user_id = tenant_user_id  # type: str
        # VPC ID。
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str
        self.connection_string = connection_string  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_used_type is not None:
            result['InstanceUsedType'] = self.instance_used_type
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time_str is not None:
            result['MaintainEndTimeStr'] = self.maintain_end_time_str
        if self.maintain_endtime is not None:
            result['MaintainEndtime'] = self.maintain_endtime
        if self.maintain_start_time_str is not None:
            result['MaintainStartTimeStr'] = self.maintain_start_time_str
        if self.maintain_starttime is not None:
            result['MaintainStarttime'] = self.maintain_starttime
        if self.object_store_size is not None:
            result['ObjectStoreSize'] = self.object_store_size
        if self.parent_instance is not None:
            result['ParentInstance'] = self.parent_instance
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_cpu is not None:
            result['ResourceCpu'] = self.resource_cpu
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_memory is not None:
            result['ResourceMemory'] = self.resource_memory
        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max
        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min
        if self.scale_replica is not None:
            result['ScaleReplica'] = self.scale_replica
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_cluster_id is not None:
            result['TenantClusterId'] = self.tenant_cluster_id
        if self.tenant_token is not None:
            result['TenantToken'] = self.tenant_token
        if self.tenant_user_id is not None:
            result['TenantUserId'] = self.tenant_user_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.connection_string is not None:
            result['connectionString'] = self.connection_string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceUsedType') is not None:
            self.instance_used_type = m.get('InstanceUsedType')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTimeStr') is not None:
            self.maintain_end_time_str = m.get('MaintainEndTimeStr')
        if m.get('MaintainEndtime') is not None:
            self.maintain_endtime = m.get('MaintainEndtime')
        if m.get('MaintainStartTimeStr') is not None:
            self.maintain_start_time_str = m.get('MaintainStartTimeStr')
        if m.get('MaintainStarttime') is not None:
            self.maintain_starttime = m.get('MaintainStarttime')
        if m.get('ObjectStoreSize') is not None:
            self.object_store_size = m.get('ObjectStoreSize')
        if m.get('ParentInstance') is not None:
            self.parent_instance = m.get('ParentInstance')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceCpu') is not None:
            self.resource_cpu = m.get('ResourceCpu')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceMemory') is not None:
            self.resource_memory = m.get('ResourceMemory')
        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')
        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')
        if m.get('ScaleReplica') is not None:
            self.scale_replica = m.get('ScaleReplica')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDBInstancesResponseBodyItemsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantClusterId') is not None:
            self.tenant_cluster_id = m.get('TenantClusterId')
        if m.get('TenantToken') is not None:
            self.tenant_token = m.get('TenantToken')
        if m.get('TenantUserId') is not None:
            self.tenant_user_id = m.get('TenantUserId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('connectionString') is not None:
            self.connection_string = m.get('connectionString')
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_record_count=None):
        self.items = items  # type: list[DescribeDBInstancesResponseBodyItems]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: long

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstancesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponse, self).to_map()
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
            temp_model = DescribeDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIPListRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityIPListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeSecurityIPListResponseBodyGroupItems(TeaModel):
    def __init__(self, aecurity_iptype=None, group_name=None, group_tag=None, security_iplist=None,
                 whitelist_net_type=None):
        self.aecurity_iptype = aecurity_iptype  # type: str
        self.group_name = group_name  # type: str
        self.group_tag = group_tag  # type: str
        self.security_iplist = security_iplist  # type: str
        self.whitelist_net_type = whitelist_net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityIPListResponseBodyGroupItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aecurity_iptype is not None:
            result['AecurityIPType'] = self.aecurity_iptype
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AecurityIPType') is not None:
            self.aecurity_iptype = m.get('AecurityIPType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')
        return self


class DescribeSecurityIPListResponseBody(TeaModel):
    def __init__(self, dbinstance_name=None, group_items=None, request_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.group_items = group_items  # type: list[DescribeSecurityIPListResponseBodyGroupItems]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.group_items:
            for k in self.group_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecurityIPListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['GroupItems'] = []
        if self.group_items is not None:
            for k in self.group_items:
                result['GroupItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.group_items = []
        if m.get('GroupItems') is not None:
            for k in m.get('GroupItems'):
                temp_model = DescribeSecurityIPListResponseBodyGroupItems()
                self.group_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSecurityIPListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSecurityIPListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecurityIPListResponse, self).to_map()
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
            temp_model = DescribeSecurityIPListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBEClusterAttributeRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbinstance_id=None, instance_attribute_type=None, region_id=None,
                 resource_owner_id=None, value=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.instance_attribute_type = instance_attribute_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBEClusterAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_attribute_type is not None:
            result['InstanceAttributeType'] = self.instance_attribute_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceAttributeType') is not None:
            self.instance_attribute_type = m.get('InstanceAttributeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyBEClusterAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBEClusterAttributeResponseBody, self).to_map()
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


class ModifyBEClusterAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyBEClusterAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBEClusterAttributeResponse, self).to_map()
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
            temp_model = ModifyBEClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterRequest(TeaModel):
    def __init__(self, dbcluster_class=None, dbcluster_id=None, dbinstance_id=None, engine=None, region_id=None,
                 resource_owner_id=None):
        self.dbcluster_class = dbcluster_class  # type: str
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine = engine  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterResponseBodyData(TeaModel):
    def __init__(self, dbcluster_id=None, dbinstance_id=None, order_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyDBClusterResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, data=None, request_id=None):
        # 代表资源一级ID的资源属性字段
        self.dbinstance_id = dbinstance_id  # type: str
        self.data = data  # type: ModifyDBClusterResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyDBClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Data') is not None:
            temp_model = ModifyDBClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBClusterResponse, self).to_map()
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
            temp_model = ModifyDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceAttributeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, instance_attribute_type=None, region_id=None, resource_owner_id=None,
                 value=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.instance_attribute_type = instance_attribute_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_attribute_type is not None:
            result['InstanceAttributeType'] = self.instance_attribute_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceAttributeType') is not None:
            self.instance_attribute_type = m.get('InstanceAttributeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyDBInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceAttributeResponseBody, self).to_map()
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


class ModifyDBInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceAttributeResponse, self).to_map()
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
            temp_model = ModifyDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIPListRequest(TeaModel):
    def __init__(self, dbinstance_id=None, group_name=None, modify_mode=None, region_id=None,
                 resource_owner_id=None, security_iplist=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.group_name = group_name  # type: str
        self.modify_mode = modify_mode  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_iplist = security_iplist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIPListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class ModifySecurityIPListResponseBody(TeaModel):
    def __init__(self, dbinstance_name=None, group_name=None, group_tag=None, request_id=None, security_iplist=None,
                 security_iptype=None, task_id=None, whitelist_net_type=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.group_name = group_name  # type: str
        self.group_tag = group_tag  # type: str
        self.request_id = request_id  # type: str
        self.security_iplist = security_iplist  # type: str
        self.security_iptype = security_iptype  # type: str
        self.task_id = task_id  # type: long
        self.whitelist_net_type = whitelist_net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIPListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')
        return self


class ModifySecurityIPListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySecurityIPListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySecurityIPListResponse, self).to_map()
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
            temp_model = ModifySecurityIPListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(self, connection_string=None, dbinstance_id=None, region_id=None, resource_owner_id=None):
        self.connection_string = connection_string  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstancePublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReleaseInstancePublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstancePublicConnectionResponseBody, self).to_map()
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


class ReleaseInstancePublicConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseInstancePublicConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseInstancePublicConnectionResponse, self).to_map()
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
            temp_model = ReleaseInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, dbinstance_id=None, region_id=None,
                 resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAccountPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAccountPasswordResponseBody, self).to_map()
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


class ResetAccountPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetAccountPasswordResponse, self).to_map()
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
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBClusterRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbinstance_id=None, region_id=None, resource_group_id=None,
                 resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        # 代表资源一级ID的资源属性字段
        self.dbinstance_id = dbinstance_id  # type: str
        # 地域
        self.region_id = region_id  # type: str
        # 资源组id
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RestartDBClusterResponseBodyData(TeaModel):
    def __init__(self, dbcluster_id=None, dbinstance_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class RestartDBClusterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RestartDBClusterResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RestartDBClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RestartDBClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartDBClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartDBClusterResponse, self).to_map()
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
            temp_model = RestartDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBEClusterRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbinstance_id=None, region_id=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartBEClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class StartBEClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartBEClusterResponseBody, self).to_map()
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


class StartBEClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartBEClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartBEClusterResponse, self).to_map()
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
            temp_model = StartBEClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBEClusterRequest(TeaModel):
    def __init__(self, dbcluster_id=None, dbinstance_id=None, region_id=None, resource_owner_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopBEClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class StopBEClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopBEClusterResponseBody, self).to_map()
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


class StopBEClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopBEClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopBEClusterResponse, self).to_map()
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
            temp_model = StopBEClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceEngineVersionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, engine_version=None, region_id=None, resource_owner_id=None,
                 switch_time_mode=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine_version = engine_version  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.switch_time_mode = switch_time_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBInstanceEngineVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class UpgradeDBInstanceEngineVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBInstanceEngineVersionResponseBody, self).to_map()
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


class UpgradeDBInstanceEngineVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeDBInstanceEngineVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeDBInstanceEngineVersionResponse, self).to_map()
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
            temp_model = UpgradeDBInstanceEngineVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


