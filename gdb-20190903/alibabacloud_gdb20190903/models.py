# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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


class CloneDBInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, backup_set_id=None, client_token=None,
                 dbinstance_category=None, dbinstance_class=None, dbinstance_description=None, dbinstance_network_type=None,
                 dbinstance_version=None, dbnode_storage=None, dbnode_storage_type=None, owner_account=None, owner_id=None,
                 pay_type=None, period=None, region_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, restore_time=None, restore_type=None, security_iplist=None, source_dbinstance_id=None,
                 used_time=None, vpcid=None, v_switch_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: str
        self.auto_renew_period = auto_renew_period  # type: str
        self.backup_set_id = backup_set_id  # type: str
        self.client_token = client_token  # type: str
        self.dbinstance_category = dbinstance_category  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_network_type = dbinstance_network_type  # type: str
        self.dbinstance_version = dbinstance_version  # type: str
        self.dbnode_storage = dbnode_storage  # type: str
        self.dbnode_storage_type = dbnode_storage_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.restore_time = restore_time  # type: str
        self.restore_type = restore_type  # type: str
        self.security_iplist = security_iplist  # type: str
        self.source_dbinstance_id = source_dbinstance_id  # type: str
        self.used_time = used_time  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_network_type is not None:
            result['DBInstanceNetworkType'] = self.dbinstance_network_type
        if self.dbinstance_version is not None:
            result['DBInstanceVersion'] = self.dbinstance_version
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbnode_storage_type is not None:
            result['DBNodeStorageType'] = self.dbnode_storage_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.source_dbinstance_id is not None:
            result['SourceDBInstanceId'] = self.source_dbinstance_id
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
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceNetworkType') is not None:
            self.dbinstance_network_type = m.get('DBInstanceNetworkType')
        if m.get('DBInstanceVersion') is not None:
            self.dbinstance_version = m.get('DBInstanceVersion')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBNodeStorageType') is not None:
            self.dbnode_storage_type = m.get('DBNodeStorageType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SourceDBInstanceId') is not None:
            self.source_dbinstance_id = m.get('SourceDBInstanceId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CloneDBInstanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneDBInstanceResponseBody, self).to_map()
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


class CloneDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneDBInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneDBInstanceResponse, self).to_map()
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
            temp_model = CloneDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_password=None, client_token=None,
                 dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
    def __init__(self, auto_renew=None, auto_renew_period=None, client_token=None, dbinstance_category=None,
                 dbinstance_class=None, dbinstance_description=None, dbinstance_network_type=None, dbinstance_version=None,
                 dbnode_storage=None, dbnode_storage_type=None, owner_account=None, owner_id=None, pay_type=None, period=None,
                 region_id=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_iplist=None, used_time=None, vpcid=None, v_switch_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: str
        self.auto_renew_period = auto_renew_period  # type: str
        self.client_token = client_token  # type: str
        self.dbinstance_category = dbinstance_category  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_network_type = dbinstance_network_type  # type: str
        self.dbinstance_version = dbinstance_version  # type: str
        self.dbnode_storage = dbnode_storage  # type: str
        self.dbnode_storage_type = dbnode_storage_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_iplist = security_iplist  # type: str
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
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_network_type is not None:
            result['DBInstanceNetworkType'] = self.dbinstance_network_type
        if self.dbinstance_version is not None:
            result['DBInstanceVersion'] = self.dbinstance_version
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbnode_storage_type is not None:
            result['DBNodeStorageType'] = self.dbnode_storage_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
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
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceNetworkType') is not None:
            self.dbinstance_network_type = m.get('DBInstanceNetworkType')
        if m.get('DBInstanceVersion') is not None:
            self.dbinstance_version = m.get('DBInstanceVersion')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBNodeStorageType') is not None:
            self.dbnode_storage_type = m.get('DBNodeStorageType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
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
    def __init__(self, dbinstance_id=None, order_id=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceResponseBody, self).to_map()
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


class CreateDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDBInstanceResponseBody

    def validate(self):
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


class CreateReadDBInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, backup_set_id=None, client_token=None,
                 dbinstance_category=None, dbinstance_id=None, dbinstance_network_type=None, dbnode_class=None, dbnode_storage=None,
                 dbnode_storage_type=None, effective_time=None, engine_version=None, order_param=None, order_type=None,
                 owner_account=None, owner_id=None, region_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, v_switch_id=None, vpc_id=None):
        self.auto_renew = auto_renew  # type: str
        self.auto_renew_period = auto_renew_period  # type: str
        self.backup_set_id = backup_set_id  # type: str
        self.client_token = client_token  # type: str
        self.dbinstance_category = dbinstance_category  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_network_type = dbinstance_network_type  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_storage = dbnode_storage  # type: str
        self.dbnode_storage_type = dbnode_storage_type  # type: str
        self.effective_time = effective_time  # type: str
        self.engine_version = engine_version  # type: str
        self.order_param = order_param  # type: str
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReadDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_category is not None:
            result['DBInstanceCategory'] = self.dbinstance_category
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_network_type is not None:
            result['DBInstanceNetworkType'] = self.dbinstance_network_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbnode_storage_type is not None:
            result['DBNodeStorageType'] = self.dbnode_storage_type
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.order_param is not None:
            result['OrderParam'] = self.order_param
        if self.order_type is not None:
            result['OrderType'] = self.order_type
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
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceCategory') is not None:
            self.dbinstance_category = m.get('DBInstanceCategory')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceNetworkType') is not None:
            self.dbinstance_network_type = m.get('DBInstanceNetworkType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBNodeStorageType') is not None:
            self.dbnode_storage_type = m.get('DBNodeStorageType')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('OrderParam') is not None:
            self.order_param = m.get('OrderParam')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
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
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateReadDBInstanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReadDBInstanceResponseBody, self).to_map()
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


class CreateReadDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateReadDBInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateReadDBInstanceResponse, self).to_map()
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
            temp_model = CreateReadDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self, client_token=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, service_name=None):
        self.client_token = client_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateServiceLinkedRoleResponseBodyRoleRole(TeaModel):
    def __init__(self, arn=None, assume_role_policy_document=None, create_date=None, description=None,
                 is_service_linked_role=None, latest_deletion_task=None, role_id=None, role_name=None, role_principal_name=None):
        self.arn = arn  # type: str
        self.assume_role_policy_document = assume_role_policy_document  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.is_service_linked_role = is_service_linked_role  # type: bool
        self.latest_deletion_task = latest_deletion_task  # type: bool
        self.role_id = role_id  # type: str
        self.role_name = role_name  # type: str
        self.role_principal_name = role_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponseBodyRoleRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('LatestDeletionTask') is not None:
            self.latest_deletion_task = m.get('LatestDeletionTask')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateServiceLinkedRoleResponseBodyRole(TeaModel):
    def __init__(self, role=None):
        self.role = role  # type: list[CreateServiceLinkedRoleResponseBodyRoleRole]

    def validate(self):
        if self.role:
            for k in self.role:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponseBodyRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Role'] = []
        if self.role is not None:
            for k in self.role:
                result['Role'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k in m.get('Role'):
                temp_model = CreateServiceLinkedRoleResponseBodyRoleRole()
                self.role.append(temp_model.from_map(k))
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, role=None):
        self.request_id = request_id  # type: str
        self.role = role  # type: CreateServiceLinkedRoleResponseBodyRole

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateServiceLinkedRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceLinkedRoleResponseBody

    def validate(self):
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


class DeleteDBDataRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBDataResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBDataResponseBody, self).to_map()
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


class DeleteDBDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDBDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBDataResponse, self).to_map()
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
            temp_model = DeleteDBDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
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


class DescribeAccountsRequest(TeaModel):
    def __init__(self, account_name=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAccountsResponseBodyAccounts(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_status=None, account_type=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_status = account_status  # type: str
        self.account_type = account_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(self, accounts=None, request_id=None):
        self.accounts = accounts  # type: list[DescribeAccountsResponseBodyAccounts]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeAccountsResponseBodyAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAccountsResponseBody

    def validate(self):
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


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, charge_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, zone_id=None):
        self.charge_type = charge_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
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
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
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
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeListSupportedStorageSizeStorageSize(TeaModel):
    def __init__(self, max=None, min=None, step=None):
        self.max = max  # type: int
        self.min = min  # type: int
        self.step = step  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeListSupportedStorageSizeStorageSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeListSupportedStorageSize(TeaModel):
    def __init__(self, storage_size=None, storage_type=None):
        self.storage_size = storage_size  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeListSupportedStorageSizeStorageSize
        self.storage_type = storage_type  # type: str

    def validate(self):
        if self.storage_size:
            self.storage_size.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeListSupportedStorageSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageSize') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeListSupportedStorageSizeStorageSize()
            self.storage_size = temp_model.from_map(m['StorageSize'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeList(TeaModel):
    def __init__(self, supported_storage_size=None):
        self.supported_storage_size = supported_storage_size  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeListSupportedStorageSize]

    def validate(self):
        if self.supported_storage_size:
            for k in self.supported_storage_size:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedStorageSize'] = []
        if self.supported_storage_size is not None:
            for k in self.supported_storage_size:
                result['SupportedStorageSize'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_storage_size = []
        if m.get('SupportedStorageSize') is not None:
            for k in m.get('SupportedStorageSize'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeListSupportedStorageSize()
                self.supported_storage_size.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClass(TeaModel):
    def __init__(self, instance_class=None, supported_storage_size_list=None, tips=None):
        self.instance_class = instance_class  # type: str
        self.supported_storage_size_list = supported_storage_size_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeList
        self.tips = tips  # type: str

    def validate(self):
        if self.supported_storage_size_list:
            self.supported_storage_size_list.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClass, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.supported_storage_size_list is not None:
            result['SupportedStorageSizeList'] = self.supported_storage_size_list.to_map()
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('SupportedStorageSizeList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClassSupportedStorageSizeList()
            self.supported_storage_size_list = temp_model.from_map(m['SupportedStorageSizeList'])
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassList(TeaModel):
    def __init__(self, supported_instance_class=None):
        self.supported_instance_class = supported_instance_class  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClass]

    def validate(self):
        if self.supported_instance_class:
            for k in self.supported_instance_class:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedInstanceClass'] = []
        if self.supported_instance_class is not None:
            for k in self.supported_instance_class:
                result['SupportedInstanceClass'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_instance_class = []
        if m.get('SupportedInstanceClass') is not None:
            for k in m.get('SupportedInstanceClass'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassListSupportedInstanceClass()
                self.supported_instance_class.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerial(TeaModel):
    def __init__(self, serial=None, supported_instance_class_list=None):
        self.serial = serial  # type: str
        self.supported_instance_class_list = supported_instance_class_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassList

    def validate(self):
        if self.supported_instance_class_list:
            self.supported_instance_class_list.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial is not None:
            result['Serial'] = self.serial
        if self.supported_instance_class_list is not None:
            result['SupportedInstanceClassList'] = self.supported_instance_class_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Serial') is not None:
            self.serial = m.get('Serial')
        if m.get('SupportedInstanceClassList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerialSupportedInstanceClassList()
            self.supported_instance_class_list = temp_model.from_map(m['SupportedInstanceClassList'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialList(TeaModel):
    def __init__(self, supported_serial=None):
        self.supported_serial = supported_serial  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerial]

    def validate(self):
        if self.supported_serial:
            for k in self.supported_serial:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedSerial'] = []
        if self.supported_serial is not None:
            for k in self.supported_serial:
                result['SupportedSerial'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_serial = []
        if m.get('SupportedSerial') is not None:
            for k in m.get('SupportedSerial'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialListSupportedSerial()
                self.supported_serial.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZone(TeaModel):
    def __init__(self, supported_serial_list=None, zone_id=None):
        self.supported_serial_list = supported_serial_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialList
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.supported_serial_list:
            self.supported_serial_list.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_serial_list is not None:
            result['SupportedSerialList'] = self.supported_serial_list.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedSerialList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZoneSupportedSerialList()
            self.supported_serial_list = temp_model.from_map(m['SupportedSerialList'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneList(TeaModel):
    def __init__(self, available_zone=None):
        self.available_zone = available_zone  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZone]

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZoneList, self).to_map()
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
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(self, available_zone_list=None, region_id=None, request_id=None):
        self.available_zone_list = available_zone_list  # type: DescribeAvailableResourceResponseBodyAvailableZoneList
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_zone_list:
            self.available_zone_list.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zone_list is not None:
            result['AvailableZoneList'] = self.available_zone_list.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZoneList') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneList()
            self.available_zone_list = temp_model.from_map(m['AvailableZoneList'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, backup_retention_period=None, enable_backup_log=None, log_backup_retention_period=None,
                 preferred_backup_period=None, preferred_backup_time=None, request_id=None):
        self.backup_retention_period = backup_retention_period  # type: int
        self.enable_backup_log = enable_backup_log  # type: str
        self.log_backup_retention_period = log_backup_retention_period  # type: int
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
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
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupPolicyResponseBody

    def validate(self):
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


class DescribeBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, dbinstance_id=None, end_time=None, owner_account=None, owner_id=None,
                 page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.backup_id = backup_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupsResponseBodyItemsBackup(TeaModel):
    def __init__(self, backup_end_time=None, backup_id=None, backup_method=None, backup_size=None,
                 backup_start_time=None, backup_status=None, backup_type=None, dbinstance_id=None):
        self.backup_end_time = backup_end_time  # type: str
        self.backup_id = backup_id  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_size = backup_size  # type: long
        self.backup_start_time = backup_start_time  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_type = backup_type  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyItemsBackup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeBackupsResponseBodyItems(TeaModel):
    def __init__(self, backup=None):
        self.backup = backup  # type: list[DescribeBackupsResponseBodyItemsBackup]

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k in m.get('Backup'):
                temp_model = DescribeBackupsResponseBodyItemsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.items = items  # type: DescribeBackupsResponseBodyItems
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('Items') is not None:
            temp_model = DescribeBackupsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponse, self).to_map()
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
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAccessWhiteListRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAccessWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBInstanceAccessWhiteListResponseBodyItemsDBInstanceIPArray(TeaModel):
    def __init__(self, dbinstance_iparray_attribute=None, dbinstance_iparray_name=None, security_ips=None):
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute  # type: str
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAccessWhiteListResponseBodyItemsDBInstanceIPArray, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class DescribeDBInstanceAccessWhiteListResponseBodyItems(TeaModel):
    def __init__(self, dbinstance_iparray=None):
        self.dbinstance_iparray = dbinstance_iparray  # type: list[DescribeDBInstanceAccessWhiteListResponseBodyItemsDBInstanceIPArray]

    def validate(self):
        if self.dbinstance_iparray:
            for k in self.dbinstance_iparray:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAccessWhiteListResponseBodyItems, self).to_map()
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
                temp_model = DescribeDBInstanceAccessWhiteListResponseBodyItemsDBInstanceIPArray()
                self.dbinstance_iparray.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAccessWhiteListResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        self.items = items  # type: DescribeDBInstanceAccessWhiteListResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAccessWhiteListResponseBody, self).to_map()
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
            temp_model = DescribeDBInstanceAccessWhiteListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceAccessWhiteListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceAccessWhiteListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAccessWhiteListResponse, self).to_map()
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
            temp_model = DescribeDBInstanceAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId, self).to_map()
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


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceReadOnlyDBInstanceIds(TeaModel):
    def __init__(self, read_only_dbinstance_id=None):
        self.read_only_dbinstance_id = read_only_dbinstance_id  # type: list[DescribeDBInstanceAttributeResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId]

    def validate(self):
        if self.read_only_dbinstance_id:
            for k in self.read_only_dbinstance_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItemsDBInstanceReadOnlyDBInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReadOnlyDBInstanceId'] = []
        if self.read_only_dbinstance_id is not None:
            for k in self.read_only_dbinstance_id:
                result['ReadOnlyDBInstanceId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.read_only_dbinstance_id = []
        if m.get('ReadOnlyDBInstanceId') is not None:
            for k in m.get('ReadOnlyDBInstanceId'):
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId()
                self.read_only_dbinstance_id.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItemsDBInstanceTagsTag, self).to_map()
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


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBInstanceAttributeResponseBodyItemsDBInstanceTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItemsDBInstanceTags, self).to_map()
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
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstance(TeaModel):
    def __init__(self, category=None, connection_string=None, creation_time=None, current_minor_version=None,
                 dbinstance_cpu=None, dbinstance_description=None, dbinstance_id=None, dbinstance_memory=None,
                 dbinstance_network_type=None, dbinstance_status=None, dbinstance_storage_type=None, dbinstance_type=None,
                 dbnode_class=None, dbnode_count=None, dbnode_storage=None, dbversion=None, expire_time=None, expired=None,
                 latest_minor_version=None, lock_mode=None, lock_reason=None, maintain_time=None, master_instance_id=None, pay_type=None,
                 port=None, public_connection_string=None, public_port=None, read_only_dbinstance_ids=None,
                 region_id=None, resource_group_id=None, tags=None, v_switch_id=None, vpc_id=None, zone_id=None):
        self.category = category  # type: str
        self.connection_string = connection_string  # type: str
        self.creation_time = creation_time  # type: str
        self.current_minor_version = current_minor_version  # type: str
        self.dbinstance_cpu = dbinstance_cpu  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_memory = dbinstance_memory  # type: long
        self.dbinstance_network_type = dbinstance_network_type  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_count = dbnode_count  # type: long
        self.dbnode_storage = dbnode_storage  # type: long
        self.dbversion = dbversion  # type: str
        self.expire_time = expire_time  # type: str
        self.expired = expired  # type: str
        self.latest_minor_version = latest_minor_version  # type: str
        self.lock_mode = lock_mode  # type: str
        self.lock_reason = lock_reason  # type: str
        self.maintain_time = maintain_time  # type: str
        self.master_instance_id = master_instance_id  # type: str
        self.pay_type = pay_type  # type: str
        self.port = port  # type: str
        self.public_connection_string = public_connection_string  # type: str
        self.public_port = public_port  # type: int
        self.read_only_dbinstance_ids = read_only_dbinstance_ids  # type: DescribeDBInstanceAttributeResponseBodyItemsDBInstanceReadOnlyDBInstanceIds
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tags = tags  # type: DescribeDBInstanceAttributeResponseBodyItemsDBInstanceTags
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.read_only_dbinstance_ids:
            self.read_only_dbinstance_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItemsDBInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.current_minor_version is not None:
            result['CurrentMinorVersion'] = self.current_minor_version
        if self.dbinstance_cpu is not None:
            result['DBInstanceCPU'] = self.dbinstance_cpu
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_memory is not None:
            result['DBInstanceMemory'] = self.dbinstance_memory
        if self.dbinstance_network_type is not None:
            result['DBInstanceNetworkType'] = self.dbinstance_network_type
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.public_port is not None:
            result['PublicPort'] = self.public_port
        if self.read_only_dbinstance_ids is not None:
            result['ReadOnlyDBInstanceIds'] = self.read_only_dbinstance_ids.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CurrentMinorVersion') is not None:
            self.current_minor_version = m.get('CurrentMinorVersion')
        if m.get('DBInstanceCPU') is not None:
            self.dbinstance_cpu = m.get('DBInstanceCPU')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceMemory') is not None:
            self.dbinstance_memory = m.get('DBInstanceMemory')
        if m.get('DBInstanceNetworkType') is not None:
            self.dbinstance_network_type = m.get('DBInstanceNetworkType')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('PublicPort') is not None:
            self.public_port = m.get('PublicPort')
        if m.get('ReadOnlyDBInstanceIds') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceReadOnlyDBInstanceIds()
            self.read_only_dbinstance_ids = temp_model.from_map(m['ReadOnlyDBInstanceIds'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBodyItems(TeaModel):
    def __init__(self, dbinstance=None):
        self.dbinstance = dbinstance  # type: list[DescribeDBInstanceAttributeResponseBodyItemsDBInstance]

    def validate(self):
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyItems, self).to_map()
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
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
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


class DescribeDBInstancePerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, key=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue(TeaModel):
    def __init__(self, timestamp=None, value=None):
        self.timestamp = timestamp  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItemPoints(TeaModel):
    def __init__(self, performance_item_value=None):
        self.performance_item_value = performance_item_value  # type: list[DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue]

    def validate(self):
        if self.performance_item_value:
            for k in self.performance_item_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItemPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceItemValue'] = []
        if self.performance_item_value is not None:
            for k in self.performance_item_value:
                result['PerformanceItemValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.performance_item_value = []
        if m.get('PerformanceItemValue') is not None:
            for k in m.get('PerformanceItemValue'):
                temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue()
                self.performance_item_value.append(temp_model.from_map(k))
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItem(TeaModel):
    def __init__(self, measurement=None, metric_name=None, points=None):
        self.measurement = measurement  # type: str
        self.metric_name = metric_name  # type: str
        self.points = points  # type: DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItemPoints

    def validate(self):
        if self.points:
            self.points.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.measurement is not None:
            result['Measurement'] = self.measurement
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.points is not None:
            result['Points'] = self.points.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Points') is not None:
            temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItemPoints()
            self.points = temp_model.from_map(m['Points'])
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(self, performance_item=None):
        self.performance_item = performance_item  # type: list[DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItem]

    def validate(self):
        if self.performance_item:
            for k in self.performance_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBodyPerformanceKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceItem'] = []
        if self.performance_item is not None:
            for k in self.performance_item:
                result['PerformanceItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.performance_item = []
        if m.get('PerformanceItem') is not None:
            for k in m.get('PerformanceItem'):
                temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceItem()
                self.performance_item.append(temp_model.from_map(k))
        return self


class DescribeDBInstancePerformanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, engine=None, performance_keys=None, request_id=None,
                 start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.engine = engine  # type: str
        self.performance_keys = performance_keys  # type: DescribeDBInstancePerformanceResponseBodyPerformanceKeys
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

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
            result['PerformanceKeys'] = self.performance_keys.to_map()
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
            temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m['PerformanceKeys'])
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


class DescribeDBInstanceStatusRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceStatusRequest, self).to_map()
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


class DescribeDBInstanceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDBInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceStatusResponse, self).to_map()
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
            temp_model = DescribeDBInstanceStatusResponseBody()
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
    def __init__(self, client_token=None, dbinstance_description=None, dbinstance_ids=None, dbinstance_status=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, tag=None):
        self.client_token = client_token  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_ids = dbinstance_ids  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId, self).to_map()
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


class DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIds(TeaModel):
    def __init__(self, read_only_dbinstance_id=None):
        self.read_only_dbinstance_id = read_only_dbinstance_id  # type: list[DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId]

    def validate(self):
        if self.read_only_dbinstance_id:
            for k in self.read_only_dbinstance_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReadOnlyDBInstanceId'] = []
        if self.read_only_dbinstance_id is not None:
            for k in self.read_only_dbinstance_id:
                result['ReadOnlyDBInstanceId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.read_only_dbinstance_id = []
        if m.get('ReadOnlyDBInstanceId') is not None:
            for k in m.get('ReadOnlyDBInstanceId'):
                temp_model = DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId()
                self.read_only_dbinstance_id.append(temp_model.from_map(k))
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
    def __init__(self, category=None, create_time=None, dbinstance_description=None, dbinstance_id=None,
                 dbinstance_status=None, dbinstance_type=None, dbnode_class=None, dbnode_count=None, dbnode_storage=None,
                 dbversion=None, expire_time=None, expired=None, lock_mode=None, lock_reason=None, master_instance_id=None,
                 pay_type=None, read_only_dbinstance_ids=None, region_id=None, resource_group_id=None, tags=None,
                 v_switch_id=None, vpc_id=None, zone_id=None):
        self.category = category  # type: str
        self.create_time = create_time  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_count = dbnode_count  # type: long
        self.dbnode_storage = dbnode_storage  # type: long
        self.dbversion = dbversion  # type: str
        self.expire_time = expire_time  # type: str
        self.expired = expired  # type: str
        self.lock_mode = lock_mode  # type: str
        self.lock_reason = lock_reason  # type: str
        self.master_instance_id = master_instance_id  # type: str
        self.pay_type = pay_type  # type: str
        self.read_only_dbinstance_ids = read_only_dbinstance_ids  # type: DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIds
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tags = tags  # type: DescribeDBInstancesResponseBodyItemsDBInstanceTags
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.read_only_dbinstance_ids:
            self.read_only_dbinstance_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyItemsDBInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.read_only_dbinstance_ids is not None:
            result['ReadOnlyDBInstanceIds'] = self.read_only_dbinstance_ids.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ReadOnlyDBInstanceIds') is not None:
            temp_model = DescribeDBInstancesResponseBodyItemsDBInstanceReadOnlyDBInstanceIds()
            self.read_only_dbinstance_ids = temp_model.from_map(m['ReadOnlyDBInstanceIds'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.items = items  # type: DescribeDBInstancesResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeDBInstancesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstancesResponseBody

    def validate(self):
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


class DescribeRegionsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
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
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeResourceUsageResponseBody(TeaModel):
    def __init__(self, backup_size=None, cold_backup_size=None, dbinstance_id=None, data_size=None, disk_used=None,
                 engine=None, log_size=None, request_id=None):
        self.backup_size = backup_size  # type: long
        self.cold_backup_size = cold_backup_size  # type: long
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
        if self.cold_backup_size is not None:
            result['ColdBackupSize'] = self.cold_backup_size
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
        if m.get('ColdBackupSize') is not None:
            self.cold_backup_size = m.get('ColdBackupSize')
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


class DescribeSecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation(TeaModel):
    def __init__(self, network_type=None, region_id=None, security_group_id=None):
        self.network_type = network_type  # type: str
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeSecurityGroupConfigurationResponseBodyItems(TeaModel):
    def __init__(self, ecs_security_group_relation=None):
        self.ecs_security_group_relation = ecs_security_group_relation  # type: list[DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation]

    def validate(self):
        if self.ecs_security_group_relation:
            for k in self.ecs_security_group_relation:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsSecurityGroupRelation'] = []
        if self.ecs_security_group_relation is not None:
            for k in self.ecs_security_group_relation:
                result['EcsSecurityGroupRelation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ecs_security_group_relation = []
        if m.get('EcsSecurityGroupRelation') is not None:
            for k in m.get('EcsSecurityGroupRelation'):
                temp_model = DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation()
                self.ecs_security_group_relation.append(temp_model.from_map(k))
        return self


class DescribeSecurityGroupConfigurationResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, items=None, request_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.items = items  # type: DescribeSecurityGroupConfigurationResponseBodyItems
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Items') is not None:
            temp_model = DescribeSecurityGroupConfigurationResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSecurityGroupConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSecurityGroupConfigurationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationResponse, self).to_map()
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
            temp_model = DescribeSecurityGroupConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(self, next_token=None, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None):
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeTagsResponseBodyTagsTagTagValues(TeaModel):
    def __init__(self, tag_value=None):
        self.tag_value = tag_value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagsResponseBodyTagsTagTagValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeTagsResponseBodyTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_values=None):
        self.tag_key = tag_key  # type: str
        self.tag_values = tag_values  # type: DescribeTagsResponseBodyTagsTagTagValues

    def validate(self):
        if self.tag_values:
            self.tag_values.validate()

    def to_map(self):
        _map = super(DescribeTagsResponseBodyTagsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValues') is not None:
            temp_model = DescribeTagsResponseBodyTagsTagTagValues()
            self.tag_values = temp_model.from_map(m['TagValues'])
        return self


class DescribeTagsResponseBodyTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeTagsResponseBodyTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTagsResponseBodyTags, self).to_map()
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
                temp_model = DescribeTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tags=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tags = tags  # type: DescribeTagsResponseBodyTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            temp_model = DescribeTagsResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTagsResponseBody

    def validate(self):
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


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, backup_retention_period=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 preferred_backup_period=None, preferred_backup_time=None, resource_owner_account=None, resource_owner_id=None):
        self.backup_retention_period = backup_retention_period  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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


class ModifyDBInstanceAccessWhiteListRequest(TeaModel):
    def __init__(self, dbinstance_iparray_attribute=None, dbinstance_iparray_name=None, dbinstance_id=None,
                 modify_mode=None, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_ips=None):
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute  # type: str
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.modify_mode = modify_mode  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_ips = security_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceAccessWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class ModifyDBInstanceAccessWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceAccessWhiteListResponseBody, self).to_map()
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


class ModifyDBInstanceAccessWhiteListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceAccessWhiteListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceAccessWhiteListResponse, self).to_map()
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
            temp_model = ModifyDBInstanceAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(self, dbinstance_description=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
    def __init__(self, dbinstance_id=None, maintain_time=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.maintain_time = maintain_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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


class ModifyDBInstanceSpecRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_class=None, dbinstance_id=None, dbinstance_storage=None,
                 dbinstance_storage_type=None, effective_time=None, engine_version=None, order_param=None, order_type=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.effective_time = effective_time  # type: str
        self.engine_version = engine_version  # type: str
        self.order_param = order_param  # type: str
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.order_param is not None:
            result['OrderParam'] = self.order_param
        if self.order_type is not None:
            result['OrderType'] = self.order_type
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
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('OrderParam') is not None:
            self.order_param = m.get('OrderParam')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
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


class ModifyDBInstanceSpecResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSpecResponseBody, self).to_map()
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


class ModifyDBInstanceSpecResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceSpecResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceSpecResponse, self).to_map()
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
            temp_model = ModifyDBInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_group_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityGroupConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class ModifySecurityGroupConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityGroupConfigurationResponseBody, self).to_map()
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


class ModifySecurityGroupConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySecurityGroupConfigurationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySecurityGroupConfigurationResponse, self).to_map()
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
            temp_model = ModifySecurityGroupConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, dbinstance_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
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
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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


class UpgradeDBInstanceKernelVersionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, switch_time=None, switch_time_mode=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.switch_time = switch_time  # type: str
        self.switch_time_mode = switch_time_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBInstanceKernelVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class UpgradeDBInstanceKernelVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBInstanceKernelVersionResponseBody, self).to_map()
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


class UpgradeDBInstanceKernelVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeDBInstanceKernelVersionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeDBInstanceKernelVersionResponse, self).to_map()
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
            temp_model = UpgradeDBInstanceKernelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


