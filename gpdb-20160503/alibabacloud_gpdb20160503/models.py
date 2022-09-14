# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddBuDBInstanceRelationRequest(TeaModel):
    def __init__(self, business_unit=None, dbinstance_id=None, owner_id=None):
        self.business_unit = business_unit  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBuDBInstanceRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_unit is not None:
            result['BusinessUnit'] = self.business_unit
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessUnit') is not None:
            self.business_unit = m.get('BusinessUnit')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class AddBuDBInstanceRelationResponseBody(TeaModel):
    def __init__(self, business_unit=None, dbinstance_name=None, request_id=None):
        self.business_unit = business_unit  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBuDBInstanceRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_unit is not None:
            result['BusinessUnit'] = self.business_unit
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessUnit') is not None:
            self.business_unit = m.get('BusinessUnit')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddBuDBInstanceRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddBuDBInstanceRelationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddBuDBInstanceRelationResponse, self).to_map()
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
            temp_model = AddBuDBInstanceRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(self, address_type=None, connection_string_prefix=None, dbinstance_id=None, owner_id=None,
                 port=None, resource_owner_account=None, resource_owner_id=None):
        self.address_type = address_type  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.port = port  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateInstancePublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateInstancePublicConnectionResponseBody, self).to_map()
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


class CheckServiceLinkedRoleRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, has_service_linked_role=None, region_id=None, request_id=None):
        self.has_service_linked_role = has_service_linked_role  # type: str
        self.region_id = region_id  # type: str
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasServiceLinkedRole') is not None:
            self.has_service_linked_role = m.get('HasServiceLinkedRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class CreateAccountRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_password=None, dbinstance_id=None,
                 database_name=None, owner_id=None, resource_group_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.database_name = database_name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountResponseBody, self).to_map()
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


class CreateAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccountResponse, self).to_map()
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
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, create_sample_data=None, dbinstance_category=None, dbinstance_class=None,
                 dbinstance_description=None, dbinstance_group_count=None, dbinstance_mode=None, engine=None, engine_version=None,
                 instance_network_type=None, instance_spec=None, master_node_num=None, owner_id=None, pay_type=None, period=None,
                 private_ip_address=None, region_id=None, resource_group_id=None, security_iplist=None, seg_node_num=None,
                 seg_storage_type=None, storage_size=None, storage_type=None, used_time=None, vpcid=None, v_switch_id=None,
                 zone_id=None):
        self.client_token = client_token  # type: str
        self.create_sample_data = create_sample_data  # type: bool
        self.dbinstance_category = dbinstance_category  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_group_count = dbinstance_group_count  # type: str
        self.dbinstance_mode = dbinstance_mode  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.instance_spec = instance_spec  # type: str
        self.master_node_num = master_node_num  # type: str
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.security_iplist = security_iplist  # type: str
        self.seg_node_num = seg_node_num  # type: str
        self.seg_storage_type = seg_storage_type  # type: str
        self.storage_size = storage_size  # type: long
        self.storage_type = storage_type  # type: str
        self.used_time = used_time  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.create_sample_data is not None:
            result['CreateSampleData'] = self.create_sample_data
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CreateSampleData') is not None:
            self.create_sample_data = m.get('CreateSampleData')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(self, connection_string=None, dbinstance_id=None, order_id=None, port=None, request_id=None):
        self.connection_string = connection_string  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: str
        self.port = port  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.port is not None:
            result['Port'] = self.port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
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


class CreateDBInstancePlanRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, plan_config=None, plan_desc=None, plan_end_date=None,
                 plan_name=None, plan_schedule_type=None, plan_start_date=None, plan_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.plan_config = plan_config  # type: str
        self.plan_desc = plan_desc  # type: str
        self.plan_end_date = plan_end_date  # type: str
        self.plan_name = plan_name  # type: str
        self.plan_schedule_type = plan_schedule_type  # type: str
        self.plan_start_date = plan_start_date  # type: str
        self.plan_type = plan_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstancePlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_config is not None:
            result['PlanConfig'] = self.plan_config
        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc
        if self.plan_end_date is not None:
            result['PlanEndDate'] = self.plan_end_date
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_schedule_type is not None:
            result['PlanScheduleType'] = self.plan_schedule_type
        if self.plan_start_date is not None:
            result['PlanStartDate'] = self.plan_start_date
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanConfig') is not None:
            self.plan_config = m.get('PlanConfig')
        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')
        if m.get('PlanEndDate') is not None:
            self.plan_end_date = m.get('PlanEndDate')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanScheduleType') is not None:
            self.plan_schedule_type = m.get('PlanScheduleType')
        if m.get('PlanStartDate') is not None:
            self.plan_start_date = m.get('PlanStartDate')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        return self


class CreateDBInstancePlanResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, plan_id=None, request_id=None, status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.error_message = error_message  # type: str
        self.plan_id = plan_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstancePlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateDBInstancePlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDBInstancePlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBInstancePlanResponse, self).to_map()
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
            temp_model = CreateDBInstancePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateECSDBInstanceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateECSDBInstanceRequestTag, self).to_map()
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


class CreateECSDBInstanceRequest(TeaModel):
    def __init__(self, backup_id=None, client_token=None, dbinstance_category=None, dbinstance_description=None,
                 encryption_key=None, encryption_type=None, engine=None, engine_version=None, instance_network_type=None,
                 instance_spec=None, master_node_num=None, owner_id=None, pay_type=None, period=None, private_ip_address=None,
                 region_id=None, resource_group_id=None, security_iplist=None, seg_node_num=None, seg_storage_type=None,
                 src_db_instance_name=None, storage_size=None, tag=None, used_time=None, vpcid=None, v_switch_id=None, zone_id=None):
        self.backup_id = backup_id  # type: str
        self.client_token = client_token  # type: str
        self.dbinstance_category = dbinstance_category  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.encryption_key = encryption_key  # type: str
        self.encryption_type = encryption_type  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.instance_spec = instance_spec  # type: str
        self.master_node_num = master_node_num  # type: int
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.security_iplist = security_iplist  # type: str
        self.seg_node_num = seg_node_num  # type: int
        self.seg_storage_type = seg_storage_type  # type: str
        self.src_db_instance_name = src_db_instance_name  # type: str
        self.storage_size = storage_size  # type: int
        self.tag = tag  # type: list[CreateECSDBInstanceRequestTag]
        self.used_time = used_time  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateECSDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type
        if self.src_db_instance_name is not None:
            result['SrcDbInstanceName'] = self.src_db_instance_name
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')
        if m.get('SrcDbInstanceName') is not None:
            self.src_db_instance_name = m.get('SrcDbInstanceName')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateECSDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateECSDBInstanceResponseBody(TeaModel):
    def __init__(self, connection_string=None, dbinstance_id=None, order_id=None, port=None, request_id=None):
        self.connection_string = connection_string  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: str
        self.port = port  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateECSDBInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.port is not None:
            result['Port'] = self.port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateECSDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateECSDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateECSDBInstanceResponse, self).to_map()
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
            temp_model = CreateECSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSampleDataRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSampleDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateSampleDataResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, request_id=None, status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSampleDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateSampleDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSampleDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSampleDataResponse, self).to_map()
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
            temp_model = CreateSampleDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self, owner_id=None, region_id=None):
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponseBody, self).to_map()
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


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponse, self).to_map()
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
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, owner_id=None, resource_group_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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


class DeleteDBInstancePlanRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, plan_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBInstancePlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class DeleteDBInstancePlanResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, plan_id=None, request_id=None, status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.error_message = error_message  # type: str
        self.plan_id = plan_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBInstancePlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteDBInstancePlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDBInstancePlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBInstancePlanResponse, self).to_map()
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
            temp_model = DeleteDBInstancePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabaseRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, resource_group_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatabaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteDatabaseResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatabaseResponseBody, self).to_map()
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


class DeleteDatabaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDatabaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDatabaseResponse, self).to_map()
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
            temp_model = DeleteDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, account_name=None, dbinstance_id=None):
        self.account_name = account_name  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeAccountsResponseBodyAccountsDBInstanceAccount(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_status=None, dbinstance_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_status = account_status  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccountsDBInstanceAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeAccountsResponseBodyAccounts(TeaModel):
    def __init__(self, dbinstance_account=None):
        self.dbinstance_account = dbinstance_account  # type: list[DescribeAccountsResponseBodyAccountsDBInstanceAccount]

    def validate(self):
        if self.dbinstance_account:
            for k in self.dbinstance_account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceAccount'] = []
        if self.dbinstance_account is not None:
            for k in self.dbinstance_account:
                result['DBInstanceAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance_account = []
        if m.get('DBInstanceAccount') is not None:
            for k in m.get('DBInstanceAccount'):
                temp_model = DescribeAccountsResponseBodyAccountsDBInstanceAccount()
                self.dbinstance_account.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(self, accounts=None, request_id=None):
        self.accounts = accounts  # type: DescribeAccountsResponseBodyAccounts
        self.request_id = request_id  # type: str

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponse, self).to_map()
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
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourcesRequest(TeaModel):
    def __init__(self, charge_type=None, region=None, zone_id=None):
        self.charge_type = charge_type  # type: str
        self.region = region  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.region is not None:
            result['Region'] = self.region
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount(TeaModel):
    def __init__(self, max_count=None, min_count=None, step=None):
        self.max_count = max_count  # type: str
        self.min_count = min_count  # type: str
        self.step = step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize(TeaModel):
    def __init__(self, max_count=None, min_count=None, step=None):
        self.max_count = max_count  # type: str
        self.min_count = min_count  # type: str
        self.step = step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses(TeaModel):
    def __init__(self, description=None, display_class=None, instance_class=None, node_count=None,
                 storage_size=None, storage_type=None):
        self.description = description  # type: str
        self.display_class = display_class  # type: str
        self.instance_class = instance_class  # type: str
        self.node_count = node_count  # type: DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount
        self.storage_size = storage_size  # type: DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize
        self.storage_type = storage_type  # type: str

    def validate(self):
        if self.node_count:
            self.node_count.validate()
        if self.storage_size:
            self.storage_size.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_class is not None:
            result['DisplayClass'] = self.display_class
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayClass') is not None:
            self.display_class = m.get('DisplayClass')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        if m.get('StorageSize') is not None:
            temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize()
            self.storage_size = temp_model.from_map(m['StorageSize'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEngines(TeaModel):
    def __init__(self, mode=None, supported_engine_version=None, supported_instance_classes=None):
        self.mode = mode  # type: str
        self.supported_engine_version = supported_engine_version  # type: str
        self.supported_instance_classes = supported_instance_classes  # type: list[DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses]

    def validate(self):
        if self.supported_instance_classes:
            for k in self.supported_instance_classes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourcesResponseBodyResourcesSupportedEngines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.supported_engine_version is not None:
            result['SupportedEngineVersion'] = self.supported_engine_version
        result['SupportedInstanceClasses'] = []
        if self.supported_instance_classes is not None:
            for k in self.supported_instance_classes:
                result['SupportedInstanceClasses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('SupportedEngineVersion') is not None:
            self.supported_engine_version = m.get('SupportedEngineVersion')
        self.supported_instance_classes = []
        if m.get('SupportedInstanceClasses') is not None:
            for k in m.get('SupportedInstanceClasses'):
                temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses()
                self.supported_instance_classes.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourcesResponseBodyResources(TeaModel):
    def __init__(self, supported_engines=None, zone_id=None):
        self.supported_engines = supported_engines  # type: list[DescribeAvailableResourcesResponseBodyResourcesSupportedEngines]
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.supported_engines:
            for k in self.supported_engines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedEngines'] = []
        if self.supported_engines is not None:
            for k in self.supported_engines:
                result['SupportedEngines'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_engines = []
        if m.get('SupportedEngines') is not None:
            for k in m.get('SupportedEngines'):
                temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEngines()
                self.supported_engines.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourcesResponseBody(TeaModel):
    def __init__(self, region_id=None, request_id=None, resources=None):
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[DescribeAvailableResourcesResponseBodyResources]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = DescribeAvailableResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAvailableResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourcesResponse, self).to_map()
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
            temp_model = DescribeAvailableResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, backup_retention_period=None, enable_recovery_point=None, preferred_backup_period=None,
                 preferred_backup_time=None, recovery_point_period=None, request_id=None):
        self.backup_retention_period = backup_retention_period  # type: int
        self.enable_recovery_point = enable_recovery_point  # type: bool
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.recovery_point_period = recovery_point_period  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.enable_recovery_point is not None:
            result['EnableRecoveryPoint'] = self.enable_recovery_point
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.recovery_point_period is not None:
            result['RecoveryPointPeriod'] = self.recovery_point_period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('EnableRecoveryPoint') is not None:
            self.enable_recovery_point = m.get('EnableRecoveryPoint')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RecoveryPointPeriod') is not None:
            self.recovery_point_period = m.get('RecoveryPointPeriod')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupPolicyResponse, self).to_map()
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterNodeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, node_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeDBClusterNodeResponseBodyNodes(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterNodeResponseBodyNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDBClusterNodeResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, nodes=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.nodes = nodes  # type: list[DescribeDBClusterNodeResponseBodyNodes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeDBClusterNodeResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBClusterNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterNodeResponse, self).to_map()
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
            temp_model = DescribeDBClusterNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, key=None, node_type=None, nodes=None, start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.node_type = node_type  # type: str
        self.nodes = nodes  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues(TeaModel):
    def __init__(self, point=None):
        self.point = point  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries(TeaModel):
    def __init__(self, name=None, role=None, values=None):
        self.name = name  # type: str
        self.role = role  # type: str
        self.values = values  # type: list[DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.role is not None:
            result['Role'] = self.role
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(self, name=None, series=None, unit=None):
        self.name = name  # type: str
        self.series = series  # type: list[DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries]
        self.unit = unit  # type: str

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBodyPerformanceKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, performance_keys=None, request_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.performance_keys = performance_keys  # type: list[DescribeDBClusterPerformanceResponseBodyPerformanceKeys]
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.performance_keys:
            for k in self.performance_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['PerformanceKeys'] = []
        if self.performance_keys is not None:
            for k in self.performance_keys:
                result['PerformanceKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performance_keys = []
        if m.get('PerformanceKeys') is not None:
            for k in m.get('PerformanceKeys'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeys()
                self.performance_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBClusterPerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBClusterPerformanceResponse, self).to_map()
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
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, resource_group_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag, self).to_map()
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


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags, self).to_map()
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
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute(TeaModel):
    def __init__(self, availability_value=None, connection_mode=None, connection_string=None, core_version=None,
                 cpu_cores=None, cpu_cores_per_node=None, creation_time=None, dbinstance_category=None,
                 dbinstance_class=None, dbinstance_class_type=None, dbinstance_cpu_cores=None, dbinstance_description=None,
                 dbinstance_disk_mbps=None, dbinstance_group_count=None, dbinstance_id=None, dbinstance_memory=None,
                 dbinstance_mode=None, dbinstance_net_type=None, dbinstance_status=None, dbinstance_storage=None,
                 encryption_key=None, encryption_type=None, engine=None, engine_version=None, expire_time=None, host_type=None,
                 instance_network_type=None, lock_mode=None, lock_reason=None, maintain_end_time=None, maintain_start_time=None,
                 master_node_num=None, max_connections=None, memory_per_node=None, memory_size=None, memory_unit=None,
                 minor_version=None, pay_type=None, port=None, read_delay_time=None, region_id=None, resource_group_id=None,
                 running_time=None, security_iplist=None, seg_node_num=None, segment_counts=None, start_time=None,
                 storage_per_node=None, storage_size=None, storage_type=None, storage_unit=None, support_restore=None, tags=None,
                 v_switch_id=None, vpc_id=None, zone_id=None):
        self.availability_value = availability_value  # type: str
        self.connection_mode = connection_mode  # type: str
        self.connection_string = connection_string  # type: str
        self.core_version = core_version  # type: str
        self.cpu_cores = cpu_cores  # type: int
        self.cpu_cores_per_node = cpu_cores_per_node  # type: int
        self.creation_time = creation_time  # type: str
        self.dbinstance_category = dbinstance_category  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_class_type = dbinstance_class_type  # type: str
        self.dbinstance_cpu_cores = dbinstance_cpu_cores  # type: int
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_disk_mbps = dbinstance_disk_mbps  # type: long
        self.dbinstance_group_count = dbinstance_group_count  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_memory = dbinstance_memory  # type: long
        self.dbinstance_mode = dbinstance_mode  # type: str
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: long
        self.encryption_key = encryption_key  # type: str
        self.encryption_type = encryption_type  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.expire_time = expire_time  # type: str
        self.host_type = host_type  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.lock_mode = lock_mode  # type: str
        self.lock_reason = lock_reason  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.master_node_num = master_node_num  # type: int
        self.max_connections = max_connections  # type: int
        self.memory_per_node = memory_per_node  # type: int
        self.memory_size = memory_size  # type: long
        self.memory_unit = memory_unit  # type: str
        self.minor_version = minor_version  # type: str
        self.pay_type = pay_type  # type: str
        self.port = port  # type: str
        self.read_delay_time = read_delay_time  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.running_time = running_time  # type: str
        self.security_iplist = security_iplist  # type: str
        self.seg_node_num = seg_node_num  # type: int
        self.segment_counts = segment_counts  # type: int
        self.start_time = start_time  # type: str
        self.storage_per_node = storage_per_node  # type: int
        self.storage_size = storage_size  # type: long
        self.storage_type = storage_type  # type: str
        self.storage_unit = storage_unit  # type: str
        self.support_restore = support_restore  # type: bool
        self.tags = tags  # type: DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.core_version is not None:
            result['CoreVersion'] = self.core_version
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.cpu_cores_per_node is not None:
            result['CpuCoresPerNode'] = self.cpu_cores_per_node
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_class_type is not None:
            result['DBInstanceClassType'] = self.dbinstance_class_type
        if self.dbinstance_cpu_cores is not None:
            result['DBInstanceCpuCores'] = self.dbinstance_cpu_cores
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_disk_mbps is not None:
            result['DBInstanceDiskMBPS'] = self.dbinstance_disk_mbps
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_memory is not None:
            result['DBInstanceMemory'] = self.dbinstance_memory
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.memory_per_node is not None:
            result['MemoryPerNode'] = self.memory_per_node
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.memory_unit is not None:
            result['MemoryUnit'] = self.memory_unit
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.read_delay_time is not None:
            result['ReadDelayTime'] = self.read_delay_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.segment_counts is not None:
            result['SegmentCounts'] = self.segment_counts
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage_per_node is not None:
            result['StoragePerNode'] = self.storage_per_node
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_unit is not None:
            result['StorageUnit'] = self.storage_unit
        if self.support_restore is not None:
            result['SupportRestore'] = self.support_restore
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CoreVersion') is not None:
            self.core_version = m.get('CoreVersion')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('CpuCoresPerNode') is not None:
            self.cpu_cores_per_node = m.get('CpuCoresPerNode')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceClassType') is not None:
            self.dbinstance_class_type = m.get('DBInstanceClassType')
        if m.get('DBInstanceCpuCores') is not None:
            self.dbinstance_cpu_cores = m.get('DBInstanceCpuCores')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceDiskMBPS') is not None:
            self.dbinstance_disk_mbps = m.get('DBInstanceDiskMBPS')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceMemory') is not None:
            self.dbinstance_memory = m.get('DBInstanceMemory')
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MemoryPerNode') is not None:
            self.memory_per_node = m.get('MemoryPerNode')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('MemoryUnit') is not None:
            self.memory_unit = m.get('MemoryUnit')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ReadDelayTime') is not None:
            self.read_delay_time = m.get('ReadDelayTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegmentCounts') is not None:
            self.segment_counts = m.get('SegmentCounts')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StoragePerNode') is not None:
            self.storage_per_node = m.get('StoragePerNode')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUnit') is not None:
            self.storage_unit = m.get('StorageUnit')
        if m.get('SupportRestore') is not None:
            self.support_restore = m.get('SupportRestore')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBodyItems(TeaModel):
    def __init__(self, dbinstance_attribute=None):
        self.dbinstance_attribute = dbinstance_attribute  # type: list[DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute]

    def validate(self):
        if self.dbinstance_attribute:
            for k in self.dbinstance_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance_attribute = []
        if m.get('DBInstanceAttribute') is not None:
            for k in m.get('DBInstanceAttribute'):
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: DescribeDBInstanceAttributeResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeDBInstanceDataBloatRequest(TeaModel):
    def __init__(self, dbinstance_id=None, page_number=None, page_size=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceDataBloatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDBInstanceDataBloatResponseBodyItems(TeaModel):
    def __init__(self, bloat_ceoff=None, bloat_size=None, database_name=None, expect_table_size=None,
                 real_table_size=None, schema_name=None, sequence=None, storage_type=None, suggested_action=None, table_name=None,
                 time_last_updated=None, time_last_vacuumed=None):
        self.bloat_ceoff = bloat_ceoff  # type: str
        self.bloat_size = bloat_size  # type: str
        self.database_name = database_name  # type: str
        self.expect_table_size = expect_table_size  # type: str
        self.real_table_size = real_table_size  # type: str
        self.schema_name = schema_name  # type: str
        self.sequence = sequence  # type: int
        self.storage_type = storage_type  # type: str
        self.suggested_action = suggested_action  # type: str
        self.table_name = table_name  # type: str
        self.time_last_updated = time_last_updated  # type: str
        self.time_last_vacuumed = time_last_vacuumed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceDataBloatResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bloat_ceoff is not None:
            result['BloatCeoff'] = self.bloat_ceoff
        if self.bloat_size is not None:
            result['BloatSize'] = self.bloat_size
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.expect_table_size is not None:
            result['ExpectTableSize'] = self.expect_table_size
        if self.real_table_size is not None:
            result['RealTableSize'] = self.real_table_size
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.suggested_action is not None:
            result['SuggestedAction'] = self.suggested_action
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated
        if self.time_last_vacuumed is not None:
            result['TimeLastVacuumed'] = self.time_last_vacuumed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BloatCeoff') is not None:
            self.bloat_ceoff = m.get('BloatCeoff')
        if m.get('BloatSize') is not None:
            self.bloat_size = m.get('BloatSize')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('ExpectTableSize') is not None:
            self.expect_table_size = m.get('ExpectTableSize')
        if m.get('RealTableSize') is not None:
            self.real_table_size = m.get('RealTableSize')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SuggestedAction') is not None:
            self.suggested_action = m.get('SuggestedAction')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')
        if m.get('TimeLastVacuumed') is not None:
            self.time_last_vacuumed = m.get('TimeLastVacuumed')
        return self


class DescribeDBInstanceDataBloatResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, request_id=None, total_count=None):
        self.items = items  # type: list[DescribeDBInstanceDataBloatResponseBodyItems]
        self.page_number = page_number  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceDataBloatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceDataBloatResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceDataBloatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceDataBloatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceDataBloatResponse, self).to_map()
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
            temp_model = DescribeDBInstanceDataBloatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceDataSkewRequest(TeaModel):
    def __init__(self, dbinstance_id=None, page_number=None, page_size=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceDataSkewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDBInstanceDataSkewResponseBodyItems(TeaModel):
    def __init__(self, database_name=None, distribute_key=None, owner=None, schema_name=None, sequence=None,
                 table_name=None, table_size=None, table_skew=None, time_last_updated=None):
        self.database_name = database_name  # type: str
        self.distribute_key = distribute_key  # type: str
        self.owner = owner  # type: str
        self.schema_name = schema_name  # type: str
        self.sequence = sequence  # type: int
        self.table_name = table_name  # type: str
        self.table_size = table_size  # type: str
        self.table_skew = table_skew  # type: str
        self.time_last_updated = time_last_updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceDataSkewResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.distribute_key is not None:
            result['DistributeKey'] = self.distribute_key
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_size is not None:
            result['TableSize'] = self.table_size
        if self.table_skew is not None:
            result['TableSkew'] = self.table_skew
        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DistributeKey') is not None:
            self.distribute_key = m.get('DistributeKey')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')
        if m.get('TableSkew') is not None:
            self.table_skew = m.get('TableSkew')
        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')
        return self


class DescribeDBInstanceDataSkewResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, request_id=None, total_count=None):
        self.items = items  # type: list[DescribeDBInstanceDataSkewResponseBodyItems]
        self.page_number = page_number  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceDataSkewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceDataSkewResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceDataSkewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceDataSkewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceDataSkewResponse, self).to_map()
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
            temp_model = DescribeDBInstanceDataSkewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceDiagnosisSummaryRequest(TeaModel):
    def __init__(self, dbinstance_id=None, page_number=None, page_size=None, role_preferd=None, start_status=None,
                 sync_mode=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.role_preferd = role_preferd  # type: str
        self.start_status = start_status  # type: str
        self.sync_mode = sync_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceDiagnosisSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_preferd is not None:
            result['RolePreferd'] = self.role_preferd
        if self.start_status is not None:
            result['StartStatus'] = self.start_status
        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RolePreferd') is not None:
            self.role_preferd = m.get('RolePreferd')
        if m.get('StartStatus') is not None:
            self.start_status = m.get('StartStatus')
        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')
        return self


class DescribeDBInstanceDiagnosisSummaryResponseBodyItems(TeaModel):
    def __init__(self, hostname=None, node_address=None, node_cid=None, node_id=None, node_name=None, node_port=None,
                 node_preferred_role=None, node_replication_mode=None, node_role=None, node_status=None, node_type=None):
        self.hostname = hostname  # type: str
        self.node_address = node_address  # type: str
        self.node_cid = node_cid  # type: str
        self.node_id = node_id  # type: str
        self.node_name = node_name  # type: str
        self.node_port = node_port  # type: str
        self.node_preferred_role = node_preferred_role  # type: str
        self.node_replication_mode = node_replication_mode  # type: str
        self.node_role = node_role  # type: str
        self.node_status = node_status  # type: str
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceDiagnosisSummaryResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.node_address is not None:
            result['NodeAddress'] = self.node_address
        if self.node_cid is not None:
            result['NodeCID'] = self.node_cid
        if self.node_id is not None:
            result['NodeID'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_port is not None:
            result['NodePort'] = self.node_port
        if self.node_preferred_role is not None:
            result['NodePreferredRole'] = self.node_preferred_role
        if self.node_replication_mode is not None:
            result['NodeReplicationMode'] = self.node_replication_mode
        if self.node_role is not None:
            result['NodeRole'] = self.node_role
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('NodeAddress') is not None:
            self.node_address = m.get('NodeAddress')
        if m.get('NodeCID') is not None:
            self.node_cid = m.get('NodeCID')
        if m.get('NodeID') is not None:
            self.node_id = m.get('NodeID')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')
        if m.get('NodePreferredRole') is not None:
            self.node_preferred_role = m.get('NodePreferredRole')
        if m.get('NodeReplicationMode') is not None:
            self.node_replication_mode = m.get('NodeReplicationMode')
        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo(TeaModel):
    def __init__(self, exception_node_num=None, normal_node_num=None, not_preferred_node_num=None,
                 not_syncing_node_num=None, preferred_node_num=None, synced_node_num=None):
        self.exception_node_num = exception_node_num  # type: int
        self.normal_node_num = normal_node_num  # type: int
        self.not_preferred_node_num = not_preferred_node_num  # type: int
        self.not_syncing_node_num = not_syncing_node_num  # type: int
        self.preferred_node_num = preferred_node_num  # type: int
        self.synced_node_num = synced_node_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_node_num is not None:
            result['ExceptionNodeNum'] = self.exception_node_num
        if self.normal_node_num is not None:
            result['NormalNodeNum'] = self.normal_node_num
        if self.not_preferred_node_num is not None:
            result['NotPreferredNodeNum'] = self.not_preferred_node_num
        if self.not_syncing_node_num is not None:
            result['NotSyncingNodeNum'] = self.not_syncing_node_num
        if self.preferred_node_num is not None:
            result['PreferredNodeNum'] = self.preferred_node_num
        if self.synced_node_num is not None:
            result['SyncedNodeNum'] = self.synced_node_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExceptionNodeNum') is not None:
            self.exception_node_num = m.get('ExceptionNodeNum')
        if m.get('NormalNodeNum') is not None:
            self.normal_node_num = m.get('NormalNodeNum')
        if m.get('NotPreferredNodeNum') is not None:
            self.not_preferred_node_num = m.get('NotPreferredNodeNum')
        if m.get('NotSyncingNodeNum') is not None:
            self.not_syncing_node_num = m.get('NotSyncingNodeNum')
        if m.get('PreferredNodeNum') is not None:
            self.preferred_node_num = m.get('PreferredNodeNum')
        if m.get('SyncedNodeNum') is not None:
            self.synced_node_num = m.get('SyncedNodeNum')
        return self


class DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo(TeaModel):
    def __init__(self, exception_node_num=None, normal_node_num=None, not_preferred_node_num=None,
                 not_syncing_node_num=None, preferred_node_num=None, synced_node_num=None):
        self.exception_node_num = exception_node_num  # type: int
        self.normal_node_num = normal_node_num  # type: int
        self.not_preferred_node_num = not_preferred_node_num  # type: int
        self.not_syncing_node_num = not_syncing_node_num  # type: int
        self.preferred_node_num = preferred_node_num  # type: int
        self.synced_node_num = synced_node_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_node_num is not None:
            result['ExceptionNodeNum'] = self.exception_node_num
        if self.normal_node_num is not None:
            result['NormalNodeNum'] = self.normal_node_num
        if self.not_preferred_node_num is not None:
            result['NotPreferredNodeNum'] = self.not_preferred_node_num
        if self.not_syncing_node_num is not None:
            result['NotSyncingNodeNum'] = self.not_syncing_node_num
        if self.preferred_node_num is not None:
            result['PreferredNodeNum'] = self.preferred_node_num
        if self.synced_node_num is not None:
            result['SyncedNodeNum'] = self.synced_node_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExceptionNodeNum') is not None:
            self.exception_node_num = m.get('ExceptionNodeNum')
        if m.get('NormalNodeNum') is not None:
            self.normal_node_num = m.get('NormalNodeNum')
        if m.get('NotPreferredNodeNum') is not None:
            self.not_preferred_node_num = m.get('NotPreferredNodeNum')
        if m.get('NotSyncingNodeNum') is not None:
            self.not_syncing_node_num = m.get('NotSyncingNodeNum')
        if m.get('PreferredNodeNum') is not None:
            self.preferred_node_num = m.get('PreferredNodeNum')
        if m.get('SyncedNodeNum') is not None:
            self.synced_node_num = m.get('SyncedNodeNum')
        return self


class DescribeDBInstanceDiagnosisSummaryResponseBody(TeaModel):
    def __init__(self, items=None, master_status_info=None, page_number=None, request_id=None,
                 segment_status_info=None, total_count=None):
        self.items = items  # type: list[DescribeDBInstanceDiagnosisSummaryResponseBodyItems]
        self.master_status_info = master_status_info  # type: DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo
        self.page_number = page_number  # type: str
        self.request_id = request_id  # type: str
        self.segment_status_info = segment_status_info  # type: DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo
        self.total_count = total_count  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.master_status_info:
            self.master_status_info.validate()
        if self.segment_status_info:
            self.segment_status_info.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceDiagnosisSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.master_status_info is not None:
            result['MasterStatusInfo'] = self.master_status_info.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.segment_status_info is not None:
            result['SegmentStatusInfo'] = self.segment_status_info.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceDiagnosisSummaryResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('MasterStatusInfo') is not None:
            temp_model = DescribeDBInstanceDiagnosisSummaryResponseBodyMasterStatusInfo()
            self.master_status_info = temp_model.from_map(m['MasterStatusInfo'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SegmentStatusInfo') is not None:
            temp_model = DescribeDBInstanceDiagnosisSummaryResponseBodySegmentStatusInfo()
            self.segment_status_info = temp_model.from_map(m['SegmentStatusInfo'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceDiagnosisSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceDiagnosisSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceDiagnosisSummaryResponse, self).to_map()
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
            temp_model = DescribeDBInstanceDiagnosisSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceErrorLogRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, host=None, keywords=None, log_level=None,
                 page_number=None, page_size=None, start_time=None, user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.host = host  # type: str
        self.keywords = keywords  # type: str
        self.log_level = log_level  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceErrorLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.host is not None:
            result['Host'] = self.host
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDBInstanceErrorLogResponseBodyItems(TeaModel):
    def __init__(self, database=None, host=None, log_context=None, log_level=None, time=None, user=None):
        self.database = database  # type: str
        self.host = host  # type: str
        self.log_context = log_context  # type: str
        self.log_level = log_level  # type: str
        self.time = time  # type: long
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceErrorLogResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.host is not None:
            result['Host'] = self.host
        if self.log_context is not None:
            result['LogContext'] = self.log_context
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.time is not None:
            result['Time'] = self.time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('LogContext') is not None:
            self.log_context = m.get('LogContext')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDBInstanceErrorLogResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, request_id=None, total_count=None):
        self.items = items  # type: list[DescribeDBInstanceErrorLogResponseBodyItems]
        self.page_number = page_number  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceErrorLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceErrorLogResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceErrorLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceErrorLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceErrorLogResponse, self).to_map()
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
            temp_model = DescribeDBInstanceErrorLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceIPArrayListRequest(TeaModel):
    def __init__(self, dbinstance_id=None, resource_group_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceIPArrayListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray(TeaModel):
    def __init__(self, dbinstance_iparray_attribute=None, dbinstance_iparray_name=None, security_iplist=None):
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute  # type: str
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        self.security_iplist = security_iplist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeDBInstanceIPArrayListResponseBodyItems(TeaModel):
    def __init__(self, dbinstance_iparray=None):
        self.dbinstance_iparray = dbinstance_iparray  # type: list[DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray]

    def validate(self):
        if self.dbinstance_iparray:
            for k in self.dbinstance_iparray:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceIPArrayListResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceIPArray'] = []
        if self.dbinstance_iparray is not None:
            for k in self.dbinstance_iparray:
                result['DBInstanceIPArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance_iparray = []
        if m.get('DBInstanceIPArray') is not None:
            for k in m.get('DBInstanceIPArray'):
                temp_model = DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray()
                self.dbinstance_iparray.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceIPArrayListResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: DescribeDBInstanceIPArrayListResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceIPArrayListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBInstanceIPArrayListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceIPArrayListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceIPArrayListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceIPArrayListResponse, self).to_map()
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
            temp_model = DescribeDBInstanceIPArrayListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceIndexUsageRequest(TeaModel):
    def __init__(self, dbinstance_id=None, page_number=None, page_size=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceIndexUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDBInstanceIndexUsageResponseBodyItems(TeaModel):
    def __init__(self, database_name=None, index_def=None, index_name=None, index_scan_times=None, index_size=None,
                 is_partition_table=None, parent_table_name=None, schema_name=None, table_name=None, time_last_updated=None):
        self.database_name = database_name  # type: str
        self.index_def = index_def  # type: str
        self.index_name = index_name  # type: str
        self.index_scan_times = index_scan_times  # type: int
        self.index_size = index_size  # type: str
        self.is_partition_table = is_partition_table  # type: bool
        self.parent_table_name = parent_table_name  # type: str
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.time_last_updated = time_last_updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceIndexUsageResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.index_def is not None:
            result['IndexDef'] = self.index_def
        if self.index_name is not None:
            result['IndexName'] = self.index_name
        if self.index_scan_times is not None:
            result['IndexScanTimes'] = self.index_scan_times
        if self.index_size is not None:
            result['IndexSize'] = self.index_size
        if self.is_partition_table is not None:
            result['IsPartitionTable'] = self.is_partition_table
        if self.parent_table_name is not None:
            result['ParentTableName'] = self.parent_table_name
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IndexDef') is not None:
            self.index_def = m.get('IndexDef')
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')
        if m.get('IndexScanTimes') is not None:
            self.index_scan_times = m.get('IndexScanTimes')
        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')
        if m.get('IsPartitionTable') is not None:
            self.is_partition_table = m.get('IsPartitionTable')
        if m.get('ParentTableName') is not None:
            self.parent_table_name = m.get('ParentTableName')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')
        return self


class DescribeDBInstanceIndexUsageResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, request_id=None, total_count=None):
        self.items = items  # type: list[DescribeDBInstanceIndexUsageResponseBodyItems]
        self.page_number = page_number  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceIndexUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceIndexUsageResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstanceIndexUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceIndexUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceIndexUsageResponse, self).to_map()
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
            temp_model = DescribeDBInstanceIndexUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceNetInfoRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo(TeaModel):
    def __init__(self, address_type=None, connection_string=None, ipaddress=None, iptype=None, port=None, vpcid=None,
                 v_switch_id=None, vpc_instance_id=None):
        self.address_type = address_type  # type: str
        self.connection_string = connection_string  # type: str
        self.ipaddress = ipaddress  # type: str
        self.iptype = iptype  # type: str
        self.port = port  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_instance_id = vpc_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.iptype is not None:
            result['IPType'] = self.iptype
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos(TeaModel):
    def __init__(self, dbinstance_net_info=None):
        self.dbinstance_net_info = dbinstance_net_info  # type: list[DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo]

    def validate(self):
        if self.dbinstance_net_info:
            for k in self.dbinstance_net_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceNetInfo'] = []
        if self.dbinstance_net_info is not None:
            for k in self.dbinstance_net_info:
                result['DBInstanceNetInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance_net_info = []
        if m.get('DBInstanceNetInfo') is not None:
            for k in m.get('DBInstanceNetInfo'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo()
                self.dbinstance_net_info.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceNetInfoResponseBody(TeaModel):
    def __init__(self, dbinstance_net_infos=None, instance_network_type=None, request_id=None):
        self.dbinstance_net_infos = dbinstance_net_infos  # type: DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos
        self.instance_network_type = instance_network_type  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbinstance_net_infos:
            self.dbinstance_net_infos.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceNetInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_net_infos is not None:
            result['DBInstanceNetInfos'] = self.dbinstance_net_infos.to_map()
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceNetInfos') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos()
            self.dbinstance_net_infos = temp_model.from_map(m['DBInstanceNetInfos'])
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
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


class DescribeDBInstanceOnECSAttributeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceOnECSAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTagsTag, self).to_map()
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


class DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTags, self).to_map()
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
                temp_model = DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttribute(TeaModel):
    def __init__(self, connection_mode=None, connection_string=None, cpu_cores=None, creation_time=None,
                 dbinstance_category=None, dbinstance_class=None, dbinstance_description=None, dbinstance_id=None,
                 dbinstance_status=None, encryption_key=None, encryption_type=None, engine=None, engine_version=None,
                 expire_time=None, instance_deploy_type=None, instance_network_type=None, lock_mode=None, master_node_num=None,
                 memory_size=None, minor_version=None, pay_type=None, port=None, region_id=None, seg_node_num=None,
                 storage_size=None, storage_type=None, support_restore=None, tags=None, v_switch_id=None, vpc_id=None,
                 zone_id=None):
        self.connection_mode = connection_mode  # type: str
        self.connection_string = connection_string  # type: str
        self.cpu_cores = cpu_cores  # type: int
        self.creation_time = creation_time  # type: str
        self.dbinstance_category = dbinstance_category  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.encryption_key = encryption_key  # type: str
        self.encryption_type = encryption_type  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.expire_time = expire_time  # type: str
        self.instance_deploy_type = instance_deploy_type  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.lock_mode = lock_mode  # type: str
        self.master_node_num = master_node_num  # type: int
        self.memory_size = memory_size  # type: int
        self.minor_version = minor_version  # type: str
        self.pay_type = pay_type  # type: str
        self.port = port  # type: str
        self.region_id = region_id  # type: str
        self.seg_node_num = seg_node_num  # type: int
        self.storage_size = storage_size  # type: int
        self.storage_type = storage_type  # type: str
        self.support_restore = support_restore  # type: bool
        self.tags = tags  # type: DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTags
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_deploy_type is not None:
            result['InstanceDeployType'] = self.instance_deploy_type
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.support_restore is not None:
            result['SupportRestore'] = self.support_restore
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceDeployType') is not None:
            self.instance_deploy_type = m.get('InstanceDeployType')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SupportRestore') is not None:
            self.support_restore = m.get('SupportRestore')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceOnECSAttributeResponseBodyItems(TeaModel):
    def __init__(self, dbinstance_attribute=None):
        self.dbinstance_attribute = dbinstance_attribute  # type: list[DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttribute]

    def validate(self):
        if self.dbinstance_attribute:
            for k in self.dbinstance_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceOnECSAttributeResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance_attribute = []
        if m.get('DBInstanceAttribute') is not None:
            for k in m.get('DBInstanceAttribute'):
                temp_model = DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceOnECSAttributeResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: DescribeDBInstanceOnECSAttributeResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceOnECSAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBInstanceOnECSAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceOnECSAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceOnECSAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceOnECSAttributeResponse, self).to_map()
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
            temp_model = DescribeDBInstanceOnECSAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancePerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, key=None, resource_group_id=None, start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstancePerformanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, engine=None, performance_keys=None, request_id=None,
                 start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.engine = engine  # type: str
        self.performance_keys = performance_keys  # type: list[str]
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('PerformanceKeys') is not None:
            self.performance_keys = m.get('PerformanceKeys')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstancePerformanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstancePerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponse, self).to_map()
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
            temp_model = DescribeDBInstancePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancePlansRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, plan_create_date=None, plan_desc=None, plan_id=None,
                 plan_schedule_type=None, plan_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.plan_create_date = plan_create_date  # type: str
        self.plan_desc = plan_desc  # type: str
        self.plan_id = plan_id  # type: str
        self.plan_schedule_type = plan_schedule_type  # type: str
        self.plan_type = plan_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancePlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_create_date is not None:
            result['PlanCreateDate'] = self.plan_create_date
        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_schedule_type is not None:
            result['PlanScheduleType'] = self.plan_schedule_type
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanCreateDate') is not None:
            self.plan_create_date = m.get('PlanCreateDate')
        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanScheduleType') is not None:
            self.plan_schedule_type = m.get('PlanScheduleType')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        return self


class DescribeDBInstancePlansResponseBodyItemsPlanList(TeaModel):
    def __init__(self, dbinstance_id=None, plan_config=None, plan_desc=None, plan_end_date=None, plan_id=None,
                 plan_name=None, plan_schedule_type=None, plan_start_date=None, plan_status=None, plan_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.plan_config = plan_config  # type: str
        self.plan_desc = plan_desc  # type: str
        self.plan_end_date = plan_end_date  # type: str
        self.plan_id = plan_id  # type: str
        self.plan_name = plan_name  # type: str
        self.plan_schedule_type = plan_schedule_type  # type: str
        self.plan_start_date = plan_start_date  # type: str
        self.plan_status = plan_status  # type: str
        self.plan_type = plan_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancePlansResponseBodyItemsPlanList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.plan_config is not None:
            result['PlanConfig'] = self.plan_config
        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc
        if self.plan_end_date is not None:
            result['PlanEndDate'] = self.plan_end_date
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_schedule_type is not None:
            result['PlanScheduleType'] = self.plan_schedule_type
        if self.plan_start_date is not None:
            result['PlanStartDate'] = self.plan_start_date
        if self.plan_status is not None:
            result['PlanStatus'] = self.plan_status
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PlanConfig') is not None:
            self.plan_config = m.get('PlanConfig')
        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')
        if m.get('PlanEndDate') is not None:
            self.plan_end_date = m.get('PlanEndDate')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanScheduleType') is not None:
            self.plan_schedule_type = m.get('PlanScheduleType')
        if m.get('PlanStartDate') is not None:
            self.plan_start_date = m.get('PlanStartDate')
        if m.get('PlanStatus') is not None:
            self.plan_status = m.get('PlanStatus')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        return self


class DescribeDBInstancePlansResponseBodyItems(TeaModel):
    def __init__(self, plan_list=None):
        self.plan_list = plan_list  # type: list[DescribeDBInstancePlansResponseBodyItemsPlanList]

    def validate(self):
        if self.plan_list:
            for k in self.plan_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePlansResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PlanList'] = []
        if self.plan_list is not None:
            for k in self.plan_list:
                result['PlanList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.plan_list = []
        if m.get('PlanList') is not None:
            for k in m.get('PlanList'):
                temp_model = DescribeDBInstancePlansResponseBodyItemsPlanList()
                self.plan_list.append(temp_model.from_map(k))
        return self


class DescribeDBInstancePlansResponseBody(TeaModel):
    def __init__(self, error_message=None, items=None, page_number=None, page_record_count=None, request_id=None,
                 status=None, total_record_count=None):
        self.error_message = error_message  # type: str
        self.items = items  # type: DescribeDBInstancePlansResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Items') is not None:
            temp_model = DescribeDBInstancePlansResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeDBInstancePlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstancePlansResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePlansResponse, self).to_map()
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
            temp_model = DescribeDBInstancePlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSQLPatternsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, query_keywords=None, source_ip=None,
                 start_time=None, user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.query_keywords = query_keywords  # type: str
        self.source_ip = source_ip  # type: str
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSQLPatternsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDBInstanceSQLPatternsResponseBodyPatterns(TeaModel):
    def __init__(self, name=None, values=None):
        self.name = name  # type: str
        self.values = values  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSQLPatternsResponseBodyPatterns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeDBInstanceSQLPatternsResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, patterns=None, request_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.patterns = patterns  # type: list[DescribeDBInstanceSQLPatternsResponseBodyPatterns]
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.patterns:
            for k in self.patterns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSQLPatternsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Patterns'] = []
        if self.patterns is not None:
            for k in self.patterns:
                result['Patterns'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.patterns = []
        if m.get('Patterns') is not None:
            for k in m.get('Patterns'):
                temp_model = DescribeDBInstanceSQLPatternsResponseBodyPatterns()
                self.patterns.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstanceSQLPatternsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceSQLPatternsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSQLPatternsResponse, self).to_map()
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
            temp_model = DescribeDBInstanceSQLPatternsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSSLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceSSLResponseBody(TeaModel):
    def __init__(self, cert_common_name=None, dbinstance_id=None, dbinstance_name=None, request_id=None,
                 sslenabled=None, sslexpired_time=None):
        self.cert_common_name = cert_common_name  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.request_id = request_id  # type: str
        self.sslenabled = sslenabled  # type: bool
        self.sslexpired_time = sslexpired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSSLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        return self


class DescribeDBInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSSLResponse, self).to_map()
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
            temp_model = DescribeDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesRequestTag, self).to_map()
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


class DescribeDBInstancesRequest(TeaModel):
    def __init__(self, dbinstance_categories=None, dbinstance_description=None, dbinstance_ids=None,
                 dbinstance_modes=None, dbinstance_statuses=None, instance_deploy_types=None, instance_network_type=None,
                 owner_id=None, page_number=None, page_size=None, region_id=None, resource_group_id=None, tag=None):
        self.dbinstance_categories = dbinstance_categories  # type: list[str]
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_ids = dbinstance_ids  # type: str
        self.dbinstance_modes = dbinstance_modes  # type: list[str]
        self.dbinstance_statuses = dbinstance_statuses  # type: list[str]
        self.instance_deploy_types = instance_deploy_types  # type: list[str]
        self.instance_network_type = instance_network_type  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[DescribeDBInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_categories is not None:
            result['DBInstanceCategories'] = self.dbinstance_categories
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_modes is not None:
            result['DBInstanceModes'] = self.dbinstance_modes
        if self.dbinstance_statuses is not None:
            result['DBInstanceStatuses'] = self.dbinstance_statuses
        if self.instance_deploy_types is not None:
            result['InstanceDeployTypes'] = self.instance_deploy_types
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceCategories') is not None:
            self.dbinstance_categories = m.get('DBInstanceCategories')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceModes') is not None:
            self.dbinstance_modes = m.get('DBInstanceModes')
        if m.get('DBInstanceStatuses') is not None:
            self.dbinstance_statuses = m.get('DBInstanceStatuses')
        if m.get('InstanceDeployTypes') is not None:
            self.instance_deploy_types = m.get('InstanceDeployTypes')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesShrinkRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesShrinkRequestTag, self).to_map()
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


class DescribeDBInstancesShrinkRequest(TeaModel):
    def __init__(self, dbinstance_categories_shrink=None, dbinstance_description=None, dbinstance_ids=None,
                 dbinstance_modes_shrink=None, dbinstance_statuses_shrink=None, instance_deploy_types_shrink=None,
                 instance_network_type=None, owner_id=None, page_number=None, page_size=None, region_id=None, resource_group_id=None,
                 tag=None):
        self.dbinstance_categories_shrink = dbinstance_categories_shrink  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_ids = dbinstance_ids  # type: str
        self.dbinstance_modes_shrink = dbinstance_modes_shrink  # type: str
        self.dbinstance_statuses_shrink = dbinstance_statuses_shrink  # type: str
        self.instance_deploy_types_shrink = instance_deploy_types_shrink  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[DescribeDBInstancesShrinkRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_categories_shrink is not None:
            result['DBInstanceCategories'] = self.dbinstance_categories_shrink
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_modes_shrink is not None:
            result['DBInstanceModes'] = self.dbinstance_modes_shrink
        if self.dbinstance_statuses_shrink is not None:
            result['DBInstanceStatuses'] = self.dbinstance_statuses_shrink
        if self.instance_deploy_types_shrink is not None:
            result['InstanceDeployTypes'] = self.instance_deploy_types_shrink
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceCategories') is not None:
            self.dbinstance_categories_shrink = m.get('DBInstanceCategories')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceModes') is not None:
            self.dbinstance_modes_shrink = m.get('DBInstanceModes')
        if m.get('DBInstanceStatuses') is not None:
            self.dbinstance_statuses_shrink = m.get('DBInstanceStatuses')
        if m.get('InstanceDeployTypes') is not None:
            self.instance_deploy_types_shrink = m.get('InstanceDeployTypes')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag, self).to_map()
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


class DescribeDBInstancesResponseBodyItemsDBInstanceTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItemsDBInstanceTags, self).to_map()
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
                temp_model = DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyItemsDBInstance(TeaModel):
    def __init__(self, connection_mode=None, create_time=None, dbinstance_category=None,
                 dbinstance_description=None, dbinstance_id=None, dbinstance_mode=None, dbinstance_net_type=None, dbinstance_status=None,
                 engine=None, engine_version=None, expire_time=None, instance_deploy_type=None,
                 instance_network_type=None, lock_mode=None, lock_reason=None, master_node_num=None, pay_type=None, region_id=None,
                 resource_group_id=None, seg_node_num=None, storage_size=None, storage_type=None, tags=None, v_switch_id=None,
                 vpc_id=None, zone_id=None):
        self.connection_mode = connection_mode  # type: str
        self.create_time = create_time  # type: str
        self.dbinstance_category = dbinstance_category  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_mode = dbinstance_mode  # type: str
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.expire_time = expire_time  # type: str
        self.instance_deploy_type = instance_deploy_type  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.lock_mode = lock_mode  # type: str
        self.lock_reason = lock_reason  # type: str
        self.master_node_num = master_node_num  # type: int
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.seg_node_num = seg_node_num  # type: str
        self.storage_size = storage_size  # type: str
        self.storage_type = storage_type  # type: str
        self.tags = tags  # type: DescribeDBInstancesResponseBodyItemsDBInstanceTags
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItemsDBInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_deploy_type is not None:
            result['InstanceDeployType'] = self.instance_deploy_type
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceDeployType') is not None:
            self.instance_deploy_type = m.get('InstanceDeployType')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstancesResponseBodyItemsDBInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBodyItems(TeaModel):
    def __init__(self, dbinstance=None):
        self.dbinstance = dbinstance  # type: list[DescribeDBInstancesResponseBodyItemsDBInstance]

    def validate(self):
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k in self.dbinstance:
                result['DBInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k in m.get('DBInstance'):
                temp_model = DescribeDBInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeDBInstancesResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBInstancesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
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


class DescribeDataBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, backup_mode=None, backup_status=None, dbinstance_id=None, data_type=None,
                 end_time=None, page_number=None, page_size=None, start_time=None):
        self.backup_id = backup_id  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_status = backup_status  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.data_type = data_type  # type: str
        self.end_time = end_time  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataBackupsResponseBodyItems(TeaModel):
    def __init__(self, backup_end_time=None, backup_end_time_local=None, backup_mode=None, backup_set_id=None,
                 backup_size=None, backup_start_time=None, backup_start_time_local=None, backup_status=None, bakset_name=None,
                 consistent_time=None, dbinstance_id=None, data_type=None):
        self.backup_end_time = backup_end_time  # type: str
        self.backup_end_time_local = backup_end_time_local  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_set_id = backup_set_id  # type: str
        self.backup_size = backup_size  # type: long
        self.backup_start_time = backup_start_time  # type: str
        self.backup_start_time_local = backup_start_time_local  # type: str
        self.backup_status = backup_status  # type: str
        self.bakset_name = bakset_name  # type: str
        self.consistent_time = consistent_time  # type: long
        self.dbinstance_id = dbinstance_id  # type: str
        self.data_type = data_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataBackupsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_end_time_local is not None:
            result['BackupEndTimeLocal'] = self.backup_end_time_local
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_start_time_local is not None:
            result['BackupStartTimeLocal'] = self.backup_start_time_local
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.bakset_name is not None:
            result['BaksetName'] = self.bakset_name
        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupEndTimeLocal') is not None:
            self.backup_end_time_local = m.get('BackupEndTimeLocal')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStartTimeLocal') is not None:
            self.backup_start_time_local = m.get('BackupStartTimeLocal')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BaksetName') is not None:
            self.bakset_name = m.get('BaksetName')
        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        return self


class DescribeDataBackupsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.items = items  # type: list[DescribeDataBackupsResponseBodyItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataBackupsResponseBody, self).to_map()
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataBackupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataBackupsResponse, self).to_map()
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
            temp_model = DescribeDataBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataShareInstancesRequest(TeaModel):
    def __init__(self, owner_id=None, page_number=None, page_size=None, region_id=None, search_value=None):
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.search_value = search_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataShareInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        return self


class DescribeDataShareInstancesResponseBodyItemsDBInstance(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_mode=None, data_share_status=None, description=None,
                 region_id=None, zone_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_mode = dbinstance_mode  # type: str
        self.data_share_status = data_share_status  # type: str
        self.description = description  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataShareInstancesResponseBodyItemsDBInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode
        if self.data_share_status is not None:
            result['DataShareStatus'] = self.data_share_status
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')
        if m.get('DataShareStatus') is not None:
            self.data_share_status = m.get('DataShareStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDataShareInstancesResponseBodyItems(TeaModel):
    def __init__(self, dbinstance=None):
        self.dbinstance = dbinstance  # type: list[DescribeDataShareInstancesResponseBodyItemsDBInstance]

    def validate(self):
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataShareInstancesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k in self.dbinstance:
                result['DBInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k in m.get('DBInstance'):
                temp_model = DescribeDataShareInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        return self


class DescribeDataShareInstancesResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeDataShareInstancesResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDataShareInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDataShareInstancesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeDataShareInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataShareInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataShareInstancesResponse, self).to_map()
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
            temp_model = DescribeDataShareInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSharePerformanceRequest(TeaModel):
    def __init__(self, end_time=None, key=None, region_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataSharePerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataSharePerformanceResponseBodyPerformanceKeysSeriesValues(TeaModel):
    def __init__(self, point=None):
        self.point = point  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataSharePerformanceResponseBodyPerformanceKeysSeriesValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeDataSharePerformanceResponseBodyPerformanceKeysSeries(TeaModel):
    def __init__(self, name=None, values=None):
        self.name = name  # type: str
        self.values = values  # type: list[DescribeDataSharePerformanceResponseBodyPerformanceKeysSeriesValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataSharePerformanceResponseBodyPerformanceKeysSeries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeDataSharePerformanceResponseBodyPerformanceKeysSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeDataSharePerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(self, name=None, series=None, unit=None):
        self.name = name  # type: str
        self.series = series  # type: list[DescribeDataSharePerformanceResponseBodyPerformanceKeysSeries]
        self.unit = unit  # type: str

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataSharePerformanceResponseBodyPerformanceKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDataSharePerformanceResponseBodyPerformanceKeysSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDataSharePerformanceResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, performance_keys=None, request_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.performance_keys = performance_keys  # type: list[DescribeDataSharePerformanceResponseBodyPerformanceKeys]
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.performance_keys:
            for k in self.performance_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataSharePerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['PerformanceKeys'] = []
        if self.performance_keys is not None:
            for k in self.performance_keys:
                result['PerformanceKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.performance_keys = []
        if m.get('PerformanceKeys') is not None:
            for k in m.get('PerformanceKeys'):
                temp_model = DescribeDataSharePerformanceResponseBodyPerformanceKeys()
                self.performance_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataSharePerformanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataSharePerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataSharePerformanceResponse, self).to_map()
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
            temp_model = DescribeDataSharePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisDimensionsRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisDimensionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDiagnosisDimensionsResponseBody(TeaModel):
    def __init__(self, databases=None, request_id=None, user_names=None):
        self.databases = databases  # type: list[str]
        self.request_id = request_id  # type: str
        self.user_names = user_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisDimensionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.databases is not None:
            result['Databases'] = self.databases
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_names is not None:
            result['UserNames'] = self.user_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Databases') is not None:
            self.databases = m.get('Databases')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')
        return self


class DescribeDiagnosisDimensionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiagnosisDimensionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiagnosisDimensionsResponse, self).to_map()
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
            temp_model = DescribeDiagnosisDimensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisMonitorPerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, query_condition=None, start_time=None,
                 user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.query_condition = query_condition  # type: str
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisMonitorPerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisMonitorPerformanceResponseBodyPerformances(TeaModel):
    def __init__(self, cost=None, database=None, query_id=None, start_time=None, status=None, user=None):
        self.cost = cost  # type: int
        self.database = database  # type: str
        self.query_id = query_id  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisMonitorPerformanceResponseBodyPerformances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.database is not None:
            result['Database'] = self.database
        if self.query_id is not None:
            result['QueryID'] = self.query_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisMonitorPerformanceResponseBody(TeaModel):
    def __init__(self, performances=None, performances_threshold=None, performances_truncated=None,
                 request_id=None):
        self.performances = performances  # type: list[DescribeDiagnosisMonitorPerformanceResponseBodyPerformances]
        self.performances_threshold = performances_threshold  # type: int
        self.performances_truncated = performances_truncated  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiagnosisMonitorPerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        if self.performances_threshold is not None:
            result['PerformancesThreshold'] = self.performances_threshold
        if self.performances_truncated is not None:
            result['PerformancesTruncated'] = self.performances_truncated
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDiagnosisMonitorPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        if m.get('PerformancesThreshold') is not None:
            self.performances_threshold = m.get('PerformancesThreshold')
        if m.get('PerformancesTruncated') is not None:
            self.performances_truncated = m.get('PerformancesTruncated')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDiagnosisMonitorPerformanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiagnosisMonitorPerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiagnosisMonitorPerformanceResponse, self).to_map()
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
            temp_model = DescribeDiagnosisMonitorPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, keyword=None, order=None, page_number=None,
                 page_size=None, query_condition=None, start_time=None, user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.keyword = keyword  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_condition = query_condition  # type: str
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisRecordsResponseBodyItems(TeaModel):
    def __init__(self, database=None, duration=None, query_id=None, sqlstmt=None, sqltruncated=None,
                 sqltruncated_threshold=None, session_id=None, start_time=None, status=None, user=None):
        self.database = database  # type: str
        self.duration = duration  # type: int
        self.query_id = query_id  # type: str
        self.sqlstmt = sqlstmt  # type: str
        self.sqltruncated = sqltruncated  # type: bool
        self.sqltruncated_threshold = sqltruncated_threshold  # type: int
        self.session_id = session_id  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisRecordsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.query_id is not None:
            result['QueryID'] = self.query_id
        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt
        if self.sqltruncated is not None:
            result['SQLTruncated'] = self.sqltruncated
        if self.sqltruncated_threshold is not None:
            result['SQLTruncatedThreshold'] = self.sqltruncated_threshold
        if self.session_id is not None:
            result['SessionID'] = self.session_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')
        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')
        if m.get('SQLTruncated') is not None:
            self.sqltruncated = m.get('SQLTruncated')
        if m.get('SQLTruncatedThreshold') is not None:
            self.sqltruncated_threshold = m.get('SQLTruncatedThreshold')
        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisRecordsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, request_id=None, total_count=None):
        self.items = items  # type: list[DescribeDiagnosisRecordsResponseBodyItems]
        self.page_number = page_number  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiagnosisRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDiagnosisRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiagnosisRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiagnosisRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiagnosisRecordsResponse, self).to_map()
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
            temp_model = DescribeDiagnosisRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisSQLInfoRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, query_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.query_id = query_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisSQLInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.query_id is not None:
            result['QueryID'] = self.query_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')
        return self


class DescribeDiagnosisSQLInfoResponseBody(TeaModel):
    def __init__(self, database=None, duration=None, max_output_rows=None, query_id=None, query_plan=None,
                 request_id=None, sqlstmt=None, session_id=None, sorted_metrics=None, start_time=None, status=None,
                 text_plan=None, user=None):
        self.database = database  # type: str
        self.duration = duration  # type: int
        self.max_output_rows = max_output_rows  # type: str
        self.query_id = query_id  # type: str
        self.query_plan = query_plan  # type: str
        self.request_id = request_id  # type: str
        self.sqlstmt = sqlstmt  # type: str
        self.session_id = session_id  # type: str
        self.sorted_metrics = sorted_metrics  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.text_plan = text_plan  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisSQLInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.max_output_rows is not None:
            result['MaxOutputRows'] = self.max_output_rows
        if self.query_id is not None:
            result['QueryID'] = self.query_id
        if self.query_plan is not None:
            result['QueryPlan'] = self.query_plan
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sqlstmt is not None:
            result['SQLStmt'] = self.sqlstmt
        if self.session_id is not None:
            result['SessionID'] = self.session_id
        if self.sorted_metrics is not None:
            result['SortedMetrics'] = self.sorted_metrics
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.text_plan is not None:
            result['TextPlan'] = self.text_plan
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MaxOutputRows') is not None:
            self.max_output_rows = m.get('MaxOutputRows')
        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')
        if m.get('QueryPlan') is not None:
            self.query_plan = m.get('QueryPlan')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SQLStmt') is not None:
            self.sqlstmt = m.get('SQLStmt')
        if m.get('SessionID') is not None:
            self.session_id = m.get('SessionID')
        if m.get('SortedMetrics') is not None:
            self.sorted_metrics = m.get('SortedMetrics')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TextPlan') is not None:
            self.text_plan = m.get('TextPlan')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeDiagnosisSQLInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiagnosisSQLInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiagnosisSQLInfoResponse, self).to_map()
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
            temp_model = DescribeDiagnosisSQLInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDownloadRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDownloadRecordsResponseBodyRecords(TeaModel):
    def __init__(self, download_id=None, download_url=None, exception_msg=None, file_name=None, status=None):
        self.download_id = download_id  # type: long
        self.download_url = download_url  # type: str
        self.exception_msg = exception_msg  # type: str
        self.file_name = file_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDownloadRecordsResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDownloadRecordsResponseBody(TeaModel):
    def __init__(self, records=None, request_id=None):
        self.records = records  # type: list[DescribeDownloadRecordsResponseBodyRecords]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDownloadRecordsResponseBody, self).to_map()
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
                temp_model = DescribeDownloadRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDownloadRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDownloadRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDownloadRecordsResponse, self).to_map()
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
            temp_model = DescribeDownloadRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthStatusRequest(TeaModel):
    def __init__(self, dbinstance_id=None, key=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusAdbpgStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusAdbpgStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusNodeMasterStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusNodeMasterStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus(TeaModel):
    def __init__(self, status=None, value=None):
        self.status = status  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeHealthStatusResponseBodyStatus(TeaModel):
    def __init__(self, adbgp_segment_disk_usage_percent_max=None, adbpg_connection_status=None,
                 adbpg_disk_status=None, adbpg_disk_usage_percent=None, adbpg_master_disk_usage_percent_max=None,
                 adbpg_master_status=None, adbpg_segment_status=None, adbpg_status=None, node_master_connection_status=None,
                 node_master_status=None, node_segment_connection_status=None, node_segment_disk_status=None):
        self.adbgp_segment_disk_usage_percent_max = adbgp_segment_disk_usage_percent_max  # type: DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax
        self.adbpg_connection_status = adbpg_connection_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus
        self.adbpg_disk_status = adbpg_disk_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus
        self.adbpg_disk_usage_percent = adbpg_disk_usage_percent  # type: DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent
        self.adbpg_master_disk_usage_percent_max = adbpg_master_disk_usage_percent_max  # type: DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax
        self.adbpg_master_status = adbpg_master_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus
        self.adbpg_segment_status = adbpg_segment_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus
        self.adbpg_status = adbpg_status  # type: DescribeHealthStatusResponseBodyStatusAdbpgStatus
        self.node_master_connection_status = node_master_connection_status  # type: DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus
        self.node_master_status = node_master_status  # type: DescribeHealthStatusResponseBodyStatusNodeMasterStatus
        self.node_segment_connection_status = node_segment_connection_status  # type: DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus
        self.node_segment_disk_status = node_segment_disk_status  # type: DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus

    def validate(self):
        if self.adbgp_segment_disk_usage_percent_max:
            self.adbgp_segment_disk_usage_percent_max.validate()
        if self.adbpg_connection_status:
            self.adbpg_connection_status.validate()
        if self.adbpg_disk_status:
            self.adbpg_disk_status.validate()
        if self.adbpg_disk_usage_percent:
            self.adbpg_disk_usage_percent.validate()
        if self.adbpg_master_disk_usage_percent_max:
            self.adbpg_master_disk_usage_percent_max.validate()
        if self.adbpg_master_status:
            self.adbpg_master_status.validate()
        if self.adbpg_segment_status:
            self.adbpg_segment_status.validate()
        if self.adbpg_status:
            self.adbpg_status.validate()
        if self.node_master_connection_status:
            self.node_master_connection_status.validate()
        if self.node_master_status:
            self.node_master_status.validate()
        if self.node_segment_connection_status:
            self.node_segment_connection_status.validate()
        if self.node_segment_disk_status:
            self.node_segment_disk_status.validate()

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBodyStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adbgp_segment_disk_usage_percent_max is not None:
            result['adbgp_segment_disk_usage_percent_max'] = self.adbgp_segment_disk_usage_percent_max.to_map()
        if self.adbpg_connection_status is not None:
            result['adbpg_connection_status'] = self.adbpg_connection_status.to_map()
        if self.adbpg_disk_status is not None:
            result['adbpg_disk_status'] = self.adbpg_disk_status.to_map()
        if self.adbpg_disk_usage_percent is not None:
            result['adbpg_disk_usage_percent'] = self.adbpg_disk_usage_percent.to_map()
        if self.adbpg_master_disk_usage_percent_max is not None:
            result['adbpg_master_disk_usage_percent_max'] = self.adbpg_master_disk_usage_percent_max.to_map()
        if self.adbpg_master_status is not None:
            result['adbpg_master_status'] = self.adbpg_master_status.to_map()
        if self.adbpg_segment_status is not None:
            result['adbpg_segment_status'] = self.adbpg_segment_status.to_map()
        if self.adbpg_status is not None:
            result['adbpg_status'] = self.adbpg_status.to_map()
        if self.node_master_connection_status is not None:
            result['node_master_connection_status'] = self.node_master_connection_status.to_map()
        if self.node_master_status is not None:
            result['node_master_status'] = self.node_master_status.to_map()
        if self.node_segment_connection_status is not None:
            result['node_segment_connection_status'] = self.node_segment_connection_status.to_map()
        if self.node_segment_disk_status is not None:
            result['node_segment_disk_status'] = self.node_segment_disk_status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adbgp_segment_disk_usage_percent_max') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbgpSegmentDiskUsagePercentMax()
            self.adbgp_segment_disk_usage_percent_max = temp_model.from_map(m['adbgp_segment_disk_usage_percent_max'])
        if m.get('adbpg_connection_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgConnectionStatus()
            self.adbpg_connection_status = temp_model.from_map(m['adbpg_connection_status'])
        if m.get('adbpg_disk_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgDiskStatus()
            self.adbpg_disk_status = temp_model.from_map(m['adbpg_disk_status'])
        if m.get('adbpg_disk_usage_percent') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgDiskUsagePercent()
            self.adbpg_disk_usage_percent = temp_model.from_map(m['adbpg_disk_usage_percent'])
        if m.get('adbpg_master_disk_usage_percent_max') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgMasterDiskUsagePercentMax()
            self.adbpg_master_disk_usage_percent_max = temp_model.from_map(m['adbpg_master_disk_usage_percent_max'])
        if m.get('adbpg_master_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgMasterStatus()
            self.adbpg_master_status = temp_model.from_map(m['adbpg_master_status'])
        if m.get('adbpg_segment_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgSegmentStatus()
            self.adbpg_segment_status = temp_model.from_map(m['adbpg_segment_status'])
        if m.get('adbpg_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusAdbpgStatus()
            self.adbpg_status = temp_model.from_map(m['adbpg_status'])
        if m.get('node_master_connection_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusNodeMasterConnectionStatus()
            self.node_master_connection_status = temp_model.from_map(m['node_master_connection_status'])
        if m.get('node_master_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusNodeMasterStatus()
            self.node_master_status = temp_model.from_map(m['node_master_status'])
        if m.get('node_segment_connection_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusNodeSegmentConnectionStatus()
            self.node_segment_connection_status = temp_model.from_map(m['node_segment_connection_status'])
        if m.get('node_segment_disk_status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatusNodeSegmentDiskStatus()
            self.node_segment_disk_status = temp_model.from_map(m['node_segment_disk_status'])
        return self


class DescribeHealthStatusResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, request_id=None, status=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: DescribeHealthStatusResponseBodyStatus

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(DescribeHealthStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = DescribeHealthStatusResponseBodyStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class DescribeHealthStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHealthStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHealthStatusResponse, self).to_map()
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
            temp_model = DescribeHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogBackupsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, page_number=None, page_size=None, start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeLogBackupsResponseBodyItems(TeaModel):
    def __init__(self, backup_id=None, dbinstance_id=None, log_file_name=None, log_file_size=None, log_time=None,
                 segment_name=None):
        self.backup_id = backup_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.log_file_name = log_file_name  # type: str
        self.log_file_size = log_file_size  # type: long
        self.log_time = log_time  # type: str
        self.segment_name = segment_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogBackupsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.log_file_name is not None:
            result['LogFileName'] = self.log_file_name
        if self.log_file_size is not None:
            result['LogFileSize'] = self.log_file_size
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.segment_name is not None:
            result['SegmentName'] = self.segment_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('LogFileName') is not None:
            self.log_file_name = m.get('LogFileName')
        if m.get('LogFileSize') is not None:
            self.log_file_size = m.get('LogFileSize')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('SegmentName') is not None:
            self.segment_name = m.get('SegmentName')
        return self


class DescribeLogBackupsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_count=None,
                 total_log_size=None):
        self.items = items  # type: list[DescribeLogBackupsResponseBodyItems]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.total_log_size = total_log_size  # type: long

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogBackupsResponseBody, self).to_map()
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_log_size is not None:
            result['TotalLogSize'] = self.total_log_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeLogBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalLogSize') is not None:
            self.total_log_size = m.get('TotalLogSize')
        return self


class DescribeLogBackupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogBackupsResponse, self).to_map()
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
            temp_model = DescribeLogBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModifyParameterLogRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeModifyParameterLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeModifyParameterLogResponseBodyChangelogs(TeaModel):
    def __init__(self, effect_time=None, parameter_name=None, parameter_valid=None, parameter_value_after=None,
                 parameter_value_before=None):
        self.effect_time = effect_time  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_valid = parameter_valid  # type: str
        self.parameter_value_after = parameter_value_after  # type: str
        self.parameter_value_before = parameter_value_before  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeModifyParameterLogResponseBodyChangelogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_valid is not None:
            result['ParameterValid'] = self.parameter_valid
        if self.parameter_value_after is not None:
            result['ParameterValueAfter'] = self.parameter_value_after
        if self.parameter_value_before is not None:
            result['ParameterValueBefore'] = self.parameter_value_before
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValid') is not None:
            self.parameter_valid = m.get('ParameterValid')
        if m.get('ParameterValueAfter') is not None:
            self.parameter_value_after = m.get('ParameterValueAfter')
        if m.get('ParameterValueBefore') is not None:
            self.parameter_value_before = m.get('ParameterValueBefore')
        return self


class DescribeModifyParameterLogResponseBody(TeaModel):
    def __init__(self, changelogs=None, request_id=None):
        self.changelogs = changelogs  # type: list[DescribeModifyParameterLogResponseBodyChangelogs]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.changelogs:
            for k in self.changelogs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeModifyParameterLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Changelogs'] = []
        if self.changelogs is not None:
            for k in self.changelogs:
                result['Changelogs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.changelogs = []
        if m.get('Changelogs') is not None:
            for k in m.get('Changelogs'):
                temp_model = DescribeModifyParameterLogResponseBodyChangelogs()
                self.changelogs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeModifyParameterLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeModifyParameterLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeModifyParameterLogResponse, self).to_map()
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
            temp_model = DescribeModifyParameterLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeParametersResponseBodyParameters(TeaModel):
    def __init__(self, current_value=None, force_restart_instance=None, is_changeable_config=None,
                 optional_range=None, parameter_description=None, parameter_name=None, parameter_value=None):
        self.current_value = current_value  # type: str
        self.force_restart_instance = force_restart_instance  # type: str
        self.is_changeable_config = is_changeable_config  # type: str
        self.optional_range = optional_range  # type: str
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.force_restart_instance is not None:
            result['ForceRestartInstance'] = self.force_restart_instance
        if self.is_changeable_config is not None:
            result['IsChangeableConfig'] = self.is_changeable_config
        if self.optional_range is not None:
            result['OptionalRange'] = self.optional_range
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('ForceRestartInstance') is not None:
            self.force_restart_instance = m.get('ForceRestartInstance')
        if m.get('IsChangeableConfig') is not None:
            self.is_changeable_config = m.get('IsChangeableConfig')
        if m.get('OptionalRange') is not None:
            self.optional_range = m.get('OptionalRange')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(self, parameters=None, request_id=None):
        self.parameters = parameters  # type: list[DescribeParametersResponseBodyParameters]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParametersResponse, self).to_map()
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
            temp_model = DescribeParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdsVSwitchsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, vpc_id=None, zone_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRdsVSwitchsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(self, ali_uid=None, bid=None, cidr_block=None, gmt_create=None, gmt_modified=None, is_default=None,
                 iz_no=None, region_no=None, status=None, v_switch_id=None, v_switch_name=None):
        self.ali_uid = ali_uid  # type: str
        self.bid = bid  # type: str
        self.cidr_block = cidr_block  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.is_default = is_default  # type: bool
        self.iz_no = iz_no  # type: str
        self.region_no = region_no  # type: str
        self.status = status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.v_switch_name = v_switch_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.iz_no is not None:
            result['IzNo'] = self.iz_no
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeRdsVSwitchsResponseBodyVSwitches(TeaModel):
    def __init__(self, v_switch=None):
        self.v_switch = v_switch  # type: list[DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch]

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRdsVSwitchsResponseBodyVSwitches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeRdsVSwitchsResponseBody(TeaModel):
    def __init__(self, request_id=None, v_switches=None):
        self.request_id = request_id  # type: str
        self.v_switches = v_switches  # type: DescribeRdsVSwitchsResponseBodyVSwitches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        _map = super(DescribeRdsVSwitchsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitches') is not None:
            temp_model = DescribeRdsVSwitchsResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeRdsVSwitchsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRdsVSwitchsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRdsVSwitchsResponse, self).to_map()
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
            temp_model = DescribeRdsVSwitchsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdsVpcsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, zone_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRdsVpcsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs(TeaModel):
    def __init__(self, cidr_block=None, gmt_create=None, gmt_modified=None, is_default=None, iz_no=None, status=None,
                 v_switch_id=None, v_switch_name=None):
        self.cidr_block = cidr_block  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.is_default = is_default  # type: bool
        self.iz_no = iz_no  # type: str
        self.status = status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.v_switch_name = v_switch_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.iz_no is not None:
            result['IzNo'] = self.iz_no
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeRdsVpcsResponseBodyVpcsVpc(TeaModel):
    def __init__(self, ali_uid=None, bid=None, cidr_block=None, gmt_create=None, gmt_modified=None, is_default=None,
                 region_no=None, status=None, v_switchs=None, vpc_id=None, vpc_name=None):
        self.ali_uid = ali_uid  # type: str
        self.bid = bid  # type: str
        self.cidr_block = cidr_block  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.is_default = is_default  # type: bool
        self.region_no = region_no  # type: str
        self.status = status  # type: str
        self.v_switchs = v_switchs  # type: list[DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs]
        self.vpc_id = vpc_id  # type: str
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.v_switchs:
            for k in self.v_switchs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRdsVpcsResponseBodyVpcsVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.status is not None:
            result['Status'] = self.status
        result['VSwitchs'] = []
        if self.v_switchs is not None:
            for k in self.v_switchs:
                result['VSwitchs'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.v_switchs = []
        if m.get('VSwitchs') is not None:
            for k in m.get('VSwitchs'):
                temp_model = DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs()
                self.v_switchs.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeRdsVpcsResponseBodyVpcs(TeaModel):
    def __init__(self, vpc=None):
        self.vpc = vpc  # type: list[DescribeRdsVpcsResponseBodyVpcsVpc]

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRdsVpcsResponseBodyVpcs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeRdsVpcsResponseBodyVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeRdsVpcsResponseBody(TeaModel):
    def __init__(self, request_id=None, vpcs=None):
        self.request_id = request_id  # type: str
        self.vpcs = vpcs  # type: DescribeRdsVpcsResponseBodyVpcs

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        _map = super(DescribeRdsVpcsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vpcs') is not None:
            temp_model = DescribeRdsVpcsResponseBodyVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        return self


class DescribeRdsVpcsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRdsVpcsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRdsVpcsResponse, self).to_map()
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
            temp_model = DescribeRdsVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(self, vpc_enabled=None, zone_id=None):
        self.vpc_enabled = vpc_enabled  # type: bool
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegionZonesZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone  # type: list[DescribeRegionsResponseBodyRegionsRegionZonesZone]

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegionZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, region_id=None, zones=None):
        self.region_id = region_id  # type: str
        self.zones = zones  # type: DescribeRegionsResponseBodyRegionsRegionZones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
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


class DescribeResourceUsageRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeResourceUsageResponseBody(TeaModel):
    def __init__(self, backup_size=None, dbinstance_id=None, data_size=None, disk_used=None, engine=None,
                 log_size=None, request_id=None):
        self.backup_size = backup_size  # type: long
        self.dbinstance_id = dbinstance_id  # type: str
        self.data_size = data_size  # type: long
        self.disk_used = disk_used  # type: long
        self.engine = engine  # type: str
        self.log_size = log_size  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.disk_used is not None:
            result['DiskUsed'] = self.disk_used
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DiskUsed') is not None:
            self.disk_used = m.get('DiskUsed')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeResourceUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResourceUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResourceUsageResponse, self).to_map()
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
            temp_model = DescribeResourceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLCollectorPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLCollectorPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeSQLCollectorPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, sqlcollector_status=None):
        self.request_id = request_id  # type: str
        self.sqlcollector_status = sqlcollector_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLCollectorPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sqlcollector_status is not None:
            result['SQLCollectorStatus'] = self.sqlcollector_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SQLCollectorStatus') is not None:
            self.sqlcollector_status = m.get('SQLCollectorStatus')
        return self


class DescribeSQLCollectorPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLCollectorPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLCollectorPolicyResponse, self).to_map()
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
            temp_model = DescribeSQLCollectorPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogByQueryIdRequest(TeaModel):
    def __init__(self, dbinstance_id=None, query_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.query_id = query_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogByQueryIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class DescribeSQLLogByQueryIdResponseBodyItems(TeaModel):
    def __init__(self, account_name=None, dbname=None, dbrole=None, execute_cost=None, execute_state=None,
                 operation_class=None, operation_execute_time=None, operation_type=None, query_id=None, return_row_counts=None,
                 sqlplan=None, sqltext=None, scan_row_counts=None, slice_ids=None, source_ip=None, source_port=None):
        self.account_name = account_name  # type: str
        self.dbname = dbname  # type: str
        self.dbrole = dbrole  # type: str
        self.execute_cost = execute_cost  # type: float
        self.execute_state = execute_state  # type: str
        self.operation_class = operation_class  # type: str
        self.operation_execute_time = operation_execute_time  # type: str
        self.operation_type = operation_type  # type: str
        self.query_id = query_id  # type: str
        self.return_row_counts = return_row_counts  # type: long
        self.sqlplan = sqlplan  # type: str
        self.sqltext = sqltext  # type: str
        self.scan_row_counts = scan_row_counts  # type: long
        self.slice_ids = slice_ids  # type: list[str]
        self.source_ip = source_ip  # type: str
        self.source_port = source_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogByQueryIdResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.dbrole is not None:
            result['DBRole'] = self.dbrole
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqlplan is not None:
            result['SQLPlan'] = self.sqlplan
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts
        if self.slice_ids is not None:
            result['SliceIds'] = self.slice_ids
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DBRole') is not None:
            self.dbrole = m.get('DBRole')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLPlan') is not None:
            self.sqlplan = m.get('SQLPlan')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')
        if m.get('SliceIds') is not None:
            self.slice_ids = m.get('SliceIds')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        return self


class DescribeSQLLogByQueryIdResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: list[DescribeSQLLogByQueryIdResponseBodyItems]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogByQueryIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSQLLogByQueryIdResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSQLLogByQueryIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLLogByQueryIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLLogByQueryIdResponse, self).to_map()
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
            temp_model = DescribeSQLLogByQueryIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogCountRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, execute_cost=None, execute_state=None,
                 max_execute_cost=None, min_execute_cost=None, operation_class=None, operation_type=None, query_keywords=None,
                 source_ip=None, start_time=None, user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.execute_cost = execute_cost  # type: str
        self.execute_state = execute_state  # type: str
        self.max_execute_cost = max_execute_cost  # type: str
        self.min_execute_cost = min_execute_cost  # type: str
        self.operation_class = operation_class  # type: str
        self.operation_type = operation_type  # type: str
        self.query_keywords = query_keywords  # type: str
        self.source_ip = source_ip  # type: str
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLLogCountResponseBodyItemsSeriesValues(TeaModel):
    def __init__(self, point=None):
        self.point = point  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogCountResponseBodyItemsSeriesValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeSQLLogCountResponseBodyItemsSeries(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[DescribeSQLLogCountResponseBodyItemsSeriesValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogCountResponseBodyItemsSeries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeSQLLogCountResponseBodyItemsSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeSQLLogCountResponseBodyItems(TeaModel):
    def __init__(self, name=None, series=None):
        self.name = name  # type: str
        self.series = series  # type: list[DescribeSQLLogCountResponseBodyItemsSeries]

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogCountResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeSQLLogCountResponseBodyItemsSeries()
                self.series.append(temp_model.from_map(k))
        return self


class DescribeSQLLogCountResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, end_time=None, items=None, request_id=None, start_time=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.end_time = end_time  # type: str
        self.items = items  # type: list[DescribeSQLLogCountResponseBodyItems]
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSQLLogCountResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSQLLogCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLLogCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLLogCountResponse, self).to_map()
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
            temp_model = DescribeSQLLogCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogFilesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, file_name=None, page_number=None, page_size=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.file_name = file_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSQLLogFilesResponseBodyItemsLogFile(TeaModel):
    def __init__(self, file_id=None, log_download_url=None, log_end_time=None, log_size=None, log_start_time=None,
                 log_status=None):
        self.file_id = file_id  # type: str
        self.log_download_url = log_download_url  # type: str
        self.log_end_time = log_end_time  # type: str
        self.log_size = log_size  # type: str
        self.log_start_time = log_start_time  # type: str
        self.log_status = log_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogFilesResponseBodyItemsLogFile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileID'] = self.file_id
        if self.log_download_url is not None:
            result['LogDownloadURL'] = self.log_download_url
        if self.log_end_time is not None:
            result['LogEndTime'] = self.log_end_time
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.log_start_time is not None:
            result['LogStartTime'] = self.log_start_time
        if self.log_status is not None:
            result['LogStatus'] = self.log_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        if m.get('LogDownloadURL') is not None:
            self.log_download_url = m.get('LogDownloadURL')
        if m.get('LogEndTime') is not None:
            self.log_end_time = m.get('LogEndTime')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('LogStartTime') is not None:
            self.log_start_time = m.get('LogStartTime')
        if m.get('LogStatus') is not None:
            self.log_status = m.get('LogStatus')
        return self


class DescribeSQLLogFilesResponseBodyItems(TeaModel):
    def __init__(self, log_file=None):
        self.log_file = log_file  # type: list[DescribeSQLLogFilesResponseBodyItemsLogFile]

    def validate(self):
        if self.log_file:
            for k in self.log_file:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogFilesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogFile'] = []
        if self.log_file is not None:
            for k in self.log_file:
                result['LogFile'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_file = []
        if m.get('LogFile') is not None:
            for k in m.get('LogFile'):
                temp_model = DescribeSQLLogFilesResponseBodyItemsLogFile()
                self.log_file.append(temp_model.from_map(k))
        return self


class DescribeSQLLogFilesResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeSQLLogFilesResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeSQLLogFilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeSQLLogFilesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSQLLogFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLLogFilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLLogFilesResponse, self).to_map()
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
            temp_model = DescribeSQLLogFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, form=None, page_number=None, page_size=None,
                 query_keywords=None, start_time=None, user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.form = form  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_keywords = query_keywords  # type: str
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.form is not None:
            result['Form'] = self.form
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLLogRecordsResponseBodyItemsSQLRecord(TeaModel):
    def __init__(self, account_name=None, dbname=None, execute_time=None, host_address=None, return_row_counts=None,
                 sqltext=None, thread_id=None, total_execution_times=None):
        self.account_name = account_name  # type: str
        self.dbname = dbname  # type: str
        self.execute_time = execute_time  # type: str
        self.host_address = host_address  # type: str
        self.return_row_counts = return_row_counts  # type: long
        self.sqltext = sqltext  # type: str
        self.thread_id = thread_id  # type: str
        self.total_execution_times = total_execution_times  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogRecordsResponseBodyItemsSQLRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.thread_id is not None:
            result['ThreadID'] = self.thread_id
        if self.total_execution_times is not None:
            result['TotalExecutionTimes'] = self.total_execution_times
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ThreadID') is not None:
            self.thread_id = m.get('ThreadID')
        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')
        return self


class DescribeSQLLogRecordsResponseBodyItems(TeaModel):
    def __init__(self, sqlrecord=None):
        self.sqlrecord = sqlrecord  # type: list[DescribeSQLLogRecordsResponseBodyItemsSQLRecord]

    def validate(self):
        if self.sqlrecord:
            for k in self.sqlrecord:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogRecordsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SQLRecord'] = []
        if self.sqlrecord is not None:
            for k in self.sqlrecord:
                result['SQLRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sqlrecord = []
        if m.get('SQLRecord') is not None:
            for k in m.get('SQLRecord'):
                temp_model = DescribeSQLLogRecordsResponseBodyItemsSQLRecord()
                self.sqlrecord.append(temp_model.from_map(k))
        return self


class DescribeSQLLogRecordsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: DescribeSQLLogRecordsResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeSQLLogRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeSQLLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSQLLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLLogRecordsResponse, self).to_map()
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
            temp_model = DescribeSQLLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, execute_cost=None, execute_state=None,
                 max_execute_cost=None, min_execute_cost=None, operation_class=None, operation_type=None, page_number=None,
                 page_size=None, query_keywords=None, source_ip=None, start_time=None, user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.execute_cost = execute_cost  # type: str
        self.execute_state = execute_state  # type: str
        self.max_execute_cost = max_execute_cost  # type: str
        self.min_execute_cost = min_execute_cost  # type: str
        self.operation_class = operation_class  # type: str
        self.operation_type = operation_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_keywords = query_keywords  # type: str
        self.source_ip = source_ip  # type: str
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSQLLogsResponseBodyItems(TeaModel):
    def __init__(self, account_name=None, dbname=None, dbrole=None, execute_cost=None, execute_state=None,
                 operation_class=None, operation_execute_time=None, operation_type=None, return_row_counts=None, sqlplan=None,
                 sqltext=None, scan_row_counts=None, source_ip=None, source_port=None):
        self.account_name = account_name  # type: str
        self.dbname = dbname  # type: str
        self.dbrole = dbrole  # type: str
        self.execute_cost = execute_cost  # type: float
        self.execute_state = execute_state  # type: str
        self.operation_class = operation_class  # type: str
        self.operation_execute_time = operation_execute_time  # type: str
        self.operation_type = operation_type  # type: str
        self.return_row_counts = return_row_counts  # type: long
        self.sqlplan = sqlplan  # type: str
        self.sqltext = sqltext  # type: str
        self.scan_row_counts = scan_row_counts  # type: long
        self.source_ip = source_ip  # type: str
        self.source_port = source_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.dbrole is not None:
            result['DBRole'] = self.dbrole
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqlplan is not None:
            result['SQLPlan'] = self.sqlplan
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DBRole') is not None:
            self.dbrole = m.get('DBRole')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLPlan') is not None:
            self.sqlplan = m.get('SQLPlan')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        return self


class DescribeSQLLogsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None):
        self.items = items  # type: list[DescribeSQLLogsResponseBodyItems]
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSQLLogsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSQLLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLLogsResponse, self).to_map()
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
            temp_model = DescribeSQLLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogsOnSliceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, execute_state=None, max_execute_cost=None, min_execute_cost=None,
                 page_number=None, page_size=None, query_id=None, slice_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.execute_state = execute_state  # type: str
        self.max_execute_cost = max_execute_cost  # type: str
        self.min_execute_cost = min_execute_cost  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_id = query_id  # type: str
        self.slice_id = slice_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogsOnSliceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.slice_id is not None:
            result['SliceId'] = self.slice_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('SliceId') is not None:
            self.slice_id = m.get('SliceId')
        return self


class DescribeSQLLogsOnSliceResponseBodySliceLogItems(TeaModel):
    def __init__(self, execute_cost=None, execute_status=None, operation_execute_end_time=None,
                 operation_execute_time=None, peak_memory=None, return_row_counts=None, segment_id=None, segment_name=None):
        self.execute_cost = execute_cost  # type: float
        self.execute_status = execute_status  # type: str
        self.operation_execute_end_time = operation_execute_end_time  # type: str
        self.operation_execute_time = operation_execute_time  # type: str
        self.peak_memory = peak_memory  # type: float
        self.return_row_counts = return_row_counts  # type: long
        self.segment_id = segment_id  # type: str
        self.segment_name = segment_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSQLLogsOnSliceResponseBodySliceLogItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_status is not None:
            result['ExecuteStatus'] = self.execute_status
        if self.operation_execute_end_time is not None:
            result['OperationExecuteEndTime'] = self.operation_execute_end_time
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.segment_id is not None:
            result['SegmentId'] = self.segment_id
        if self.segment_name is not None:
            result['SegmentName'] = self.segment_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteStatus') is not None:
            self.execute_status = m.get('ExecuteStatus')
        if m.get('OperationExecuteEndTime') is not None:
            self.operation_execute_end_time = m.get('OperationExecuteEndTime')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SegmentId') is not None:
            self.segment_id = m.get('SegmentId')
        if m.get('SegmentName') is not None:
            self.segment_name = m.get('SegmentName')
        return self


class DescribeSQLLogsOnSliceResponseBody(TeaModel):
    def __init__(self, page_number=None, page_record_count=None, request_id=None, slice_log_items=None):
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.slice_log_items = slice_log_items  # type: list[DescribeSQLLogsOnSliceResponseBodySliceLogItems]

    def validate(self):
        if self.slice_log_items:
            for k in self.slice_log_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSQLLogsOnSliceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SliceLogItems'] = []
        if self.slice_log_items is not None:
            for k in self.slice_log_items:
                result['SliceLogItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.slice_log_items = []
        if m.get('SliceLogItems') is not None:
            for k in m.get('SliceLogItems'):
                temp_model = DescribeSQLLogsOnSliceResponseBodySliceLogItems()
                self.slice_log_items.append(temp_model.from_map(k))
        return self


class DescribeSQLLogsOnSliceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSQLLogsOnSliceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSQLLogsOnSliceResponse, self).to_map()
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
            temp_model = DescribeSQLLogsOnSliceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSampleDataRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSampleDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeSampleDataResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, has_sample_data=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.error_message = error_message  # type: str
        self.has_sample_data = has_sample_data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSampleDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.has_sample_data is not None:
            result['HasSampleData'] = self.has_sample_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HasSampleData') is not None:
            self.has_sample_data = m.get('HasSampleData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSampleDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSampleDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSampleDataResponse, self).to_map()
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
            temp_model = DescribeSampleDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, end_time=None, page_number=None, page_size=None, sqlid=None,
                 start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname  # type: str
        self.end_time = end_time  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sqlid = sqlid  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord(TeaModel):
    def __init__(self, dbname=None, execution_start_time=None, host_address=None, lock_times=None,
                 parse_row_counts=None, query_times=None, return_row_counts=None, sqltext=None):
        self.dbname = dbname  # type: str
        self.execution_start_time = execution_start_time  # type: str
        self.host_address = host_address  # type: str
        self.lock_times = lock_times  # type: long
        self.parse_row_counts = parse_row_counts  # type: long
        self.query_times = query_times  # type: long
        self.return_row_counts = return_row_counts  # type: long
        self.sqltext = sqltext  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.lock_times is not None:
            result['LockTimes'] = self.lock_times
        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts
        if self.query_times is not None:
            result['QueryTimes'] = self.query_times
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('LockTimes') is not None:
            self.lock_times = m.get('LockTimes')
        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')
        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        return self


class DescribeSlowLogRecordsResponseBodyItems(TeaModel):
    def __init__(self, sqlslow_record=None):
        self.sqlslow_record = sqlslow_record  # type: list[DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord]

    def validate(self):
        if self.sqlslow_record:
            for k in self.sqlslow_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SQLSlowRecord'] = []
        if self.sqlslow_record is not None:
            for k in self.sqlslow_record:
                result['SQLSlowRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sqlslow_record = []
        if m.get('SQLSlowRecord') is not None:
            for k in m.get('SQLSlowRecord'):
                temp_model = DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord()
                self.sqlslow_record.append(temp_model.from_map(k))
        return self


class DescribeSlowLogRecordsResponseBody(TeaModel):
    def __init__(self, engine=None, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.engine = engine  # type: str
        self.items = items  # type: DescribeSlowLogRecordsResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSlowLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlowLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponse, self).to_map()
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
            temp_model = DescribeSlowLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowSQLLogsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, execute_state=None, max_execute_cost=None,
                 min_execute_cost=None, operation_class=None, operation_type=None, page_number=None, page_size=None,
                 query_keywords=None, source_ip=None, start_time=None, user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.execute_state = execute_state  # type: str
        self.max_execute_cost = max_execute_cost  # type: str
        self.min_execute_cost = min_execute_cost  # type: str
        self.operation_class = operation_class  # type: str
        self.operation_type = operation_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_keywords = query_keywords  # type: str
        self.source_ip = source_ip  # type: str
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowSQLLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeSlowSQLLogsResponseBodyItems(TeaModel):
    def __init__(self, account_name=None, dbname=None, dbrole=None, execute_cost=None, execute_state=None,
                 operation_class=None, operation_execute_time=None, operation_type=None, query_id=None, return_row_counts=None,
                 sqlplan=None, sqltext=None, scan_row_counts=None, source_ip=None, source_port=None):
        self.account_name = account_name  # type: str
        self.dbname = dbname  # type: str
        self.dbrole = dbrole  # type: str
        self.execute_cost = execute_cost  # type: float
        self.execute_state = execute_state  # type: str
        self.operation_class = operation_class  # type: str
        self.operation_execute_time = operation_execute_time  # type: str
        self.operation_type = operation_type  # type: str
        self.query_id = query_id  # type: str
        self.return_row_counts = return_row_counts  # type: long
        self.sqlplan = sqlplan  # type: str
        self.sqltext = sqltext  # type: str
        self.scan_row_counts = scan_row_counts  # type: long
        self.source_ip = source_ip  # type: str
        self.source_port = source_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowSQLLogsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.dbrole is not None:
            result['DBRole'] = self.dbrole
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqlplan is not None:
            result['SQLPlan'] = self.sqlplan
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DBRole') is not None:
            self.dbrole = m.get('DBRole')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLPlan') is not None:
            self.sqlplan = m.get('SQLPlan')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        return self


class DescribeSlowSQLLogsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None):
        self.items = items  # type: list[DescribeSlowSQLLogsResponseBodyItems]
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowSQLLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSlowSQLLogsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSlowSQLLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlowSQLLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlowSQLLogsResponse, self).to_map()
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
            temp_model = DescribeSlowSQLLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpecificationRequest(TeaModel):
    def __init__(self, cpu_cores=None, dbinstance_id=None, owner_id=None, storage_type=None, total_node_num=None):
        self.cpu_cores = cpu_cores  # type: int
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.storage_type = storage_type  # type: str
        self.total_node_num = total_node_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpecificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.total_node_num is not None:
            result['TotalNodeNum'] = self.total_node_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('TotalNodeNum') is not None:
            self.total_node_num = m.get('TotalNodeNum')
        return self


class DescribeSpecificationResponseBodyDBInstanceClass(TeaModel):
    def __init__(self, text=None, value=None):
        self.text = text  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpecificationResponseBodyDBInstanceClass, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeSpecificationResponseBodyDBInstanceGroupCount(TeaModel):
    def __init__(self, text=None, value=None):
        self.text = text  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpecificationResponseBodyDBInstanceGroupCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeSpecificationResponseBodyStorageNotice(TeaModel):
    def __init__(self, text=None, value=None):
        self.text = text  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSpecificationResponseBodyStorageNotice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeSpecificationResponseBody(TeaModel):
    def __init__(self, dbinstance_class=None, dbinstance_group_count=None, request_id=None, storage_notice=None):
        self.dbinstance_class = dbinstance_class  # type: list[DescribeSpecificationResponseBodyDBInstanceClass]
        self.dbinstance_group_count = dbinstance_group_count  # type: list[DescribeSpecificationResponseBodyDBInstanceGroupCount]
        self.request_id = request_id  # type: str
        self.storage_notice = storage_notice  # type: list[DescribeSpecificationResponseBodyStorageNotice]

    def validate(self):
        if self.dbinstance_class:
            for k in self.dbinstance_class:
                if k:
                    k.validate()
        if self.dbinstance_group_count:
            for k in self.dbinstance_group_count:
                if k:
                    k.validate()
        if self.storage_notice:
            for k in self.storage_notice:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSpecificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceClass'] = []
        if self.dbinstance_class is not None:
            for k in self.dbinstance_class:
                result['DBInstanceClass'].append(k.to_map() if k else None)
        result['DBInstanceGroupCount'] = []
        if self.dbinstance_group_count is not None:
            for k in self.dbinstance_group_count:
                result['DBInstanceGroupCount'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StorageNotice'] = []
        if self.storage_notice is not None:
            for k in self.storage_notice:
                result['StorageNotice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance_class = []
        if m.get('DBInstanceClass') is not None:
            for k in m.get('DBInstanceClass'):
                temp_model = DescribeSpecificationResponseBodyDBInstanceClass()
                self.dbinstance_class.append(temp_model.from_map(k))
        self.dbinstance_group_count = []
        if m.get('DBInstanceGroupCount') is not None:
            for k in m.get('DBInstanceGroupCount'):
                temp_model = DescribeSpecificationResponseBodyDBInstanceGroupCount()
                self.dbinstance_group_count.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.storage_notice = []
        if m.get('StorageNotice') is not None:
            for k in m.get('StorageNotice'):
                temp_model = DescribeSpecificationResponseBodyStorageNotice()
                self.storage_notice.append(temp_model.from_map(k))
        return self


class DescribeSpecificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSpecificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSpecificationResponse, self).to_map()
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
            temp_model = DescribeSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, resource_type=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagsRequest, self).to_map()
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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
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
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeTagsResponseBodyTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagsResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[DescribeTagsResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTagsResponse, self).to_map()
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
            temp_model = DescribeTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserEncryptionKeyListRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUserEncryptionKeyListResponseBodyKmsKeys(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListResponseBodyKmsKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DescribeUserEncryptionKeyListResponseBody(TeaModel):
    def __init__(self, kms_keys=None, request_id=None):
        self.kms_keys = kms_keys  # type: list[DescribeUserEncryptionKeyListResponseBodyKmsKeys]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.kms_keys:
            for k in self.kms_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KmsKeys'] = []
        if self.kms_keys is not None:
            for k in self.kms_keys:
                result['KmsKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.kms_keys = []
        if m.get('KmsKeys') is not None:
            for k in m.get('KmsKeys'):
                temp_model = DescribeUserEncryptionKeyListResponseBodyKmsKeys()
                self.kms_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserEncryptionKeyListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserEncryptionKeyListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListResponse, self).to_map()
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
            temp_model = DescribeUserEncryptionKeyListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadDiagnosisRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, lang=None, query_condition=None,
                 resource_group_id=None, start_time=None, user=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.database = database  # type: str
        self.end_time = end_time  # type: str
        self.lang = lang  # type: str
        self.query_condition = query_condition  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.start_time = start_time  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadDiagnosisRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database is not None:
            result['Database'] = self.database
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DownloadDiagnosisRecordsResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, download_id=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.download_id = download_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadDiagnosisRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.download_id is not None:
            result['DownloadId'] = self.download_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadDiagnosisRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DownloadDiagnosisRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DownloadDiagnosisRecordsResponse, self).to_map()
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
            temp_model = DownloadDiagnosisRecordsResponseBody()
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
    def __init__(self, next_token=None, owner_account=None, owner_id=None, region_id=None, resource_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None, tag=None):
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
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
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
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


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, dbinstance_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountDescriptionResponseBody, self).to_map()
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


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAccountDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccountDescriptionResponse, self).to_map()
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
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, backup_retention_period=None, dbinstance_id=None, enable_recovery_point=None,
                 preferred_backup_period=None, preferred_backup_time=None, recovery_point_period=None):
        self.backup_retention_period = backup_retention_period  # type: int
        self.dbinstance_id = dbinstance_id  # type: str
        self.enable_recovery_point = enable_recovery_point  # type: bool
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.recovery_point_period = recovery_point_period  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.enable_recovery_point is not None:
            result['EnableRecoveryPoint'] = self.enable_recovery_point
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.recovery_point_period is not None:
            result['RecoveryPointPeriod'] = self.recovery_point_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EnableRecoveryPoint') is not None:
            self.enable_recovery_point = m.get('EnableRecoveryPoint')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RecoveryPointPeriod') is not None:
            self.recovery_point_period = m.get('RecoveryPointPeriod')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPolicyResponseBody, self).to_map()
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


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBackupPolicyResponse, self).to_map()
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
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionModeRequest(TeaModel):
    def __init__(self, connection_mode=None, dbinstance_id=None):
        self.connection_mode = connection_mode  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConnectionModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class ModifyDBInstanceConnectionModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConnectionModeResponseBody, self).to_map()
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


class ModifyDBInstanceConnectionModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceConnectionModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceConnectionModeResponse, self).to_map()
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
            temp_model = ModifyDBInstanceConnectionModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, current_connection_string=None, dbinstance_id=None,
                 port=None):
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.current_connection_string = current_connection_string  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConnectionStringRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyDBInstanceConnectionStringResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConnectionStringResponseBody, self).to_map()
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


class ModifyDBInstanceConnectionStringResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceConnectionStringResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceConnectionStringResponse, self).to_map()
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
            temp_model = ModifyDBInstanceConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(self, dbinstance_description=None, dbinstance_id=None, resource_group_id=None):
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyDBInstanceDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceDescriptionResponseBody, self).to_map()
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


class ModifyDBInstanceDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceDescriptionResponse, self).to_map()
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
            temp_model = ModifyDBInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceMaintainTimeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, resource_group_id=None, start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ModifyDBInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceMaintainTimeResponseBody, self).to_map()
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


class ModifyDBInstanceMaintainTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceMaintainTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceMaintainTimeResponse, self).to_map()
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
            temp_model = ModifyDBInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceNetworkTypeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, instance_network_type=None, private_ip_address=None, vpcid=None,
                 v_switch_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceNetworkTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ModifyDBInstanceNetworkTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceNetworkTypeResponseBody, self).to_map()
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


class ModifyDBInstanceNetworkTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceNetworkTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceNetworkTypeResponse, self).to_map()
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
            temp_model = ModifyDBInstanceNetworkTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceResourceGroupRequest(TeaModel):
    def __init__(self, dbinstance_id=None, new_resource_group_id=None, owner_account=None, owner_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.new_resource_group_id = new_resource_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBInstanceResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceResourceGroupResponseBody, self).to_map()
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


class ModifyDBInstanceResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceResourceGroupResponse, self).to_map()
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
            temp_model = ModifyDBInstanceResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceSSLRequest(TeaModel):
    def __init__(self, connection_string=None, dbinstance_id=None, sslenabled=None):
        self.connection_string = connection_string  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.sslenabled = sslenabled  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSSLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        return self


class ModifyDBInstanceSSLResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSSLResponseBody, self).to_map()
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


class ModifyDBInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceSSLResponse, self).to_map()
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
            temp_model = ModifyDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParametersRequest(TeaModel):
    def __init__(self, dbinstance_id=None, force_restart_instance=None, parameters=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.force_restart_instance = force_restart_instance  # type: bool
        self.parameters = parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.force_restart_instance is not None:
            result['ForceRestartInstance'] = self.force_restart_instance
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ForceRestartInstance') is not None:
            self.force_restart_instance = m.get('ForceRestartInstance')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class ModifyParametersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParametersResponseBody, self).to_map()
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


class ModifyParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyParametersResponse, self).to_map()
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
            temp_model = ModifyParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySQLCollectorPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, sqlcollector_status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.sqlcollector_status = sqlcollector_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySQLCollectorPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.sqlcollector_status is not None:
            result['SQLCollectorStatus'] = self.sqlcollector_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SQLCollectorStatus') is not None:
            self.sqlcollector_status = m.get('SQLCollectorStatus')
        return self


class ModifySQLCollectorPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySQLCollectorPolicyResponseBody, self).to_map()
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


class ModifySQLCollectorPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySQLCollectorPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySQLCollectorPolicyResponse, self).to_map()
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
            temp_model = ModifySQLCollectorPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(self, dbinstance_iparray_attribute=None, dbinstance_iparray_name=None, dbinstance_id=None,
                 resource_group_id=None, security_iplist=None):
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute  # type: str
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.security_iplist = security_iplist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIpsResponseBody, self).to_map()
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


class ModifySecurityIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySecurityIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySecurityIpsResponse, self).to_map()
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
            temp_model = ModifySecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PauseInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class PauseInstanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, request_id=None, status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PauseInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PauseInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PauseInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PauseInstanceResponse, self).to_map()
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
            temp_model = PauseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebalanceDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebalanceDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class RebalanceDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebalanceDBInstanceResponseBody, self).to_map()
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


class RebalanceDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RebalanceDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebalanceDBInstanceResponse, self).to_map()
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
            temp_model = RebalanceDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(self, address_type=None, current_connection_string=None, dbinstance_id=None):
        self.address_type = address_type  # type: str
        self.current_connection_string = current_connection_string  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstancePublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
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
    def __init__(self, account_name=None, account_password=None, dbinstance_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
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


class RestartDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class RestartDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBInstanceResponseBody, self).to_map()
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


class RestartDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartDBInstanceResponse, self).to_map()
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
            temp_model = RestartDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ResumeInstanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, request_id=None, status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ResumeInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeInstanceResponse, self).to_map()
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
            temp_model = ResumeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDBInstancePlanStatusRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, plan_id=None, plan_status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.plan_id = plan_id  # type: str
        self.plan_status = plan_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDBInstancePlanStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_status is not None:
            result['PlanStatus'] = self.plan_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanStatus') is not None:
            self.plan_status = m.get('PlanStatus')
        return self


class SetDBInstancePlanStatusResponseBody(TeaModel):
    def __init__(self, error_message=None, plan_id=None, request_id=None, status=None):
        self.error_message = error_message  # type: str
        self.plan_id = plan_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDBInstancePlanStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDBInstancePlanStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDBInstancePlanStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDBInstancePlanStatusResponse, self).to_map()
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
            temp_model = SetDBInstancePlanStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataShareInstanceRequest(TeaModel):
    def __init__(self, instance_list=None, operation_type=None, owner_id=None, region_id=None):
        self.instance_list = instance_list  # type: list[str]
        self.operation_type = operation_type  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataShareInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetDataShareInstanceShrinkRequest(TeaModel):
    def __init__(self, instance_list_shrink=None, operation_type=None, owner_id=None, region_id=None):
        self.instance_list_shrink = instance_list_shrink  # type: str
        self.operation_type = operation_type  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataShareInstanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_list_shrink is not None:
            result['InstanceList'] = self.instance_list_shrink
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            self.instance_list_shrink = m.get('InstanceList')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetDataShareInstanceResponseBody(TeaModel):
    def __init__(self, err_message=None, request_id=None, status=None):
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDataShareInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDataShareInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDataShareInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDataShareInstanceResponse, self).to_map()
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
            temp_model = SetDataShareInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchDBInstanceNetTypeRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, dbinstance_id=None, port=None):
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchDBInstanceNetTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class SwitchDBInstanceNetTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchDBInstanceNetTypeResponseBody, self).to_map()
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


class SwitchDBInstanceNetTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchDBInstanceNetTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchDBInstanceNetTypeResponse, self).to_map()
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
            temp_model = SwitchDBInstanceNetTypeResponseBody()
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
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None, tag=None):
        self.owner_account = owner_account  # type: str
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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


class UnloadSampleDataRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnloadSampleDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UnloadSampleDataResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, request_id=None, status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnloadSampleDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UnloadSampleDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnloadSampleDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnloadSampleDataResponse, self).to_map()
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
            temp_model = UnloadSampleDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, owner_account=None, owner_id=None, region_id=None, resource_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.owner_account = owner_account  # type: str
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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


class UpdateDBInstancePlanRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_id=None, plan_config=None, plan_desc=None, plan_end_date=None,
                 plan_id=None, plan_name=None, plan_start_date=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.plan_config = plan_config  # type: str
        self.plan_desc = plan_desc  # type: str
        self.plan_end_date = plan_end_date  # type: str
        self.plan_id = plan_id  # type: str
        self.plan_name = plan_name  # type: str
        self.plan_start_date = plan_start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDBInstancePlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.plan_config is not None:
            result['PlanConfig'] = self.plan_config
        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc
        if self.plan_end_date is not None:
            result['PlanEndDate'] = self.plan_end_date
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_start_date is not None:
            result['PlanStartDate'] = self.plan_start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlanConfig') is not None:
            self.plan_config = m.get('PlanConfig')
        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')
        if m.get('PlanEndDate') is not None:
            self.plan_end_date = m.get('PlanEndDate')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanStartDate') is not None:
            self.plan_start_date = m.get('PlanStartDate')
        return self


class UpdateDBInstancePlanResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, error_message=None, plan_id=None, request_id=None, status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.error_message = error_message  # type: str
        self.plan_id = plan_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDBInstancePlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateDBInstancePlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDBInstancePlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDBInstancePlanResponse, self).to_map()
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
            temp_model = UpdateDBInstancePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_class=None, dbinstance_group_count=None, dbinstance_id=None, instance_spec=None,
                 master_node_num=None, owner_id=None, pay_type=None, region_id=None, resource_group_id=None, seg_node_num=None,
                 storage_size=None, upgrade_type=None):
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_group_count = dbinstance_group_count  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.instance_spec = instance_spec  # type: str
        self.master_node_num = master_node_num  # type: str
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.seg_node_num = seg_node_num  # type: str
        self.storage_size = storage_size  # type: str
        self.upgrade_type = upgrade_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        return self


class UpgradeDBInstanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeDBInstanceResponse, self).to_map()
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
            temp_model = UpgradeDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBVersionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, major_version=None, minor_version=None, owner_id=None, region_id=None,
                 switch_time=None, switch_time_mode=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.major_version = major_version  # type: str
        self.minor_version = minor_version  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.switch_time = switch_time  # type: str
        self.switch_time_mode = switch_time_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class UpgradeDBVersionResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_name=None, request_id=None, task_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeDBVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeDBVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeDBVersionResponse, self).to_map()
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
            temp_model = UpgradeDBVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


