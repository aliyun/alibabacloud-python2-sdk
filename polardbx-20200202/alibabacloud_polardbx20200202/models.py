# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(self, connection_string_prefix=None, dbinstance_name=None, owner_account=None, owner_id=None,
                 port=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.port = port  # type: str
        self.region_id = region_id  # type: str
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
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AllocateInstancePublicConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AllocateInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPolarxOrderRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None, scale_out_token=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str
        self.scale_out_token = scale_out_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPolarxOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_out_token is not None:
            result['ScaleOutToken'] = self.scale_out_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleOutToken') is not None:
            self.scale_out_token = m.get('ScaleOutToken')
        return self


class CancelPolarxOrderResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPolarxOrderResponseBody, self).to_map()
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


class CancelPolarxOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelPolarxOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelPolarxOrderResponse, self).to_map()
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
            temp_model = CancelPolarxOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCloudResourceAuthorizedRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None, role_arn=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str
        self.role_arn = role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCloudResourceAuthorizedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class CheckCloudResourceAuthorizedResponseBodyData(TeaModel):
    def __init__(self, authorization_state=None, role_arn=None):
        self.authorization_state = authorization_state  # type: str
        self.role_arn = role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCloudResourceAuthorizedResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_state is not None:
            result['AuthorizationState'] = self.authorization_state
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationState') is not None:
            self.authorization_state = m.get('AuthorizationState')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class CheckCloudResourceAuthorizedResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CheckCloudResourceAuthorizedResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CheckCloudResourceAuthorizedResponseBody, self).to_map()
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
            temp_model = CheckCloudResourceAuthorizedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckCloudResourceAuthorizedResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckCloudResourceAuthorizedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckCloudResourceAuthorizedResponse, self).to_map()
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
            temp_model = CheckCloudResourceAuthorizedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_password=None, account_privilege=None,
                 dbinstance_name=None, dbname=None, region_id=None, security_account_name=None, security_account_password=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.account_privilege = account_privilege  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.dbname = dbname  # type: str
        self.region_id = region_id  # type: str
        self.security_account_name = security_account_name  # type: str
        self.security_account_password = security_account_password  # type: str

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
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupRequest(TeaModel):
    def __init__(self, backup_type=None, dbinstance_name=None, region_id=None):
        self.backup_type = backup_type  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateBackupResponseBodyData(TeaModel):
    def __init__(self, backup_set_id=None):
        self.backup_set_id = backup_set_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        return self


class CreateBackupResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[CreateBackupResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateBackupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = CreateBackupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBackupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBackupResponse, self).to_map()
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
            temp_model = CreateBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBRequest(TeaModel):
    def __init__(self, account_name=None, account_privilege=None, charset=None, dbinstance_name=None,
                 db_description=None, db_name=None, region_id=None, security_account_name=None, security_account_password=None):
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str
        self.charset = charset  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.db_description = db_description  # type: str
        self.db_name = db_name  # type: str
        self.region_id = region_id  # type: str
        self.security_account_name = security_account_name  # type: str
        self.security_account_password = security_account_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class CreateDBResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDBResponse, self).to_map()
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
            temp_model = CreateDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, client_token=None, dbnode_class=None, dbnode_count=None,
                 engine_version=None, is_read_dbinstance=None, network_type=None, pay_type=None, period=None,
                 primary_dbinstance_name=None, region_id=None, resource_group_id=None, used_time=None, vpcid=None, v_switch_id=None,
                 zone_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.client_token = client_token  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_count = dbnode_count  # type: int
        self.engine_version = engine_version  # type: str
        self.is_read_dbinstance = is_read_dbinstance  # type: bool
        self.network_type = network_type  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.primary_dbinstance_name = primary_dbinstance_name  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.used_time = used_time  # type: int
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.is_read_dbinstance is not None:
            result['IsReadDBInstance'] = self.is_read_dbinstance
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.primary_dbinstance_name is not None:
            result['PrimaryDBInstanceName'] = self.primary_dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('IsReadDBInstance') is not None:
            self.is_read_dbinstance = m.get('IsReadDBInstance')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PrimaryDBInstanceName') is not None:
            self.primary_dbinstance_name = m.get('PrimaryDBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
    def __init__(self, dbinstance_name=None, order_id=None, request_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolarxInstanceRequest(TeaModel):
    def __init__(self, client_token=None, description=None, duration=None, instance_series=None, is_auto_renew=None,
                 master_inst_id=None, my_sqlversion=None, pay_type=None, pricing_cycle=None, quantity=None, region_id=None,
                 specification=None, type=None, vpc_id=None, vswitch_id=None, zone_id=None, is_ha=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.duration = duration  # type: int
        self.instance_series = instance_series  # type: str
        self.is_auto_renew = is_auto_renew  # type: bool
        self.master_inst_id = master_inst_id  # type: str
        self.my_sqlversion = my_sqlversion  # type: int
        self.pay_type = pay_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.quantity = quantity  # type: int
        self.region_id = region_id  # type: str
        self.specification = specification  # type: str
        self.type = type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str
        self.is_ha = is_ha  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolarxInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_series is not None:
            result['InstanceSeries'] = self.instance_series
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        if self.master_inst_id is not None:
            result['MasterInstId'] = self.master_inst_id
        if self.my_sqlversion is not None:
            result['MySQLVersion'] = self.my_sqlversion
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.is_ha is not None:
            result['isHa'] = self.is_ha
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceSeries') is not None:
            self.instance_series = m.get('InstanceSeries')
        if m.get('IsAutoRenew') is not None:
            self.is_auto_renew = m.get('IsAutoRenew')
        if m.get('MasterInstId') is not None:
            self.master_inst_id = m.get('MasterInstId')
        if m.get('MySQLVersion') is not None:
            self.my_sqlversion = m.get('MySQLVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('isHa') is not None:
            self.is_ha = m.get('isHa')
        return self


class CreatePolarxInstanceResponseBodyDataDrdsInstanceIdList(TeaModel):
    def __init__(self, drds_instance_id_list=None):
        self.drds_instance_id_list = drds_instance_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolarxInstanceResponseBodyDataDrdsInstanceIdList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id_list is not None:
            result['drdsInstanceIdList'] = self.drds_instance_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drdsInstanceIdList') is not None:
            self.drds_instance_id_list = m.get('drdsInstanceIdList')
        return self


class CreatePolarxInstanceResponseBodyData(TeaModel):
    def __init__(self, drds_instance_id_list=None, order_id=None):
        self.drds_instance_id_list = drds_instance_id_list  # type: CreatePolarxInstanceResponseBodyDataDrdsInstanceIdList
        self.order_id = order_id  # type: long

    def validate(self):
        if self.drds_instance_id_list:
            self.drds_instance_id_list.validate()

    def to_map(self):
        _map = super(CreatePolarxInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id_list is not None:
            result['DrdsInstanceIdList'] = self.drds_instance_id_list.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceIdList') is not None:
            temp_model = CreatePolarxInstanceResponseBodyDataDrdsInstanceIdList()
            self.drds_instance_id_list = temp_model.from_map(m['DrdsInstanceIdList'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreatePolarxInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: CreatePolarxInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreatePolarxInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreatePolarxInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePolarxInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePolarxInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolarxInstanceResponse, self).to_map()
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
            temp_model = CreatePolarxInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolarxOrderRequest(TeaModel):
    def __init__(self, dbinstance_name=None, node_count=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.node_count = node_count  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolarxOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreatePolarxOrderResponseBodyOrderResultList(TeaModel):
    def __init__(self, dbinstance_name=None, order_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolarxOrderResponseBodyOrderResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreatePolarxOrderResponseBody(TeaModel):
    def __init__(self, order_result_list=None, request_id=None):
        self.order_result_list = order_result_list  # type: list[CreatePolarxOrderResponseBodyOrderResultList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.order_result_list:
            for k in self.order_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePolarxOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderResultList'] = []
        if self.order_result_list is not None:
            for k in self.order_result_list:
                result['OrderResultList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.order_result_list = []
        if m.get('OrderResultList') is not None:
            for k in m.get('OrderResultList'):
                temp_model = CreatePolarxOrderResponseBodyOrderResultList()
                self.order_result_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolarxOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePolarxOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolarxOrderResponse, self).to_map()
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
            temp_model = CreatePolarxOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSuperAccountRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_password=None, dbinstance_name=None,
                 region_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSuperAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateSuperAccountResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSuperAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSuperAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSuperAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSuperAccountResponse, self).to_map()
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
            temp_model = CreateSuperAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, account_name=None, dbinstance_name=None, region_id=None, security_account_name=None,
                 security_account_password=None):
        self.account_name = account_name  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str
        self.security_account_name = security_account_name  # type: str
        self.security_account_password = security_account_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccountResponse, self).to_map()
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
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBRequest(TeaModel):
    def __init__(self, dbinstance_name=None, db_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.db_name = db_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDBResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDBResponse, self).to_map()
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
            temp_model = DeleteDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountListRequest(TeaModel):
    def __init__(self, account_name=None, account_type=None, dbinstance_name=None, region_id=None):
        self.account_name = account_name  # type: str
        self.account_type = account_type  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAccountListResponseBodyData(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_privilege=None, account_type=None,
                 dbinstance_name=None, dbname=None, gmt_created=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str
        self.account_type = account_type  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.dbname = dbname  # type: str
        self.gmt_created = gmt_created  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        return self


class DescribeAccountListResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[DescribeAccountListResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAccountListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAccountListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAccountListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAccountListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAccountListResponse, self).to_map()
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
            temp_model = DescribeAccountListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBackupPolicyResponseBodyData(TeaModel):
    def __init__(self, backup_period=None, backup_plan_begin=None, backup_set_retention=None, backup_type=None,
                 backup_way=None, dbinstance_name=None, force_clean_on_high_space_usage=None, is_enabled=None,
                 local_log_retention=None, log_local_retention_space=None, remove_log_retention=None):
        self.backup_period = backup_period  # type: str
        self.backup_plan_begin = backup_plan_begin  # type: str
        self.backup_set_retention = backup_set_retention  # type: int
        self.backup_type = backup_type  # type: str
        self.backup_way = backup_way  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage  # type: int
        self.is_enabled = is_enabled  # type: int
        self.local_log_retention = local_log_retention  # type: int
        self.log_local_retention_space = log_local_retention_space  # type: int
        self.remove_log_retention = remove_log_retention  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[DescribeBackupPolicyResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeBackupPolicyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupSetListRequest(TeaModel):
    def __init__(self, dbinstance_name=None, end_time=None, page_number=None, page_size=None, region_id=None,
                 start_time=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.end_time = end_time  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupSetListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupSetListResponseBodyData(TeaModel):
    def __init__(self, backup_model=None, backup_set_id=None, backup_set_size=None, backup_type=None,
                 begin_time=None, end_time=None, status=None):
        self.backup_model = backup_model  # type: int
        self.backup_set_id = backup_set_id  # type: long
        self.backup_set_size = backup_set_size  # type: long
        self.backup_type = backup_type  # type: int
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupSetListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_model is not None:
            result['BackupModel'] = self.backup_model
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupModel') is not None:
            self.backup_model = m.get('BackupModel')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeBackupSetListResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[DescribeBackupSetListResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupSetListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeBackupSetListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBackupSetListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupSetListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupSetListResponse, self).to_map()
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
            temp_model = DescribeBackupSetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBinaryLogListRequest(TeaModel):
    def __init__(self, dbinstance_name=None, end_time=None, page_number=None, page_size=None, region_id=None,
                 start_time=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.end_time = end_time  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBinaryLogListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBinaryLogListResponseBodyLogList(TeaModel):
    def __init__(self, begin_time=None, created_time=None, download_link=None, end_time=None, file_name=None,
                 id=None, log_size=None, modified_time=None, purge_status=None, upload_host=None, upload_status=None):
        self.begin_time = begin_time  # type: str
        self.created_time = created_time  # type: str
        self.download_link = download_link  # type: str
        self.end_time = end_time  # type: str
        self.file_name = file_name  # type: str
        self.id = id  # type: long
        self.log_size = log_size  # type: long
        self.modified_time = modified_time  # type: str
        self.purge_status = purge_status  # type: int
        self.upload_host = upload_host  # type: str
        self.upload_status = upload_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBinaryLogListResponseBodyLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.purge_status is not None:
            result['PurgeStatus'] = self.purge_status
        if self.upload_host is not None:
            result['UploadHost'] = self.upload_host
        if self.upload_status is not None:
            result['UploadStatus'] = self.upload_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PurgeStatus') is not None:
            self.purge_status = m.get('PurgeStatus')
        if m.get('UploadHost') is not None:
            self.upload_host = m.get('UploadHost')
        if m.get('UploadStatus') is not None:
            self.upload_status = m.get('UploadStatus')
        return self


class DescribeBinaryLogListResponseBody(TeaModel):
    def __init__(self, log_list=None, page_number=None, page_size=None, request_id=None, total_number=None):
        self.log_list = log_list  # type: list[DescribeBinaryLogListResponseBodyLogList]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_number = total_number  # type: int

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBinaryLogListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = DescribeBinaryLogListResponseBodyLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class DescribeBinaryLogListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBinaryLogListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBinaryLogListResponse, self).to_map()
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
            temp_model = DescribeBinaryLogListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCharacterSetRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCharacterSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCharacterSetResponseBodyData(TeaModel):
    def __init__(self, character_set=None, engine=None):
        self.character_set = character_set  # type: list[str]
        self.engine = engine  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCharacterSetResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_set is not None:
            result['CharacterSet'] = self.character_set
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterSet') is not None:
            self.character_set = m.get('CharacterSet')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeCharacterSetResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: DescribeCharacterSetResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCharacterSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeCharacterSetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCharacterSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCharacterSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCharacterSetResponse, self).to_map()
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
            temp_model = DescribeCharacterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs(TeaModel):
    def __init__(self, connection_string=None, port=None, type=None, vpcid=None, v_switch_id=None):
        self.connection_string = connection_string  # type: str
        self.port = port  # type: str
        self.type = type  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes(TeaModel):
    def __init__(self, compute_node_id=None, data_node_id=None, id=None, node_class=None, region_id=None,
                 zone_id=None):
        self.compute_node_id = compute_node_id  # type: str
        self.data_node_id = data_node_id  # type: str
        self.id = id  # type: str
        self.node_class = node_class  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_node_id is not None:
            result['ComputeNodeId'] = self.compute_node_id
        if self.data_node_id is not None:
            result['DataNodeId'] = self.data_node_id
        if self.id is not None:
            result['Id'] = self.id
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComputeNodeId') is not None:
            self.compute_node_id = m.get('ComputeNodeId')
        if m.get('DataNodeId') is not None:
            self.data_node_id = m.get('DataNodeId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstance(TeaModel):
    def __init__(self, commodity_code=None, conn_addrs=None, connection_string=None, create_time=None,
                 dbinstance_type=None, dbnode_class=None, dbnode_count=None, dbnodes=None, dbtype=None, dbversion=None,
                 description=None, engine=None, expire_date=None, expired=None, id=None, kind_code=None,
                 latest_minor_version=None, lock_mode=None, maintain_end_time=None, maintain_start_time=None, minor_version=None,
                 network=None, pay_type=None, port=None, read_dbinstances=None, region_id=None,
                 rights_separation_enabled=None, rights_separation_status=None, status=None, storage_used=None, type=None, vpcid=None,
                 v_switch_id=None, zone_id=None):
        self.commodity_code = commodity_code  # type: str
        self.conn_addrs = conn_addrs  # type: list[DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs]
        self.connection_string = connection_string  # type: str
        self.create_time = create_time  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_count = dbnode_count  # type: int
        self.dbnodes = dbnodes  # type: list[DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes]
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.description = description  # type: str
        self.engine = engine  # type: str
        self.expire_date = expire_date  # type: str
        self.expired = expired  # type: str
        self.id = id  # type: str
        self.kind_code = kind_code  # type: int
        self.latest_minor_version = latest_minor_version  # type: str
        self.lock_mode = lock_mode  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.minor_version = minor_version  # type: str
        self.network = network  # type: str
        self.pay_type = pay_type  # type: str
        self.port = port  # type: str
        self.read_dbinstances = read_dbinstances  # type: list[str]
        self.region_id = region_id  # type: str
        self.rights_separation_enabled = rights_separation_enabled  # type: bool
        self.rights_separation_status = rights_separation_status  # type: str
        self.status = status  # type: str
        self.storage_used = storage_used  # type: long
        self.type = type  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.conn_addrs:
            for k in self.conn_addrs:
                if k:
                    k.validate()
        if self.dbnodes:
            for k in self.dbnodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k in self.conn_addrs:
                result['ConnAddrs'].append(k.to_map() if k else None)
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k in self.dbnodes:
                result['DBNodes'].append(k.to_map() if k else None)
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.id is not None:
            result['Id'] = self.id
        if self.kind_code is not None:
            result['KindCode'] = self.kind_code
        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.network is not None:
            result['Network'] = self.network
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rights_separation_enabled is not None:
            result['RightsSeparationEnabled'] = self.rights_separation_enabled
        if self.rights_separation_status is not None:
            result['RightsSeparationStatus'] = self.rights_separation_status
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k in m.get('ConnAddrs'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k))
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k in m.get('DBNodes'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes()
                self.dbnodes.append(temp_model.from_map(k))
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')
        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RightsSeparationEnabled') is not None:
            self.rights_separation_enabled = m.get('RightsSeparationEnabled')
        if m.get('RightsSeparationStatus') is not None:
            self.rights_separation_status = m.get('RightsSeparationStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(self, dbinstance=None, request_id=None):
        self.dbinstance = dbinstance  # type: DescribeDBInstanceAttributeResponseBodyDBInstance
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbinstance:
            self.dbinstance.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstance') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstance()
            self.dbinstance = temp_model.from_map(m['DBInstance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceConfigRequest(TeaModel):
    def __init__(self, config_name=None, dbinstance_name=None, region_id=None):
        self.config_name = config_name  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceConfigResponseBodyData(TeaModel):
    def __init__(self, config_name=None, config_value=None, db_instance_name=None):
        self.config_name = config_name  # type: str
        self.config_value = config_value  # type: str
        self.db_instance_name = db_instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        return self


class DescribeDBInstanceConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDBInstanceConfigResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceConfigResponseBody, self).to_map()
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
            temp_model = DescribeDBInstanceConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInstanceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceConfigResponse, self).to_map()
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
            temp_model = DescribeDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSSLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceSSLResponseBodyData(TeaModel):
    def __init__(self, cert_common_name=None, sslenabled=None, sslexpired_time=None):
        self.cert_common_name = cert_common_name  # type: str
        self.sslenabled = sslenabled  # type: bool
        self.sslexpired_time = sslexpired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSSLResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        return self


class DescribeDBInstanceSSLResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDBInstanceSSLResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSSLResponseBody, self).to_map()
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
            temp_model = DescribeDBInstanceSSLResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInstanceSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceTDERequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceTDERequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceTDEResponseBodyData(TeaModel):
    def __init__(self, tdestatus=None):
        self.tdestatus = tdestatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceTDEResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class DescribeDBInstanceTDEResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDBInstanceTDEResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceTDEResponseBody, self).to_map()
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
            temp_model = DescribeDBInstanceTDEResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceTDEResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInstanceTDEResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceTDEResponse, self).to_map()
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
            temp_model = DescribeDBInstanceTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceTopologyRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceTopologyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp(TeaModel):
    def __init__(self, connection_string=None, dbinstance_net_type=None, port=None):
        self.connection_string = connection_string  # type: str
        self.dbinstance_net_type = dbinstance_net_type  # type: int
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems(TeaModel):
    def __init__(self, character_type=None, connection_ip=None, dbinstance_conn_type=None,
                 dbinstance_create_time=None, dbinstance_description=None, dbinstance_id=None, dbinstance_name=None,
                 dbinstance_status=None, dbinstance_status_description=None, disk_size=None, engine=None, engine_version=None,
                 lock_mode=None, lock_reason=None, maintain_end_time=None, maintain_start_time=None, max_connections=None,
                 max_iops=None):
        self.character_type = character_type  # type: str
        self.connection_ip = connection_ip  # type: list[DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp]
        self.dbinstance_conn_type = dbinstance_conn_type  # type: int
        self.dbinstance_create_time = dbinstance_create_time  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.dbinstance_status = dbinstance_status  # type: int
        self.dbinstance_status_description = dbinstance_status_description  # type: str
        self.disk_size = disk_size  # type: long
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.lock_mode = lock_mode  # type: int
        self.lock_reason = lock_reason  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.max_connections = max_connections  # type: int
        self.max_iops = max_iops  # type: int

    def validate(self):
        if self.connection_ip:
            for k in self.connection_ip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        result['ConnectionIp'] = []
        if self.connection_ip is not None:
            for k in self.connection_ip:
                result['ConnectionIp'].append(k.to_map() if k else None)
        if self.dbinstance_conn_type is not None:
            result['DBInstanceConnType'] = self.dbinstance_conn_type
        if self.dbinstance_create_time is not None:
            result['DBInstanceCreateTime'] = self.dbinstance_create_time
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_status_description is not None:
            result['DBInstanceStatusDescription'] = self.dbinstance_status_description
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_iops is not None:
            result['MaxIops'] = self.max_iops
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        self.connection_ip = []
        if m.get('ConnectionIp') is not None:
            for k in m.get('ConnectionIp'):
                temp_model = DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp()
                self.connection_ip.append(temp_model.from_map(k))
        if m.get('DBInstanceConnType') is not None:
            self.dbinstance_conn_type = m.get('DBInstanceConnType')
        if m.get('DBInstanceCreateTime') is not None:
            self.dbinstance_create_time = m.get('DBInstanceCreateTime')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStatusDescription') is not None:
            self.dbinstance_status_description = m.get('DBInstanceStatusDescription')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxIops') is not None:
            self.max_iops = m.get('MaxIops')
        return self


class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology(TeaModel):
    def __init__(self, dbinstance_conn_type=None, dbinstance_create_time=None, dbinstance_description=None,
                 dbinstance_id=None, dbinstance_name=None, dbinstance_status=None, dbinstance_status_description=None,
                 dbinstance_storage=None, engine=None, engine_version=None, items=None, lock_mode=None, lock_reason=None,
                 maintain_end_time=None, maintain_start_time=None):
        self.dbinstance_conn_type = dbinstance_conn_type  # type: str
        self.dbinstance_create_time = dbinstance_create_time  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.dbinstance_status = dbinstance_status  # type: int
        self.dbinstance_status_description = dbinstance_status_description  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.items = items  # type: list[DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems]
        self.lock_mode = lock_mode  # type: int
        self.lock_reason = lock_reason  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_conn_type is not None:
            result['DBInstanceConnType'] = self.dbinstance_conn_type
        if self.dbinstance_create_time is not None:
            result['DBInstanceCreateTime'] = self.dbinstance_create_time
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_status_description is not None:
            result['DBInstanceStatusDescription'] = self.dbinstance_status_description
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceConnType') is not None:
            self.dbinstance_conn_type = m.get('DBInstanceConnType')
        if m.get('DBInstanceCreateTime') is not None:
            self.dbinstance_create_time = m.get('DBInstanceCreateTime')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStatusDescription') is not None:
            self.dbinstance_status_description = m.get('DBInstanceStatusDescription')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        return self


class DescribeDBInstanceTopologyResponseBodyData(TeaModel):
    def __init__(self, logic_instance_topology=None):
        self.logic_instance_topology = logic_instance_topology  # type: DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology

    def validate(self):
        if self.logic_instance_topology:
            self.logic_instance_topology.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceTopologyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logic_instance_topology is not None:
            result['LogicInstanceTopology'] = self.logic_instance_topology.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogicInstanceTopology') is not None:
            temp_model = DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology()
            self.logic_instance_topology = temp_model.from_map(m['LogicInstanceTopology'])
        return self


class DescribeDBInstanceTopologyResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDBInstanceTopologyResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceTopologyResponseBody, self).to_map()
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
            temp_model = DescribeDBInstanceTopologyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceTopologyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInstanceTopologyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceTopologyResponse, self).to_map()
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
            temp_model = DescribeDBInstanceTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesRequest, self).to_map()
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


class DescribeDBInstancesResponseBodyDBInstancesNodes(TeaModel):
    def __init__(self, class_code=None, id=None, region_id=None, zone_id=None):
        self.class_code = class_code  # type: str
        self.id = id  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstancesNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_code is not None:
            result['ClassCode'] = self.class_code
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBodyDBInstances(TeaModel):
    def __init__(self, commodity_code=None, create_time=None, dbtype=None, dbversion=None, description=None,
                 engine=None, expire_time=None, expired=None, id=None, lock_mode=None, lock_reason=None, minor_version=None,
                 network=None, node_class=None, node_count=None, nodes=None, pay_type=None, read_dbinstances=None,
                 region_id=None, status=None, storage_used=None, type=None, vpcid=None, zone_id=None):
        self.commodity_code = commodity_code  # type: str
        self.create_time = create_time  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.description = description  # type: str
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.expired = expired  # type: bool
        self.id = id  # type: str
        self.lock_mode = lock_mode  # type: str
        self.lock_reason = lock_reason  # type: str
        self.minor_version = minor_version  # type: str
        self.network = network  # type: str
        self.node_class = node_class  # type: str
        self.node_count = node_count  # type: int
        self.nodes = nodes  # type: list[DescribeDBInstancesResponseBodyDBInstancesNodes]
        self.pay_type = pay_type  # type: str
        self.read_dbinstances = read_dbinstances  # type: list[str]
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.storage_used = storage_used  # type: long
        self.type = type  # type: str
        self.vpcid = vpcid  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.id is not None:
            result['Id'] = self.id
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.network is not None:
            result['Network'] = self.network
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeDBInstancesResponseBodyDBInstancesNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(self, dbinstances=None, page_number=None, page_size=None, request_id=None, total_number=None):
        self.dbinstances = dbinstances  # type: list[DescribeDBInstancesResponseBodyDBInstances]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_number = total_number  # type: int

    def validate(self):
        if self.dbinstances:
            for k in self.dbinstances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k in self.dbinstances:
                result['DBInstances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k in m.get('DBInstances'):
                temp_model = DescribeDBInstancesResponseBodyDBInstances()
                self.dbinstances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBNodePerformanceRequest(TeaModel):
    def __init__(self, character_type=None, dbinstance_name=None, dbnode_ids=None, end_time=None, key=None,
                 region_id=None, start_time=None):
        self.character_type = character_type  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.dbnode_ids = dbnode_ids  # type: str
        self.end_time = end_time  # type: str
        self.key = key  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBNodePerformanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids
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
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue(TeaModel):
    def __init__(self, timestamp=None, value=None):
        self.timestamp = timestamp  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue, self).to_map()
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


class DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPoints(TeaModel):
    def __init__(self, performance_item_value=None):
        self.performance_item_value = performance_item_value  # type: list[DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue]

    def validate(self):
        if self.performance_item_value:
            for k in self.performance_item_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPoints, self).to_map()
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
                temp_model = DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue()
                self.performance_item_value.append(temp_model.from_map(k))
        return self


class DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItem(TeaModel):
    def __init__(self, dbnode_id=None, measurement=None, metric_name=None, points=None):
        self.dbnode_id = dbnode_id  # type: str
        self.measurement = measurement  # type: str
        self.metric_name = metric_name  # type: str
        self.points = points  # type: DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPoints

    def validate(self):
        if self.points:
            self.points.validate()

    def to_map(self):
        _map = super(DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.measurement is not None:
            result['Measurement'] = self.measurement
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.points is not None:
            result['Points'] = self.points.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Points') is not None:
            temp_model = DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPoints()
            self.points = temp_model.from_map(m['Points'])
        return self


class DescribeDBNodePerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(self, performance_item=None):
        self.performance_item = performance_item  # type: list[DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItem]

    def validate(self):
        if self.performance_item:
            for k in self.performance_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBNodePerformanceResponseBodyPerformanceKeys, self).to_map()
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
                temp_model = DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItem()
                self.performance_item.append(temp_model.from_map(k))
        return self


class DescribeDBNodePerformanceResponseBody(TeaModel):
    def __init__(self, dbinstance_name=None, end_time=None, performance_keys=None, request_id=None, start_time=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.end_time = end_time  # type: str
        self.performance_keys = performance_keys  # type: DescribeDBNodePerformanceResponseBodyPerformanceKeys
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        _map = super(DescribeDBNodePerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PerformanceKeys') is not None:
            temp_model = DescribeDBNodePerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m['PerformanceKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBNodePerformanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBNodePerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBNodePerformanceResponse, self).to_map()
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
            temp_model = DescribeDBNodePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbListRequest(TeaModel):
    def __init__(self, dbinstance_name=None, dbname=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.dbname = dbname  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDbListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDbListResponseBodyDataAccounts(TeaModel):
    def __init__(self, account_name=None, account_privilege=None):
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDbListResponseBodyDataAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        return self


class DescribeDbListResponseBodyData(TeaModel):
    def __init__(self, accounts=None, character_set_name=None, dbdescription=None, dbinstance_name=None,
                 dbname=None):
        self.accounts = accounts  # type: list[DescribeDbListResponseBodyDataAccounts]
        self.character_set_name = character_set_name  # type: str
        self.dbdescription = dbdescription  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.dbname = dbname  # type: str

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDbListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name
        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeDbListResponseBodyDataAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')
        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DescribeDbListResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[DescribeDbListResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDbListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDbListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDbListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDbListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDbListResponse, self).to_map()
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
            temp_model = DescribeDbListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDistributeTableListRequest(TeaModel):
    def __init__(self, dbinstance_name=None, db_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.db_name = db_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDistributeTableListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDistributeTableListResponseBodyDataTables(TeaModel):
    def __init__(self, db_key=None, table_name=None, table_type=None, tb_key=None):
        self.db_key = db_key  # type: str
        self.table_name = table_name  # type: str
        self.table_type = table_type  # type: str
        self.tb_key = tb_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDistributeTableListResponseBodyDataTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_key is not None:
            result['DbKey'] = self.db_key
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.tb_key is not None:
            result['TbKey'] = self.tb_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbKey') is not None:
            self.db_key = m.get('DbKey')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('TbKey') is not None:
            self.tb_key = m.get('TbKey')
        return self


class DescribeDistributeTableListResponseBodyData(TeaModel):
    def __init__(self, tables=None):
        self.tables = tables  # type: list[DescribeDistributeTableListResponseBodyDataTables]

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDistributeTableListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = DescribeDistributeTableListResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        return self


class DescribeDistributeTableListResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: DescribeDistributeTableListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDistributeTableListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDistributeTableListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDistributeTableListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDistributeTableListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDistributeTableListResponse, self).to_map()
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
            temp_model = DescribeDistributeTableListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterTemplatesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, param_level=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.param_level = param_level  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.param_level is not None:
            result['ParamLevel'] = self.param_level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeParameterTemplatesResponseBodyDataParameters(TeaModel):
    def __init__(self, checking_code=None, dynamic=None, parameter_description=None, parameter_name=None,
                 parameter_value=None, revisable=None):
        self.checking_code = checking_code  # type: str
        self.dynamic = dynamic  # type: int
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str
        self.revisable = revisable  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterTemplatesResponseBodyDataParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.revisable is not None:
            result['Revisable'] = self.revisable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('Revisable') is not None:
            self.revisable = m.get('Revisable')
        return self


class DescribeParameterTemplatesResponseBodyData(TeaModel):
    def __init__(self, engine=None, engine_version=None, parameter_count=None, parameters=None):
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.parameter_count = parameter_count  # type: int
        self.parameters = parameters  # type: list[DescribeParameterTemplatesResponseBodyDataParameters]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParameterTemplatesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeParameterTemplatesResponseBodyDataParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class DescribeParameterTemplatesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeParameterTemplatesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeParameterTemplatesResponseBody, self).to_map()
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
            temp_model = DescribeParameterTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParameterTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeParameterTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParameterTemplatesResponse, self).to_map()
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
            temp_model = DescribeParameterTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, dbinstance_id=None, param_level=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.param_level = param_level  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.param_level is not None:
            result['ParamLevel'] = self.param_level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeParametersResponseBodyDataConfigParameters(TeaModel):
    def __init__(self, parameter_description=None, parameter_name=None, parameter_value=None):
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersResponseBodyDataConfigParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParametersResponseBodyDataRunningParameters(TeaModel):
    def __init__(self, parameter_description=None, parameter_name=None, parameter_value=None):
        self.parameter_description = parameter_description  # type: str
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersResponseBodyDataRunningParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParametersResponseBodyData(TeaModel):
    def __init__(self, config_parameters=None, engine=None, engine_version=None, running_parameters=None):
        self.config_parameters = config_parameters  # type: list[DescribeParametersResponseBodyDataConfigParameters]
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.running_parameters = running_parameters  # type: list[DescribeParametersResponseBodyDataRunningParameters]

    def validate(self):
        if self.config_parameters:
            for k in self.config_parameters:
                if k:
                    k.validate()
        if self.running_parameters:
            for k in self.running_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParametersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigParameters'] = []
        if self.config_parameters is not None:
            for k in self.config_parameters:
                result['ConfigParameters'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        result['RunningParameters'] = []
        if self.running_parameters is not None:
            for k in self.running_parameters:
                result['RunningParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_parameters = []
        if m.get('ConfigParameters') is not None:
            for k in m.get('ConfigParameters'):
                temp_model = DescribeParametersResponseBodyDataConfigParameters()
                self.config_parameters.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        self.running_parameters = []
        if m.get('RunningParameters') is not None:
            for k in m.get('RunningParameters'):
                temp_model = DescribeParametersResponseBodyDataRunningParameters()
                self.running_parameters.append(temp_model.from_map(k))
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeParametersResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeParametersResponseBody, self).to_map()
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
            temp_model = DescribeParametersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolarxDataNodesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolarxDataNodesRequest, self).to_map()
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


class DescribePolarxDataNodesResponseBodyDBInstanceDataNodes(TeaModel):
    def __init__(self, dbinstance_description=None, dbinstance_id=None, dbinstance_name=None):
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_name = dbinstance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolarxDataNodesResponseBodyDBInstanceDataNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        return self


class DescribePolarxDataNodesResponseBody(TeaModel):
    def __init__(self, dbinstance_data_nodes=None, page_number=None, page_size=None, request_id=None,
                 total_number=None):
        self.dbinstance_data_nodes = dbinstance_data_nodes  # type: list[DescribePolarxDataNodesResponseBodyDBInstanceDataNodes]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_number = total_number  # type: int

    def validate(self):
        if self.dbinstance_data_nodes:
            for k in self.dbinstance_data_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolarxDataNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceDataNodes'] = []
        if self.dbinstance_data_nodes is not None:
            for k in self.dbinstance_data_nodes:
                result['DBInstanceDataNodes'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstance_data_nodes = []
        if m.get('DBInstanceDataNodes') is not None:
            for k in m.get('DBInstanceDataNodes'):
                temp_model = DescribePolarxDataNodesResponseBodyDBInstanceDataNodes()
                self.dbinstance_data_nodes.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class DescribePolarxDataNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePolarxDataNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolarxDataNodesResponse, self).to_map()
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
            temp_model = DescribePolarxDataNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolarxDbInstancesRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, page_number=None, page_size=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolarxDbInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePolarxDbInstancesResponseBodyDbInstancesDbInstance(TeaModel):
    def __init__(self, create_time=None, dbinstance_id=None, dbtype=None, dbversion=None, description=None,
                 engine=None, expire_time=None, lock_mode=None, network=None, node_class=None, node_count=None,
                 pay_type=None, region_id=None, status=None, status_desc=None, storage_used=None, vpcid=None, zone_id=None,
                 lock_reason=None):
        self.create_time = create_time  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.description = description  # type: str
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.lock_mode = lock_mode  # type: str
        self.network = network  # type: str
        self.node_class = node_class  # type: str
        self.node_count = node_count  # type: int
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.status_desc = status_desc  # type: str
        self.storage_used = storage_used  # type: int
        self.vpcid = vpcid  # type: str
        self.zone_id = zone_id  # type: str
        self.lock_reason = lock_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolarxDbInstancesResponseBodyDbInstancesDbInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.network is not None:
            result['Network'] = self.network
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.lock_reason is not None:
            result['lockReason'] = self.lock_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('lockReason') is not None:
            self.lock_reason = m.get('lockReason')
        return self


class DescribePolarxDbInstancesResponseBodyDbInstances(TeaModel):
    def __init__(self, db_instance=None):
        self.db_instance = db_instance  # type: list[DescribePolarxDbInstancesResponseBodyDbInstancesDbInstance]

    def validate(self):
        if self.db_instance:
            for k in self.db_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolarxDbInstancesResponseBodyDbInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DbInstance'] = []
        if self.db_instance is not None:
            for k in self.db_instance:
                result['DbInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.db_instance = []
        if m.get('DbInstance') is not None:
            for k in m.get('DbInstance'):
                temp_model = DescribePolarxDbInstancesResponseBodyDbInstancesDbInstance()
                self.db_instance.append(temp_model.from_map(k))
        return self


class DescribePolarxDbInstancesResponseBody(TeaModel):
    def __init__(self, db_instances=None, page_number=None, page_size=None, request_id=None, success=None,
                 total=None):
        self.db_instances = db_instances  # type: DescribePolarxDbInstancesResponseBodyDbInstances
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: str

    def validate(self):
        if self.db_instances:
            self.db_instances.validate()

    def to_map(self):
        _map = super(DescribePolarxDbInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_instances is not None:
            result['DbInstances'] = self.db_instances.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbInstances') is not None:
            temp_model = DescribePolarxDbInstancesResponseBodyDbInstances()
            self.db_instances = temp_model.from_map(m['DbInstances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribePolarxDbInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePolarxDbInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolarxDbInstancesResponse, self).to_map()
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
            temp_model = DescribePolarxDbInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolarxPgInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, resource_group_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolarxPgInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribePolarxPgInstancesResponseBodyDBInstances(TeaModel):
    def __init__(self, commodity_code=None, create_time=None, dbtype=None, dbversion=None, description=None,
                 engine=None, expire_time=None, expired=None, id=None, lock_mode=None, lock_reason=None, network=None,
                 node_class=None, node_count=None, pay_type=None, region_id=None, status=None, storage_used=None, vpcid=None,
                 zone_id=None):
        self.commodity_code = commodity_code  # type: str
        self.create_time = create_time  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.description = description  # type: str
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.expired = expired  # type: bool
        self.id = id  # type: str
        self.lock_mode = lock_mode  # type: str
        self.lock_reason = lock_reason  # type: str
        self.network = network  # type: str
        self.node_class = node_class  # type: str
        self.node_count = node_count  # type: int
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.storage_used = storage_used  # type: int
        self.vpcid = vpcid  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolarxPgInstancesResponseBodyDBInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.id is not None:
            result['Id'] = self.id
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.network is not None:
            result['Network'] = self.network
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribePolarxPgInstancesResponseBody(TeaModel):
    def __init__(self, dbinstances=None, expire_date=None, page_number=None, page_size=None, request_id=None):
        self.dbinstances = dbinstances  # type: list[DescribePolarxPgInstancesResponseBodyDBInstances]
        self.expire_date = expire_date  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbinstances:
            for k in self.dbinstances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolarxPgInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k in self.dbinstances:
                result['DBInstances'].append(k.to_map() if k else None)
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k in m.get('DBInstances'):
                temp_model = DescribePolarxPgInstancesResponseBodyDBInstances()
                self.dbinstances.append(temp_model.from_map(k))
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolarxPgInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePolarxPgInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolarxPgInstancesResponse, self).to_map()
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
            temp_model = DescribePolarxPgInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
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
    def __init__(self, region_id=None, support_polarx_10=None, support_polarx_20=None, zones=None):
        self.region_id = region_id  # type: str
        self.support_polarx_10 = support_polarx_10  # type: bool
        self.support_polarx_20 = support_polarx_20  # type: bool
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
        if self.support_polarx_10 is not None:
            result['SupportPolarx10'] = self.support_polarx_10
        if self.support_polarx_20 is not None:
            result['SupportPolarx20'] = self.support_polarx_20
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupportPolarx10') is not None:
            self.support_polarx_10 = m.get('SupportPolarx10')
        if m.get('SupportPolarx20') is not None:
            self.support_polarx_20 = m.get('SupportPolarx20')
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
    def __init__(self, code=None, error_code=None, message=None, regions=None, request_id=None, success=None):
        self.code = code  # type: int
        self.error_code = error_code  # type: int
        self.message = message  # type: str
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScaleOutMigrateTaskListRequest(TeaModel):
    def __init__(self, dbinstance_name=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScaleOutMigrateTaskListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
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
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeScaleOutMigrateTaskListResponseBody(TeaModel):
    def __init__(self, progress=None, request_id=None):
        self.progress = progress  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScaleOutMigrateTaskListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScaleOutMigrateTaskListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeScaleOutMigrateTaskListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeScaleOutMigrateTaskListResponse, self).to_map()
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
            temp_model = DescribeScaleOutMigrateTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIpsRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSecurityIpsResponseBodyDataGroupItems(TeaModel):
    def __init__(self, group_name=None, security_iplist=None):
        self.group_name = group_name  # type: str
        self.security_iplist = security_iplist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityIpsResponseBodyDataGroupItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeSecurityIpsResponseBodyData(TeaModel):
    def __init__(self, dbinstance_name=None, group_items=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.group_items = group_items  # type: list[DescribeSecurityIpsResponseBodyDataGroupItems]

    def validate(self):
        if self.group_items:
            for k in self.group_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecurityIpsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['GroupItems'] = []
        if self.group_items is not None:
            for k in self.group_items:
                result['GroupItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.group_items = []
        if m.get('GroupItems') is not None:
            for k in m.get('GroupItems'):
                temp_model = DescribeSecurityIpsResponseBodyDataGroupItems()
                self.group_items.append(temp_model.from_map(k))
        return self


class DescribeSecurityIpsResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: DescribeSecurityIpsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeSecurityIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeSecurityIpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSecurityIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSecurityIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecurityIpsResponse, self).to_map()
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
            temp_model = DescribeSecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None, start_time=None,
                 status=None, task_action=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_action = task_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class DescribeTasksResponseBodyItems(TeaModel):
    def __init__(self, begin_time=None, dbname=None, finish_time=None, progress=None, progress_info=None,
                 scale_out_token=None, status=None, task_action=None, task_error_code=None, task_error_message=None, task_id=None):
        self.begin_time = begin_time  # type: str
        self.dbname = dbname  # type: str
        self.finish_time = finish_time  # type: str
        self.progress = progress  # type: str
        self.progress_info = progress_info  # type: str
        self.scale_out_token = scale_out_token  # type: str
        self.status = status  # type: str
        self.task_action = task_action  # type: str
        self.task_error_code = task_error_code  # type: str
        self.task_error_message = task_error_message  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTasksResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.progress_info is not None:
            result['ProgressInfo'] = self.progress_info
        if self.scale_out_token is not None:
            result['ScaleOutToken'] = self.scale_out_token
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_error_code is not None:
            result['TaskErrorCode'] = self.task_error_code
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProgressInfo') is not None:
            self.progress_info = m.get('ProgressInfo')
        if m.get('ScaleOutToken') is not None:
            self.scale_out_token = m.get('ScaleOutToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskErrorCode') is not None:
            self.task_error_code = m.get('TaskErrorCode')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.items = items  # type: list[DescribeTasksResponseBodyItems]
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTasksResponseBody, self).to_map()
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
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTasksResponse, self).to_map()
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
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserEncryptionKeyListRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUserEncryptionKeyListResponseBodyData(TeaModel):
    def __init__(self, key_ids=None):
        self.key_ids = key_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyIds') is not None:
            self.key_ids = m.get('KeyIds')
        return self


class DescribeUserEncryptionKeyListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeUserEncryptionKeyListResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListResponseBody, self).to_map()
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
            temp_model = DescribeUserEncryptionKeyListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserEncryptionKeyListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserEncryptionKeyListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserEncryptionKeyListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolarxCommodityRequest(TeaModel):
    def __init__(self, dbinstance_name=None, order_type=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.order_type = order_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolarxCommodityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPolarxCommodityResponseBodyComponentList(TeaModel):
    def __init__(self, name=None, type=None, values=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolarxCommodityResponseBodyComponentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetPolarxCommodityResponseBodyDBInstanceConnAddrs(TeaModel):
    def __init__(self, connection_string=None, port=None, type=None, vpcid=None, v_switch_id=None):
        self.connection_string = connection_string  # type: str
        self.port = port  # type: str
        self.type = type  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolarxCommodityResponseBodyDBInstanceConnAddrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class GetPolarxCommodityResponseBodyDBInstanceDBNodes(TeaModel):
    def __init__(self, id=None, node_class=None, region_id=None, zone_id=None):
        self.id = id  # type: str
        self.node_class = node_class  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolarxCommodityResponseBodyDBInstanceDBNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetPolarxCommodityResponseBodyDBInstance(TeaModel):
    def __init__(self, commodity_code=None, conn_addrs=None, connection_string=None, create_time=None,
                 dbinstance_type=None, dbnode_class=None, dbnode_count=None, dbnodes=None, dbtype=None, dbversion=None,
                 description=None, engine=None, expire_date=None, expired=None, id=None, latest_minor_version=None,
                 lock_mode=None, maintain_end_time=None, maintain_start_time=None, minor_version=None, network=None,
                 pay_type=None, port=None, read_dbinstances=None, region_id=None, status=None, storage_used=None, type=None,
                 vpcid=None, v_switch_id=None, zone_id=None):
        self.commodity_code = commodity_code  # type: str
        self.conn_addrs = conn_addrs  # type: list[GetPolarxCommodityResponseBodyDBInstanceConnAddrs]
        self.connection_string = connection_string  # type: str
        self.create_time = create_time  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.dbnode_class = dbnode_class  # type: str
        self.dbnode_count = dbnode_count  # type: int
        self.dbnodes = dbnodes  # type: list[GetPolarxCommodityResponseBodyDBInstanceDBNodes]
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.description = description  # type: str
        self.engine = engine  # type: str
        self.expire_date = expire_date  # type: str
        self.expired = expired  # type: str
        self.id = id  # type: str
        self.latest_minor_version = latest_minor_version  # type: str
        self.lock_mode = lock_mode  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.minor_version = minor_version  # type: str
        self.network = network  # type: str
        self.pay_type = pay_type  # type: str
        self.port = port  # type: str
        self.read_dbinstances = read_dbinstances  # type: list[str]
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.storage_used = storage_used  # type: long
        self.type = type  # type: str
        self.vpcid = vpcid  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.conn_addrs:
            for k in self.conn_addrs:
                if k:
                    k.validate()
        if self.dbnodes:
            for k in self.dbnodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPolarxCommodityResponseBodyDBInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k in self.conn_addrs:
                result['ConnAddrs'].append(k.to_map() if k else None)
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k in self.dbnodes:
                result['DBNodes'].append(k.to_map() if k else None)
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.id is not None:
            result['Id'] = self.id
        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.network is not None:
            result['Network'] = self.network
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k in m.get('ConnAddrs'):
                temp_model = GetPolarxCommodityResponseBodyDBInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k))
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k in m.get('DBNodes'):
                temp_model = GetPolarxCommodityResponseBodyDBInstanceDBNodes()
                self.dbnodes.append(temp_model.from_map(k))
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetPolarxCommodityResponseBody(TeaModel):
    def __init__(self, component_list=None, dbinstance=None, request_id=None):
        self.component_list = component_list  # type: list[GetPolarxCommodityResponseBodyComponentList]
        self.dbinstance = dbinstance  # type: GetPolarxCommodityResponseBodyDBInstance
        self.request_id = request_id  # type: str

    def validate(self):
        if self.component_list:
            for k in self.component_list:
                if k:
                    k.validate()
        if self.dbinstance:
            self.dbinstance.validate()

    def to_map(self):
        _map = super(GetPolarxCommodityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentList'] = []
        if self.component_list is not None:
            for k in self.component_list:
                result['ComponentList'].append(k.to_map() if k else None)
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.component_list = []
        if m.get('ComponentList') is not None:
            for k in m.get('ComponentList'):
                temp_model = GetPolarxCommodityResponseBodyComponentList()
                self.component_list.append(temp_model.from_map(k))
        if m.get('DBInstance') is not None:
            temp_model = GetPolarxCommodityResponseBodyDBInstance()
            self.dbinstance = temp_model.from_map(m['DBInstance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolarxCommodityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPolarxCommodityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPolarxCommodityResponse, self).to_map()
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
            temp_model = GetPolarxCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, dbinstance_name=None, region_id=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

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
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountDescriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAccountDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceClassRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_name=None, region_id=None, target_dbinstance_class=None):
        self.client_token = client_token  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str
        self.target_dbinstance_class = target_dbinstance_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceClassRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.target_dbinstance_class is not None:
            result['TargetDBInstanceClass'] = self.target_dbinstance_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TargetDBInstanceClass') is not None:
            self.target_dbinstance_class = m.get('TargetDBInstanceClass')
        return self


class ModifyDBInstanceClassResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceClassResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceClassResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBInstanceClassResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceClassResponse, self).to_map()
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
            temp_model = ModifyDBInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConfigRequest(TeaModel):
    def __init__(self, config_name=None, config_value=None, dbinstance_name=None, region_id=None):
        self.config_name = config_name  # type: str
        self.config_value = config_value  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDBInstanceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConfigResponseBody, self).to_map()
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


class ModifyDBInstanceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBInstanceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceConfigResponse, self).to_map()
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
            temp_model = ModifyDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(self, dbinstance_description=None, dbinstance_name=None, region_id=None):
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDBInstanceDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseDescriptionRequest(TeaModel):
    def __init__(self, dbinstance_name=None, db_description=None, db_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.db_description = db_description  # type: str
        self.db_name = db_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDatabaseDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDatabaseDescriptionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDatabaseDescriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDatabaseDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDatabaseDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDatabaseDescriptionResponse, self).to_map()
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
            temp_model = ModifyDatabaseDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParameterRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, param_level=None, parameters=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.param_level = param_level  # type: str
        self.parameters = parameters  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.param_level is not None:
            result['ParamLevel'] = self.param_level
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyParameterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParameterResponseBody, self).to_map()
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


class ModifyParameterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyParameterResponse, self).to_map()
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
            temp_model = ModifyParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(self, dbinstance_name=None, group_name=None, modify_mode=None, region_id=None,
                 security_iplist=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.group_name = group_name  # type: str
        self.modify_mode = modify_mode  # type: str
        self.region_id = region_id  # type: str
        self.security_iplist = security_iplist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySecurityIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifySecurityIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(self, current_connection_string=None, dbinstance_name=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.current_connection_string = current_connection_string  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstancePublicConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
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
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleaseInstancePublicConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBackupPolicyRequest(TeaModel):
    def __init__(self, backup_period=None, backup_plan_begin=None, backup_set_retention=None, backup_type=None,
                 backup_way=None, dbinstance_name=None, force_clean_on_high_space_usage=None, is_enabled=None,
                 local_log_retention=None, log_local_retention_space=None, region_id=None, remove_log_retention=None):
        self.backup_period = backup_period  # type: str
        self.backup_plan_begin = backup_plan_begin  # type: str
        self.backup_set_retention = backup_set_retention  # type: int
        self.backup_type = backup_type  # type: str
        self.backup_way = backup_way  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage  # type: int
        self.is_enabled = is_enabled  # type: int
        self.local_log_retention = local_log_retention  # type: int
        self.log_local_retention_space = log_local_retention_space  # type: int
        self.region_id = region_id  # type: str
        self.remove_log_retention = remove_log_retention  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        return self


class UpdateBackupPolicyResponseBodyData(TeaModel):
    def __init__(self, backup_period=None, backup_plan_begin=None, backup_set_retention=None, backup_type=None,
                 backup_way=None, dbinstance_name=None, force_clean_on_high_space_usage=None, is_enabled=None,
                 local_log_retention=None, log_local_retention_space=None, remove_log_retention=None):
        self.backup_period = backup_period  # type: str
        self.backup_plan_begin = backup_plan_begin  # type: str
        self.backup_set_retention = backup_set_retention  # type: int
        self.backup_type = backup_type  # type: str
        self.backup_way = backup_way  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage  # type: int
        self.is_enabled = is_enabled  # type: int
        self.local_log_retention = local_log_retention  # type: int
        self.log_local_retention_space = log_local_retention_space  # type: int
        self.remove_log_retention = remove_log_retention  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBackupPolicyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        return self


class UpdateBackupPolicyResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[UpdateBackupPolicyResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = UpdateBackupPolicyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBackupPolicyResponse, self).to_map()
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
            temp_model = UpdateBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDBInstanceSSLRequest(TeaModel):
    def __init__(self, cert_common_name=None, dbinstance_name=None, enable_ssl=None, region_id=None):
        self.cert_common_name = cert_common_name  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.enable_ssl = enable_ssl  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDBInstanceSSLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateDBInstanceSSLResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDBInstanceSSLResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateDBInstanceSSLResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateDBInstanceSSLResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateDBInstanceSSLResponseBody, self).to_map()
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
            temp_model = UpdateDBInstanceSSLResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDBInstanceSSLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDBInstanceSSLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDBInstanceSSLResponse, self).to_map()
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
            temp_model = UpdateDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDBInstanceTDERequest(TeaModel):
    def __init__(self, dbinstance_name=None, encryption_key=None, region_id=None, role_arn=None, tdestatus=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.encryption_key = encryption_key  # type: str
        self.region_id = region_id  # type: str
        self.role_arn = role_arn  # type: str
        self.tdestatus = tdestatus  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDBInstanceTDERequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class UpdateDBInstanceTDEResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDBInstanceTDEResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateDBInstanceTDEResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateDBInstanceTDEResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateDBInstanceTDEResponseBody, self).to_map()
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
            temp_model = UpdateDBInstanceTDEResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDBInstanceTDEResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDBInstanceTDEResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDBInstanceTDEResponse, self).to_map()
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
            temp_model = UpdateDBInstanceTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolarDBXInstanceNodeRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_name=None, db_instance_node_count=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.db_instance_node_count = db_instance_node_count  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolarDBXInstanceNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_instance_node_count is not None:
            result['DbInstanceNodeCount'] = self.db_instance_node_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbInstanceNodeCount') is not None:
            self.db_instance_node_count = m.get('DbInstanceNodeCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdatePolarDBXInstanceNodeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePolarDBXInstanceNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePolarDBXInstanceNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePolarDBXInstanceNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePolarDBXInstanceNodeResponse, self).to_map()
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
            temp_model = UpdatePolarDBXInstanceNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceKernelVersionRequest(TeaModel):
    def __init__(self, dbinstance_name=None, region_id=None, switch_time=None, upgrade_time=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.region_id = region_id  # type: str
        self.switch_time = switch_time  # type: str
        self.upgrade_time = upgrade_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBInstanceKernelVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('UpgradeTime') is not None:
            self.upgrade_time = m.get('UpgradeTime')
        return self


class UpgradeDBInstanceKernelVersionResponseBody(TeaModel):
    def __init__(self, dbinstance_name=None, request_id=None, target_minor_version=None, task_id=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.request_id = request_id  # type: str
        self.target_minor_version = target_minor_version  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeDBInstanceKernelVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeDBInstanceKernelVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeDBInstanceKernelVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeDBInstanceKernelVersionResponse, self).to_map()
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
            temp_model = UpgradeDBInstanceKernelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


