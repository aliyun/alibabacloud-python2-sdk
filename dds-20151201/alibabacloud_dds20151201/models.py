# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateNodePrivateNetworkAddressRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, dbinstance_id=None, node_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None,
                 zone_id=None):
        # The name of the account.
        # 
        # > * The name must be 4 to 16 characters in length and can contain lowercase letters, digits, and underscores (\_). It must start with a lowercase letter.
        # > * You need to set the account name and password only when you apply for an endpoint for a shard or Configserver node for the first time. In this case, the account name and password are used for all shard and Configserver nodes.
        # > * The permissions of this account are fixed to read-only.
        self.account_name = account_name  # type: str
        # The password of the account.
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `!#$%^&*()_+-=`
        # *   The password must be 8 to 32 characters in length.
        self.account_password = account_password  # type: str
        # The ID of the sharded cluster instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the shard or Configserver node.
        # 
        # >  You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the ID of the shard or Configserver node.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The zone ID of the instance.
        # 
        # >  You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateNodePrivateNetworkAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class AllocateNodePrivateNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateNodePrivateNetworkAddressResponseBody, self).to_map()
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


class AllocateNodePrivateNetworkAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllocateNodePrivateNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocateNodePrivateNetworkAddressResponse, self).to_map()
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
            temp_model = AllocateNodePrivateNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocatePublicNetworkAddressRequest(TeaModel):
    def __init__(self, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance
        # 
        # > If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the mongos, shard, or Configserver node in the sharded cluster instance. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to view the ID of the mongos, shard, or Configserver node.
        # 
        # > This parameter is required only when you specify the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocatePublicNetworkAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class AllocatePublicNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocatePublicNetworkAddressResponseBody, self).to_map()
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


class AllocatePublicNetworkAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllocatePublicNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocatePublicNetworkAddressResponse, self).to_map()
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
            temp_model = AllocatePublicNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCloudResourceAuthorizedRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, target_region_id=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the region ID of the instance.
        self.target_region_id = target_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCloudResourceAuthorizedRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        return self


class CheckCloudResourceAuthorizedResponseBody(TeaModel):
    def __init__(self, authorization_state=None, request_id=None, role_arn=None):
        # Indicates whether KMS keys are authorized to ApsaraDB for MongoDB instances. Valid values:
        # 
        # *   **0**: KMS keys are not authorized.
        # *   **1**: KMS keys are authorized.
        # *   **2**: KMS is not enabled.
        self.authorization_state = authorization_state  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The role information of the authorized Alibaba Resource Name (ARN).
        # 
        # >  This parameter is returned only when the value of the **AuthorizationState** parameter is **1**.
        self.role_arn = role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCloudResourceAuthorizedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_state is not None:
            result['AuthorizationState'] = self.authorization_state
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationState') is not None:
            self.authorization_state = m.get('AuthorizationState')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class CheckCloudResourceAuthorizedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckCloudResourceAuthorizedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CheckCloudResourceAuthorizedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRecoveryConditionRequest(TeaModel):
    def __init__(self, backup_id=None, database_names=None, owner_account=None, owner_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, restore_time=None, security_token=None,
                 source_dbinstance=None):
        # The point in time to which the instance is restored. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > * The value can be any time within the past seven days. The time must be earlier than the current time, but later than the time when the instance was created.
        # > * You must specify one of the RestoreTime and **BackupId** parameters.
        self.backup_id = backup_id  # type: str
        # The ID of the source instance.
        self.database_names = database_names  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the backup.
        # 
        # > * You can call the [DescribeBackups](~~62172~~) operation to query the ID of the backup.
        # > * You must specify one of the **RestoreTime** and BackupId parameters.
        # > * This parameter is not applicable to sharded cluster instances.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The name of the source database. The value is a JSON array.
        # 
        # >  If you do not specify this parameter, all databases are restored.
        self.restore_time = restore_time  # type: str
        self.security_token = security_token  # type: str
        # The operation that you want to perform. Set the value to **CheckRecoveryCondition**.
        self.source_dbinstance = source_dbinstance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckRecoveryConditionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names
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
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.source_dbinstance is not None:
            result['SourceDBInstance'] = self.source_dbinstance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')
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
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SourceDBInstance') is not None:
            self.source_dbinstance = m.get('SourceDBInstance')
        return self


class CheckRecoveryConditionResponseBody(TeaModel):
    def __init__(self, dbinstance_name=None, is_valid=None, request_id=None):
        # The ID of the request.
        self.dbinstance_name = dbinstance_name  # type: str
        # The ID of the instance.
        self.is_valid = is_valid  # type: bool
        # The ID of the resource group.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckRecoveryConditionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckRecoveryConditionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckRecoveryConditionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckRecoveryConditionResponse, self).to_map()
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
            temp_model = CheckRecoveryConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupRequest(TeaModel):
    def __init__(self, backup_method=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The backup method of the instance. Default value: Physical. Valid values:
        # 
        # *   **Logical**\
        # *   **Physical**\
        # 
        # >  Only replica set instances and sharded cluster instances support this parameter. You do not need to specify this parameter for standalone instances. All standalone instances use snapshot backup.
        self.backup_method = backup_method  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateBackupResponseBody(TeaModel):
    def __init__(self, backup_id=None, request_id=None):
        # The ID of the backup set.
        self.backup_id = backup_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBackupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDBInstanceRequestTag, self).to_map()
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


class CreateDBInstanceRequest(TeaModel):
    def __init__(self, account_password=None, auto_renew=None, backup_id=None, business_info=None, charge_type=None,
                 client_token=None, cluster_id=None, coupon_no=None, dbinstance_class=None, dbinstance_description=None,
                 dbinstance_storage=None, database_names=None, encrypted=None, encryption_key=None, engine=None, engine_version=None,
                 global_security_group_ids=None, hidden_zone_id=None, network_type=None, owner_account=None, owner_id=None, period=None,
                 provisioned_iops=None, readonly_replicas=None, region_id=None, replication_factor=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, restore_time=None, secondary_zone_id=None, security_iplist=None,
                 security_token=None, src_dbinstance_id=None, storage_engine=None, storage_type=None, tag=None, v_switch_id=None,
                 vpc_id=None, zone_id=None):
        # The network type of the instance. Set the value to VPC.
        self.account_password = account_password  # type: str
        # The storage engine of the instance. Default value: WiredTiger. Valid values:
        # 
        # *   **WiredTiger**\
        # *   **RocksDB**\
        # *   **TerarkDB**\
        # 
        # >  *   When you call this operation to clone an instance or restore an instance from the recycle bin, set the value of this parameter to the storage engine of the source instance.
        # >  *   For more information about the limits on database versions and storage engines, see [MongoDB versions and storage engines](~~61906~~).
        self.auto_renew = auto_renew  # type: str
        # Specifies whether to enable auto-renewal for the instance. Default value: false. Valid values:
        # 
        # *   **true**: The instance is automatically renewed.
        # *   **false**: The instance is manually renewed.
        # 
        # > This parameter is valid and optional when the **ChargeType** parameter is set to **PrePaid**.
        self.backup_id = backup_id  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.business_info = business_info  # type: str
        # The ID of the VPC.
        self.charge_type = charge_type  # type: str
        # The version of the database engine. Valid values:
        # 
        # *   **6.0**\
        # *   **5.0**\
        # *   **4.4**\
        # *   **4.2**\
        # *   **4.0**\
        # 
        # > When you call this operation to clone an instance or restore an instance from the recycle bin, set the value of this parameter to the engine version of the source instance.
        self.client_token = client_token  # type: str
        # cn
        self.cluster_id = cluster_id  # type: str
        # The number of **read-only nodes** in the replica set instance. Default value: **0**. Valid values: **0** to **5**.
        self.coupon_no = coupon_no  # type: str
        # The IP addresses in an IP address whitelist. Multiple IP addresses are separated by commas (,), and each IP address in the IP address whitelist must be unique. The following types of values are supported:
        # 
        # *   0.0.0.0/0
        # *   IP addresses, such as 10.23.12.24.
        # *   Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.0/24. In this case, /24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32.
        # 
        # > *   A maximum of 1,000 IP addresses or CIDR blocks can be configured for each instance.
        # > *   If you enter 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. Proceed with caution.
        self.dbinstance_class = dbinstance_class  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PostPaid**: pay-as-you-go. This is the default value.
        # *   **PrePaid**: subscription.
        # 
        # > If you set this parameter to **PrePaid**, you must also specify the **Period** parameter.
        self.dbinstance_description = dbinstance_description  # type: str
        # The password of the root account. The password must meet the following requirements:
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   Special characters include ! # $ % ^ & \* ( ) \_ + - =\
        # *   The password of the account must be 8 to 32 characters in length.
        self.dbinstance_storage = dbinstance_storage  # type: int
        # The number of **nodes** in the replica set instance. Default value: 3. Valid values:
        # 
        # *   **3**\
        # *   **5**\
        # *   **7**\
        self.database_names = database_names  # type: str
        self.encrypted = encrypted  # type: bool
        self.encryption_key = encryption_key  # type: str
        # The storage capacity of the instance. Unit: GB.
        # 
        # The values that can be specified for this parameter vary based on the instance types. For more information, see [Replica set instance types](~~311410~~).
        self.engine = engine  # type: str
        # The name of the instance. The name of the instance must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain digits, letters, underscores (\_), and hyphens (-).
        # *   The name must be 2 to 256 characters in length.
        self.engine_version = engine_version  # type: str
        # The ID of the request.
        self.global_security_group_ids = global_security_group_ids  # type: str
        # Template for global IP whitelist of the instance, multiple IP whitelist templates should be separated by a comma (,) in English and cannot be repeated. (In function gray scale).
        self.hidden_zone_id = hidden_zone_id  # type: str
        # The ID of the source instance.
        # 
        # > When you call this operation to clone an instance, this parameter is required. The **BackupId** or **RestoreTime** parameter is also required. When you call this operation to restore an instance from the recycle bin, this parameter is required. The **BackupId** or **RestoreTime** parameter is not required.
        self.network_type = network_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the vSwitch to which the instance is connected.
        self.period = period  # type: int
        self.provisioned_iops = provisioned_iops  # type: long
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd1** :ESSD PL1.
        # *   **cloud_essd2**: ESSD PL2.
        # *   **cloud_essd3**: ESSD PL3.
        # *   **local_ssd**: local SSD.
        self.readonly_replicas = readonly_replicas  # type: str
        # The database engine of the instance. The value is fixed as **MongoDB**.
        self.region_id = region_id  # type: str
        # The ID of the dedicated cluster to which the instance belongs.
        self.replication_factor = replication_factor  # type: str
        # The zone where the secondary node resides for multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G.
        # *   **cn-hangzhou-h**: Hangzhou Zone H.
        # *   **cn-hangzhou-i**: Hangzhou Zone I.
        # *   **cn-hongkong-b**: Hongkong Zone B.
        # *   **cn-hongkong-c**: Hongkong Zone C.
        # *   **cn-hongkong-d**: Hongkong Zone D.
        # *   **cn-wulanchabu-a**: Ulanqab Zone A.
        # *   **cn-wulanchabu-b**: Ulanqab Zone B.
        # *   **cn-wulanchabu-c**: Ulanqab Zone C.
        # *   **ap-southeast-1a**: Singapore Zone A.
        # *   **ap-southeast-1b**: Singapore Zone B.
        # *   **ap-southeast-1c**: Singapore Zone C.
        # *   **ap-southeast-5a**: Jakarta Zone A.
        # *   **ap-southeast-5b**: Jakarta Zone B.
        # *   **ap-southeast-5c**: Jakarta Zone C.
        # *   **eu-central-1a**: Frankfurt Zone A.
        # *   **eu-central-1b**: Frankfurt Zone B.
        # *   **eu-central-1c**: Frankfurt Zone C.
        # 
        # >  *   This parameter is valid and required when the **EngineVersion** parameter is set to **4.4** or **5.0**.
        # >  *   The value of this parameter cannot be the same as the value of the **ZoneId** or **HiddenZoneId** parameter.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The name of the database.
        # 
        # > When you call this operation to clone an instance, you can set this parameter to specify the database to clone. Otherwise, all databases of the instance are cloned.
        self.restore_time = restore_time  # type: str
        # cn
        self.secondary_zone_id = secondary_zone_id  # type: str
        # The subscription period of the instance. Unit: months.
        # 
        # Valid values: **1** to **9**, **12**, **24**, **36**, and **60**.
        # 
        # > When you set the **ChargeType** parameter to **PrePaid**, this parameter is valid and required.
        self.security_iplist = security_iplist  # type: str
        self.security_token = security_token  # type: str
        # The business information. This is an additional parameter.
        self.src_dbinstance_id = src_dbinstance_id  # type: str
        # The ID of the resource group to which the instance belongs.
        self.storage_engine = storage_engine  # type: str
        # The zone where the hidden node resides for multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G.
        # *   **cn-hangzhou-h**: Hangzhou Zone H.
        # *   **cn-hangzhou-i**: Hangzhou Zone I.
        # *   **cn-hongkong-b**: Hongkong Zone B.
        # *   **cn-hongkong-c**: Hongkong Zone C.
        # *   **cn-hongkong-d**: Hongkong Zone D.
        # *   **cn-wulanchabu-a**: Ulanqab Zone A.
        # *   **cn-wulanchabu-b**: Ulanqab Zone B.
        # *   **cn-wulanchabu-c**: Ulanqab Zone C.
        # *   **ap-southeast-1a**: Singapore Zone A.
        # *   **ap-southeast-1b**: Singapore Zone B.
        # *   **ap-southeast-1c**: Singapore Zone C.
        # *   **ap-southeast-5a**: Jakarta Zone A.
        # *   **ap-southeast-5b**: Jakarta Zone B.
        # *   **ap-southeast-5c**: Jakarta Zone C.
        # *   **eu-central-1a**: Frankfurt Zone A.
        # *   **eu-central-1b**: Frankfurt Zone B.
        # *   **eu-central-1c**: Frankfurt Zone C.
        # 
        # >  *   This parameter is valid and required when the **EngineVersion** parameter is set to **4.4** or **5.0**.
        # >  *   The value of this parameter cannot be the same as the value of the **ZoneId** or **SecondaryZoneId** parameter.
        self.storage_type = storage_type  # type: str
        self.tag = tag  # type: list[CreateDBInstanceRequestTag]
        # The point in time to which the instance is restored, which must be within seven days. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format (UTC time).
        # 
        # > When you call this operation to restore an instance to the specified time, this parameter is required. The **SrcDBInstanceId** parameter is also required.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the backup set. You can call the [DescribeBackups](~~62172~~) operation to query the backup set ID.
        # 
        # > When you call this operation to clone an instance based on the backup set, this parameter is required. The **SrcDBInstanceId** parameter is also required.
        self.vpc_id = vpc_id  # type: str
        # The instance type. You can also call the [DescribeAvailableResource](~~149719~~) operation to query the instance type.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.global_security_group_ids is not None:
            result['GlobalSecurityGroupIds'] = self.global_security_group_ids
        if self.hidden_zone_id is not None:
            result['HiddenZoneId'] = self.hidden_zone_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id
        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('GlobalSecurityGroupIds') is not None:
            self.global_security_group_ids = m.get('GlobalSecurityGroupIds')
        if m.get('HiddenZoneId') is not None:
            self.hidden_zone_id = m.get('HiddenZoneId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')
        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None, request_id=None):
        # data.dbInstanceId
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the instance.
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


class CreateGlobalSecurityIPGroupRequest(TeaModel):
    def __init__(self, gip_list=None, global_ig_name=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.gip_list = gip_list  # type: str
        self.global_ig_name = global_ig_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGlobalSecurityIPGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gip_list is not None:
            result['GIpList'] = self.gip_list
        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')
        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup(TeaModel):
    def __init__(self, gip_list=None, global_ig_name=None, global_security_group_id=None, region_id=None):
        self.gip_list = gip_list  # type: str
        self.global_ig_name = global_ig_name  # type: str
        self.global_security_group_id = global_security_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gip_list is not None:
            result['GIpList'] = self.gip_list
        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')
        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateGlobalSecurityIPGroupResponseBody(TeaModel):
    def __init__(self, global_security_ipgroup=None, request_id=None):
        self.global_security_ipgroup = global_security_ipgroup  # type: list[CreateGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.global_security_ipgroup:
            for k in self.global_security_ipgroup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateGlobalSecurityIPGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GlobalSecurityIPGroup'] = []
        if self.global_security_ipgroup is not None:
            for k in self.global_security_ipgroup:
                result['GlobalSecurityIPGroup'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.global_security_ipgroup = []
        if m.get('GlobalSecurityIPGroup') is not None:
            for k in m.get('GlobalSecurityIPGroup'):
                temp_model = CreateGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup()
                self.global_security_ipgroup.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGlobalSecurityIPGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGlobalSecurityIPGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGlobalSecurityIPGroupResponse, self).to_map()
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
            temp_model = CreateGlobalSecurityIPGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNodeRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, auto_pay=None, business_info=None,
                 client_token=None, coupon_no=None, dbinstance_id=None, node_class=None, node_storage=None, node_type=None,
                 owner_account=None, owner_id=None, readonly_replicas=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None, shard_direct=None):
        # The username of the account. The username must meet the following requirements:
        # 
        # * The username starts with a lowercase letter.
        # * The username contains lowercase letters, digits, and underscores (\_).
        # * The username is 4 to 16 characters in length.
        # 
        # > * Keywords cannot be used as account usernames.
        # > * The permissions of this account are fixed at read-only.
        # > * The username and password are required to be set only when you apply for an endpoint for the shard node for the first time.
        self.account_name = account_name  # type: str
        # The password of the account. The password must meet the following requirements:
        # 
        # * The password contains at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters.
        # * These special characters include ! @ # $ % ^ & \* ( ) \_ + - =\
        # * The password is 8 to 32 characters in length.
        # 
        # >  The account password of the shard node cannot be reset.
        self.account_password = account_password  # type: str
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # 
        # *   **true**: enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. You can perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > **Orders**. On the **Orders** page, find the order and complete the payment.********\
        # 
        # >  This parameter is required when the billing method of the instance is subscription.
        self.auto_pay = auto_pay  # type: bool
        # The business information. This is an additional parameter.
        self.business_info = business_info  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The coupon code. Default value: **youhuiquan\_promotion\_option\_id\_for\_blank**.
        self.coupon_no = coupon_no  # type: str
        # The ID of the sharded cluster instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The specifications of the shard or mongos node. For more information, see [Instance types](~~57141~~).
        self.node_class = node_class  # type: str
        # The disk capacity of the node. Unit: GB.
        # 
        # Valid values: **10** to **2000**. The value must be a multiple of 10. Unit: GB.
        # 
        # >  This parameter is required if the NodeType parameter is set to **shard**.
        self.node_storage = node_storage  # type: int
        # The type of the node. Valid values:
        # 
        # *   **shard**: shard node
        # *   **mongos**: mongos node
        self.node_type = node_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of read-only nodes in the shard node.
        # 
        # Valid values: **0** to **5**. The value must be an integer. Default value: **0**.
        # 
        # >  This parameter is available only for ApsaraDB for MongoDB instances that are purchased on the China site (aliyun.com).
        self.readonly_replicas = readonly_replicas  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # Specifies whether to apply for an endpoint for the shard node. Default value: false. Valid values:
        # 
        # *   **true**: applies for an endpoint for the shard node.
        # *   **false** : does not apply for an endpoint for the shard node.
        self.shard_direct = shard_direct  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.shard_direct is not None:
            result['ShardDirect'] = self.shard_direct
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ShardDirect') is not None:
            self.shard_direct = m.get('ShardDirect')
        return self


class CreateNodeResponseBody(TeaModel):
    def __init__(self, node_id=None, order_id=None, request_id=None):
        # The ID of the node.
        self.node_id = node_id  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNodeResponse, self).to_map()
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
            temp_model = CreateNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNodeBatchRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, auto_pay=None, business_info=None,
                 client_token=None, coupon_no=None, dbinstance_id=None, from_app=None, nodes_info=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None, shard_direct=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.business_info = business_info  # type: str
        # The ID of the added mongos or shard node.
        self.client_token = client_token  # type: str
        self.coupon_no = coupon_no  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.from_app = from_app  # type: str
        self.nodes_info = nodes_info  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.shard_direct = shard_direct  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNodeBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.nodes_info is not None:
            result['NodesInfo'] = self.nodes_info
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
        if self.shard_direct is not None:
            result['ShardDirect'] = self.shard_direct
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('NodesInfo') is not None:
            self.nodes_info = m.get('NodesInfo')
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
        if m.get('ShardDirect') is not None:
            self.shard_direct = m.get('ShardDirect')
        return self


class CreateNodeBatchResponseBody(TeaModel):
    def __init__(self, node_id=None, order_id=None, request_id=None):
        self.node_id = node_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNodeBatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNodeBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNodeBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNodeBatchResponse, self).to_map()
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
            temp_model = CreateNodeBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateShardingDBInstanceRequestConfigServer(TeaModel):
    def __init__(self, class_=None, storage=None):
        # The instance type of the ConfigServer node. Valid values:
        # 
        # *   **mdb.shard.2x.xlarge.d**: 4 cores, 8 GB (dedicated). Only instances that run MongoDB 4.4 and later support this instance type.
        # *   **dds.cs.mid** :1 core, 2 GB (general-purpose). Only instances that run MongoDB 4.2 and earlier support this instance type.
        self.class_ = class_  # type: str
        # The storage space of the ConfigServer node. Unit: GB.
        # 
        # > The values that can be specified for this parameter vary based on the instance types. For more information, see [Sharded cluster instance types](~~311414~~).
        self.storage = storage  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateShardingDBInstanceRequestConfigServer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.storage is not None:
            result['Storage'] = self.storage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        return self


class CreateShardingDBInstanceRequestMongos(TeaModel):
    def __init__(self, class_=None):
        # The instance type of the mongos node. For more information, see [Sharded cluster instance types](~~311414~~).
        # 
        # > 
        # 
        # *   **N** specifies the serial number of the mongos node for which the instance type is specified. For example, **Mongos.2.Class** specifies the instance type of the second mongos node.
        # 
        # *   Valid values for **N**: **2** to **32**.
        self.class_ = class_  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateShardingDBInstanceRequestMongos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class CreateShardingDBInstanceRequestReplicaSet(TeaModel):
    def __init__(self, class_=None, readonly_replicas=None, storage=None):
        # The instance type of the shard node. For more information, see [Sharded cluster instance types](~~311414~~).
        # 
        # > 
        # 
        # *   **N** specifies the serial number of the shard node for which the instance type is specified. For example, **ReplicaSet.2.Class** specifies the instance type of the second shard node.
        # 
        # *   Valid values for **N**: **2** to **32**.
        self.class_ = class_  # type: str
        # The number of read-only nodes in shard node N.
        # 
        # Valid values: **0** to **5**. Default value: **0**.
        # 
        # > **N** specifies the serial number of the shard node for which you want to set the number of read-only nodes. For example, **ReplicaSet.2.ReadonlyReplicas** specifies the number of read-only nodes in the second shard node.
        self.readonly_replicas = readonly_replicas  # type: int
        # The storage space of the shard node. Unit: GB.
        # 
        # > 
        # 
        # *   The values that can be specified for this parameter vary based on the instance types. For more information, see [Sharded cluster instance types](~~311414~~).
        # 
        # *   **N** specifies the serial number of the shard node for which the storage space is specified. For example, **ReplicaSet.2.Storage** specifies the storage space of the second shard node.
        self.storage = storage  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateShardingDBInstanceRequestReplicaSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.storage is not None:
            result['Storage'] = self.storage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        return self


class CreateShardingDBInstanceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateShardingDBInstanceRequestTag, self).to_map()
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


class CreateShardingDBInstanceRequest(TeaModel):
    def __init__(self, account_password=None, auto_renew=None, charge_type=None, client_token=None,
                 config_server=None, dbinstance_description=None, encrypted=None, encryption_key=None, engine=None,
                 engine_version=None, global_security_group_ids=None, hidden_zone_id=None, mongos=None, network_type=None,
                 owner_account=None, owner_id=None, period=None, protocol_type=None, provisioned_iops=None, region_id=None,
                 replica_set=None, resource_group_id=None, resource_owner_account=None, resource_owner_id=None,
                 restore_time=None, secondary_zone_id=None, security_iplist=None, security_token=None, src_dbinstance_id=None,
                 storage_engine=None, storage_type=None, tag=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # The password of the root account. The password must meet the following requirements:
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   The special characters include ! # $ % ^ & \* ( ) \_ + - =\
        # *   The password of the account must be 8 to 32 characters in length.
        self.account_password = account_password  # type: str
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        # 
        # > This parameter is available and optional if you set the value of **ChargeType** to **PrePaid**.
        self.auto_renew = auto_renew  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PostPaid** (default): pay-as-you-go
        # *   **PrePaid**: subscription
        # 
        # > **Period** is required if you set the value of this parameter to **PrePaid**.
        self.charge_type = charge_type  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The ConfigServer nodes of the instance.
        self.config_server = config_server  # type: list[CreateShardingDBInstanceRequestConfigServer]
        # The name of the instance. The name of the instance must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   It can contain digits, letters, underscores (\_), and hyphens (-).
        # *   It must be 2 to 256 characters in length.
        self.dbinstance_description = dbinstance_description  # type: str
        # Specifies whether to encrypt the disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.encrypted = encrypted  # type: bool
        # The ID of the custom key.
        self.encryption_key = encryption_key  # type: str
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine  # type: str
        # The version of the database engine. Valid values:
        # 
        # *   **6.0**\
        # *   **5.0**\
        # *   **4.4**\
        # *   **4.2**\
        # *   **4.0**\
        # *   **3.4**\
        # 
        # > 
        # 
        # *   For more information about the limits on database versions and storage engines, see [MongoDB versions and storage engines](~~61906~~).
        # 
        # *   If you call this operation to clone an instance, set the value of this parameter to the engine version of the source instance.
        self.engine_version = engine_version  # type: str
        # 实例的全局IP白名单模板，多个IP白名单模板请用英文逗号（,）分隔，不可重复。
        self.global_security_group_ids = global_security_group_ids  # type: str
        # The ID of secondary zone 2 for multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hong Kong Zone B
        # *   **cn-hongkong-c**: Hong Kong Zone C
        # *   **cn-hongkong-d**: Hong Kong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > 
        # 
        # *   This parameter is available and required if you set the value of **EngineVersion** to **4.4** or **5.0**.
        # 
        # *   The value of this parameter cannot be the same as the value of **ZoneId** or **SecondaryZoneId**.
        # 
        # *   For more information about the multi-zone deployment policy of a sharded cluster instance, see [Create a multi-zone sharded cluster instance](~~117865~~).
        self.hidden_zone_id = hidden_zone_id  # type: str
        # The mongos nodes of the instance.
        self.mongos = mongos  # type: list[CreateShardingDBInstanceRequestMongos]
        # The network type of the instance. Set the value to VPC.
        # 
        # ****\
        self.network_type = network_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The subscription period of the instance. Unit: month.
        # 
        # Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, and 60************************\
        # 
        # > This parameter is available and required if you set the value of **ChargeType** to **PrePaid**.
        self.period = period  # type: int
        # The access protocol type of the instance. Valid values:
        # 
        # *   **mongodb**: the MongoDB protocol
        # *   **dynamodb**: the DynamoDB protocol
        self.protocol_type = protocol_type  # type: str
        self.provisioned_iops = provisioned_iops  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The shard nodes of the instance.
        self.replica_set = replica_set  # type: list[CreateShardingDBInstanceRequestReplicaSet]
        # The resource group ID. For more information, see [View the basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The point in time to restore the instance, which must be within seven days. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in Coordinated Universal Time (UTC).
        # 
        # > This parameter is required only if you call this operation to clone an instance. If you specify this parameter, you must also specify **SrcDBInstanceId**.
        self.restore_time = restore_time  # type: str
        # The ID of secondary zone 1 for multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hong Kong Zone B
        # *   **cn-hongkong-c**: Hong Kong Zone C
        # *   **cn-hongkong-d**: Hong Kong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > 
        # 
        # *   This parameter is available and required if you set the value of **EngineVersion** to **4.4** or **5.0**.
        # 
        # *   The value of this parameter cannot be the same as the value of **ZoneId** or **HiddenZoneId**.
        # *   For more information about the multi-zone deployment policy of a sharded cluster instance, see [Create a multi-zone sharded cluster instance](~~117865~~).
        self.secondary_zone_id = secondary_zone_id  # type: str
        # The IP addresses in an IP address whitelist of the instance. Multiple IP addresses are separated by commas (,), and each IP address in the IP address whitelist must be unique. The following types of values are supported:
        # 
        # *   0.0.0.0/0
        # *   IP addresses, such as 10.23.12.24.
        # *   CIDR blocks, such as 10.23.12.0/24. In this case, 24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32.
        # 
        # > 
        # 
        # *   A maximum of 1,000 IP addresses and CIDR blocks can be configured for each instance.
        # 
        # *   If you enter 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. Proceed with caution.
        self.security_iplist = security_iplist  # type: str
        self.security_token = security_token  # type: str
        # The source instance ID.
        # 
        # > This parameter is required only if you call this operation to clone an instance. If you specify this parameter, you must also specify **RestoreTime**.
        self.src_dbinstance_id = src_dbinstance_id  # type: str
        # The storage engine of the instance. Set the value to **WiredTiger**.
        # 
        # > 
        # 
        # *   If you call this operation to clone an instance, set the value of this parameter to the storage engine of the source instance.
        # 
        # *   For more information about the limits on database versions and storage engines, see [MongoDB versions and storage engines](~~61906~~).
        self.storage_engine = storage_engine  # type: str
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd1**: ESSD PL1
        # *   **cloud_essd2**: ESSD PL2
        # *   **cloud_essd3**: ESSD PL3
        # *   **local_ssd**: local SSD
        # 
        # > 
        # 
        # *   Instances of MongoDB 4.4 and later support only cloud disks. **cloud_essd1** is selected if you leave this parameter empty.
        # 
        # *   Instances of MongoDB 4.2 and earlier support only local disks. **local_ssd** is selected if you leave this parameter empty.
        self.storage_type = storage_type  # type: str
        self.tag = tag  # type: list[CreateShardingDBInstanceRequestTag]
        # The vSwitch ID.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.config_server:
            for k in self.config_server:
                if k:
                    k.validate()
        if self.mongos:
            for k in self.mongos:
                if k:
                    k.validate()
        if self.replica_set:
            for k in self.replica_set:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateShardingDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['ConfigServer'] = []
        if self.config_server is not None:
            for k in self.config_server:
                result['ConfigServer'].append(k.to_map() if k else None)
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.global_security_group_ids is not None:
            result['GlobalSecurityGroupIds'] = self.global_security_group_ids
        if self.hidden_zone_id is not None:
            result['HiddenZoneId'] = self.hidden_zone_id
        result['Mongos'] = []
        if self.mongos is not None:
            for k in self.mongos:
                result['Mongos'].append(k.to_map() if k else None)
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ReplicaSet'] = []
        if self.replica_set is not None:
            for k in self.replica_set:
                result['ReplicaSet'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id
        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.config_server = []
        if m.get('ConfigServer') is not None:
            for k in m.get('ConfigServer'):
                temp_model = CreateShardingDBInstanceRequestConfigServer()
                self.config_server.append(temp_model.from_map(k))
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('GlobalSecurityGroupIds') is not None:
            self.global_security_group_ids = m.get('GlobalSecurityGroupIds')
        if m.get('HiddenZoneId') is not None:
            self.hidden_zone_id = m.get('HiddenZoneId')
        self.mongos = []
        if m.get('Mongos') is not None:
            for k in m.get('Mongos'):
                temp_model = CreateShardingDBInstanceRequestMongos()
                self.mongos.append(temp_model.from_map(k))
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.replica_set = []
        if m.get('ReplicaSet') is not None:
            for k in m.get('ReplicaSet'):
                temp_model = CreateShardingDBInstanceRequestReplicaSet()
                self.replica_set.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')
        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateShardingDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateShardingDBInstanceResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, order_id=None, request_id=None):
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The order ID.
        self.order_id = order_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateShardingDBInstanceResponseBody, self).to_map()
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


class CreateShardingDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateShardingDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateShardingDBInstanceResponse, self).to_map()
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
            temp_model = CreateShardingDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class DeleteGlobalSecurityIPGroupRequest(TeaModel):
    def __init__(self, global_ig_name=None, global_security_group_id=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.global_ig_name = global_ig_name  # type: str
        self.global_security_group_id = global_security_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGlobalSecurityIPGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteGlobalSecurityIPGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGlobalSecurityIPGroupResponseBody, self).to_map()
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


class DeleteGlobalSecurityIPGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGlobalSecurityIPGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGlobalSecurityIPGroupResponse, self).to_map()
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
            temp_model = DeleteGlobalSecurityIPGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNodeRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the shard or mongos node to be deleted. You can call the [DescribeDBInstanceAttribute](~~61923~~) operation to query the node ID.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class DeleteNodeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None, task_id=None):
        # The order ID of the instance.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNodeResponse, self).to_map()
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
            temp_model = DeleteNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, account_name=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The name of the account. Set the value to **root**.
        self.account_name = account_name  # type: str
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_status=None, character_type=None,
                 dbinstance_id=None):
        # The description of the account.
        # 
        # > This parameter is returned only after you configure the description of the account by calling the [ModifyAccountDescription](~~468391~~) operation.
        self.account_description = account_description  # type: str
        # The name of the account.
        self.account_name = account_name  # type: str
        # The status of the account.
        # 
        # *   **Unavailable**\
        # *   **Available**\
        self.account_status = account_status  # type: str
        # The role of the account. Valid values:
        # 
        # *   **db**: shard
        # *   **cs**: Configserver
        # *   **mongos**: mongos
        # *   **logic:** sharded cluster instance
        # *   **normal:** replica set instance
        self.character_type = character_type  # type: str
        # The name of the instance to which the account belongs.
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccountsAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
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
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeAccountsResponseBodyAccounts(TeaModel):
    def __init__(self, account=None):
        self.account = account  # type: list[DescribeAccountsResponseBodyAccountsAccount]

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = DescribeAccountsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(self, accounts=None, request_id=None):
        # The username of the account.
        self.accounts = accounts  # type: DescribeAccountsResponseBodyAccounts
        # The request ID.
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


class DescribeActiveOperationTaskCountRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeActiveOperationTaskCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeActiveOperationTaskCountResponseBody(TeaModel):
    def __init__(self, need_pop=None, request_id=None, task_count=None):
        # Indicates whether any O&M tasks need pop-up windows to notify users actions. Valid values: 
        # 
        # - **0**: No O&M tasks need pop-up windows to notify users actions.
        # - **1**: Some O&M tasks need pop-up windows to notify users actions.
        self.need_pop = need_pop  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of pending O&M tasks.
        self.task_count = task_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeActiveOperationTaskCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_pop is not None:
            result['NeedPop'] = self.need_pop
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedPop') is not None:
            self.need_pop = m.get('NeedPop')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class DescribeActiveOperationTaskCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeActiveOperationTaskCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeActiveOperationTaskCountResponse, self).to_map()
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
            temp_model = DescribeActiveOperationTaskCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeActiveOperationTaskTypeRequest(TeaModel):
    def __init__(self, is_history=None, owner_account=None, owner_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # Specifies whether to return all O\&M tasks. Valid values:
        # 
        # *   **0**: returns only pending tasks.
        # *   **1**: returns all tasks.
        # 
        # Default value: **0**.
        self.is_history = is_history  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeActiveOperationTaskTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_history is not None:
            result['IsHistory'] = self.is_history
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsHistory') is not None:
            self.is_history = m.get('IsHistory')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeActiveOperationTaskTypeResponseBodyTypeList(TeaModel):
    def __init__(self, count=None, task_type=None, task_type_info_en=None, task_type_info_zh=None):
        # The number of pending tasks.
        self.count = count  # type: int
        # The type of the task. Valid values:
        # 
        # *   **rds\_apsaradb\_transfer**: instance migration
        # *   **rds\_apsaradb\_upgrade**: minor version update
        self.task_type = task_type  # type: str
        # The task type (English).
        self.task_type_info_en = task_type_info_en  # type: str
        # The task type (Chinese).
        self.task_type_info_zh = task_type_info_zh  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeActiveOperationTaskTypeResponseBodyTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_info_en is not None:
            result['TaskTypeInfoEn'] = self.task_type_info_en
        if self.task_type_info_zh is not None:
            result['TaskTypeInfoZh'] = self.task_type_info_zh
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeInfoEn') is not None:
            self.task_type_info_en = m.get('TaskTypeInfoEn')
        if m.get('TaskTypeInfoZh') is not None:
            self.task_type_info_zh = m.get('TaskTypeInfoZh')
        return self


class DescribeActiveOperationTaskTypeResponseBody(TeaModel):
    def __init__(self, request_id=None, type_list=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The list of tasks.
        self.type_list = type_list  # type: list[DescribeActiveOperationTaskTypeResponseBodyTypeList]

    def validate(self):
        if self.type_list:
            for k in self.type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeActiveOperationTaskTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TypeList'] = []
        if self.type_list is not None:
            for k in self.type_list:
                result['TypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.type_list = []
        if m.get('TypeList') is not None:
            for k in m.get('TypeList'):
                temp_model = DescribeActiveOperationTaskTypeResponseBodyTypeList()
                self.type_list.append(temp_model.from_map(k))
        return self


class DescribeActiveOperationTaskTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeActiveOperationTaskTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeActiveOperationTaskTypeResponse, self).to_map()
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
            temp_model = DescribeActiveOperationTaskTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogFilterRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, role_type=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The role of the node in the instance. Valid values:
        # 
        # * **mongos**: mongos node.
        # * **db** : shard node.
        # * **logic** : logical instance.
        self.role_type = role_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditLogFilterRequest, self).to_map()
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
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAuditLogFilterResponseBody(TeaModel):
    def __init__(self, filter=None, request_id=None, role_type=None):
        # The type of the audit log entries. Valid values:
        # 
        # *   **admin**: O\&M and management operations
        # *   **slow**: slow query logs
        # *   **query**: query operations
        # *   **insert**: insert operations
        # *   **update**: update operations
        # *   **delete**: delete operations
        # *   **command**: protocol commands such as the aggregate method
        self.filter = filter  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The role of the node.
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditLogFilterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeAuditLogFilterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditLogFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditLogFilterResponse, self).to_map()
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
            temp_model = DescribeAuditLogFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditPolicyRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAuditPolicyResponseBody(TeaModel):
    def __init__(self, log_audit_status=None, request_id=None):
        # Indicates whether the log audit feature is enabled. Valid values:
        # 
        # *   Enable
        # *   Disabled
        # 
        # Default value: Disabled.
        self.log_audit_status = log_audit_status  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_audit_status is not None:
            result['LogAuditStatus'] = self.log_audit_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogAuditStatus') is not None:
            self.log_audit_status = m.get('LogAuditStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAuditPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditPolicyResponse, self).to_map()
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
            temp_model = DescribeAuditPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, database=None, end_time=None, form=None, node_id=None, order_type=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, query_keywords=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, start_time=None, user=None):
        # The ID of the instance.
        # 
        # > If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database to be queried. By default, all databases are queried.
        self.database = database  # type: str
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > The end time must be within 24 hours from the start time. Otherwise, the query fails.
        self.end_time = end_time  # type: str
        # The form of the audit log that the operation returns. Default value: File. Valid values:
        # 
        # *   **File** triggers the generation of audit logs. If this parameter is set to File, only common parameters are returned.
        # *   **Stream**: returns data streams.
        self.form = form  # type: str
        # The ID of the mongos node or shard node whose parameter modification records you want to query in the instance. If the instance is a sharded cluster instance, you must specify this parameter.
        # 
        # > This parameter is valid only when you specify the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        # The order of time in which the log entries to return are sorted. Valid values:
        # 
        # *   **asc**: The log entries are sorted by time in ascending order.
        # *   **desc**: The log entries are sorted by time in descending order.
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. Pages start from page 1. Valid values: any non-zero positive integer. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return per page. Default value: 30. Valid values: **30**, **50**, and **100**.
        self.page_size = page_size  # type: int
        # The keywords that are used for queries. Separate multiple keywords with spaces. The maximum number of keywords is 10.
        self.query_keywords = query_keywords  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The account of the database. If you do not specify this parameter, this operation returns records of all accounts.
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditRecordsRequest, self).to_map()
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
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeAuditRecordsResponseBodyItemsSQLRecord(TeaModel):
    def __init__(self, account_name=None, dbname=None, execute_time=None, host_address=None, return_row_counts=None,
                 syntax=None, table_name=None, thread_id=None, total_execution_times=None):
        # The account of the database.
        self.account_name = account_name  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The time when the statement was executed. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.execute_time = execute_time  # type: str
        # The IP addresses of the client.
        self.host_address = host_address  # type: str
        # The number of SQL audit log entries that are returned.
        self.return_row_counts = return_row_counts  # type: long
        # The statement that was executed.
        self.syntax = syntax  # type: str
        # The name of the collection.
        self.table_name = table_name  # type: str
        # The ID of the thread.
        self.thread_id = thread_id  # type: str
        # The execution time of the statement. Unit: microseconds.
        self.total_execution_times = total_execution_times  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditRecordsResponseBodyItemsSQLRecord, self).to_map()
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
        if self.syntax is not None:
            result['Syntax'] = self.syntax
        if self.table_name is not None:
            result['TableName'] = self.table_name
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
        if m.get('Syntax') is not None:
            self.syntax = m.get('Syntax')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ThreadID') is not None:
            self.thread_id = m.get('ThreadID')
        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')
        return self


class DescribeAuditRecordsResponseBodyItems(TeaModel):
    def __init__(self, sqlrecord=None):
        self.sqlrecord = sqlrecord  # type: list[DescribeAuditRecordsResponseBodyItemsSQLRecord]

    def validate(self):
        if self.sqlrecord:
            for k in self.sqlrecord:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAuditRecordsResponseBodyItems, self).to_map()
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
                temp_model = DescribeAuditRecordsResponseBodyItemsSQLRecord()
                self.sqlrecord.append(temp_model.from_map(k))
        return self


class DescribeAuditRecordsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        # An array that consists of the information of audit log entries.
        self.items = items  # type: DescribeAuditRecordsResponseBodyItems
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The maximum number of entries on the current page.
        self.page_record_count = page_record_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeAuditRecordsResponseBody, self).to_map()
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
            temp_model = DescribeAuditRecordsResponseBodyItems()
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


class DescribeAuditRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditRecordsResponse, self).to_map()
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
            temp_model = DescribeAuditRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailabilityZonesRequest(TeaModel):
    def __init__(self, accept_language=None, db_type=None, exclude_secondary_zone_id=None, exclude_zone_id=None,
                 instance_charge_type=None, mongo_type=None, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, storage_support=None, storage_type=None,
                 zone_id=None):
        # Specifies the language of the returned values of the **RegionName** and **ZoneName** parameters. Default value: zh. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English
        self.accept_language = accept_language  # type: str
        # The database engine type of the instance. Valid values:
        # 
        # *   **normal**: replica set instance
        # *   **sharding**: sharded cluster instance
        self.db_type = db_type  # type: str
        self.exclude_secondary_zone_id = exclude_secondary_zone_id  # type: str
        self.exclude_zone_id = exclude_zone_id  # type: str
        # The billing method of the instance. Default value: PrePaid. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type  # type: str
        # The edition of the ApsaraDB for MongoDB instance. The instance can be of a high-availability edition or beta edition.
        self.mongo_type = mongo_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the latest available regions.
        self.region_id = region_id  # type: str
        # The ID of the resource group. For more information, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The zones to be displayed. The values include the zones in which you can create an instance that uses cloud disks, the zones in which you can create an instance that uses local disks, and the zones in which you can create an instance that uses cloud disks and local disks.
        self.storage_support = storage_support  # type: str
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd1**: PL1.enhanced SSD (ESSD)
        # *   **cloud_essd2**: PL2 ESSD.
        # *   **cloud_essd3**: PL3 ESSD.
        # *   **local_ssd**: local SSD.
        # 
        # > 
        # 
        # *   Instances of MongoDB 4.4 and later only support cloud disks. **cloud_essd1** is selected if you leave this parameter empty.
        # 
        # *   Instances of MongoDB 4.2 and earlier support only local disks. **local_ssd** is selected if you leave this parameter empty.
        self.storage_type = storage_type  # type: str
        # The zone ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query available zones.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailabilityZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.exclude_secondary_zone_id is not None:
            result['ExcludeSecondaryZoneId'] = self.exclude_secondary_zone_id
        if self.exclude_zone_id is not None:
            result['ExcludeZoneId'] = self.exclude_zone_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.mongo_type is not None:
            result['MongoType'] = self.mongo_type
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
        if self.storage_support is not None:
            result['StorageSupport'] = self.storage_support
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('ExcludeSecondaryZoneId') is not None:
            self.exclude_secondary_zone_id = m.get('ExcludeSecondaryZoneId')
        if m.get('ExcludeZoneId') is not None:
            self.exclude_zone_id = m.get('ExcludeZoneId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('MongoType') is not None:
            self.mongo_type = m.get('MongoType')
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
        if m.get('StorageSupport') is not None:
            self.storage_support = m.get('StorageSupport')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailabilityZonesResponseBodyAvailableZones(TeaModel):
    def __init__(self, region_id=None, zone_id=None, zone_name=None):
        # The ID of the region. You can call the [DescribeRegions](~~61933~~) operation to query the latest available regions.
        self.region_id = region_id  # type: str
        # The ID of the zone.
        self.zone_id = zone_id  # type: str
        # The name of the zone.
        # 
        # The return value of the ZoneName parameter is in the language that is specified by the **AcceptLanguage** parameter. For example, if the value of the ZoneId parameter in the response is **cn-hangzhou-h**, the following values are returned for the ZoneName parameter:
        # 
        # *   If the value of the **AcceptLanguage** parameter is **zh**, ** H** is returned for the ZoneName parameter.
        # *   If the value of the **AcceptLanguage** parameter is **en**, **Hangzhou Zone H** is returned for the ZoneName parameter.
        self.zone_name = zone_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailabilityZonesResponseBodyAvailableZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeAvailabilityZonesResponseBody(TeaModel):
    def __init__(self, available_zones=None, request_id=None):
        # The details of the zones in which you can create ApsaraDB for MongoDB instances.
        self.available_zones = available_zones  # type: list[DescribeAvailabilityZonesResponseBodyAvailableZones]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_zones:
            for k in self.available_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailabilityZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZones'] = []
        if self.available_zones is not None:
            for k in self.available_zones:
                result['AvailableZones'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_zones = []
        if m.get('AvailableZones') is not None:
            for k in m.get('AvailableZones'):
                temp_model = DescribeAvailabilityZonesResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailabilityZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAvailabilityZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailabilityZonesResponse, self).to_map()
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
            temp_model = DescribeAvailabilityZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableEngineVersionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableEngineVersionRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAvailableEngineVersionResponseBodyEngineVersions(TeaModel):
    def __init__(self, engine_version=None):
        self.engine_version = engine_version  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableEngineVersionResponseBodyEngineVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        return self


class DescribeAvailableEngineVersionResponseBody(TeaModel):
    def __init__(self, engine_versions=None, request_id=None):
        # The list of one or more engine versions to which an ApsaraDB for MongoDB instance can be upgraded.
        # 
        # >  An empty string is returned if the latest version is being used.
        self.engine_versions = engine_versions  # type: DescribeAvailableEngineVersionResponseBodyEngineVersions
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.engine_versions:
            self.engine_versions.validate()

    def to_map(self):
        _map = super(DescribeAvailableEngineVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_versions is not None:
            result['EngineVersions'] = self.engine_versions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EngineVersions') is not None:
            temp_model = DescribeAvailableEngineVersionResponseBodyEngineVersions()
            self.engine_versions = temp_model.from_map(m['EngineVersions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableEngineVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAvailableEngineVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailableEngineVersionResponse, self).to_map()
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
            temp_model = DescribeAvailableEngineVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, db_type=None, instance_charge_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None, storage_type=None,
                 zone_id=None):
        # The architecture of the instance. Valid values:
        # 
        # *   **normal**: replica set instance
        # *   **sharding**: sharded cluster instance
        self.db_type = db_type  # type: str
        # The billing method of the instance. Default value: PrePaid. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the region. You can call the [DescribeRegions](~~61933~~) operation to query the latest available regions.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.storage_type = storage_type  # type: str
        # The ID of the zone. You can call the [DescribeRegions](~~61933~~) operation to query the available zones.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
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
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
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
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResourceDBInstanceStorageRange(TeaModel):
    def __init__(self, max=None, min=None, step=None):
        # The maximum storage capacity. Unit: GB.
        self.max = max  # type: int
        # The minimum storage capacity. Unit: GB.
        self.min = min  # type: int
        # The step size for adjusting the storage capacity. Unit: GB.
        self.step = step  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResourceDBInstanceStorageRange, self).to_map()
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


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource(TeaModel):
    def __init__(self, dbinstance_storage_range=None, instance_class=None, instance_class_remark=None):
        # The storage capacity range of the instance.
        self.dbinstance_storage_range = dbinstance_storage_range  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResourceDBInstanceStorageRange
        # The instance family.
        self.instance_class = instance_class  # type: str
        # The type of the instance.
        self.instance_class_remark = instance_class_remark  # type: str

    def validate(self):
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_class_remark is not None:
            result['InstanceClassRemark'] = self.instance_class_remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceStorageRange') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResourceDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(m['DBInstanceStorageRange'])
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceClassRemark') is not None:
            self.instance_class_remark = m.get('InstanceClassRemark')
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources(TeaModel):
    def __init__(self, available_resource=None):
        self.available_resource = available_resource  # type: list[DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource]

    def validate(self):
        if self.available_resource:
            for k in self.available_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources, self).to_map()
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
                temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeType(TeaModel):
    def __init__(self, available_resources=None, network_types=None, node_type=None):
        # The details of the available resources.
        self.available_resources = available_resources  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources
        # The network type of the instance.
        self.network_types = network_types  # type: str
        # The number of nodes in the instance.
        self.node_type = node_type  # type: str

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        if self.network_types is not None:
            result['NetworkTypes'] = self.network_types
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources()
            self.available_resources = temp_model.from_map(m['AvailableResources'])
        if m.get('NetworkTypes') is not None:
            self.network_types = m.get('NetworkTypes')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes(TeaModel):
    def __init__(self, supported_node_type=None):
        self.supported_node_type = supported_node_type  # type: list[DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeType]

    def validate(self):
        if self.supported_node_type:
            for k in self.supported_node_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedNodeType'] = []
        if self.supported_node_type is not None:
            for k in self.supported_node_type:
                result['SupportedNodeType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_node_type = []
        if m.get('SupportedNodeType') is not None:
            for k in m.get('SupportedNodeType'):
                temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeType()
                self.supported_node_type.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngine(TeaModel):
    def __init__(self, engine=None, supported_node_types=None):
        # The storage engine of the instance.
        self.engine = engine  # type: str
        # The supported instance types.
        self.supported_node_types = supported_node_types  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes

    def validate(self):
        if self.supported_node_types:
            self.supported_node_types.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.supported_node_types is not None:
            result['SupportedNodeTypes'] = self.supported_node_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('SupportedNodeTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes()
            self.supported_node_types = temp_model.from_map(m['SupportedNodeTypes'])
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEngines(TeaModel):
    def __init__(self, supported_engine=None):
        self.supported_engine = supported_engine  # type: list[DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngine]

    def validate(self):
        if self.supported_engine:
            for k in self.supported_engine:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEngines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedEngine'] = []
        if self.supported_engine is not None:
            for k in self.supported_engine:
                result['SupportedEngine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_engine = []
        if m.get('SupportedEngine') is not None:
            for k in m.get('SupportedEngine'):
                temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersion(TeaModel):
    def __init__(self, supported_engines=None, version=None):
        # The supported storage engines.
        self.supported_engines = supported_engines  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEngines
        # The database engine version of the instance.
        self.version = version  # type: str

    def validate(self):
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedEngines') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEngines()
            self.supported_engines = temp_model.from_map(m['SupportedEngines'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions(TeaModel):
    def __init__(self, supported_engine_version=None):
        self.supported_engine_version = supported_engine_version  # type: list[DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersion]

    def validate(self):
        if self.supported_engine_version:
            for k in self.supported_engine_version:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedEngineVersion'] = []
        if self.supported_engine_version is not None:
            for k in self.supported_engine_version:
                result['SupportedEngineVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_engine_version = []
        if m.get('SupportedEngineVersion') is not None:
            for k in m.get('SupportedEngineVersion'):
                temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZone(TeaModel):
    def __init__(self, region_id=None, supported_engine_versions=None, zone_id=None):
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The supported storage engine versions.
        self.supported_engine_versions = supported_engine_versions  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions
        # The ID of the zone.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupportedEngineVersions') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m['SupportedEngineVersions'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZones(TeaModel):
    def __init__(self, available_zone=None):
        self.available_zone = available_zone  # type: list[DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZone]

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZones, self).to_map()
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
                temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBType(TeaModel):
    def __init__(self, available_zones=None, db_type=None):
        # The available zones.
        self.available_zones = available_zones  # type: DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZones
        # The architecture of the instance. Valid values:
        # 
        # *   **normal**: replica set instance
        # *   **sharding**: sharded cluster instance
        self.db_type = db_type  # type: str

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZones()
            self.available_zones = temp_model.from_map(m['AvailableZones'])
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        return self


class DescribeAvailableResourceResponseBodySupportedDBTypes(TeaModel):
    def __init__(self, supported_dbtype=None):
        self.supported_dbtype = supported_dbtype  # type: list[DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBType]

    def validate(self):
        if self.supported_dbtype:
            for k in self.supported_dbtype:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodySupportedDBTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedDBType'] = []
        if self.supported_dbtype is not None:
            for k in self.supported_dbtype:
                result['SupportedDBType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_dbtype = []
        if m.get('SupportedDBType') is not None:
            for k in m.get('SupportedDBType'):
                temp_model = DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBType()
                self.supported_dbtype.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, supported_dbtypes=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The supported database types.
        self.supported_dbtypes = supported_dbtypes  # type: DescribeAvailableResourceResponseBodySupportedDBTypes

    def validate(self):
        if self.supported_dbtypes:
            self.supported_dbtypes.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supported_dbtypes is not None:
            result['SupportedDBTypes'] = self.supported_dbtypes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportedDBTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportedDBTypes()
            self.supported_dbtypes = temp_model.from_map(m['SupportedDBTypes'])
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAvailableResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DescribeBackupDBsRequest(TeaModel):
    def __init__(self, backup_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, restore_time=None, security_token=None,
                 source_dbinstance=None):
        # The ID of the backup set.
        # 
        # > * You can call the [DescribeBackups](~~62172~~) operation to query the backup ID.
        # > * You must specify one of the **RestoreTime** and BackupId parameters.
        self.backup_id = backup_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value of this parameter must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: 30. Valid values: **30**, **50**, and **100**.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The point in time to which the instance is restored. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > * The time can be a point in time within the past seven days. The time must be earlier than the current time, but later than the time when the instance was created.
        # > * You must specify one of the RestoreTime and **BackupId** parameters.
        self.restore_time = restore_time  # type: str
        self.security_token = security_token  # type: str
        # The ID of the source instance.
        self.source_dbinstance = source_dbinstance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupDBsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.source_dbinstance is not None:
            result['SourceDBInstance'] = self.source_dbinstance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SourceDBInstance') is not None:
            self.source_dbinstance = m.get('SourceDBInstance')
        return self


class DescribeBackupDBsResponseBodyDatabasesDatabase(TeaModel):
    def __init__(self, dbname=None):
        # The name of the database.
        self.dbname = dbname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupDBsResponseBodyDatabasesDatabase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DescribeBackupDBsResponseBodyDatabases(TeaModel):
    def __init__(self, database=None):
        self.database = database  # type: list[DescribeBackupDBsResponseBodyDatabasesDatabase]

    def validate(self):
        if self.database:
            for k in self.database:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupDBsResponseBodyDatabases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Database'] = []
        if self.database is not None:
            for k in self.database:
                result['Database'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.database = []
        if m.get('Database') is not None:
            for k in m.get('Database'):
                temp_model = DescribeBackupDBsResponseBodyDatabasesDatabase()
                self.database.append(temp_model.from_map(k))
        return self


class DescribeBackupDBsResponseBody(TeaModel):
    def __init__(self, databases=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # Details about the databases.
        self.databases = databases  # type: DescribeBackupDBsResponseBodyDatabases
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of returned databases.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.databases:
            self.databases.validate()

    def to_map(self):
        _map = super(DescribeBackupDBsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.databases is not None:
            result['Databases'] = self.databases.to_map()
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
        if m.get('Databases') is not None:
            temp_model = DescribeBackupDBsResponseBodyDatabases()
            self.databases = temp_model.from_map(m['Databases'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupDBsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupDBsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupDBsResponse, self).to_map()
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
            temp_model = DescribeBackupDBsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, backup_interval=None, backup_retention_period=None, enable_backup_log=None,
                 log_backup_retention_period=None, preferred_backup_period=None, preferred_backup_time=None, request_id=None,
                 snapshot_backup_type=None):
        # The frequency at which high-frequency backups are created. Valid values:
        # 
        # *   **-1**: disables high-frequency backup.
        # *   **15**: every 15 minutes.
        # *   **30**: every 30 minutes.
        # *   **60**: every hour.
        # *   **120**: every 2 hours.
        # *   **180**: every 3 hours.
        # *   **240**: every 4 hours.
        # *   **360**: every 6 hours.
        # *   **480**: every 8 hours.
        # *   **720**: every 12 hours.
        self.backup_interval = backup_interval  # type: int
        # The retention period of backups. Unit: days.
        self.backup_retention_period = backup_retention_period  # type: str
        # Indicates whether log backup is enabled. Default value: 0. Valid values:
        # 
        # *   **0**: disables log backup.
        # *   **1**: enables log backup.
        self.enable_backup_log = enable_backup_log  # type: int
        # The number of days for which to retain log backups. Valid values: 7 to 730.
        self.log_backup_retention_period = log_backup_retention_period  # type: int
        # The day of a week on which to back up data. Valid values:
        # 
        # *   **Monday**\
        # *   **Tuesday**\
        # *   **Wednesday**\
        # *   **Thursday**\
        # *   **Friday**\
        # *   **Saturday**\
        # *   **Sunday**\
        self.preferred_backup_period = preferred_backup_period  # type: str
        # The time range to back up data. The time is in the *HH:mm*Z-*HH:mm*Z format. The time is displayed in UTC.
        self.preferred_backup_time = preferred_backup_time  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The snapshot backup type. Default value: Standard. Valid values:
        # 
        # *   **Flash**: single-digit second backup
        # *   **Standard**: standard backup
        self.snapshot_backup_type = snapshot_backup_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_interval is not None:
            result['BackupInterval'] = self.backup_interval
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
        if self.snapshot_backup_type is not None:
            result['SnapshotBackupType'] = self.snapshot_backup_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupInterval') is not None:
            self.backup_interval = m.get('BackupInterval')
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
        if m.get('SnapshotBackupType') is not None:
            self.snapshot_backup_type = m.get('SnapshotBackupType')
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


class DescribeBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, dbinstance_id=None, end_time=None, node_id=None, owner_account=None,
                 owner_id=None, page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None, start_time=None):
        # The ID of the backup set. You can call the [CreateBackup](~~62171~~) operation to obtain the value of this parameter.
        # 
        # If you set the DBInstanceId parameter to the ID of a sharded cluster instance, the number of backup IDs is the same as the number of shards. Multiple , with commas (,) in the middle.
        self.backup_id = backup_id  # type: str
        # The ID of the instance.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The ID of the shard node in the sharded cluster instance.
        # 
        # >  This parameter is valid only when **DBInstanceId** is set to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30, 50, and 100**. Default value: **30**.
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupsResponseBodyBackupsBackup(TeaModel):
    def __init__(self, backup_dbnames=None, backup_download_url=None, backup_end_time=None, backup_id=None,
                 backup_intranet_download_url=None, backup_method=None, backup_mode=None, backup_size=None, backup_start_time=None,
                 backup_status=None, backup_type=None):
        # The name of the database that has been backed up.
        self.backup_dbnames = backup_dbnames  # type: str
        # The Internet download URL of the backup set. If the download URL is unavailable, this parameter is an empty string.
        self.backup_download_url = backup_download_url  # type: str
        # The end of the backup time range. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format and displayed in UTC.
        self.backup_end_time = backup_end_time  # type: str
        # The ID of the backup set.
        self.backup_id = backup_id  # type: int
        # The internal download URL of the backup set.
        # 
        # >  You can use this URL to download the backup set from on the ECS instance which is on the same network as the ApsaraDB for MongoDB instance.
        self.backup_intranet_download_url = backup_intranet_download_url  # type: str
        # The backup method. Valid values:
        # 
        # *   **Snapshot**\
        # *   **Physical**\
        # *   **Logical**\
        self.backup_method = backup_method  # type: str
        # The backup mode.
        # 
        # *   **Automated**: automatic backup
        # *   **Manual**: manual backup
        self.backup_mode = backup_mode  # type: str
        # The size of the backup set. Unit: bytes.
        self.backup_size = backup_size  # type: long
        # The beginning of the backup time range. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format and displayed in UTC.
        self.backup_start_time = backup_start_time  # type: str
        # The status of the backup. Valid values:
        # 
        # *   **Success**: The backup task is successful.
        # *   **Failed**: The backup task failed.
        self.backup_status = backup_status  # type: str
        # The backup method.
        # 
        # *   **FullBackup**: a full backup
        # *   **IncrementalBackup**: an incremental backup
        self.backup_type = backup_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyBackupsBackup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_dbnames is not None:
            result['BackupDBNames'] = self.backup_dbnames
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        return self


class DescribeBackupsResponseBodyBackups(TeaModel):
    def __init__(self, backup=None):
        self.backup = backup  # type: list[DescribeBackupsResponseBodyBackupsBackup]

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyBackups, self).to_map()
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
                temp_model = DescribeBackupsResponseBodyBackupsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(self, backups=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # Details about backup sets.
        self.backups = backups  # type: DescribeBackupsResponseBodyBackups
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of backup sets that were returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.backups:
            self.backups.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backups is not None:
            result['Backups'] = self.backups.to_map()
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
        if m.get('Backups') is not None:
            temp_model = DescribeBackupsResponseBodyBackups()
            self.backups = temp_model.from_map(m['Backups'])
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DescribeClusterBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, dbinstance_id=None, end_time=None, is_only_get_cluster_back_up=None,
                 owner_account=None, owner_id=None, page_no=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, start_time=None):
        self.backup_id = backup_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.is_only_get_cluster_back_up = is_only_get_cluster_back_up  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_only_get_cluster_back_up is not None:
            result['IsOnlyGetClusterBackUp'] = self.is_only_get_cluster_back_up
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('IsOnlyGetClusterBackUp') is not None:
            self.is_only_get_cluster_back_up = m.get('IsOnlyGetClusterBackUp')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeClusterBackupsResponseBodyClusterBackupsBackups(TeaModel):
    def __init__(self, backup_download_url=None, backup_end_time=None, backup_id=None,
                 backup_intranet_download_url=None, backup_name=None, backup_size=None, backup_start_time=None, backup_status=None,
                 instance_name=None, is_avail=None):
        self.backup_download_url = backup_download_url  # type: str
        self.backup_end_time = backup_end_time  # type: str
        self.backup_id = backup_id  # type: str
        self.backup_intranet_download_url = backup_intranet_download_url  # type: str
        self.backup_name = backup_name  # type: str
        self.backup_size = backup_size  # type: str
        self.backup_start_time = backup_start_time  # type: str
        self.backup_status = backup_status  # type: str
        self.instance_name = instance_name  # type: str
        self.is_avail = is_avail  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterBackupsResponseBodyClusterBackupsBackups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url
        if self.backup_name is not None:
            result['BackupName'] = self.backup_name
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')
        if m.get('BackupName') is not None:
            self.backup_name = m.get('BackupName')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')
        return self


class DescribeClusterBackupsResponseBodyClusterBackupsExtraInfo(TeaModel):
    def __init__(self, registry_from_history=None):
        self.registry_from_history = registry_from_history  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterBackupsResponseBodyClusterBackupsExtraInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registry_from_history is not None:
            result['RegistryFromHistory'] = self.registry_from_history
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegistryFromHistory') is not None:
            self.registry_from_history = m.get('RegistryFromHistory')
        return self


class DescribeClusterBackupsResponseBodyClusterBackups(TeaModel):
    def __init__(self, backups=None, cluster_backup_end_time=None, cluster_backup_id=None,
                 cluster_backup_mode=None, cluster_backup_size=None, cluster_backup_start_time=None, cluster_backup_status=None,
                 extra_info=None, is_avail=None, progress=None):
        self.backups = backups  # type: list[DescribeClusterBackupsResponseBodyClusterBackupsBackups]
        self.cluster_backup_end_time = cluster_backup_end_time  # type: str
        self.cluster_backup_id = cluster_backup_id  # type: str
        self.cluster_backup_mode = cluster_backup_mode  # type: str
        self.cluster_backup_size = cluster_backup_size  # type: str
        self.cluster_backup_start_time = cluster_backup_start_time  # type: str
        self.cluster_backup_status = cluster_backup_status  # type: str
        self.extra_info = extra_info  # type: DescribeClusterBackupsResponseBodyClusterBackupsExtraInfo
        self.is_avail = is_avail  # type: int
        self.progress = progress  # type: str

    def validate(self):
        if self.backups:
            for k in self.backups:
                if k:
                    k.validate()
        if self.extra_info:
            self.extra_info.validate()

    def to_map(self):
        _map = super(DescribeClusterBackupsResponseBodyClusterBackups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Backups'] = []
        if self.backups is not None:
            for k in self.backups:
                result['Backups'].append(k.to_map() if k else None)
        if self.cluster_backup_end_time is not None:
            result['ClusterBackupEndTime'] = self.cluster_backup_end_time
        if self.cluster_backup_id is not None:
            result['ClusterBackupId'] = self.cluster_backup_id
        if self.cluster_backup_mode is not None:
            result['ClusterBackupMode'] = self.cluster_backup_mode
        if self.cluster_backup_size is not None:
            result['ClusterBackupSize'] = self.cluster_backup_size
        if self.cluster_backup_start_time is not None:
            result['ClusterBackupStartTime'] = self.cluster_backup_start_time
        if self.cluster_backup_status is not None:
            result['ClusterBackupStatus'] = self.cluster_backup_status
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backups = []
        if m.get('Backups') is not None:
            for k in m.get('Backups'):
                temp_model = DescribeClusterBackupsResponseBodyClusterBackupsBackups()
                self.backups.append(temp_model.from_map(k))
        if m.get('ClusterBackupEndTime') is not None:
            self.cluster_backup_end_time = m.get('ClusterBackupEndTime')
        if m.get('ClusterBackupId') is not None:
            self.cluster_backup_id = m.get('ClusterBackupId')
        if m.get('ClusterBackupMode') is not None:
            self.cluster_backup_mode = m.get('ClusterBackupMode')
        if m.get('ClusterBackupSize') is not None:
            self.cluster_backup_size = m.get('ClusterBackupSize')
        if m.get('ClusterBackupStartTime') is not None:
            self.cluster_backup_start_time = m.get('ClusterBackupStartTime')
        if m.get('ClusterBackupStatus') is not None:
            self.cluster_backup_status = m.get('ClusterBackupStatus')
        if m.get('ExtraInfo') is not None:
            temp_model = DescribeClusterBackupsResponseBodyClusterBackupsExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeClusterBackupsResponseBody(TeaModel):
    def __init__(self, cluster_backups=None, max_results=None, page_number=None, page_size=None, request_id=None):
        self.cluster_backups = cluster_backups  # type: list[DescribeClusterBackupsResponseBodyClusterBackups]
        self.max_results = max_results  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster_backups:
            for k in self.cluster_backups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterBackupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterBackups'] = []
        if self.cluster_backups is not None:
            for k in self.cluster_backups:
                result['ClusterBackups'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_backups = []
        if m.get('ClusterBackups') is not None:
            for k in m.get('ClusterBackups'):
                temp_model = DescribeClusterBackupsResponseBodyClusterBackups()
                self.cluster_backups.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterBackupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterBackupsResponse, self).to_map()
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
            temp_model = DescribeClusterBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRecoverTimeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterRecoverTimeRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeClusterRecoverTimeResponseBodyRestoreRanges(TeaModel):
    def __init__(self, restore_begin_time=None, restore_end_time=None, restore_type=None):
        self.restore_begin_time = restore_begin_time  # type: str
        self.restore_end_time = restore_end_time  # type: str
        self.restore_type = restore_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterRecoverTimeResponseBodyRestoreRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restore_begin_time is not None:
            result['RestoreBeginTime'] = self.restore_begin_time
        if self.restore_end_time is not None:
            result['RestoreEndTime'] = self.restore_end_time
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RestoreBeginTime') is not None:
            self.restore_begin_time = m.get('RestoreBeginTime')
        if m.get('RestoreEndTime') is not None:
            self.restore_end_time = m.get('RestoreEndTime')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        return self


class DescribeClusterRecoverTimeResponseBody(TeaModel):
    def __init__(self, request_id=None, restore_ranges=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.restore_ranges = restore_ranges  # type: list[DescribeClusterRecoverTimeResponseBodyRestoreRanges]

    def validate(self):
        if self.restore_ranges:
            for k in self.restore_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterRecoverTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RestoreRanges'] = []
        if self.restore_ranges is not None:
            for k in self.restore_ranges:
                result['RestoreRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.restore_ranges = []
        if m.get('RestoreRanges') is not None:
            for k in m.get('RestoreRanges'):
                temp_model = DescribeClusterRecoverTimeResponseBodyRestoreRanges()
                self.restore_ranges.append(temp_model.from_map(k))
        return self


class DescribeClusterRecoverTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterRecoverTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterRecoverTimeResponse, self).to_map()
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
            temp_model = DescribeClusterRecoverTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, engine=None, is_delete=None, owner_account=None, owner_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine  # type: str
        # Specifies whether to delete the instance. Valid values:
        # 
        # *   **false**: queries the details of running instances.
        # *   **true**: queries the details of deleted instances.
        self.is_delete = is_delete  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the resource group. For more information, see [View the basic information of a resource group](~~151181~~).
        # 
        # > This parameter is available only if you use the China site (aliyun.com).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverListConfigserverAttribute(TeaModel):
    def __init__(self, connect_string=None, max_connections=None, max_iops=None, node_class=None,
                 node_description=None, node_id=None, node_storage=None, port=None, status=None):
        # The endpoint of the Configserver node.
        self.connect_string = connect_string  # type: str
        # The maximum number of connections to the Configserver node.
        self.max_connections = max_connections  # type: int
        # The maximum IOPS of the Configserver node.
        self.max_iops = max_iops  # type: int
        # The type of the Configserver node.
        self.node_class = node_class  # type: str
        # The name of the Configserver node.
        self.node_description = node_description  # type: str
        # The ID of the Configserver node.
        self.node_id = node_id  # type: str
        # The storage capacity of the Configserver node.
        self.node_storage = node_storage  # type: int
        # The port number that is used to connect to the Configserver node.
        self.port = port  # type: int
        # The state of the Configserver node. For more information, see [Instance states](~~63870~~).
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverListConfigserverAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.port is not None:
            result['Port'] = self.port
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList(TeaModel):
    def __init__(self, configserver_attribute=None):
        self.configserver_attribute = configserver_attribute  # type: list[DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverListConfigserverAttribute]

    def validate(self):
        if self.configserver_attribute:
            for k in self.configserver_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigserverAttribute'] = []
        if self.configserver_attribute is not None:
            for k in self.configserver_attribute:
                result['ConfigserverAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configserver_attribute = []
        if m.get('ConfigserverAttribute') is not None:
            for k in m.get('ConfigserverAttribute'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverListConfigserverAttribute()
                self.configserver_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosListMongosAttribute(TeaModel):
    def __init__(self, connect_sting=None, max_connections=None, max_iops=None, node_class=None,
                 node_description=None, node_id=None, port=None, status=None, vpcid=None, v_switch_id=None,
                 vpc_cloud_instance_id=None):
        # The endpoint of the mongos node.
        self.connect_sting = connect_sting  # type: str
        # The maximum number of connections to the mongos node.
        self.max_connections = max_connections  # type: int
        # The maximum IOPS of the mongos node.
        self.max_iops = max_iops  # type: int
        # The type of the mongos node.
        self.node_class = node_class  # type: str
        # The name of the mongos node.
        self.node_description = node_description  # type: str
        # The ID of the mongos node.
        self.node_id = node_id  # type: str
        # The port number that is used to connect to the mongos node.
        self.port = port  # type: int
        # The state of the mongos node. For more information, see [Instance states](~~63870~~).
        self.status = status  # type: str
        # The VPC ID of the instance.
        # 
        # > This parameter is returned if the network type of the instance is VPC.
        self.vpcid = vpcid  # type: str
        # The vSwitch ID of the instance.
        # 
        # > This parameter is returned if the network type of the instance is VPC.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the mongos node.
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosListMongosAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_sting is not None:
            result['ConnectSting'] = self.connect_sting
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.port is not None:
            result['Port'] = self.port
        if self.status is not None:
            result['Status'] = self.status
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectSting') is not None:
            self.connect_sting = m.get('ConnectSting')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList(TeaModel):
    def __init__(self, mongos_attribute=None):
        self.mongos_attribute = mongos_attribute  # type: list[DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosListMongosAttribute]

    def validate(self):
        if self.mongos_attribute:
            for k in self.mongos_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MongosAttribute'] = []
        if self.mongos_attribute is not None:
            for k in self.mongos_attribute:
                result['MongosAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mongos_attribute = []
        if m.get('MongosAttribute') is not None:
            for k in m.get('MongosAttribute'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosListMongosAttribute()
                self.mongos_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSetsReplicaSet(TeaModel):
    def __init__(self, connection_domain=None, connection_port=None, network_type=None, replica_set_role=None,
                 vpccloud_instance_id=None, vpcid=None, v_switch_id=None):
        # The endpoint of the node.
        self.connection_domain = connection_domain  # type: str
        # The port number that is used to connect to the node.
        self.connection_port = connection_port  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**\
        # *   **VPC**\
        self.network_type = network_type  # type: str
        # The role of the node. Valid values:
        # 
        # *   **Primary**\
        # *   **Secondary**\
        self.replica_set_role = replica_set_role  # type: str
        # The instance ID.
        # 
        # > This parameter is returned if the network type of the instance is VPC.
        self.vpccloud_instance_id = vpccloud_instance_id  # type: str
        # The VPC ID of the instance.
        # 
        # > This parameter is returned if the network type of the instance is VPC.
        self.vpcid = vpcid  # type: str
        # The vSwitch ID of the instance.
        # 
        # > This parameter is returned if the network type of the instance is VPC.
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSetsReplicaSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.connection_port is not None:
            result['ConnectionPort'] = self.connection_port
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role
        if self.vpccloud_instance_id is not None:
            result['VPCCloudInstanceId'] = self.vpccloud_instance_id
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('ConnectionPort') is not None:
            self.connection_port = m.get('ConnectionPort')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')
        if m.get('VPCCloudInstanceId') is not None:
            self.vpccloud_instance_id = m.get('VPCCloudInstanceId')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets(TeaModel):
    def __init__(self, replica_set=None):
        self.replica_set = replica_set  # type: list[DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSetsReplicaSet]

    def validate(self):
        if self.replica_set:
            for k in self.replica_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReplicaSet'] = []
        if self.replica_set is not None:
            for k in self.replica_set:
                result['ReplicaSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.replica_set = []
        if m.get('ReplicaSet') is not None:
            for k in m.get('ReplicaSet'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSetsReplicaSet()
                self.replica_set.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardListShardAttribute(TeaModel):
    def __init__(self, connect_string=None, max_connections=None, max_iops=None, node_class=None,
                 node_description=None, node_id=None, node_storage=None, port=None, readonly_replicas=None, status=None):
        # The endpoint of the shard node.
        self.connect_string = connect_string  # type: str
        # The maximum number of connections to the shard node.
        self.max_connections = max_connections  # type: int
        # The maximum IOPS of the shard node.
        self.max_iops = max_iops  # type: int
        # The type of the shard node.
        self.node_class = node_class  # type: str
        # The name of the shard node.
        self.node_description = node_description  # type: str
        # The ID of the shard node.
        self.node_id = node_id  # type: str
        # The storage capacity of the shard node.
        self.node_storage = node_storage  # type: int
        # The port number that is used to connect to the shard node.
        self.port = port  # type: int
        # The number of read-only nodes in the shard node. Valid values: **0** to **5**. The value must be an integer.
        self.readonly_replicas = readonly_replicas  # type: int
        # The state of the shard node. For more information, see [Instance states](~~63870~~).
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardListShardAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.port is not None:
            result['Port'] = self.port
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList(TeaModel):
    def __init__(self, shard_attribute=None):
        self.shard_attribute = shard_attribute  # type: list[DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardListShardAttribute]

    def validate(self):
        if self.shard_attribute:
            for k in self.shard_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ShardAttribute'] = []
        if self.shard_attribute is not None:
            for k in self.shard_attribute:
                result['ShardAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.shard_attribute = []
        if m.get('ShardAttribute') is not None:
            for k in m.get('ShardAttribute'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardListShardAttribute()
                self.shard_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the instance.
        self.key = key  # type: str
        # The tag value of the instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTagsTag, self).to_map()
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


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags, self).to_map()
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
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstance(TeaModel):
    def __init__(self, bursting_enabled=None, capacity_unit=None, charge_type=None, configserver_list=None,
                 creation_time=None, current_kernel_version=None, dbinstance_class=None, dbinstance_description=None,
                 dbinstance_id=None, dbinstance_order_status=None, dbinstance_release_protection=None, dbinstance_status=None,
                 dbinstance_storage=None, dbinstance_type=None, destroy_time=None, encrypted=None, encryption_key=None, engine=None,
                 engine_version=None, expire_time=None, hidden_zone_id=None, kind_code=None, last_downgrade_time=None,
                 lock_mode=None, maintain_end_time=None, maintain_start_time=None, max_connections=None, max_iops=None,
                 mongos_list=None, network_type=None, protocol_type=None, provisioned_iops=None, readonly_replicas=None,
                 region_id=None, replacate_id=None, replica_set_name=None, replica_sets=None, replication_factor=None,
                 resource_group_id=None, secondary_zone_id=None, shard_list=None, storage_engine=None, storage_type=None,
                 sync_percent=None, tags=None, use_cluster_backup=None, vpccloud_instance_ids=None, vpcid=None, v_switch_id=None,
                 vpc_auth_mode=None, zone_id=None):
        self.bursting_enabled = bursting_enabled  # type: bool
        # The read and write throughput consumed by the instance.
        self.capacity_unit = capacity_unit  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The details of the Configserver nodes.
        # 
        # > This parameter is returned if the instance is a sharded cluster instance.
        self.configserver_list = configserver_list  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList
        # The time when the instance was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time  # type: str
        # The minor version of the current database in the instance.
        self.current_kernel_version = current_kernel_version  # type: str
        # The instance type.
        self.dbinstance_class = dbinstance_class  # type: str
        # The name of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The status of the orders generated for the instance. Valid values:
        # 
        # *   **all_completed**: All orders are being produced or complete.
        # *   **order_unpaid**: The instance has unpaid orders.
        # *   **order_wait_for_produce**: The order is being delivered for production.
        # 
        # > The order production process includes placing an order, paying for an order, delivering an order for production, producing an order, and complete.
        # 
        # *   If an order is in the **order_wait_for_produce** state for a long time, an error occurs when the order is being delivered for production. The system will automatically retry.
        # *   The instance status change only when the order is in the producing and complete state, such as changing configurations and running.
        self.dbinstance_order_status = dbinstance_order_status  # type: str
        # Indicates whether release protection is enabled for the instance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.dbinstance_release_protection = dbinstance_release_protection  # type: bool
        # The state of the instance. For more information, see [Instance states](~~63870~~).
        self.dbinstance_status = dbinstance_status  # type: str
        # The storage capacity of the instance.
        self.dbinstance_storage = dbinstance_storage  # type: int
        # The architecture of the instance. Valid values:
        # 
        # *   **replicate**: replica set instance
        # *   **sharding**: sharded cluster instance
        self.dbinstance_type = dbinstance_type  # type: str
        # The time when the instance data was destroyed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.destroy_time = destroy_time  # type: str
        # 是否开启云盘加密
        self.encrypted = encrypted  # type: bool
        # 云盘加密对应的kms-key
        self.encryption_key = encryption_key  # type: str
        # The database engine of the instance.
        self.engine = engine  # type: str
        # The database engine version of the instance.
        # 
        # *   **6.0**\
        # *   **5.0**\
        # *   **4.4**\
        # *   **4.2**\
        # *   **4.0**\
        self.engine_version = engine_version  # type: str
        # The time when the subscription instance expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        # 
        # > This parameter is returned if the instance is a subscription instance.
        self.expire_time = expire_time  # type: str
        # The ID of the secondary zone 2 of the instance. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hongkong Zone B
        # *   **cn-hongkong-c**: Hongkong Zone C
        # *   **cn-hongkong-d**: Hongkong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > 
        # 
        # *   This parameter is returned if the instance is a replica set or sharded cluster instance that runs MongoDB 4.4 or 5.0 and uses multi-zone deployment.
        # 
        # *   This parameter is returned only if you use the Chine site (aliyun.com).
        self.hidden_zone_id = hidden_zone_id  # type: str
        # The kind code of the instance. Valid values:
        # 
        # *   **0**: physical machine
        # *   **1**: Elastic Compute Service (ECS) instance
        # *   **2**: Docker cluster
        # *   **18**: Kubernetes cluster
        self.kind_code = kind_code  # type: str
        # The date when the last downgrade operation was performed on the instance.
        self.last_downgrade_time = last_downgrade_time  # type: str
        # The lock state of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before it is rolled back.
        # *   **LockByDiskQuota**: The instance is automatically locked due to exhausted storage capacity.
        # *   **Released**: The instance is released.
        self.lock_mode = lock_mode  # type: str
        # The end time of the maintenance window. The time follows the ISO 8601 standard in the *HH:mm*Z format. The time is displayed in UTC.
        self.maintain_end_time = maintain_end_time  # type: str
        # The start time of the maintenance window. The time follows the ISO 8601 standard in the *HH:mm*Z format. The time is displayed in UTC.
        self.maintain_start_time = maintain_start_time  # type: str
        # The maximum number of connections to the instance.
        self.max_connections = max_connections  # type: int
        # The maximum IOPS of the instance.
        self.max_iops = max_iops  # type: int
        # The details of the mongos nodes.
        # 
        # > This parameter is returned if the instance is a sharded cluster instance.
        self.mongos_list = mongos_list  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**\
        # *   **VPC**\
        self.network_type = network_type  # type: str
        # The access protocol type of the instance. Valid values:
        # 
        # *   **mongodb**\
        # *   **dynamodb**\
        # 
        # > This parameter is returned if the instance is a sharded cluster instance.
        self.protocol_type = protocol_type  # type: str
        self.provisioned_iops = provisioned_iops  # type: long
        # The number of read-only nodes in the instance.
        self.readonly_replicas = readonly_replicas  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The logical ID of the replica instance.
        # 
        # > ApsaraDB for MongoDB does not support new instances of this type. This parameter applies only to previous-version replica instances.
        self.replacate_id = replacate_id  # type: str
        # The name of the replica set instance.
        # 
        # > This parameter is returned if the instance is a replica set instance.
        self.replica_set_name = replica_set_name  # type: str
        # The details of the replica set instances.
        # 
        # > This parameter is returned if the instance is a replica set instance.
        self.replica_sets = replica_sets  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets
        # The number of nodes in the instance.
        # 
        # > This parameter is returned if the instance is a replica set instance.
        self.replication_factor = replication_factor  # type: str
        # The ID of the resource group.
        # 
        # > This parameter is returned only if you use the China site (aliyun.com).
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the secondary zone 1 of the instance. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hongkong Zone B
        # *   **cn-hongkong-c**: Hongkong Zone C
        # *   **cn-hongkong-d**: Hongkong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > 
        # 
        # *   This parameter is returned if the instance is a replica set or sharded cluster instance that runs MongoDB 4.4 or 5.0 and uses multi-zone deployment.
        # 
        # *   This parameter is returned only if you use the Chine site (aliyun.com).
        self.secondary_zone_id = secondary_zone_id  # type: str
        # The details of the shard nodes.
        # 
        # > This parameter is returned if the instance is a sharded cluster instance.
        self.shard_list = shard_list  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList
        # The storage engine of the instance.
        self.storage_engine = storage_engine  # type: str
        # The storage type of the instance. Valid values:
        # 
        # **cloud_essd1**: ESSD PL1 **cloud_essd2**: ESSD of PL2 **cloud_essd3**: ESSD of PL3 **local_ssd**: local SSD
        self.storage_type = storage_type  # type: str
        self.sync_percent = sync_percent  # type: str
        # The details of the instance tags.
        self.tags = tags  # type: DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags
        self.use_cluster_backup = use_cluster_backup  # type: bool
        # The instance ID.
        # 
        # > This parameter is returned if the network type of the instance is VPC.
        self.vpccloud_instance_ids = vpccloud_instance_ids  # type: str
        # The VPC ID of the instance.
        # 
        # > This parameter is returned if the network type of the instance is VPC.
        self.vpcid = vpcid  # type: str
        # The vSwitch ID of the instance.
        # 
        # > This parameter is returned if the network type of the instance is VPC.
        self.v_switch_id = v_switch_id  # type: str
        # Indicates whether password-free access within the VPC is enabled. Valid values:
        # 
        # *   **Open**: Password-free access is enabled.
        # *   **Close**: Password-free access is disabled, and you must use a password for access.
        # *   **NotSupport**: Password-free access is not supported.
        self.vpc_auth_mode = vpc_auth_mode  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.configserver_list:
            self.configserver_list.validate()
        if self.mongos_list:
            self.mongos_list.validate()
        if self.replica_sets:
            self.replica_sets.validate()
        if self.shard_list:
            self.shard_list.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.capacity_unit is not None:
            result['CapacityUnit'] = self.capacity_unit
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.configserver_list is not None:
            result['ConfigserverList'] = self.configserver_list.to_map()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.current_kernel_version is not None:
            result['CurrentKernelVersion'] = self.current_kernel_version
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_order_status is not None:
            result['DBInstanceOrderStatus'] = self.dbinstance_order_status
        if self.dbinstance_release_protection is not None:
            result['DBInstanceReleaseProtection'] = self.dbinstance_release_protection
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.hidden_zone_id is not None:
            result['HiddenZoneId'] = self.hidden_zone_id
        if self.kind_code is not None:
            result['KindCode'] = self.kind_code
        if self.last_downgrade_time is not None:
            result['LastDowngradeTime'] = self.last_downgrade_time
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.mongos_list is not None:
            result['MongosList'] = self.mongos_list.to_map()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replacate_id is not None:
            result['ReplacateId'] = self.replacate_id
        if self.replica_set_name is not None:
            result['ReplicaSetName'] = self.replica_set_name
        if self.replica_sets is not None:
            result['ReplicaSets'] = self.replica_sets.to_map()
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.shard_list is not None:
            result['ShardList'] = self.shard_list.to_map()
        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.sync_percent is not None:
            result['SyncPercent'] = self.sync_percent
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.use_cluster_backup is not None:
            result['UseClusterBackup'] = self.use_cluster_backup
        if self.vpccloud_instance_ids is not None:
            result['VPCCloudInstanceIds'] = self.vpccloud_instance_ids
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('CapacityUnit') is not None:
            self.capacity_unit = m.get('CapacityUnit')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ConfigserverList') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceConfigserverList()
            self.configserver_list = temp_model.from_map(m['ConfigserverList'])
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CurrentKernelVersion') is not None:
            self.current_kernel_version = m.get('CurrentKernelVersion')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceOrderStatus') is not None:
            self.dbinstance_order_status = m.get('DBInstanceOrderStatus')
        if m.get('DBInstanceReleaseProtection') is not None:
            self.dbinstance_release_protection = m.get('DBInstanceReleaseProtection')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HiddenZoneId') is not None:
            self.hidden_zone_id = m.get('HiddenZoneId')
        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')
        if m.get('LastDowngradeTime') is not None:
            self.last_downgrade_time = m.get('LastDowngradeTime')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('MongosList') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceMongosList()
            self.mongos_list = temp_model.from_map(m['MongosList'])
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplacateId') is not None:
            self.replacate_id = m.get('ReplacateId')
        if m.get('ReplicaSetName') is not None:
            self.replica_set_name = m.get('ReplicaSetName')
        if m.get('ReplicaSets') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceReplicaSets()
            self.replica_sets = temp_model.from_map(m['ReplicaSets'])
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('ShardList') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceShardList()
            self.shard_list = temp_model.from_map(m['ShardList'])
        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SyncPercent') is not None:
            self.sync_percent = m.get('SyncPercent')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UseClusterBackup') is not None:
            self.use_cluster_backup = m.get('UseClusterBackup')
        if m.get('VPCCloudInstanceIds') is not None:
            self.vpccloud_instance_ids = m.get('VPCCloudInstanceIds')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstances(TeaModel):
    def __init__(self, dbinstance=None):
        self.dbinstance = dbinstance  # type: list[DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstance]

    def validate(self):
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBodyDBInstances, self).to_map()
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
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstancesDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(self, dbinstances=None, request_id=None):
        # The details of the instances.
        self.dbinstances = dbinstances  # type: DescribeDBInstanceAttributeResponseBodyDBInstances
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbinstances:
            self.dbinstances.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstances') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstances()
            self.dbinstances = temp_model.from_map(m['DBInstances'])
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


class DescribeDBInstanceEncryptionKeyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, encryption_key=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The custom key for the instance. You can call the [DescribeUserEncryptionKeyList](~~151729~~) operation to query the list of custom keys for an ApsaraDB for MongoDB instance.
        self.encryption_key = encryption_key  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceEncryptionKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
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
        return self


class DescribeDBInstanceEncryptionKeyResponseBody(TeaModel):
    def __init__(self, creator=None, delete_date=None, description=None, encryption_key=None,
                 encryption_key_status=None, key_usage=None, material_expire_time=None, origin=None, request_id=None):
        # The UID of the key creator.
        self.creator = creator  # type: str
        # The scheduled time when the key for the instance will be deleted. If the value is empty, the key will not be deleted.
        self.delete_date = delete_date  # type: str
        # The description of the key for the instance.
        self.description = description  # type: str
        # The key for the instance.
        self.encryption_key = encryption_key  # type: str
        # Indicates whether the key for the instance is enabled. Valid values:
        # 
        # *   **Enabled**\
        # *   **Disabled**\
        self.encryption_key_status = encryption_key_status  # type: str
        # The purpose of the key for the instance.
        self.key_usage = key_usage  # type: str
        # The expiration time of the key for the instance. The time is displayed in UTC. If the value is empty, the key for the instance will not expire.
        self.material_expire_time = material_expire_time  # type: str
        # The source of the key for the instance.
        self.origin = origin  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceEncryptionKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date
        if self.description is not None:
            result['Description'] = self.description
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_key_status is not None:
            result['EncryptionKeyStatus'] = self.encryption_key_status
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionKeyStatus') is not None:
            self.encryption_key_status = m.get('EncryptionKeyStatus')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceEncryptionKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceEncryptionKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceEncryptionKeyResponse, self).to_map()
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
            temp_model = DescribeDBInstanceEncryptionKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceMonitorRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceMonitorRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDBInstanceMonitorResponseBody(TeaModel):
    def __init__(self, granularity=None, request_id=None):
        # The collection frequency of monitoring data. The value is **1** or **300**. Unit: seconds.
        self.granularity = granularity  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceMonitorResponse, self).to_map()
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
            temp_model = DescribeDBInstanceMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancePerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, key=None, node_id=None, owner_account=None, owner_id=None,
                 replica_set_role=None, resource_owner_account=None, resource_owner_id=None, role_id=None, security_token=None,
                 start_time=None):
        # The ID of the instance.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time  # type: str
        # A performance metric. For more information about the valid values, see [Performance metrics](~~64048~~).
        # 
        # >  If you specify multiple metrics, separate them with commas (,).
        self.key = key  # type: str
        # The ID of the mongos or shard node in a sharded cluster instance. You can specify this parameter to view the performance data of a single node.
        # 
        # >  This parameter is valid only when **DBInstanceId** is set to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The role of the node in a standalone or replica set instance.
        # 
        # * **Primary**\
        # * **Secondary**\
        # 
        # > * This parameter is valid only when you specify the **DBInstanceId** parameter to the ID of a standalone instance or a replica set instance.
        # > * If you set the **DBInstanceId** parameter to the ID of a standalone instance, the value of this parameter can only be **Primary**.
        self.replica_set_role = replica_set_role  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The role ID of the node in a standalone or replica set instance. You can call the [DescribeReplicaSetRole](~~62134~~) operation to query the role ID of the node.
        # 
        # >  This parameter is valid only when you specify the **DBInstanceId** parameter to the ID of a standalone instance or a replica set instance.
        self.role_id = role_id  # type: str
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValuesPerformanceValue(TeaModel):
    def __init__(self, date=None, value=None):
        # The date and time when the metric value was generated.
        self.date = date  # type: str
        # The value of the performance metric.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValuesPerformanceValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues(TeaModel):
    def __init__(self, performance_value=None):
        self.performance_value = performance_value  # type: list[DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValuesPerformanceValue]

    def validate(self):
        if self.performance_value:
            for k in self.performance_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceValue'] = []
        if self.performance_value is not None:
            for k in self.performance_value:
                result['PerformanceValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.performance_value = []
        if m.get('PerformanceValue') is not None:
            for k in m.get('PerformanceValue'):
                temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValuesPerformanceValue()
                self.performance_value.append(temp_model.from_map(k))
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKey(TeaModel):
    def __init__(self, key=None, performance_values=None, unit=None, value_format=None):
        # The performance metric.
        self.key = key  # type: str
        # Details about the performance metric values.
        self.performance_values = performance_values  # type: DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues
        # The unit of the performance metric.
        self.unit = unit  # type: str
        # The format of the performance metric value. If the performance metric contains multiple fields, the fields are separated with **\&amp;** symbols.
        # 
        # For example, if you query disk usage, the returned **ValueFormat** value is in the **ins_size\&amp;data_size\&amp;log_size** format.
        self.value_format = value_format  # type: str

    def validate(self):
        if self.performance_values:
            self.performance_values.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.performance_values is not None:
            result['PerformanceValues'] = self.performance_values.to_map()
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.value_format is not None:
            result['ValueFormat'] = self.value_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('PerformanceValues') is not None:
            temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues()
            self.performance_values = temp_model.from_map(m['PerformanceValues'])
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('ValueFormat') is not None:
            self.value_format = m.get('ValueFormat')
        return self


class DescribeDBInstancePerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(self, performance_key=None):
        self.performance_key = performance_key  # type: list[DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKey]

    def validate(self):
        if self.performance_key:
            for k in self.performance_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBodyPerformanceKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceKey'] = []
        if self.performance_key is not None:
            for k in self.performance_key:
                result['PerformanceKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.performance_key = []
        if m.get('PerformanceKey') is not None:
            for k in m.get('PerformanceKey'):
                temp_model = DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKey()
                self.performance_key.append(temp_model.from_map(k))
        return self


class DescribeDBInstancePerformanceResponseBody(TeaModel):
    def __init__(self, end_time=None, performance_keys=None, request_id=None, start_time=None):
        # The end of the time range to query. The time is in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.end_time = end_time  # type: str
        # Details about the performance metrics.
        self.performance_keys = performance_keys  # type: DescribeDBInstancePerformanceResponseBodyPerformanceKeys
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The beginning of the time range to query. The time is in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.start_time = start_time  # type: str

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        _map = super(DescribeDBInstancePerformanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSSLRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDBInstanceSSLResponseBody(TeaModel):
    def __init__(self, cert_common_name=None, request_id=None, sslexpired_time=None, sslstatus=None):
        # The name of the SSL certificate.
        self.cert_common_name = cert_common_name  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The time when the SSL certificate expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in Coordinated Universal Time (UTC).
        self.sslexpired_time = sslexpired_time  # type: str
        # The status of the SSL feature. Valid values:
        # 
        # *   **Open**: The SSL feature is enabled.
        # *   **Closed**: The SSL feature is disabled.
        self.sslstatus = sslstatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSSLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time
        if self.sslstatus is not None:
            result['SSLStatus'] = self.sslstatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        if m.get('SSLStatus') is not None:
            self.sslstatus = m.get('SSLStatus')
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


class DescribeDBInstanceTDEInfoRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceTDEInfoRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDBInstanceTDEInfoResponseBody(TeaModel):
    def __init__(self, encryption_key=None, encryptor_name=None, request_id=None, role_arn=None, tdestatus=None):
        self.encryption_key = encryption_key  # type: str
        self.encryptor_name = encryptor_name  # type: str
        self.request_id = request_id  # type: str
        self.role_arn = role_arn  # type: str
        self.tdestatus = tdestatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceTDEInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryptor_name is not None:
            result['EncryptorName'] = self.encryptor_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptorName') is not None:
            self.encryptor_name = m.get('EncryptorName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class DescribeDBInstanceTDEInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceTDEInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceTDEInfoResponse, self).to_map()
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
            temp_model = DescribeDBInstanceTDEInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the instance. Valid values of N: **1** to **20**.
        # 
        # *   The key cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   It can be up to 64 characters in length.
        # *   It cannot be an empty string.
        self.key = key  # type: str
        # The tag value of the instance. Valid values of N: **1** to **20**.
        # 
        # *   The value cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   The value can be up to 128 characters in length.
        # *   It can be an empty string.
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
    def __init__(self, charge_type=None, connection_domain=None, dbinstance_class=None,
                 dbinstance_description=None, dbinstance_id=None, dbinstance_status=None, dbinstance_type=None, dbnode_type=None,
                 engine=None, engine_version=None, expire_time=None, expired=None, network_type=None, owner_account=None,
                 owner_id=None, page_number=None, page_size=None, region_id=None, replication_factor=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None, tag=None,
                 v_switch_id=None, vpc_id=None, zone_id=None):
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The endpoint of the node. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the endpoint of the node.
        self.connection_domain = connection_domain  # type: str
        # The instance type. For more information about valid values, see [Instance types](~~57141~~).
        self.dbinstance_class = dbinstance_class  # type: str
        # The name of the instance. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   It can contain digits, letters, underscores (\_), and hyphens (-).
        # *   It must be 2 to 256 characters in length.
        self.dbinstance_description = dbinstance_description  # type: str
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The state of the instance. For more information about valid values, see [Instance states](~~63870~~).
        self.dbinstance_status = dbinstance_status  # type: str
        # The architecture of the instance. Valid values:
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        self.dbinstance_type = dbinstance_type  # type: str
        # The type of the node in the instance. This parameter is used to filter standard or test instance.
        # 
        # 1.  Valid value for a standalone or DBFS instance.
        # 2.  Valid value for a standard instance that comes in the replica set or sharded cluster architecture: standard
        # 3.  Valid value when all instances are displayed: default
        self.dbnode_type = dbnode_type  # type: str
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine  # type: str
        # The database engine version of the instance. Valid values:
        # 
        # *   **5.0**\
        # *   **4.4**\
        # *   **4.2**\
        # *   **4.0**\
        # *   **3.4**\
        self.engine_version = engine_version  # type: str
        # The time when the instance expires.
        self.expire_time = expire_time  # type: str
        # Specifies whether the instance has expired. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.expired = expired  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**\
        # *   **VPC**\
        self.network_type = network_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value of this parameter must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size  # type: int
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The number of nodes in the replica set instance. Valid values:
        # 
        # *   **3**\
        # *   **5**\
        # *   **7**\
        self.replication_factor = replication_factor  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The tags of the instance.
        self.tag = tag  # type: list[DescribeDBInstancesRequestTag]
        # The vSwitch ID of the instance.
        self.v_switch_id = v_switch_id  # type: str
        # The VPC ID of the instance.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

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
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_type is not None:
            result['DBNodeType'] = self.dbnode_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
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
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeType') is not None:
            self.dbnode_type = m.get('DBNodeType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
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
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosListMongosAttribute(TeaModel):
    def __init__(self, node_class=None, node_description=None, node_id=None):
        # The type of the mongos node.
        self.node_class = node_class  # type: str
        # The description of the mongos node.
        self.node_description = node_description  # type: str
        # The ID of the mongos node.
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosListMongosAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList(TeaModel):
    def __init__(self, mongos_attribute=None):
        self.mongos_attribute = mongos_attribute  # type: list[DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosListMongosAttribute]

    def validate(self):
        if self.mongos_attribute:
            for k in self.mongos_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MongosAttribute'] = []
        if self.mongos_attribute is not None:
            for k in self.mongos_attribute:
                result['MongosAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mongos_attribute = []
        if m.get('MongosAttribute') is not None:
            for k in m.get('MongosAttribute'):
                temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosListMongosAttribute()
                self.mongos_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardListShardAttribute(TeaModel):
    def __init__(self, node_class=None, node_description=None, node_id=None, node_storage=None,
                 readonly_replicas=None):
        # The type of the shard node.
        self.node_class = node_class  # type: str
        # The description of the shard node.
        self.node_description = node_description  # type: str
        # The ID of the shard node.
        self.node_id = node_id  # type: str
        # The storage capacity of the shard node. Unit: GB.
        self.node_storage = node_storage  # type: int
        # The number of read-only nodes in the shard node. Valid values: **0** to **5**.
        self.readonly_replicas = readonly_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardListShardAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        return self


class DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList(TeaModel):
    def __init__(self, shard_attribute=None):
        self.shard_attribute = shard_attribute  # type: list[DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardListShardAttribute]

    def validate(self):
        if self.shard_attribute:
            for k in self.shard_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ShardAttribute'] = []
        if self.shard_attribute is not None:
            for k in self.shard_attribute:
                result['ShardAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.shard_attribute = []
        if m.get('ShardAttribute') is not None:
            for k in m.get('ShardAttribute'):
                temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardListShardAttribute()
                self.shard_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyDBInstancesDBInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstancesDBInstanceTagsTag, self).to_map()
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


class DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBInstancesResponseBodyDBInstancesDBInstanceTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags, self).to_map()
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
                temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyDBInstancesDBInstance(TeaModel):
    def __init__(self, capacity_unit=None, charge_type=None, creation_time=None, dbinstance_class=None,
                 dbinstance_description=None, dbinstance_id=None, dbinstance_status=None, dbinstance_storage=None, dbinstance_type=None,
                 destroy_time=None, engine=None, engine_version=None, expire_time=None, hidden_zone_id=None, kind_code=None,
                 last_downgrade_time=None, lock_mode=None, mongos_list=None, network_type=None, region_id=None, replication_factor=None,
                 resource_group_id=None, secondary_zone_id=None, shard_list=None, storage_type=None, tags=None, vpc_auth_mode=None,
                 zone_id=None):
        # The read and write throughput consumed by the instance.
        # 
        # > This parameter is returned when the instance is a serverless instance.
        self.capacity_unit = capacity_unit  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The time when the instance was created. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time  # type: str
        # The instance type.
        self.dbinstance_class = dbinstance_class  # type: str
        # The description of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The status of the instance. For more information, see [Instance states](~~63870~~).
        self.dbinstance_status = dbinstance_status  # type: str
        # The storage capacity of the instance.
        self.dbinstance_storage = dbinstance_storage  # type: int
        # The architecture of the instance. Valid values:
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        self.dbinstance_type = dbinstance_type  # type: str
        # The time when the instance data was destroyed. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > 
        # 
        # *   Subscription instances are released 15 days after expiration. After the instances are released, the data of the instances is deleted and cannot be restored.
        # 
        # *   Pay-as-you-go instances are locked after the payments have been overdue for longer than 24 hours. The instances are released after the payments have been overdue for longer than 15 days. The data of released instances is deleted and cannot be restored.
        self.destroy_time = destroy_time  # type: str
        # The database engine of the instance.
        self.engine = engine  # type: str
        # The database engine version of the instance. Valid values:
        # 
        # *   **5.0**\
        # *   **4.4**\
        # *   **4.2**\
        # *   **4.0**\
        # *   **3.4**\
        self.engine_version = engine_version  # type: str
        # The time when the instance expires. The time is in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.expire_time = expire_time  # type: str
        # The ID of the secondary zone 2 of the instance. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hongkong Zone B
        # *   **cn-hongkong-c**: Hongkong Zone C
        # *   **cn-hongkong-d**: Hongkong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > 
        # 
        # *   This parameter is returned if the instance is a replica set or sharded cluster instance that runs MongoDB 4.4 or 5.0 and uses multi-zone deployment.
        # 
        # *   This parameter is returned only if you use the Chine site (aliyun.com).
        self.hidden_zone_id = hidden_zone_id  # type: str
        # The kind code of the instance. Valid values:
        # 
        # *   **0**: physical machine
        # *   **1**: ECS instance
        # *   **2**: Docker cluster
        # *   **18**: Kubernetes cluster
        self.kind_code = kind_code  # type: str
        # The date when the last downgrade operation was performed.
        self.last_downgrade_time = last_downgrade_time  # type: str
        # The lock state of the instance. Valid values:
        # 
        # *   **Unlock**: The cluster is not locked.
        # *   **ManualLock**: The instance is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked due to instance expiration.
        # *   **LockByRestoration**: The instance is automatically locked before it is rolled back.
        # *   **LockByDiskQuota**: The instance is automatically locked due to exhausted storage capacity.
        # *   **Released**: The instance is released. After an instance is released, the instance cannot be unlocked. You can only restore the backup data of the instance to a new instance. This process requires a long period of time.
        self.lock_mode = lock_mode  # type: str
        # The details of the mongos nodes.
        # 
        # > This parameter is returned if the instance is a sharded cluster instance.
        self.mongos_list = mongos_list  # type: DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**\
        # *   **VPC**\
        self.network_type = network_type  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The number of nodes in the instance.
        # 
        # > This parameter is returned if the instance is a replica set instance.
        self.replication_factor = replication_factor  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the secondary zone 1 of the instance. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hongkong Zone B
        # *   **cn-hongkong-c**: Hongkong Zone C
        # *   **cn-hongkong-d**: Hongkong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > 
        # 
        # *   This parameter is returned if the instance is a replica set or sharded cluster instance that runs MongoDB 4.4 or 5.0 and uses multi-zone deployment.
        # 
        # *   This parameter is returned only if you use the Chine site (aliyun.com).
        self.secondary_zone_id = secondary_zone_id  # type: str
        # The details of the shard nodes.
        # 
        # > This parameter is returned if the instance is a sharded cluster instance.
        self.shard_list = shard_list  # type: DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd**: enhanced SSD (ESSD)
        # *   **local_ssd**: local SSD
        self.storage_type = storage_type  # type: str
        # The details of the resource tags.
        self.tags = tags  # type: DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags
        # Indicates whether password-free access within a VPC is enabled. Valid values:
        # 
        # *   **Open**: Password-free access is enabled.
        # *   **Close**: Password-free access is disabled.
        self.vpc_auth_mode = vpc_auth_mode  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.mongos_list:
            self.mongos_list.validate()
        if self.shard_list:
            self.shard_list.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstancesDBInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity_unit is not None:
            result['CapacityUnit'] = self.capacity_unit
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.hidden_zone_id is not None:
            result['HiddenZoneId'] = self.hidden_zone_id
        if self.kind_code is not None:
            result['KindCode'] = self.kind_code
        if self.last_downgrade_time is not None:
            result['LastDowngradeTime'] = self.last_downgrade_time
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.mongos_list is not None:
            result['MongosList'] = self.mongos_list.to_map()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id
        if self.shard_list is not None:
            result['ShardList'] = self.shard_list.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CapacityUnit') is not None:
            self.capacity_unit = m.get('CapacityUnit')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HiddenZoneId') is not None:
            self.hidden_zone_id = m.get('HiddenZoneId')
        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')
        if m.get('LastDowngradeTime') is not None:
            self.last_downgrade_time = m.get('LastDowngradeTime')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MongosList') is not None:
            temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceMongosList()
            self.mongos_list = temp_model.from_map(m['MongosList'])
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')
        if m.get('ShardList') is not None:
            temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceShardList()
            self.shard_list = temp_model.from_map(m['ShardList'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBodyDBInstances(TeaModel):
    def __init__(self, dbinstance=None):
        self.dbinstance = dbinstance  # type: list[DescribeDBInstancesResponseBodyDBInstancesDBInstance]

    def validate(self):
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBodyDBInstances, self).to_map()
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
                temp_model = DescribeDBInstancesResponseBodyDBInstancesDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(self, dbinstances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The details of the instances.
        self.dbinstances = dbinstances  # type: DescribeDBInstancesResponseBodyDBInstances
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The number of instances in the query results.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dbinstances:
            self.dbinstances.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances.to_map()
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
        if m.get('DBInstances') is not None:
            temp_model = DescribeDBInstancesResponseBodyDBInstances()
            self.dbinstances = temp_model.from_map(m['DBInstances'])
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


class DescribeDBInstancesOverviewRequest(TeaModel):
    def __init__(self, charge_type=None, engine_version=None, instance_class=None, instance_ids=None,
                 instance_status=None, instance_type=None, network_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None, v_switch_id=None,
                 vpc_id=None, zone_id=None):
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The database engine version of the instance. Valid values: **5.0**, **4.4**, **4.2**, **4.0**, and **3.4**.
        self.engine_version = engine_version  # type: str
        # The instance type of the instance. The instance type varies based on the instance architecture. For more information about instance types supported by different instance architectures, see the following topics:
        # 
        # *   [Standalone instance types](~~311407~~)
        # *   [Replica set instance types](~~311410~~)
        # *   [Sharded cluster instance types](~~311414~~)
        self.instance_class = instance_class  # type: str
        # The ID of the instance for which you want to query the overview information.
        # 
        # > * If you do not specify this parameter, the overview information of all instances under this account is queried.
        # > * Separate the instance IDs with commas (,).
        self.instance_ids = instance_ids  # type: str
        # The state of the instance. For more information about valid values, see [Instance states](~~63870~~).
        self.instance_status = instance_status  # type: str
        # The category of the instance. Valid values:
        # 
        # - **sharding**: sharded cluster instance
        # - **replicate**: replica set or standalone instance
        # 
        # > * To query the overview information of a sharded cluster instance, you must set the parameter to **sharding**.
        # > * If you do not specify this parameter, the overview information of all instances under this account is queried.
        self.instance_type = instance_type  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**\
        # *   **VPC**\
        self.network_type = network_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group. For more information, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id  # type: str
        # The ID of the zone.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
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
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
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
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesOverviewResponseBodyDBInstancesMongosList(TeaModel):
    def __init__(self, node_class=None, node_description=None, node_id=None):
        # The type of the mongos node.
        self.node_class = node_class  # type: str
        # The description of the mongos node.
        self.node_description = node_description  # type: str
        # The ID of the mongos node.
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesOverviewResponseBodyDBInstancesMongosList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeDBInstancesOverviewResponseBodyDBInstancesShardList(TeaModel):
    def __init__(self, node_class=None, node_description=None, node_id=None, node_storage=None,
                 readonly_replicas=None):
        # The instance type of the shard node.
        self.node_class = node_class  # type: str
        # The description of the shard node.
        self.node_description = node_description  # type: str
        # The ID of the shard node.
        self.node_id = node_id  # type: str
        # The storage capacity of the shard node. Unit: GB.
        self.node_storage = node_storage  # type: int
        # The number of read-only nodes in the shard node. Valid values: **0** to **5**.
        self.readonly_replicas = readonly_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesOverviewResponseBodyDBInstancesShardList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_description is not None:
            result['NodeDescription'] = self.node_description
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeDescription') is not None:
            self.node_description = m.get('NodeDescription')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        return self


class DescribeDBInstancesOverviewResponseBodyDBInstancesTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N of the instance. Valid values of N: **1** to **20**.
        # 
        # *   The key cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   The key can be up to 64 characters in length.
        # *   The key cannot be an empty string.
        self.key = key  # type: str
        # The value of tag N of the instance. Valid values of N: **1** to **20**.
        # 
        # *   The value cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   The value can be up to 128 characters in length.
        # *   The value can be an empty string.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesOverviewResponseBodyDBInstancesTags, self).to_map()
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


class DescribeDBInstancesOverviewResponseBodyDBInstances(TeaModel):
    def __init__(self, capacity_unit=None, charge_type=None, creation_time=None, dbinstance_class=None,
                 dbinstance_description=None, dbinstance_id=None, dbinstance_status=None, dbinstance_storage=None, dbinstance_type=None,
                 destroy_time=None, engine=None, engine_version=None, expire_time=None, kind_code=None, last_downgrade_time=None,
                 lock_mode=None, mongos_list=None, network_type=None, region_id=None, replication_factor=None,
                 resource_group_id=None, shard_list=None, tags=None, vpc_auth_mode=None, zone_id=None):
        # The I/O throughput consumed by the instance.
        # 
        # > * This parameter is returned when the instance is a serverless instance.
        # > * Serverless instances are available only in the China site (aliyun.com).
        self.capacity_unit = capacity_unit  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The time when the instance was created. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time  # type: str
        # The instance type of the instance. The instance type varies based on the instance architecture. For more information about instance types supported by different instance architectures, see the following topics:
        # 
        # *   [Standalone instance types](~~311407~~)
        # *   [Replica set instance types](~~311410~~)
        # *   [Sharded cluster instance types](~~311414~~)
        self.dbinstance_class = dbinstance_class  # type: str
        # The description of the instance.
        self.dbinstance_description = dbinstance_description  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The state of the instance. For more information about valid values, see [Instance states](~~63870~~).
        self.dbinstance_status = dbinstance_status  # type: str
        # The storage capacity of the instance.
        self.dbinstance_storage = dbinstance_storage  # type: int
        # The category of the instance. Valid values:
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        self.dbinstance_type = dbinstance_type  # type: str
        # The time when the instance data was destroyed. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.destroy_time = destroy_time  # type: str
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine  # type: str
        # The database engine version of the instance.
        self.engine_version = engine_version  # type: str
        # The time when the instance expires. The time is in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.expire_time = expire_time  # type: str
        # The kind code of the instance. Valid values:
        # 
        # *   **0**: physical machine
        # *   **1**: Elastic Compute Service (ECS) instance
        # *   **2**: Docker cluster
        # *   **18**: Kubernetes cluster
        self.kind_code = kind_code  # type: str
        # The last time when the instance was downgraded.
        self.last_downgrade_time = last_downgrade_time  # type: str
        # Indicates whether the instance is locked. Valid values:
        # 
        # *   **Unlock**: The instance is not locked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The instance is automatically locked after it expires.
        # *   **LockByRestoration**: The instance is automatically locked before it is rolled back.
        # *   **LockByDiskQuota**: The instance is automatically locked after the storage capacity is exhausted.
        # *   **Released**: The instance is released. After an instance is released, the instance cannot be unlocked. You can only restore the backup data of the instance to a new instance. This process requires an extended period of time.
        self.lock_mode = lock_mode  # type: str
        # Details about the mongos node.
        # 
        # >  This parameter is returned if the instance is a sharded cluster instance.
        self.mongos_list = mongos_list  # type: list[DescribeDBInstancesOverviewResponseBodyDBInstancesMongosList]
        # The network type of the instance. Valid values:
        # 
        # *   **Classic**\
        # *   **VPC**\
        self.network_type = network_type  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str
        # The number of nodes in the instance.
        # 
        # >  This parameter is returned if the instance is a replica set instance.
        self.replication_factor = replication_factor  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # Details about the shard node.
        # 
        # >  This parameter is returned if the instance is a sharded cluster instance.
        self.shard_list = shard_list  # type: list[DescribeDBInstancesOverviewResponseBodyDBInstancesShardList]
        # The tags of the instance.
        self.tags = tags  # type: list[DescribeDBInstancesOverviewResponseBodyDBInstancesTags]
        # Indicates whether password-free access within a VPC is enabled. Valid values:
        # 
        # *   **Open**: Password-free access is enabled.
        # *   **Close**: Password-free access is disabled.
        self.vpc_auth_mode = vpc_auth_mode  # type: str
        # The zone ID of the instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.mongos_list:
            for k in self.mongos_list:
                if k:
                    k.validate()
        if self.shard_list:
            for k in self.shard_list:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesOverviewResponseBodyDBInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity_unit is not None:
            result['CapacityUnit'] = self.capacity_unit
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.kind_code is not None:
            result['KindCode'] = self.kind_code
        if self.last_downgrade_time is not None:
            result['LastDowngradeTime'] = self.last_downgrade_time
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        result['MongosList'] = []
        if self.mongos_list is not None:
            for k in self.mongos_list:
                result['MongosList'].append(k.to_map() if k else None)
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['ShardList'] = []
        if self.shard_list is not None:
            for k in self.shard_list:
                result['ShardList'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CapacityUnit') is not None:
            self.capacity_unit = m.get('CapacityUnit')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')
        if m.get('LastDowngradeTime') is not None:
            self.last_downgrade_time = m.get('LastDowngradeTime')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        self.mongos_list = []
        if m.get('MongosList') is not None:
            for k in m.get('MongosList'):
                temp_model = DescribeDBInstancesOverviewResponseBodyDBInstancesMongosList()
                self.mongos_list.append(temp_model.from_map(k))
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.shard_list = []
        if m.get('ShardList') is not None:
            for k in m.get('ShardList'):
                temp_model = DescribeDBInstancesOverviewResponseBodyDBInstancesShardList()
                self.shard_list.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDBInstancesOverviewResponseBodyDBInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesOverviewResponseBody(TeaModel):
    def __init__(self, dbinstances=None, request_id=None, total_count=None):
        # Details about the instances.
        self.dbinstances = dbinstances  # type: list[DescribeDBInstancesOverviewResponseBodyDBInstances]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of instances in the query result.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.dbinstances:
            for k in self.dbinstances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k in self.dbinstances:
                result['DBInstances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k in m.get('DBInstances'):
                temp_model = DescribeDBInstancesOverviewResponseBodyDBInstances()
                self.dbinstances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDBInstancesOverviewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstancesOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesOverviewResponse, self).to_map()
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
            temp_model = DescribeDBInstancesOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeErrorLogRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, end_time=None, node_id=None, owner_account=None,
                 owner_id=None, page_number=None, page_size=None, resource_group_id=None, resource_owner_account=None,
                 resource_owner_id=None, role_type=None, security_token=None, start_time=None):
        # The ID of the instance.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The end of the time range to query. The end time must be later than the start time and within 24 hours from the start time. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The ID of the mongos node or shard node whose error logs you want to query in the instance. If the instance is a sharded cluster instance, you must specify this parameter.
        # 
        # >  This parameter is valid only when **DBInstanceId** is set to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30** to **100**.
        self.page_size = page_size  # type: int
        # The ID of the resource group. For more information, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The role of the node whose error logs you want to query in the instance. Valid values:
        # 
        # *   **primary**\
        # *   **secondary**\
        # 
        # >  If you set the **NodeId** parameter to the ID of a mongos node, the RoleType parameter must be set to **primary**.
        self.role_type = role_type  # type: str
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeErrorLogRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeErrorLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, category=None, conn_info=None, content=None, create_time=None, id=None):
        # The category of the log entry. Valid values:
        # 
        # *   NETWORK: network connection log
        # *   ACCESS: access control log
        # *   \-: general log
        # *   COMMAND: slow query log
        # *   SHARDING: sharded cluster log
        # *   STORAGE: storage engine log
        # *   CONNPOOL: connection pool log
        # *   ASIO: asynchronous I/O operation log
        # *   WRITE: slow update log
        self.category = category  # type: str
        # The connection information of the log entry.
        self.conn_info = conn_info  # type: str
        # The content of the log entry.
        self.content = content  # type: str
        # The time when the log entry was generated. The time is in the *yyyy-MM-dd*T*HH:mm:ss***Z format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The ID of the log entry.
        self.id = id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeErrorLogRecordsResponseBodyItemsLogRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.conn_info is not None:
            result['ConnInfo'] = self.conn_info
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ConnInfo') is not None:
            self.conn_info = m.get('ConnInfo')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeErrorLogRecordsResponseBodyItems(TeaModel):
    def __init__(self, log_records=None):
        self.log_records = log_records  # type: list[DescribeErrorLogRecordsResponseBodyItemsLogRecords]

    def validate(self):
        if self.log_records:
            for k in self.log_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeErrorLogRecordsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogRecords'] = []
        if self.log_records is not None:
            for k in self.log_records:
                result['LogRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_records = []
        if m.get('LogRecords') is not None:
            for k in m.get('LogRecords'):
                temp_model = DescribeErrorLogRecordsResponseBodyItemsLogRecords()
                self.log_records.append(temp_model.from_map(k))
        return self


class DescribeErrorLogRecordsResponseBody(TeaModel):
    def __init__(self, engine=None, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        # The database engine.
        self.engine = engine  # type: str
        # Details about the log entries returned.
        self.items = items  # type: DescribeErrorLogRecordsResponseBodyItems
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_record_count = page_record_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries.
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeErrorLogRecordsResponseBody, self).to_map()
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
            temp_model = DescribeErrorLogRecordsResponseBodyItems()
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


class DescribeErrorLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeErrorLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeErrorLogRecordsResponse, self).to_map()
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
            temp_model = DescribeErrorLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalSecurityIPGroupRequest(TeaModel):
    def __init__(self, global_security_group_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.global_security_group_id = global_security_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalSecurityIPGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup(TeaModel):
    def __init__(self, dbinstances=None, gip_list=None, global_ig_name=None, global_security_group_id=None,
                 region_id=None):
        self.dbinstances = dbinstances  # type: list[str]
        self.gip_list = gip_list  # type: str
        self.global_ig_name = global_ig_name  # type: str
        self.global_security_group_id = global_security_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances
        if self.gip_list is not None:
            result['GIpList'] = self.gip_list
        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstances') is not None:
            self.dbinstances = m.get('DBInstances')
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')
        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeGlobalSecurityIPGroupResponseBody(TeaModel):
    def __init__(self, global_security_ipgroup=None, request_id=None):
        self.global_security_ipgroup = global_security_ipgroup  # type: list[DescribeGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.global_security_ipgroup:
            for k in self.global_security_ipgroup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalSecurityIPGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GlobalSecurityIPGroup'] = []
        if self.global_security_ipgroup is not None:
            for k in self.global_security_ipgroup:
                result['GlobalSecurityIPGroup'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.global_security_ipgroup = []
        if m.get('GlobalSecurityIPGroup') is not None:
            for k in m.get('GlobalSecurityIPGroup'):
                temp_model = DescribeGlobalSecurityIPGroupResponseBodyGlobalSecurityIPGroup()
                self.global_security_ipgroup.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGlobalSecurityIPGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeGlobalSecurityIPGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGlobalSecurityIPGroupResponse, self).to_map()
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
            temp_model = DescribeGlobalSecurityIPGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalSecurityIPGroupRelationRequest(TeaModel):
    def __init__(self, dbcluster_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalSecurityIPGroupRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeGlobalSecurityIPGroupRelationResponseBodyGlobalSecurityIPGroupRel(TeaModel):
    def __init__(self, gip_list=None, global_ig_name=None, global_security_group_id=None, region_id=None):
        self.gip_list = gip_list  # type: str
        self.global_ig_name = global_ig_name  # type: str
        self.global_security_group_id = global_security_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGlobalSecurityIPGroupRelationResponseBodyGlobalSecurityIPGroupRel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gip_list is not None:
            result['GIpList'] = self.gip_list
        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')
        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeGlobalSecurityIPGroupRelationResponseBody(TeaModel):
    def __init__(self, dbcluster_id=None, global_security_ipgroup_rel=None, request_id=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.global_security_ipgroup_rel = global_security_ipgroup_rel  # type: list[DescribeGlobalSecurityIPGroupRelationResponseBodyGlobalSecurityIPGroupRel]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.global_security_ipgroup_rel:
            for k in self.global_security_ipgroup_rel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGlobalSecurityIPGroupRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['GlobalSecurityIPGroupRel'] = []
        if self.global_security_ipgroup_rel is not None:
            for k in self.global_security_ipgroup_rel:
                result['GlobalSecurityIPGroupRel'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.global_security_ipgroup_rel = []
        if m.get('GlobalSecurityIPGroupRel') is not None:
            for k in m.get('GlobalSecurityIPGroupRel'):
                temp_model = DescribeGlobalSecurityIPGroupRelationResponseBodyGlobalSecurityIPGroupRel()
                self.global_security_ipgroup_rel.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGlobalSecurityIPGroupRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeGlobalSecurityIPGroupRelationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGlobalSecurityIPGroupRelationResponse, self).to_map()
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
            temp_model = DescribeGlobalSecurityIPGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_type=None, owner_account=None, owner_id=None,
                 page_number=None, page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The category of the instance. Valid values:
        # 
        # *   **replicate**: the standalone or replica set instance
        # *   **sharding**: the sharded cluster instance
        # 
        # Default value: **replicate**.
        self.dbinstance_type = dbinstance_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be a positive integer that does not exceed the maximum value of the Integer parameter. Default value: **1**.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**.
        # 
        # >  Default value: **30**.
        self.page_size = page_size  # type: long
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAutoRenewalAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem(TeaModel):
    def __init__(self, auto_renew=None, dbinstance_type=None, db_instance_id=None, duration=None, region_id=None):
        # Indicates whether auto-renewal is enabled for the instance. Valid values:
        # 
        # *   **true**: Auto-renewal is enabled for the instance.
        # *   **false**: Auto-renewal is disabled for the instance.
        self.auto_renew = auto_renew  # type: str
        # The category of the instance. Valid values:
        # 
        # *   **replicate**: the standalone or replica set instance
        # *   **sharding**: the sharded cluster instance
        self.dbinstance_type = dbinstance_type  # type: str
        # The ID of the instance.
        self.db_instance_id = db_instance_id  # type: str
        # The auto-renewal period. Unit: months.
        # 
        # > * This parameter is ruturned only when the returned value of the **AutoRenew** parameter is **true**.
        # > * You can call the [ModifyInstanceAutoRenewalAttribute](~~145979~~) operation to modify the auto-renewal period.
        self.duration = duration  # type: str
        # The region ID of the instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAutoRenewalAttributeResponseBodyItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceAutoRenewalAttributeResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class DescribeInstanceAutoRenewalAttributeResponseBody(TeaModel):
    def __init__(self, items=None, items_numbers=None, page_number=None, page_record_count=None, request_id=None):
        # Details about returned entries.
        self.items = items  # type: DescribeInstanceAutoRenewalAttributeResponseBodyItems
        # The total number of entries returned.
        self.items_numbers = items_numbers  # type: int
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries that were returned on the current page.
        self.page_record_count = page_record_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeInstanceAutoRenewalAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.items_numbers is not None:
            result['ItemsNumbers'] = self.items_numbers
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = DescribeInstanceAutoRenewalAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ItemsNumbers') is not None:
            self.items_numbers = m.get('ItemsNumbers')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceAutoRenewalAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceAutoRenewalAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceAutoRenewalAttributeResponse, self).to_map()
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
            temp_model = DescribeInstanceAutoRenewalAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKernelReleaseNotesRequest(TeaModel):
    def __init__(self, kernel_version=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The number of the minor database version. For example: **mongodb\_20180522\_0.4.8**.
        # 
        # *   If you specify this parameter, a list of version numbers later than the version specified is returned.
        # *   If you do not specify this parameter, a list of all the version numbers is returned.
        self.kernel_version = kernel_version  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKernelReleaseNotesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')
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
        return self


class DescribeKernelReleaseNotesResponseBodyReleaseNotesReleaseNote(TeaModel):
    def __init__(self, kernel_version=None, release_note=None):
        # The version number.
        self.kernel_version = kernel_version  # type: str
        # Publishes the log.
        self.release_note = release_note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKernelReleaseNotesResponseBodyReleaseNotesReleaseNote, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        return self


class DescribeKernelReleaseNotesResponseBodyReleaseNotes(TeaModel):
    def __init__(self, release_note=None):
        self.release_note = release_note  # type: list[DescribeKernelReleaseNotesResponseBodyReleaseNotesReleaseNote]

    def validate(self):
        if self.release_note:
            for k in self.release_note:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeKernelReleaseNotesResponseBodyReleaseNotes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReleaseNote'] = []
        if self.release_note is not None:
            for k in self.release_note:
                result['ReleaseNote'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.release_note = []
        if m.get('ReleaseNote') is not None:
            for k in m.get('ReleaseNote'):
                temp_model = DescribeKernelReleaseNotesResponseBodyReleaseNotesReleaseNote()
                self.release_note.append(temp_model.from_map(k))
        return self


class DescribeKernelReleaseNotesResponseBody(TeaModel):
    def __init__(self, release_notes=None, request_id=None):
        # The list of version release notes.
        self.release_notes = release_notes  # type: DescribeKernelReleaseNotesResponseBodyReleaseNotes
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.release_notes:
            self.release_notes.validate()

    def to_map(self):
        _map = super(DescribeKernelReleaseNotesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_notes is not None:
            result['ReleaseNotes'] = self.release_notes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReleaseNotes') is not None:
            temp_model = DescribeKernelReleaseNotesResponseBodyReleaseNotes()
            self.release_notes = temp_model.from_map(m['ReleaseNotes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeKernelReleaseNotesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeKernelReleaseNotesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeKernelReleaseNotesResponse, self).to_map()
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
            temp_model = DescribeKernelReleaseNotesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMongoDBLogConfigRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance. You can call the [DescribeDBInstances](~~61939~~) operation to query the ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMongoDBLogConfigRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeMongoDBLogConfigResponseBody(TeaModel):
    def __init__(self, enable_audit=None, is_etl_meta_exist=None, is_user_project_logstore_exist=None,
                 preserve_storage_for_standard=None, preserve_storage_for_trail=None, request_id=None, service_type=None, ttl_for_standard=None,
                 ttl_for_trail=None, used_storage_for_standard=None, used_storage_for_trail=None, user_project_name=None):
        # Indicates whether to enable the audit log feature is enabled.
        # 
        # *   **true**\
        # *   **false**\
        self.enable_audit = enable_audit  # type: bool
        # Indicates whether a rule to distribute logs to Logtail is created. For more information, see [Logtail overview](~~28979~~). Valid values:
        # 
        # *   **1**: A rule to distribute logs to Logtail is created.
        # *   **0** or **null**: A rule to distribute logs to Logtail is not created.
        self.is_etl_meta_exist = is_etl_meta_exist  # type: int
        # Indicates whether a Log Service project exists in the current region. Valid values:
        # 
        # *   **1**: A Log Service project exists in the current region.
        # *   **0** or **null**: A Log Service project does not exist in the current region.
        self.is_user_project_logstore_exist = is_user_project_logstore_exist  # type: int
        # The maximum storage space for the formal edition of the audit log feature. If the value is **-1**, no maximum is set.
        self.preserve_storage_for_standard = preserve_storage_for_standard  # type: long
        # The maximum storage space for the free trial edition of the audit log feature. Unit: bytes. You can set the maximum up to 107,374,182,400 bytes.
        self.preserve_storage_for_trail = preserve_storage_for_trail  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The type of the audit log feature. Valid values:
        # 
        # *   **Trail**: the free trial edition
        # *   **Standard**: the official edition
        self.service_type = service_type  # type: str
        # The retention period for the official edition of the audit log feature. Valid values: 1 to 365 days.
        self.ttl_for_standard = ttl_for_standard  # type: long
        # The retention period for the free trial edition of the audit log feature.
        self.ttl_for_trail = ttl_for_trail  # type: long
        # The used storage space for the formal edition of the audit log feature. Unit: bytes.
        self.used_storage_for_standard = used_storage_for_standard  # type: long
        # The used storage space for the free trial edition of the audit log feature. Unit: bytes.
        self.used_storage_for_trail = used_storage_for_trail  # type: long
        # The name of the Log Service project.
        self.user_project_name = user_project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMongoDBLogConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.is_etl_meta_exist is not None:
            result['IsEtlMetaExist'] = self.is_etl_meta_exist
        if self.is_user_project_logstore_exist is not None:
            result['IsUserProjectLogstoreExist'] = self.is_user_project_logstore_exist
        if self.preserve_storage_for_standard is not None:
            result['PreserveStorageForStandard'] = self.preserve_storage_for_standard
        if self.preserve_storage_for_trail is not None:
            result['PreserveStorageForTrail'] = self.preserve_storage_for_trail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.ttl_for_standard is not None:
            result['TtlForStandard'] = self.ttl_for_standard
        if self.ttl_for_trail is not None:
            result['TtlForTrail'] = self.ttl_for_trail
        if self.used_storage_for_standard is not None:
            result['UsedStorageForStandard'] = self.used_storage_for_standard
        if self.used_storage_for_trail is not None:
            result['UsedStorageForTrail'] = self.used_storage_for_trail
        if self.user_project_name is not None:
            result['UserProjectName'] = self.user_project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('IsEtlMetaExist') is not None:
            self.is_etl_meta_exist = m.get('IsEtlMetaExist')
        if m.get('IsUserProjectLogstoreExist') is not None:
            self.is_user_project_logstore_exist = m.get('IsUserProjectLogstoreExist')
        if m.get('PreserveStorageForStandard') is not None:
            self.preserve_storage_for_standard = m.get('PreserveStorageForStandard')
        if m.get('PreserveStorageForTrail') is not None:
            self.preserve_storage_for_trail = m.get('PreserveStorageForTrail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('TtlForStandard') is not None:
            self.ttl_for_standard = m.get('TtlForStandard')
        if m.get('TtlForTrail') is not None:
            self.ttl_for_trail = m.get('TtlForTrail')
        if m.get('UsedStorageForStandard') is not None:
            self.used_storage_for_standard = m.get('UsedStorageForStandard')
        if m.get('UsedStorageForTrail') is not None:
            self.used_storage_for_trail = m.get('UsedStorageForTrail')
        if m.get('UserProjectName') is not None:
            self.user_project_name = m.get('UserProjectName')
        return self


class DescribeMongoDBLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMongoDBLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMongoDBLogConfigResponse, self).to_map()
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
            temp_model = DescribeMongoDBLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterModificationHistoryRequest(TeaModel):
    def __init__(self, character_type=None, dbinstance_id=None, end_time=None, node_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None, start_time=None):
        # The role of the instance. Valid values:
        # 
        # *   **db**: shard
        # *   **cs**: Configserver
        # *   **mongos**: mongos
        # *   **logic**: sharded cluster instance
        self.character_type = character_type  # type: str
        # The ID of the instance.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The ID of the mongos node or shard node whose parameter modification records you want to query in the instance. If the instance is a sharded cluster instance, you must specify this parameter.
        # 
        # >  This parameter is valid only when **DBInstanceId** is set to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterModificationHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeParameterModificationHistoryResponseBodyHistoricalParametersHistoricalParameter(TeaModel):
    def __init__(self, modify_time=None, new_parameter_value=None, old_parameter_value=None, parameter_name=None):
        # The time when the parameter was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modify_time = modify_time  # type: str
        # The parameter value after modification.
        self.new_parameter_value = new_parameter_value  # type: str
        # The parameter value before modification.
        self.old_parameter_value = old_parameter_value  # type: str
        # The name of the modified parameter.
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterModificationHistoryResponseBodyHistoricalParametersHistoricalParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.new_parameter_value is not None:
            result['NewParameterValue'] = self.new_parameter_value
        if self.old_parameter_value is not None:
            result['OldParameterValue'] = self.old_parameter_value
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('NewParameterValue') is not None:
            self.new_parameter_value = m.get('NewParameterValue')
        if m.get('OldParameterValue') is not None:
            self.old_parameter_value = m.get('OldParameterValue')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        return self


class DescribeParameterModificationHistoryResponseBodyHistoricalParameters(TeaModel):
    def __init__(self, historical_parameter=None):
        self.historical_parameter = historical_parameter  # type: list[DescribeParameterModificationHistoryResponseBodyHistoricalParametersHistoricalParameter]

    def validate(self):
        if self.historical_parameter:
            for k in self.historical_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParameterModificationHistoryResponseBodyHistoricalParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HistoricalParameter'] = []
        if self.historical_parameter is not None:
            for k in self.historical_parameter:
                result['HistoricalParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.historical_parameter = []
        if m.get('HistoricalParameter') is not None:
            for k in m.get('HistoricalParameter'):
                temp_model = DescribeParameterModificationHistoryResponseBodyHistoricalParametersHistoricalParameter()
                self.historical_parameter.append(temp_model.from_map(k))
        return self


class DescribeParameterModificationHistoryResponseBody(TeaModel):
    def __init__(self, historical_parameters=None, request_id=None):
        # Details about the parameter modification records.
        self.historical_parameters = historical_parameters  # type: DescribeParameterModificationHistoryResponseBodyHistoricalParameters
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.historical_parameters:
            self.historical_parameters.validate()

    def to_map(self):
        _map = super(DescribeParameterModificationHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.historical_parameters is not None:
            result['HistoricalParameters'] = self.historical_parameters.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HistoricalParameters') is not None:
            temp_model = DescribeParameterModificationHistoryResponseBodyHistoricalParameters()
            self.historical_parameters = temp_model.from_map(m['HistoricalParameters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParameterModificationHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeParameterModificationHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParameterModificationHistoryResponse, self).to_map()
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
            temp_model = DescribeParameterModificationHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterTemplatesRequest(TeaModel):
    def __init__(self, engine=None, engine_version=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine  # type: str
        # The database engine version of the instance. Valid values:
        # 
        # *   **5.0**\
        # *   **4.4**\
        # *   **4.2**\
        # *   **4.0**\
        # *   **3.4**\
        self.engine_version = engine_version  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeParameterTemplatesResponseBodyParametersTemplateRecord(TeaModel):
    def __init__(self, checking_code=None, force_modify=None, force_restart=None, parameter_description=None,
                 parameter_name=None, parameter_value=None):
        # The value range of modifiable parameters.
        self.checking_code = checking_code  # type: str
        # Indicates whether the parameter is modifiable.
        # 
        # *   **false**: The parameter cannot be modified.
        # *   **true**: The parameter can be modified.
        self.force_modify = force_modify  # type: bool
        # Indicates whether a restart is required for parameter modifications to take effect.
        # 
        # *   **false**: A restart is not required. Parameter modifications immediately take effect.
        # *   **true**: A restart is required for parameter modifications to take effect.
        self.force_restart = force_restart  # type: bool
        # The description of the parameter.
        self.parameter_description = parameter_description  # type: str
        # The name of the parameter.
        self.parameter_name = parameter_name  # type: str
        # The default value of the parameter.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterTemplatesResponseBodyParametersTemplateRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.force_modify is not None:
            result['ForceModify'] = self.force_modify
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ForceModify') is not None:
            self.force_modify = m.get('ForceModify')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParameterTemplatesResponseBodyParameters(TeaModel):
    def __init__(self, template_record=None):
        self.template_record = template_record  # type: list[DescribeParameterTemplatesResponseBodyParametersTemplateRecord]

    def validate(self):
        if self.template_record:
            for k in self.template_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParameterTemplatesResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TemplateRecord'] = []
        if self.template_record is not None:
            for k in self.template_record:
                result['TemplateRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.template_record = []
        if m.get('TemplateRecord') is not None:
            for k in m.get('TemplateRecord'):
                temp_model = DescribeParameterTemplatesResponseBodyParametersTemplateRecord()
                self.template_record.append(temp_model.from_map(k))
        return self


class DescribeParameterTemplatesResponseBody(TeaModel):
    def __init__(self, engine=None, engine_version=None, parameter_count=None, parameters=None, request_id=None):
        # The database engine of the instance.
        self.engine = engine  # type: str
        # The database engine version of the instance.
        self.engine_version = engine_version  # type: str
        # The number of parameters that are supported by the instance.
        self.parameter_count = parameter_count  # type: str
        # Details about the parameter templates.
        self.parameters = parameters  # type: DescribeParameterTemplatesResponseBodyParameters
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super(DescribeParameterTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')
        if m.get('Parameters') is not None:
            temp_model = DescribeParameterTemplatesResponseBodyParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParameterTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeParameterTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeParameterTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, character_type=None, dbinstance_id=None, extra_param=None, node_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The role of the instance. Valid values:
        # 
        # *   db: a shard node.
        # *   cs: a Configserver node.
        # *   mongos: a mongos node.
        self.character_type = character_type  # type: str
        # The instance ID.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The parameter that is available in the future.
        self.extra_param = extra_param  # type: str
        # The ID of the mongos or shard node in the specified sharded cluster instance.
        # 
        # >  This parameter is valid only when you specify the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.extra_param is not None:
            result['ExtraParam'] = self.extra_param
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ExtraParam') is not None:
            self.extra_param = m.get('ExtraParam')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class DescribeParametersResponseBodyConfigParametersParameter(TeaModel):
    def __init__(self, checking_code=None, force_restart=None, modifiable_status=None, parameter_description=None,
                 parameter_name=None, parameter_value=None):
        # The valid values of the parameter.
        self.checking_code = checking_code  # type: str
        # Indicates whether a restart is required for parameter modifications to take effect. Valid values:
        # 
        # *   **false**: A restart is not required. Modifications take effect immediately.
        # *   **true**: A restart is required for parameter modifications to take effect.
        self.force_restart = force_restart  # type: bool
        # Indicates whether the parameter value can be modified. Valid values:
        # 
        # *   **false**: The parameter value cannot be modified.
        # *   **true**: The parameter value can be modified.
        self.modifiable_status = modifiable_status  # type: bool
        # The description of the parameter.
        self.parameter_description = parameter_description  # type: str
        # The name of the parameter.
        self.parameter_name = parameter_name  # type: str
        # The value of the parameter.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersResponseBodyConfigParametersParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.modifiable_status is not None:
            result['ModifiableStatus'] = self.modifiable_status
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ModifiableStatus') is not None:
            self.modifiable_status = m.get('ModifiableStatus')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParametersResponseBodyConfigParameters(TeaModel):
    def __init__(self, parameter=None):
        self.parameter = parameter  # type: list[DescribeParametersResponseBodyConfigParametersParameter]

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParametersResponseBodyConfigParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameter = []
        if m.get('Parameter') is not None:
            for k in m.get('Parameter'):
                temp_model = DescribeParametersResponseBodyConfigParametersParameter()
                self.parameter.append(temp_model.from_map(k))
        return self


class DescribeParametersResponseBodyRunningParametersParameter(TeaModel):
    def __init__(self, character_type=None, checking_code=None, force_restart=None, modifiable_status=None,
                 parameter_description=None, parameter_name=None, parameter_value=None):
        # The role of the instance. Valid values:
        # 
        # *   **db**: a shard node.
        # *   **cs**: a Configserver node.
        # *   **mongos**: a mongos node.
        self.character_type = character_type  # type: str
        # The valid values of the parameter.
        self.checking_code = checking_code  # type: str
        # Indicates whether a restart is required for parameter modifications to take effect. Valid values:
        # 
        # *   **false**: A restart is not required. Modifications take effect immediately.
        # *   **true**: A restart is required for parameter modifications to take effect.
        self.force_restart = force_restart  # type: str
        # Indicates whether the parameter value can be modified. Valid values:
        # 
        # *   **false**: The parameter value cannot be modified.
        # *   **true**: The parameter value can be modified.
        self.modifiable_status = modifiable_status  # type: str
        # The description of the parameter.
        self.parameter_description = parameter_description  # type: str
        # The name of the parameter.
        self.parameter_name = parameter_name  # type: str
        # The value of the parameter.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersResponseBodyRunningParametersParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.modifiable_status is not None:
            result['ModifiableStatus'] = self.modifiable_status
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ModifiableStatus') is not None:
            self.modifiable_status = m.get('ModifiableStatus')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParametersResponseBodyRunningParameters(TeaModel):
    def __init__(self, parameter=None):
        self.parameter = parameter  # type: list[DescribeParametersResponseBodyRunningParametersParameter]

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParametersResponseBodyRunningParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameter = []
        if m.get('Parameter') is not None:
            for k in m.get('Parameter'):
                temp_model = DescribeParametersResponseBodyRunningParametersParameter()
                self.parameter.append(temp_model.from_map(k))
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(self, config_parameters=None, engine=None, engine_version=None, request_id=None,
                 running_parameters=None):
        # The settings of parameters that are being configured.
        self.config_parameters = config_parameters  # type: DescribeParametersResponseBodyConfigParameters
        # The database engine of the instance. Default value: **mongodb**.
        self.engine = engine  # type: str
        # The database engine version of the instance.
        self.engine_version = engine_version  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The settings of the parameters that have taken effect.
        self.running_parameters = running_parameters  # type: DescribeParametersResponseBodyRunningParameters

    def validate(self):
        if self.config_parameters:
            self.config_parameters.validate()
        if self.running_parameters:
            self.running_parameters.validate()

    def to_map(self):
        _map = super(DescribeParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_parameters is not None:
            result['ConfigParameters'] = self.config_parameters.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.running_parameters is not None:
            result['RunningParameters'] = self.running_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigParameters') is not None:
            temp_model = DescribeParametersResponseBodyConfigParameters()
            self.config_parameters = temp_model.from_map(m['ConfigParameters'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunningParameters') is not None:
            temp_model = DescribeParametersResponseBodyRunningParameters()
            self.running_parameters = temp_model.from_map(m['RunningParameters'])
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


class DescribePriceRequest(TeaModel):
    def __init__(self, business_info=None, commodity_code=None, coupon_no=None, dbinstances=None,
                 order_param_out=None, order_type=None, owner_account=None, owner_id=None, product_code=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The business information. This is an additional parameter.
        self.business_info = business_info  # type: str
        # The code of the instance. Valid values:
        # 
        # *   **dds**: a replica set instance that uses the pay-as-you-go billing method
        # *   **badds**: a replica set instance that uses the subscription billing method
        # *   **dds_sharding**: a sharded cluster instance that uses the pay-as-you-go billing method
        # *   **badds_sharding**: a sharded cluster instance that uses the subscription billing method
        # *   **badds_sharding_intl**: a sharded cluster instance that uses the subscription billing method and is available on the International site (alibabacloud.com)
        # *   **badds_sharding_jp**: a sharded cluster instance that uses the subscription billing method and is available on the Japan site (jp.alibabacloud.com)
        self.commodity_code = commodity_code  # type: str
        # The coupon code. Default value: **youhuiquan_promotion_option_id_for_blank**.
        self.coupon_no = coupon_no  # type: str
        # A JSON string that contains the details of the ApsaraDB for MongoDB instance. For more information, see the [DBInstances](~~197291~~) parameter in the DescribePrice operation.
        self.dbinstances = dbinstances  # type: str
        # Specifies whether to return the OrderParams parameter. Valid values:
        # 
        # *   **false** (default)
        # *   **true**\
        self.order_param_out = order_param_out  # type: str
        # The order type. Valid values:
        # 
        # *   **BUY**\
        # *   **UPGRADE**\
        # *   **RENEW**\
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The code of the service. Default value: **dds**.
        self.product_code = product_code  # type: str
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group. For more information, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances
        if self.order_param_out is not None:
            result['OrderParamOut'] = self.order_param_out
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DBInstances') is not None:
            self.dbinstances = m.get('DBInstances')
        if m.get('OrderParamOut') is not None:
            self.order_param_out = m.get('OrderParamOut')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
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
        return self


class DescribePriceResponseBodyOrderCouponsCouponPromotionRuleIdList(TeaModel):
    def __init__(self, promotion_rule_id=None):
        self.promotion_rule_id = promotion_rule_id  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodyOrderCouponsCouponPromotionRuleIdList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_rule_id is not None:
            result['PromotionRuleId'] = self.promotion_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PromotionRuleId') is not None:
            self.promotion_rule_id = m.get('PromotionRuleId')
        return self


class DescribePriceResponseBodyOrderCouponsCoupon(TeaModel):
    def __init__(self, activity_category=None, coupon_no=None, description=None, is_selected=None, name=None,
                 option_code=None, promotion_option_code=None, promotion_rule_id_list=None):
        # The billing method to which the coupon was applied. Valid values: **payondemand**: subscription. **payasyougo**: pay-as-you-go.
        self.activity_category = activity_category  # type: str
        # The coupon ID.
        self.coupon_no = coupon_no  # type: str
        # The description of the coupon.
        self.description = description  # type: str
        # Indicates whether the coupon was selected. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_selected = is_selected  # type: str
        # The coupon name.
        self.name = name  # type: str
        # The code of the coupon.
        self.option_code = option_code  # type: str
        # The promotional option code.
        self.promotion_option_code = promotion_option_code  # type: str
        # The rules that match the coupon.
        self.promotion_rule_id_list = promotion_rule_id_list  # type: DescribePriceResponseBodyOrderCouponsCouponPromotionRuleIdList

    def validate(self):
        if self.promotion_rule_id_list:
            self.promotion_rule_id_list.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyOrderCouponsCoupon, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_category is not None:
            result['ActivityCategory'] = self.activity_category
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.description is not None:
            result['Description'] = self.description
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        if self.name is not None:
            result['Name'] = self.name
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_rule_id_list is not None:
            result['PromotionRuleIdList'] = self.promotion_rule_id_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityCategory') is not None:
            self.activity_category = m.get('ActivityCategory')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionRuleIdList') is not None:
            temp_model = DescribePriceResponseBodyOrderCouponsCouponPromotionRuleIdList()
            self.promotion_rule_id_list = temp_model.from_map(m['PromotionRuleIdList'])
        return self


class DescribePriceResponseBodyOrderCoupons(TeaModel):
    def __init__(self, coupon=None):
        self.coupon = coupon  # type: list[DescribePriceResponseBodyOrderCouponsCoupon]

    def validate(self):
        if self.coupon:
            for k in self.coupon:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyOrderCoupons, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Coupon'] = []
        if self.coupon is not None:
            for k in self.coupon:
                result['Coupon'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.coupon = []
        if m.get('Coupon') is not None:
            for k in m.get('Coupon'):
                temp_model = DescribePriceResponseBodyOrderCouponsCoupon()
                self.coupon.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBodyOrderRuleIds(TeaModel):
    def __init__(self, rule_id=None):
        self.rule_id = rule_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodyOrderRuleIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribePriceResponseBodyOrder(TeaModel):
    def __init__(self, coupons=None, currency=None, discount_amount=None, original_amount=None, rule_ids=None,
                 show_discount_info=None, trade_amount=None):
        # The coupons.
        self.coupons = coupons  # type: DescribePriceResponseBodyOrderCoupons
        # The currency.
        self.currency = currency  # type: str
        # The discount amount of the order.
        self.discount_amount = discount_amount  # type: str
        # The original price of the order.
        self.original_amount = original_amount  # type: str
        # The rules of the order.
        self.rule_ids = rule_ids  # type: DescribePriceResponseBodyOrderRuleIds
        self.show_discount_info = show_discount_info  # type: bool
        # The final price of the order.
        self.trade_amount = trade_amount  # type: str

    def validate(self):
        if self.coupons:
            self.coupons.validate()
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        if self.show_discount_info is not None:
            result['ShowDiscountInfo'] = self.show_discount_info
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = DescribePriceResponseBodyOrderCoupons()
            self.coupons = temp_model.from_map(m['Coupons'])
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('RuleIds') is not None:
            temp_model = DescribePriceResponseBodyOrderRuleIds()
            self.rule_ids = temp_model.from_map(m['RuleIds'])
        if m.get('ShowDiscountInfo') is not None:
            self.show_discount_info = m.get('ShowDiscountInfo')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class DescribePriceResponseBodyRulesRule(TeaModel):
    def __init__(self, name=None, rule_desc_id=None, title=None):
        # The name of the rule.
        self.name = name  # type: str
        # The ID of the policy.
        self.rule_desc_id = rule_desc_id  # type: long
        # The title of the rule.
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodyRulesRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribePriceResponseBodyRules(TeaModel):
    def __init__(self, rule=None):
        self.rule = rule  # type: list[DescribePriceResponseBodyRulesRule]

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyRules, self).to_map()
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
                temp_model = DescribePriceResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBodySubOrdersSubOrderRuleIds(TeaModel):
    def __init__(self, rule_id=None):
        self.rule_id = rule_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodySubOrdersSubOrderRuleIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribePriceResponseBodySubOrdersSubOrder(TeaModel):
    def __init__(self, discount_amount=None, instance_id=None, original_amount=None, rule_ids=None,
                 trade_amount=None):
        # The discount amount of the order.
        self.discount_amount = discount_amount  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The original price of the order.
        self.original_amount = original_amount  # type: str
        # The promotion rules.
        self.rule_ids = rule_ids  # type: DescribePriceResponseBodySubOrdersSubOrderRuleIds
        # The actual price of the order.
        self.trade_amount = trade_amount  # type: str

    def validate(self):
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodySubOrdersSubOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('RuleIds') is not None:
            temp_model = DescribePriceResponseBodySubOrdersSubOrderRuleIds()
            self.rule_ids = temp_model.from_map(m['RuleIds'])
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class DescribePriceResponseBodySubOrders(TeaModel):
    def __init__(self, sub_order=None):
        self.sub_order = sub_order  # type: list[DescribePriceResponseBodySubOrdersSubOrder]

    def validate(self):
        if self.sub_order:
            for k in self.sub_order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodySubOrders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubOrder'] = []
        if self.sub_order is not None:
            for k in self.sub_order:
                result['SubOrder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sub_order = []
        if m.get('SubOrder') is not None:
            for k in m.get('SubOrder'):
                temp_model = DescribePriceResponseBodySubOrdersSubOrder()
                self.sub_order.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(self, order=None, order_params=None, request_id=None, rules=None, sub_orders=None, trace_id=None):
        # The order.
        self.order = order  # type: DescribePriceResponseBodyOrder
        # The order parameters.
        # 
        # > This parameter is returned only when the **OrderParamOut** parameter is set to **true**.
        self.order_params = order_params  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The promotion rules.
        self.rules = rules  # type: DescribePriceResponseBodyRules
        # The coupon rules.
        self.sub_orders = sub_orders  # type: DescribePriceResponseBodySubOrders
        # The ID of the trace.
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.order:
            self.order.validate()
        if self.rules:
            self.rules.validate()
        if self.sub_orders:
            self.sub_orders.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order.to_map()
        if self.order_params is not None:
            result['OrderParams'] = self.order_params
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.sub_orders is not None:
            result['SubOrders'] = self.sub_orders.to_map()
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = DescribePriceResponseBodyOrder()
            self.order = temp_model.from_map(m['Order'])
        if m.get('OrderParams') is not None:
            self.order_params = m.get('OrderParams')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rules') is not None:
            temp_model = DescribePriceResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('SubOrders') is not None:
            temp_model = DescribePriceResponseBodySubOrders()
            self.sub_orders = temp_model.from_map(m['SubOrders'])
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePriceResponse, self).to_map()
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
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # Specifies the language of the returned **RegionName** and **ZoneName** values. Default value: zh. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English
        self.accept_language = accept_language  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the region.
        # 
        # >  If you do not specify this parameter, all supported regions are queried.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRegionsResponseBodyRegionsDdsRegionZonesZone(TeaModel):
    def __init__(self, vpc_enabled=None, zone_id=None, zone_name=None):
        # Indicates whether a virtual private cloud (VPC) is supported. Valid values:
        # 
        # *   **true**: VPC is supported.
        # *   **false**: VPC is not supported.
        self.vpc_enabled = vpc_enabled  # type: bool
        # The ID of the zone.
        self.zone_id = zone_id  # type: str
        # The name of the zone.
        # 
        # The return value of the LocalName parameter is in the language that is specified by the **AcceptLanguage** parameter.
        self.zone_name = zone_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsDdsRegionZonesZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeRegionsResponseBodyRegionsDdsRegionZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone  # type: list[DescribeRegionsResponseBodyRegionsDdsRegionZonesZone]

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsDdsRegionZones, self).to_map()
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
                temp_model = DescribeRegionsResponseBodyRegionsDdsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsDdsRegion(TeaModel):
    def __init__(self, end_point=None, region_id=None, region_name=None, zones=None):
        self.end_point = end_point  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the region.
        # 
        # The return value of the LocalName parameter is in the language that is specified by the **AcceptLanguage** parameter.
        self.region_name = region_name  # type: str
        # Details about the zones.
        self.zones = zones  # type: DescribeRegionsResponseBodyRegionsDdsRegionZones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsDdsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsDdsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, dds_region=None):
        self.dds_region = dds_region  # type: list[DescribeRegionsResponseBodyRegionsDdsRegion]

    def validate(self):
        if self.dds_region:
            for k in self.dds_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DdsRegion'] = []
        if self.dds_region is not None:
            for k in self.dds_region:
                result['DdsRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dds_region = []
        if m.get('DdsRegion') is not None:
            for k in m.get('DdsRegion'):
                temp_model = DescribeRegionsResponseBodyRegionsDdsRegion()
                self.dds_region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # Details about the regions.
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        # The ID of the request.
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


class DescribeRenewalPriceRequest(TeaModel):
    def __init__(self, business_info=None, coupon_no=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The business information. This is an additional parameter.
        self.business_info = business_info  # type: str
        # The coupon code. Default value: **youhuiquan_promotion_option_id_for_blank**.
        self.coupon_no = coupon_no  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenewalPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRenewalPriceResponseBodyOrderCouponsCoupon(TeaModel):
    def __init__(self, coupon_no=None, description=None, is_selected=None, name=None):
        # The coupon number.
        self.coupon_no = coupon_no  # type: str
        # The description of the coupon.
        self.description = description  # type: str
        # Indicates whether the coupon was selected.
        self.is_selected = is_selected  # type: str
        # The name of the coupon.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodyOrderCouponsCoupon, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.description is not None:
            result['Description'] = self.description
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeRenewalPriceResponseBodyOrderCoupons(TeaModel):
    def __init__(self, coupon=None):
        self.coupon = coupon  # type: list[DescribeRenewalPriceResponseBodyOrderCouponsCoupon]

    def validate(self):
        if self.coupon:
            for k in self.coupon:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodyOrderCoupons, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Coupon'] = []
        if self.coupon is not None:
            for k in self.coupon:
                result['Coupon'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.coupon = []
        if m.get('Coupon') is not None:
            for k in m.get('Coupon'):
                temp_model = DescribeRenewalPriceResponseBodyOrderCouponsCoupon()
                self.coupon.append(temp_model.from_map(k))
        return self


class DescribeRenewalPriceResponseBodyOrderRuleIds(TeaModel):
    def __init__(self, rule_id=None):
        self.rule_id = rule_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodyOrderRuleIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeRenewalPriceResponseBodyOrder(TeaModel):
    def __init__(self, coupons=None, currency=None, discount_amount=None, original_amount=None, rule_ids=None,
                 trade_amount=None):
        # Details about the coupons.
        self.coupons = coupons  # type: DescribeRenewalPriceResponseBodyOrderCoupons
        # The type of the currency. Valid values:
        # 
        # *   USD: United States dollar
        # *   JPY: Japanese Yen
        self.currency = currency  # type: str
        # The discount amount of the order.
        self.discount_amount = discount_amount  # type: float
        # The original price of the order.
        self.original_amount = original_amount  # type: float
        # The IDs of the matched rules.
        self.rule_ids = rule_ids  # type: DescribeRenewalPriceResponseBodyOrderRuleIds
        # The actual price of the order.
        self.trade_amount = trade_amount  # type: float

    def validate(self):
        if self.coupons:
            self.coupons.validate()
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodyOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = DescribeRenewalPriceResponseBodyOrderCoupons()
            self.coupons = temp_model.from_map(m['Coupons'])
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('RuleIds') is not None:
            temp_model = DescribeRenewalPriceResponseBodyOrderRuleIds()
            self.rule_ids = temp_model.from_map(m['RuleIds'])
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class DescribeRenewalPriceResponseBodyRulesRule(TeaModel):
    def __init__(self, name=None, rule_desc_id=None, title=None):
        # The name of the rule.
        self.name = name  # type: str
        # The ID of the rule.
        self.rule_desc_id = rule_desc_id  # type: long
        # The title of the rule.
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodyRulesRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeRenewalPriceResponseBodyRules(TeaModel):
    def __init__(self, rule=None):
        self.rule = rule  # type: list[DescribeRenewalPriceResponseBodyRulesRule]

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodyRules, self).to_map()
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
                temp_model = DescribeRenewalPriceResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeRenewalPriceResponseBodySubOrdersSubOrderRuleIds(TeaModel):
    def __init__(self, rule_id=None):
        self.rule_id = rule_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodySubOrdersSubOrderRuleIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeRenewalPriceResponseBodySubOrdersSubOrder(TeaModel):
    def __init__(self, discount_amount=None, instance_id=None, original_amount=None, rule_ids=None,
                 trade_amount=None):
        # The discount amount of the order.
        self.discount_amount = discount_amount  # type: float
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The original price of the order.
        self.original_amount = original_amount  # type: float
        # The IDs of the matched rules.
        self.rule_ids = rule_ids  # type: DescribeRenewalPriceResponseBodySubOrdersSubOrderRuleIds
        # The actual price of the order.
        self.trade_amount = trade_amount  # type: float

    def validate(self):
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodySubOrdersSubOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('RuleIds') is not None:
            temp_model = DescribeRenewalPriceResponseBodySubOrdersSubOrderRuleIds()
            self.rule_ids = temp_model.from_map(m['RuleIds'])
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class DescribeRenewalPriceResponseBodySubOrders(TeaModel):
    def __init__(self, sub_order=None):
        self.sub_order = sub_order  # type: list[DescribeRenewalPriceResponseBodySubOrdersSubOrder]

    def validate(self):
        if self.sub_order:
            for k in self.sub_order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBodySubOrders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubOrder'] = []
        if self.sub_order is not None:
            for k in self.sub_order:
                result['SubOrder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sub_order = []
        if m.get('SubOrder') is not None:
            for k in m.get('SubOrder'):
                temp_model = DescribeRenewalPriceResponseBodySubOrdersSubOrder()
                self.sub_order.append(temp_model.from_map(k))
        return self


class DescribeRenewalPriceResponseBody(TeaModel):
    def __init__(self, order=None, request_id=None, rules=None, sub_orders=None):
        # The list of orders.
        self.order = order  # type: DescribeRenewalPriceResponseBodyOrder
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details about the promotion rules.
        self.rules = rules  # type: DescribeRenewalPriceResponseBodyRules
        # The rules matching the coupons.
        self.sub_orders = sub_orders  # type: DescribeRenewalPriceResponseBodySubOrders

    def validate(self):
        if self.order:
            self.order.validate()
        if self.rules:
            self.rules.validate()
        if self.sub_orders:
            self.sub_orders.validate()

    def to_map(self):
        _map = super(DescribeRenewalPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.sub_orders is not None:
            result['SubOrders'] = self.sub_orders.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = DescribeRenewalPriceResponseBodyOrder()
            self.order = temp_model.from_map(m['Order'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rules') is not None:
            temp_model = DescribeRenewalPriceResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('SubOrders') is not None:
            temp_model = DescribeRenewalPriceResponseBodySubOrders()
            self.sub_orders = temp_model.from_map(m['SubOrders'])
        return self


class DescribeRenewalPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRenewalPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRenewalPriceResponse, self).to_map()
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
            temp_model = DescribeRenewalPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeReplicaSetRoleRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicaSetRoleRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeReplicaSetRoleResponseBodyReplicaSetsReplicaSet(TeaModel):
    def __init__(self, connection_domain=None, connection_port=None, expired_time=None, network_type=None,
                 replica_set_role=None, role_id=None):
        # The endpoint of the node.
        self.connection_domain = connection_domain  # type: str
        # The port of the node.
        self.connection_port = connection_port  # type: str
        # The remaining duration of the classic network endpoint. Unit: seconds.
        self.expired_time = expired_time  # type: str
        # The network type. Valid values:
        # 
        # *   **VPC**\
        # *   **Classic**\
        # *   **Public**\
        self.network_type = network_type  # type: str
        # The role of the node in the replica set.
        # 
        # *   **Primary**\
        # *   **Secondary**\
        self.replica_set_role = replica_set_role  # type: str
        # The role ID of the node.
        self.role_id = role_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicaSetRoleResponseBodyReplicaSetsReplicaSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain
        if self.connection_port is not None:
            result['ConnectionPort'] = self.connection_port
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')
        if m.get('ConnectionPort') is not None:
            self.connection_port = m.get('ConnectionPort')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class DescribeReplicaSetRoleResponseBodyReplicaSets(TeaModel):
    def __init__(self, replica_set=None):
        self.replica_set = replica_set  # type: list[DescribeReplicaSetRoleResponseBodyReplicaSetsReplicaSet]

    def validate(self):
        if self.replica_set:
            for k in self.replica_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicaSetRoleResponseBodyReplicaSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReplicaSet'] = []
        if self.replica_set is not None:
            for k in self.replica_set:
                result['ReplicaSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.replica_set = []
        if m.get('ReplicaSet') is not None:
            for k in m.get('ReplicaSet'):
                temp_model = DescribeReplicaSetRoleResponseBodyReplicaSetsReplicaSet()
                self.replica_set.append(temp_model.from_map(k))
        return self


class DescribeReplicaSetRoleResponseBody(TeaModel):
    def __init__(self, dbinstance_id=None, replica_sets=None, request_id=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # Details about the replica set roles.
        self.replica_sets = replica_sets  # type: DescribeReplicaSetRoleResponseBodyReplicaSets
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.replica_sets:
            self.replica_sets.validate()

    def to_map(self):
        _map = super(DescribeReplicaSetRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.replica_sets is not None:
            result['ReplicaSets'] = self.replica_sets.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ReplicaSets') is not None:
            temp_model = DescribeReplicaSetRoleResponseBodyReplicaSets()
            self.replica_sets = temp_model.from_map(m['ReplicaSets'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeReplicaSetRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeReplicaSetRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeReplicaSetRoleResponse, self).to_map()
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
            temp_model = DescribeReplicaSetRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoleZoneInfoRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoleZoneInfoRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRoleZoneInfoResponseBodyZoneInfosZoneInfo(TeaModel):
    def __init__(self, ins_name=None, node_type=None, role_id=None, role_type=None, zone_id=None):
        # The ID of the node.
        self.ins_name = ins_name  # type: str
        # The type of the node. Valid values:
        # 
        # *   **normal**\
        # *   **configServer**\
        # *   **shard**\
        # *   **mongos**\
        # 
        # >  Valid value for replica set instances: **normal**. Valid values for replica set instances: **configServer**, **shard**, and **mongos**.
        self.node_type = node_type  # type: str
        # The ID of the role.
        self.role_id = role_id  # type: str
        # The role of the node. Valid values:
        # 
        # *   **Primary**\
        # *   **Secondary**\
        # *   **Hidden**\
        self.role_type = role_type  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRoleZoneInfoResponseBodyZoneInfosZoneInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRoleZoneInfoResponseBodyZoneInfos(TeaModel):
    def __init__(self, zone_info=None):
        self.zone_info = zone_info  # type: list[DescribeRoleZoneInfoResponseBodyZoneInfosZoneInfo]

    def validate(self):
        if self.zone_info:
            for k in self.zone_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRoleZoneInfoResponseBodyZoneInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ZoneInfo'] = []
        if self.zone_info is not None:
            for k in self.zone_info:
                result['ZoneInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zone_info = []
        if m.get('ZoneInfo') is not None:
            for k in m.get('ZoneInfo'):
                temp_model = DescribeRoleZoneInfoResponseBodyZoneInfosZoneInfo()
                self.zone_info.append(temp_model.from_map(k))
        return self


class DescribeRoleZoneInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, zone_infos=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of information of nodes in the zone.
        self.zone_infos = zone_infos  # type: DescribeRoleZoneInfoResponseBodyZoneInfos

    def validate(self):
        if self.zone_infos:
            self.zone_infos.validate()

    def to_map(self):
        _map = super(DescribeRoleZoneInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_infos is not None:
            result['ZoneInfos'] = self.zone_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneInfos') is not None:
            temp_model = DescribeRoleZoneInfoResponseBodyZoneInfos()
            self.zone_infos = temp_model.from_map(m['ZoneInfos'])
        return self


class DescribeRoleZoneInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRoleZoneInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRoleZoneInfoResponse, self).to_map()
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
            temp_model = DescribeRoleZoneInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRunningLogRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, end_time=None, node_id=None, order_type=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, role_id=None, role_type=None, security_token=None, start_time=None):
        # The ID of the instance.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time and within 24 hours from the start time. Otherwise, the query fails.
        self.end_time = end_time  # type: str
        # The ID of the mongos node or shard node whose operational logs you want to query in the instance. If the instance is a sharded cluster instance, you must specify this parameter.
        # 
        # >  This parameter is valid only when **DBInstanceId** is set to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        # The order of time in which the operational log entries to return are sorted. Valid values:
        # 
        # *   asc: The log entries are sorted by time in ascending order.
        # *   desc: The log entries are sorted by time in descending order.
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30** to **100**.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The role ID of the node. You can call the [DescribeReplicaSetRole](~~62134~~) operation to query the role ID.
        self.role_id = role_id  # type: str
        # The role of the node whose error logs you want to query in the instance. Valid values:
        # 
        # *   **primary**\
        # *   **secondary**\
        # 
        # >  If you set the **NodeId** parameter to the ID of a mongos node, the **RoleType** parameter must be set to **primary**.
        self.role_type = role_type  # type: str
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRunningLogRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRunningLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, category=None, conn_info=None, content=None, create_time=None):
        # The category of the log entry. Valid values:
        self.category = category  # type: str
        # The connection information of the log entry.
        self.conn_info = conn_info  # type: str
        # The content of the log entry.
        self.content = content  # type: str
        # The time when the log entry was generated. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRunningLogRecordsResponseBodyItemsLogRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.conn_info is not None:
            result['ConnInfo'] = self.conn_info
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ConnInfo') is not None:
            self.conn_info = m.get('ConnInfo')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class DescribeRunningLogRecordsResponseBodyItems(TeaModel):
    def __init__(self, log_records=None):
        self.log_records = log_records  # type: list[DescribeRunningLogRecordsResponseBodyItemsLogRecords]

    def validate(self):
        if self.log_records:
            for k in self.log_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRunningLogRecordsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogRecords'] = []
        if self.log_records is not None:
            for k in self.log_records:
                result['LogRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_records = []
        if m.get('LogRecords') is not None:
            for k in m.get('LogRecords'):
                temp_model = DescribeRunningLogRecordsResponseBodyItemsLogRecords()
                self.log_records.append(temp_model.from_map(k))
        return self


class DescribeRunningLogRecordsResponseBody(TeaModel):
    def __init__(self, engine=None, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        # The database engine.
        self.engine = engine  # type: str
        # Details about the operational log entries.
        self.items = items  # type: DescribeRunningLogRecordsResponseBodyItems
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_record_count = page_record_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries.
        self.total_record_count = total_record_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeRunningLogRecordsResponseBody, self).to_map()
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
            temp_model = DescribeRunningLogRecordsResponseBodyItems()
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


class DescribeRunningLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRunningLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRunningLogRecordsResponse, self).to_map()
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
            temp_model = DescribeRunningLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSecurityGroupConfigurationResponseBodyItemsRdsEcsSecurityGroupRel(TeaModel):
    def __init__(self, net_type=None, region_id=None, security_group_id=None):
        # The network type of the ECS security group. Valid values:
        # 
        # *   **vpc**\
        # *   **classic**\
        self.net_type = net_type  # type: str
        # The region ID of the ECS security group.
        self.region_id = region_id  # type: str
        # The ID of the ECS security group.
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationResponseBodyItemsRdsEcsSecurityGroupRel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeSecurityGroupConfigurationResponseBodyItems(TeaModel):
    def __init__(self, rds_ecs_security_group_rel=None):
        self.rds_ecs_security_group_rel = rds_ecs_security_group_rel  # type: list[DescribeSecurityGroupConfigurationResponseBodyItemsRdsEcsSecurityGroupRel]

    def validate(self):
        if self.rds_ecs_security_group_rel:
            for k in self.rds_ecs_security_group_rel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RdsEcsSecurityGroupRel'] = []
        if self.rds_ecs_security_group_rel is not None:
            for k in self.rds_ecs_security_group_rel:
                result['RdsEcsSecurityGroupRel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rds_ecs_security_group_rel = []
        if m.get('RdsEcsSecurityGroupRel') is not None:
            for k in m.get('RdsEcsSecurityGroupRel'):
                temp_model = DescribeSecurityGroupConfigurationResponseBodyItemsRdsEcsSecurityGroupRel()
                self.rds_ecs_security_group_rel.append(temp_model.from_map(k))
        return self


class DescribeSecurityGroupConfigurationResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None):
        # Details about the ECS security groups.
        self.items = items  # type: DescribeSecurityGroupConfigurationResponseBodyItems
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupConfigurationResponseBody, self).to_map()
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DescribeSecurityIpsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityIpsRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup(TeaModel):
    def __init__(self, security_ip_group_attribute=None, security_ip_group_name=None, security_ip_list=None):
        # The attribute of the IP whitelist. This parameter is empty by default.
        self.security_ip_group_attribute = security_ip_group_attribute  # type: str
        # The name of the IP whitelist.
        self.security_ip_group_name = security_ip_group_name  # type: str
        # The IP addresses in the whitelist.
        self.security_ip_list = security_ip_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_ip_group_attribute is not None:
            result['SecurityIpGroupAttribute'] = self.security_ip_group_attribute
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityIpGroupAttribute') is not None:
            self.security_ip_group_attribute = m.get('SecurityIpGroupAttribute')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')
        return self


class DescribeSecurityIpsResponseBodySecurityIpGroups(TeaModel):
    def __init__(self, security_ip_group=None):
        self.security_ip_group = security_ip_group  # type: list[DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup]

    def validate(self):
        if self.security_ip_group:
            for k in self.security_ip_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecurityIpsResponseBodySecurityIpGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecurityIpGroup'] = []
        if self.security_ip_group is not None:
            for k in self.security_ip_group:
                result['SecurityIpGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.security_ip_group = []
        if m.get('SecurityIpGroup') is not None:
            for k in m.get('SecurityIpGroup'):
                temp_model = DescribeSecurityIpsResponseBodySecurityIpGroupsSecurityIpGroup()
                self.security_ip_group.append(temp_model.from_map(k))
        return self


class DescribeSecurityIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, security_ip_groups=None, security_ips=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the information of IP whitelists.
        self.security_ip_groups = security_ip_groups  # type: DescribeSecurityIpsResponseBodySecurityIpGroups
        # The IP addresses in the default whitelist.
        self.security_ips = security_ips  # type: str

    def validate(self):
        if self.security_ip_groups:
            self.security_ip_groups.validate()

    def to_map(self):
        _map = super(DescribeSecurityIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_groups is not None:
            result['SecurityIpGroups'] = self.security_ip_groups.to_map()
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroups') is not None:
            temp_model = DescribeSecurityIpsResponseBodySecurityIpGroups()
            self.security_ip_groups = temp_model.from_map(m['SecurityIpGroups'])
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class DescribeSecurityIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSecurityIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeSecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeShardingNetworkAddressRequest(TeaModel):
    def __init__(self, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of an instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # A sharded cluster instance consists of three components: mongos, shard, and Configserver.
        # 
        # >  You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the ID of the mongos, shard, or Configserverr node.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeShardingNetworkAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class DescribeShardingNetworkAddressResponseBodyCompatibleConnectionsCompatibleConnection(TeaModel):
    def __init__(self, expired_time=None, ipaddress=None, network_address=None, network_type=None, port=None,
                 vpcid=None, vswitch_id=None):
        # The remaining duration of the classic network address. Unit: seconds.
        self.expired_time = expired_time  # type: str
        # The IP address of the instance.
        self.ipaddress = ipaddress  # type: str
        # The endpoint of the instance.
        self.network_address = network_address  # type: str
        # The network type. Valid values:
        # 
        # *   **VPC**\
        # *   **Classic**\
        # *   **Public**: pubic endpoint
        self.network_type = network_type  # type: str
        # The port number.
        self.port = port  # type: str
        # The ID of the VPC.
        # 
        # >  This parameter is returned when the network type is **VPC**.
        self.vpcid = vpcid  # type: str
        # The vSwitch ID of the VPC.
        # 
        # >  This parameter is returned when the network type is **VPC**.
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeShardingNetworkAddressResponseBodyCompatibleConnectionsCompatibleConnection, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.network_address is not None:
            result['NetworkAddress'] = self.network_address
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetworkAddress') is not None:
            self.network_address = m.get('NetworkAddress')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeShardingNetworkAddressResponseBodyCompatibleConnections(TeaModel):
    def __init__(self, compatible_connection=None):
        self.compatible_connection = compatible_connection  # type: list[DescribeShardingNetworkAddressResponseBodyCompatibleConnectionsCompatibleConnection]

    def validate(self):
        if self.compatible_connection:
            for k in self.compatible_connection:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeShardingNetworkAddressResponseBodyCompatibleConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CompatibleConnection'] = []
        if self.compatible_connection is not None:
            for k in self.compatible_connection:
                result['CompatibleConnection'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.compatible_connection = []
        if m.get('CompatibleConnection') is not None:
            for k in m.get('CompatibleConnection'):
                temp_model = DescribeShardingNetworkAddressResponseBodyCompatibleConnectionsCompatibleConnection()
                self.compatible_connection.append(temp_model.from_map(k))
        return self


class DescribeShardingNetworkAddressResponseBodyNetworkAddressesNetworkAddress(TeaModel):
    def __init__(self, expired_time=None, ipaddress=None, network_address=None, network_type=None, node_id=None,
                 node_type=None, port=None, role=None, vpcid=None, vswitch_id=None):
        # The remaining duration of the classic network address. Unit: seconds.
        self.expired_time = expired_time  # type: str
        # The IP address of the instance.
        self.ipaddress = ipaddress  # type: str
        # The endpoint of the instance.
        self.network_address = network_address  # type: str
        # The network type. Valid values:
        # 
        # - **VPC**\
        # - **Classic**\
        # - **Public**: pubic endpoint
        self.network_type = network_type  # type: str
        # The ID of the mongos.
        self.node_id = node_id  # type: str
        # The type of the node. Valid values:
        # 
        # - **mongos**\
        # - **shard**\
        # - **configserver**\
        self.node_type = node_type  # type: str
        # The port number.
        self.port = port  # type: str
        # The role of the node. Valid values:
        # 
        # - Primary
        # - Secondary
        self.role = role  # type: str
        # The ID of the VPC.
        # 
        # >  This parameter is returned when the network type is **VPC**.
        self.vpcid = vpcid  # type: str
        # The vSwitch ID of the VPC.
        # 
        # >  This parameter is returned when the network type is **VPC**.
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeShardingNetworkAddressResponseBodyNetworkAddressesNetworkAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.network_address is not None:
            result['NetworkAddress'] = self.network_address
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('NetworkAddress') is not None:
            self.network_address = m.get('NetworkAddress')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeShardingNetworkAddressResponseBodyNetworkAddresses(TeaModel):
    def __init__(self, network_address=None):
        self.network_address = network_address  # type: list[DescribeShardingNetworkAddressResponseBodyNetworkAddressesNetworkAddress]

    def validate(self):
        if self.network_address:
            for k in self.network_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeShardingNetworkAddressResponseBodyNetworkAddresses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkAddress'] = []
        if self.network_address is not None:
            for k in self.network_address:
                result['NetworkAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network_address = []
        if m.get('NetworkAddress') is not None:
            for k in m.get('NetworkAddress'):
                temp_model = DescribeShardingNetworkAddressResponseBodyNetworkAddressesNetworkAddress()
                self.network_address.append(temp_model.from_map(k))
        return self


class DescribeShardingNetworkAddressResponseBody(TeaModel):
    def __init__(self, compatible_connections=None, network_addresses=None, request_id=None):
        # An array that consists of the endpoints of DynamoDB instances.
        self.compatible_connections = compatible_connections  # type: DescribeShardingNetworkAddressResponseBodyCompatibleConnections
        # An array that consists of the endpoints of ApsaraDB for MongoDB instances.
        self.network_addresses = network_addresses  # type: DescribeShardingNetworkAddressResponseBodyNetworkAddresses
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.compatible_connections:
            self.compatible_connections.validate()
        if self.network_addresses:
            self.network_addresses.validate()

    def to_map(self):
        _map = super(DescribeShardingNetworkAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_connections is not None:
            result['CompatibleConnections'] = self.compatible_connections.to_map()
        if self.network_addresses is not None:
            result['NetworkAddresses'] = self.network_addresses.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompatibleConnections') is not None:
            temp_model = DescribeShardingNetworkAddressResponseBodyCompatibleConnections()
            self.compatible_connections = temp_model.from_map(m['CompatibleConnections'])
        if m.get('NetworkAddresses') is not None:
            temp_model = DescribeShardingNetworkAddressResponseBodyNetworkAddresses()
            self.network_addresses = temp_model.from_map(m['NetworkAddresses'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeShardingNetworkAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeShardingNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeShardingNetworkAddressResponse, self).to_map()
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
            temp_model = DescribeShardingNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, end_time=None, node_id=None, order_type=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, start_time=None):
        # The ID of the instance.
        # 
        # > If you set this parameter to the ID of a sharded cluster instance, you must also specify the `NodeId` parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # > 
        # 
        # *   The end time must be later than the start time.
        # 
        # *   The end time must be within 24 hours from the start time. Otherwise, the query fails.
        self.end_time = end_time  # type: str
        # The ID of the shard node.
        # 
        # > This parameter is required only when you specify the `DBInstanceId` parameter to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        # The order of time in which the log entries to return are sorted. Valid values:
        # 
        # *   asc: The log entries are sorted by time in ascending order.
        # *   desc: The log entries are sorted by time in descending order.
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of the page to return. The value of this parameter must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: **30** to **100**.
        self.page_size = page_size  # type: int
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowLogRecordsResponseBodyItemsLogRecords(TeaModel):
    def __init__(self, account_name=None, dbname=None, docs_examined=None, execution_start_time=None,
                 host_address=None, keys_examined=None, query_times=None, return_row_counts=None, sqltext=None, table_name=None):
        # The username of the database account that performs the operation.
        self.account_name = account_name  # type: str
        # The name of the database.
        self.dbname = dbname  # type: str
        # The number of documents that are scanned during the operation.
        self.docs_examined = docs_examined  # type: long
        # The start time of the operation. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.execution_start_time = execution_start_time  # type: str
        # The host IP address that is used to connect to the database.
        self.host_address = host_address  # type: str
        # The number of rows involved in index scans.
        self.keys_examined = keys_examined  # type: long
        # The execution time of the statement. Unit: milliseconds.
        self.query_times = query_times  # type: str
        # The number of rows returned by the SQL statement.
        self.return_row_counts = return_row_counts  # type: long
        # The SQL statement that is executed during the slow operation.
        self.sqltext = sqltext  # type: str
        # The name of the collection.
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodyItemsLogRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.docs_examined is not None:
            result['DocsExamined'] = self.docs_examined
        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.keys_examined is not None:
            result['KeysExamined'] = self.keys_examined
        if self.query_times is not None:
            result['QueryTimes'] = self.query_times
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DocsExamined') is not None:
            self.docs_examined = m.get('DocsExamined')
        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('KeysExamined') is not None:
            self.keys_examined = m.get('KeysExamined')
        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSlowLogRecordsResponseBodyItems(TeaModel):
    def __init__(self, log_records=None):
        self.log_records = log_records  # type: list[DescribeSlowLogRecordsResponseBodyItemsLogRecords]

    def validate(self):
        if self.log_records:
            for k in self.log_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlowLogRecordsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogRecords'] = []
        if self.log_records is not None:
            for k in self.log_records:
                result['LogRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_records = []
        if m.get('LogRecords') is not None:
            for k in m.get('LogRecords'):
                temp_model = DescribeSlowLogRecordsResponseBodyItemsLogRecords()
                self.log_records.append(temp_model.from_map(k))
        return self


class DescribeSlowLogRecordsResponseBody(TeaModel):
    def __init__(self, engine=None, items=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        # The database engine.
        self.engine = engine  # type: str
        # Details of the slow query logs.
        self.items = items  # type: DescribeSlowLogRecordsResponseBodyItems
        # The page number of the returned page. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of slow query log entries returned on the page.
        self.page_record_count = page_record_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
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


class DescribeTagsRequest(TeaModel):
    def __init__(self, next_token=None, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None):
        # The token used to start the next query to retrieve more results.
        # 
        # >  This parameter is not required in the first query. If not all results are returned in one query, you can pass in the NextToken value returned in the previous query to perform the query again.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The resource type. Set the value to **INSTANCE**.
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


class DescribeTagsResponseBodyTags(TeaModel):
    def __init__(self, tag_key=None, tag_values=None):
        # The key of the tag.
        self.tag_key = tag_key  # type: str
        # The values of the tags.
        self.tag_values = tag_values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagsResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tags=None):
        # The token used to start the next query.
        # 
        # >  If not all results are returned in the first query, this parameter is returned. You can pass in the value of this parameter in the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details about the tags.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
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
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None, target_region_id=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The zone ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent zone list.
        self.target_region_id = target_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        return self


class DescribeUserEncryptionKeyListResponseBodyKeyIds(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = key_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListResponseBodyKeyIds, self).to_map()
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
    def __init__(self, key_ids=None, request_id=None):
        # The list of custom keys.
        self.key_ids = key_ids  # type: DescribeUserEncryptionKeyListResponseBodyKeyIds
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.key_ids:
            self.key_ids.validate()

    def to_map(self):
        _map = super(DescribeUserEncryptionKeyListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyIds') is not None:
            temp_model = DescribeUserEncryptionKeyListResponseBodyKeyIds()
            self.key_ids = temp_model.from_map(m['KeyIds'])
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


class DestroyInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The ID of the instance.
        # 
        # > **InstanceId** and **DBInstanceId** serve the same function. You need only to specify one of them.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the instance.
        # 
        # > **InstanceId** and **DBInstanceId** serve the same function. You need only to specify one of them.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of a resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DestroyInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DestroyInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DestroyInstanceResponseBody, self).to_map()
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


class DestroyInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DestroyInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DestroyInstanceResponse, self).to_map()
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
            temp_model = DestroyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateResourceRequest(TeaModel):
    def __init__(self, dbinstance_class=None, dbinstance_id=None, engine=None, engine_version=None,
                 owner_account=None, owner_id=None, readonly_replicas=None, region_id=None, replication_factor=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, shards_info=None, storage=None, zone_id=None):
        # The stype of the instance.
        # 
        # > This parameter is required when you check whether resources are sufficient for creating or upgrading a replica set instance. For more information about instance types, see [Instance types](~~57141~~).
        self.dbinstance_class = dbinstance_class  # type: str
        # The ID of the instance. This parameter is required when you check whether resources are sufficient for upgrading an instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine  # type: str
        # The version of the database engine. Valid values:
        # 
        # *   **5.0**\
        # *   **4.4**\
        # *   **4.2**\
        # *   **4.0**\
        # *   **3.4**\
        self.engine_version = engine_version  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of read-only nodes in the instance. Valid values: **1** to **5**.
        # 
        # > This parameter is not required for standalone or serverless instances.
        self.readonly_replicas = readonly_replicas  # type: str
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the region ID.
        self.region_id = region_id  # type: str
        # The number of nodes in the instance.
        # 
        # *   Set the value to **1** for standalone instances.
        # *   Valid values for replica set instances: **3**, **5**, and **7**\
        # 
        # > This parameter is not required for serverless instances.
        self.replication_factor = replication_factor  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The node information about the sharded cluster instance. This parameter is required when you check whether resources are sufficient for creating or upgrading a sharded cluster instance.
        # 
        # To check whether resources are sufficient for creating a sharded cluster instance, specify the specifications of each node in the instance. The value must be a JSON string. Example:
        # 
        #     {
        #          "ConfigSvrs":
        #              [{"Storage":20,"DBInstanceClass":"dds.cs.mid"}],
        #          "Mongos":
        #              [{"DBInstanceClass":"dds.mongos.standard"},{"DBInstanceClass":"dds.mongos.standard"}],
        #          "Shards":
        #              [{"Storage":50,"DBInstanceClass":"dds.shard.standard"},{"Storage":50,"DBInstanceClass":"dds.shard.standard"},   {"Storage":50,"DBInstanceClass":"dds.shard.standard"}]
        #      }
        # 
        # Parameters in the example:
        # 
        # *   ConfigSvrs: the Configserver node.
        # *   Mongos: the mongos node.
        # *   Shards: the shard node.
        # *   Storage: the storage space of the node.
        # *   DBInstanceClass: the instance type of the node. For more information, see [Sharded cluster instance types](~~311414~~).
        # 
        # To check whether resources are sufficient for upgrading a single node of a sharded cluster instance, specify only the information about the node to be upgraded. The value must be a JSON string. Example:
        # 
        #     {
        #          "NodeId": "d-bp147c4d9ca7****", "NodeClass": "dds.shard.standard"
        #     } 
        # 
        # Parameters in the example:
        # 
        # *   NodeId: the ID of the node.
        # *   NodeClass: the instance type of the node. For more information, see [Sharded cluster instance types](~~311414~~).
        self.shards_info = shards_info  # type: str
        # The storage capacity of the replica set instance. Unit: GB.
        # 
        # > This parameter is required for the instances that use cloud disks.
        self.storage = storage  # type: str
        # The zone ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EvaluateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.shards_info is not None:
            result['ShardsInfo'] = self.shards_info
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ShardsInfo') is not None:
            self.shards_info = m.get('ShardsInfo')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class EvaluateResourceResponseBody(TeaModel):
    def __init__(self, dbinstance_available=None, engine=None, engine_version=None, request_id=None):
        # Indicates whether the resources are sufficient in the region. Valid values:
        # 
        # *   **1**: The resources are sufficient.
        # *   **0**: The resources are insufficient.
        self.dbinstance_available = dbinstance_available  # type: str
        # The database engine of the instance. Only MongoDB is returned.
        self.engine = engine  # type: str
        # The version of the database engine.
        self.engine_version = engine_version  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EvaluateResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_available is not None:
            result['DBInstanceAvailable'] = self.dbinstance_available
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceAvailable') is not None:
            self.dbinstance_available = m.get('DBInstanceAvailable')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EvaluateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EvaluateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EvaluateResourceResponse, self).to_map()
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
            temp_model = EvaluateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag.
        self.key = key  # type: str
        # The value of tag.
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
        # The token used to start the next query to retrieve more results.
        # 
        # >  This parameter is not required in the first query. If not all results are returned in one query, you can pass in the **NextToken** value returned in the previous query to perform the query again.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the region ID of the instance.
        self.region_id = region_id  # type: str
        # The resource IDs. You must specify this parameter or the Tag parameter.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The resource type. Set the value to **INSTANCE**.
        self.resource_type = resource_type  # type: str
        # The tags that are attached to the resources.
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
        # The ID of the resource. It is the ID of the ApsaraDB for MongoDB instance.
        self.resource_id = resource_id  # type: str
        # The resource type. The return value is fixed to **ALIYUN: KVSTORE: INSTANCE**, indicating an ApsaraDB for MongoDB instance.
        self.resource_type = resource_type  # type: str
        # The key of the tag.
        self.tag_key = tag_key  # type: str
        # The value of the tag.
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
        # The token used to start the next query.
        # 
        # >  If not all results are returned in the first query, this parameter is returned. You can pass in the returned value of this parameter in the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details about the tags of the instance.
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


class MigrateAvailableZoneRequest(TeaModel):
    def __init__(self, dbinstance_id=None, effective_time=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, vswitch=None, zone_id=None):
        # The ID of the instance.
        # 
        # > If the instance is deployed in a VPC, you must specify the **Vswitch** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The time when the instance is migrated to the destination zone. Valid values:
        # 
        # *   **Immediately**: The instance is immediately migrated to the destination zone.
        # *   **MaintainTime**: The instance is migrated to the destination zone during the maintenance window of the instance.
        # 
        # Default value: **Immediately**.
        self.effective_time = effective_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the vSwitch in the destination zone.
        # 
        # > If the instance is deployed in a VPC, you must specify this parameter.
        self.vswitch = vswitch  # type: str
        # The ID of the destination zone.
        # 
        # > 
        # 
        # *   The source zone and the destination zone belong to the same region.
        # 
        # *   You can call the [DescribeRegions](~~61933~~) operation to query the zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateAvailableZoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class MigrateAvailableZoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateAvailableZoneResponseBody, self).to_map()
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


class MigrateAvailableZoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MigrateAvailableZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MigrateAvailableZoneResponse, self).to_map()
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
            temp_model = MigrateAvailableZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateToOtherZoneRequest(TeaModel):
    def __init__(self, effective_time=None, instance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, v_switch_id=None, zone_id=None):
        # The time when the instance is migrated to the destination zone. Valid values:
        # 
        # *   **Immediately**: The instance is immediately migrated to the destination zone.
        # *   **MaintainTime**: The instance is migrated during the maintenance period of the instance.
        # 
        # Default value: **Immediately**.
        self.effective_time = effective_time  # type: str
        # The ID of the instance.
        # 
        # >  If the network type of the instance is VPC, you must specify the **Vswitch** parameter .
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the vSwitch in the destination zone.
        # 
        # >  This parameter is valid and required only when the network type of the instance is VPC.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the destination zone to which you want to migrate the ApsaraDB for MongoDB instance.
        # 
        # > * The destination and source zones must be in one region.
        # > * You can call [DescribeRegions](~~61933~~) to query the zone IDs.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateToOtherZoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class MigrateToOtherZoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateToOtherZoneResponseBody, self).to_map()
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


class MigrateToOtherZoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MigrateToOtherZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MigrateToOtherZoneResponse, self).to_map()
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
            temp_model = MigrateToOtherZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(self, account_description=None, account_name=None, dbinstance_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The description of the account.
        # 
        # *   It cannot start with http:// or https://.
        # *   It must start with a letter.
        # *   It must be 2 to 256 characters in length, and can contain letters, digits, underscores (\_), and hyphens (-).
        self.account_description = account_description  # type: str
        # The name of the account for which you want to modify the description.
        self.account_name = account_name  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class ModifyAuditLogFilterRequest(TeaModel):
    def __init__(self, dbinstance_id=None, filter=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, role_type=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The type of the audit log entries to be collected. Valid values:
        # 
        # *   **admin**: O\&M and management operations
        # *   **slow**: slow query logs
        # *   **query**: query operations
        # *   **insert**: insert operations
        # *   **update**: update operations
        # *   **delete**: delete operations
        # *   **command**: protocol commands such as the aggregate method
        self.filter = filter  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The role of the node in the instance. Valid values:
        # 
        # *   **primary**\
        # *   **secondary**\
        self.role_type = role_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAuditLogFilterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyAuditLogFilterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAuditLogFilterResponseBody, self).to_map()
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


class ModifyAuditLogFilterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAuditLogFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAuditLogFilterResponse, self).to_map()
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
            temp_model = ModifyAuditLogFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAuditPolicyRequest(TeaModel):
    def __init__(self, audit_log_switch_source=None, audit_status=None, dbinstance_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None, service_type=None,
                 storage_period=None):
        # The request source for the audit log feature. Set the value to **Console**.
        self.audit_log_switch_source = audit_log_switch_source  # type: str
        # Specifies whether the audit log feature is enabled. Valid values:
        # 
        # *   **enable**\
        # *   **disabled**\
        self.audit_status = audit_status  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The type of the audit log feature. Valid values:
        # 
        # *   **Trail**: the free trial edition
        # *   **Standard**: the official edition
        # 
        # >  Default value: **Trial**. Starting from January 6, 2022, the official edition of the audit log feature has been launched in all regions, and new applications for the free trial edition have ended. We recommend that you set this parameter to **Standard**.
        self.service_type = service_type  # type: str
        # The log retention period. Valid values: 1 to 365 days. Default value: 30 days.
        self.storage_period = storage_period  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAuditPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_log_switch_source is not None:
            result['AuditLogSwitchSource'] = self.audit_log_switch_source
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.storage_period is not None:
            result['StoragePeriod'] = self.storage_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditLogSwitchSource') is not None:
            self.audit_log_switch_source = m.get('AuditLogSwitchSource')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('StoragePeriod') is not None:
            self.storage_period = m.get('StoragePeriod')
        return self


class ModifyAuditPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAuditPolicyResponseBody, self).to_map()
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


class ModifyAuditPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAuditPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAuditPolicyResponse, self).to_map()
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
            temp_model = ModifyAuditPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, backup_interval=None, backup_retention_period=None, dbinstance_id=None,
                 enable_backup_log=None, log_backup_retention_period=None, owner_account=None, owner_id=None,
                 preferred_backup_period=None, preferred_backup_time=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None, snapshot_backup_type=None):
        # The frequency at which high-frequency backups are created. Valid values:
        # 
        # *   **-1**: disables high-frequency backup.
        # *   **15**: every 15 minutes.
        # *   **30**: every 30 minutes.
        # *   **60**: every hour.
        # *   **120**: every 2 hours.
        # *   **180**: every 3 hours.
        # *   **240**: every 4 hours.
        # *   **360**: every 6 hours.
        # *   **480**: every 8 hours.
        # *   **720**: every 12 hours.
        # 
        # > * If **SnapshotBackupType** is set to **Standard**, this parameter is set to **-1** and cannot be changed.
        # > * High-frequency backup takes effect only when **SnapshotBackupType** is set to **Flash** and the value of this parameter is greater than 0.
        self.backup_interval = backup_interval  # type: str
        # The retention period of full backups.
        # 
        # > * If your instance is created before September 10, 2021, backups are retained for seven days by default.
        # > * If your instance is created after September 10, 2021, backups are retained for 30 days by default.
        self.backup_retention_period = backup_retention_period  # type: long
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # Specifies whether to enable log backup. Default value: 0. Valid values:
        # 
        # *   **0**: disables log backup.
        # *   **1**: enables log backup.
        self.enable_backup_log = enable_backup_log  # type: long
        # The number of days for which log backups are retained. Default value: 7.
        # 
        # Valid values: 7 to 730.
        self.log_backup_retention_period = log_backup_retention_period  # type: long
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The day of a week on which to back up data. Valid values:
        # 
        # *   **Monday**\
        # *   **Tuesday**\
        # *   **Wednesday**\
        # *   **Thursday**\
        # *   **Friday**\
        # *   **Saturday**\
        # *   **Sunday**\
        # 
        # >  Separate multiple values with commas (,).
        self.preferred_backup_period = preferred_backup_period  # type: str
        # The time range to back up data. Specify the time in the *HH:mm*Z-*HH:mm*Z format. The time must be in UTC.
        # 
        # >  The time range is 1 hour.
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The snapshot backup type. Default value: Standard. Valid values:
        # 
        # *   **Flash**: single-digit second backup
        # *   **Standard**: standard backup
        self.snapshot_backup_type = snapshot_backup_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_interval is not None:
            result['BackupInterval'] = self.backup_interval
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.snapshot_backup_type is not None:
            result['SnapshotBackupType'] = self.snapshot_backup_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupInterval') is not None:
            self.backup_interval = m.get('BackupInterval')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SnapshotBackupType') is not None:
            self.snapshot_backup_type = m.get('SnapshotBackupType')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(self, current_connection_string=None, dbinstance_id=None, new_connection_string=None,
                 new_port=None, node_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The current connection string, which is to be modified.
        self.current_connection_string = current_connection_string  # type: str
        # The ID of the instance.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The new connection string. It must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter.
        # 
        # >  You need only to specify the prefix of the connection string. The content other than the prefix cannot be modified.
        self.new_connection_string = new_connection_string  # type: str
        # this parameter can be used. The new port should be within the range of 1000 to 65535.
        # >When the DBInstanceId parameter is passed in as a cloud disk instance ID
        self.new_port = new_port  # type: int
        # The ID of the mongos in the specified sharded cluster instance. Only one mongos ID can be specified in each call.
        # 
        # >  This parameter is valid only if you set the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceConnectionStringRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.new_connection_string is not None:
            result['NewConnectionString'] = self.new_connection_string
        if self.new_port is not None:
            result['NewPort'] = self.new_port
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NewConnectionString') is not None:
            self.new_connection_string = m.get('NewConnectionString')
        if m.get('NewPort') is not None:
            self.new_port = m.get('NewPort')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class ModifyDBInstanceConnectionStringResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, dbinstance_description=None, dbinstance_id=None, node_id=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The name of the instance.
        # 
        # > 
        # 
        # *   The name cannot start with `http://` or `https://`.
        # 
        # *   The name must start with a letter.
        # 
        # *   The name must be 2 to 256 characters in length, and can contain letters, underscores (\_), hyphens (-), and digits.
        self.dbinstance_description = dbinstance_description  # type: str
        # The ID of the instance
        # 
        # > To modify the name of a shard or mongos node in a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the shard or mongos node in the sharded cluster instance.
        # 
        # > This parameter is valid only if you set the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class ModifyDBInstanceDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, dbinstance_id=None, maintain_end_time=None, maintain_start_time=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The end time of the maintenance window. Specify the time in the *HH:mmZ* format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time of the maintenance window.
        self.maintain_end_time = maintain_end_time  # type: str
        # The start time of the maintenance window. Specify the time in the *HH:mm*Z format. The time must be in UTC.
        self.maintain_start_time = maintain_start_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
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
        return self


class ModifyDBInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class ModifyDBInstanceMonitorRequest(TeaModel):
    def __init__(self, dbinstance_id=None, granularity=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The collection frequency of monitoring data. Valid values: **1** or **300**. Unit: seconds.
        self.granularity = granularity  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.granularity is not None:
            result['Granularity'] = self.granularity
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
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
        return self


class ModifyDBInstanceMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceMonitorResponseBody, self).to_map()
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


class ModifyDBInstanceMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceMonitorResponse, self).to_map()
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
            temp_model = ModifyDBInstanceMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceNetExpireTimeRequest(TeaModel):
    def __init__(self, classic_expend_expired_days=None, connection_string=None, dbinstance_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The retention period of the original classic network address. Valid values: **14**, **30**, **60**, and** 120**. Unit: day.
        self.classic_expend_expired_days = classic_expend_expired_days  # type: int
        # The connection string of the instance
        self.connection_string = connection_string  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceNetExpireTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classic_expend_expired_days is not None:
            result['ClassicExpendExpiredDays'] = self.classic_expend_expired_days
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassicExpendExpiredDays') is not None:
            self.classic_expend_expired_days = m.get('ClassicExpendExpiredDays')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyDBInstanceNetExpireTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceNetExpireTimeResponseBody, self).to_map()
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


class ModifyDBInstanceNetExpireTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceNetExpireTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceNetExpireTimeResponse, self).to_map()
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
            temp_model = ModifyDBInstanceNetExpireTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceNetworkTypeRequest(TeaModel):
    def __init__(self, classic_expired_days=None, dbinstance_id=None, network_type=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, retain_classic=None,
                 security_token=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # The retention period of the original classic network address when you change the network type to VPC. Valid values: **14**, **30**, **60**, and **120**. Unit: days.
        # 
        # >  This parameter is required when the **NetworkType** parameter is set to **VPC** and the **RetainClassic** parameter is set to **True**.
        self.classic_expired_days = classic_expired_days  # type: int
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The network type to switch to. Valid values:
        # 
        # *   **VPC**\
        # *   **Classic**\
        self.network_type = network_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # Specifies whether to retain the original classic network address when you change the network type to VPC. Valid values:
        # 
        # - **True**: retains the original classic network address.
        # - **False**: does not retain the original classic network address.
        # 
        # > * This parameter is required when the **NetworkType** parameter is set to **VPC**.
        # > * If you set this parameter to **True**, you must also specify the **ClassicExpiredDays** parameter.
        self.retain_classic = retain_classic  # type: str
        self.security_token = security_token  # type: str
        # The ID of the vSwitch.
        # 
        # >  This parameter is required when the **NetworkType** parameter is set to **VPC**.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC).
        # 
        # >  This parameter is required when the **NetworkType** parameter is set to **VPC**.
        self.vpc_id = vpc_id  # type: str
        # The zone ID of the instance. You can call the [DescribeRegions](~~468365~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceNetworkTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classic_expired_days is not None:
            result['ClassicExpiredDays'] = self.classic_expired_days
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retain_classic is not None:
            result['RetainClassic'] = self.retain_classic
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetainClassic') is not None:
            self.retain_classic = m.get('RetainClassic')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ModifyDBInstanceNetworkTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class ModifyDBInstanceSSLRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, sslaction=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The operation on the SSL feature. Valid values: Valid values:
        # 
        # *   **Open**: enables SSL encryption.
        # *   **Close**: disables SSL encryption.
        # *   **Update**: updates the SSL certificate.
        self.sslaction = sslaction  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSSLRequest, self).to_map()
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
        if self.sslaction is not None:
            result['SSLAction'] = self.sslaction
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SSLAction') is not None:
            self.sslaction = m.get('SSLAction')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyDBInstanceSSLResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class ModifyDBInstanceSpecRequest(TeaModel):
    def __init__(self, auto_pay=None, business_info=None, coupon_no=None, dbinstance_class=None, dbinstance_id=None,
                 dbinstance_storage=None, effective_time=None, extra_param=None, order_type=None, owner_account=None, owner_id=None,
                 readonly_replicas=None, replication_factor=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # 
        # *   **true**: enables automatic payment. Make sure that your Alibaba Cloud account has a sufficient balance.
        # *   **false**: disables automatic payment. You can perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > **User Center**. In the left-side navigation pane, choose **Order Management** > **Order**. On the **Orders for Services** tab, find the order and pay for the order.
        self.auto_pay = auto_pay  # type: bool
        # The business information.
        self.business_info = business_info  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The instance type. For more information, see [Instance types](~~57141~~). You can also call the [DescribeAvailableResource](~~149719~~) operation to view instance types.
        # 
        # > You must specify at least one of the DBInstanceClass and **DBInstanceStorage** parameters.
        self.dbinstance_class = dbinstance_class  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The storage capacity of the instance. Valid values: 10 to 3000. The value must be a multiple of 10. Unit: GB. The values that can be specified for this parameter are subject to the instance types. For more information, see [Instance types](~~57141~~).
        # 
        # > 
        # 
        # *   You must specify at least one of the DBInstanceStorage and **DBInstanceClass** parameters.
        # 
        # *   Storage capacity can be scaled down only for pay-as-you-go replica set instances. The new storage capacity you specify must be greater than the used storage capacity.
        self.dbinstance_storage = dbinstance_storage  # type: str
        # The time when the changed configurations take effect. Default value: Immediately. Valid values:
        # 
        # *   **Immediately**: The configurations immediately take effect.
        # *   **MaintainTime**: The configurations take effect during the maintenance window of the instance.
        self.effective_time = effective_time  # type: str
        # Additional parameter
        self.extra_param = extra_param  # type: str
        # The type of the configuration change. Default value: DOWNGRADE. Valid values:
        # 
        # *   **UPGRADE**\
        # *   **DOWNGRADE**\
        # 
        # > This parameter can be configured only when the billing method of the instance is subscription.
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of read-only nodes. Valid values: **0** to **5**.
        # 
        # If your instance has only **Classic Network** and **VPC** endpoints, you must apply for a public endpoint or release the classic network endpoint for the instance before you can change the **Read-only Nodes** value.
        # 
        # > You can go to the **Database Connections** page to view the types of networks that are enabled.
        self.readonly_replicas = readonly_replicas  # type: str
        # The number of nodes in the instance.
        # 
        # *   Valid values of replica set instances: **3**, **5**, and **7**\
        # *   Valid values of standalone instances: **1**\
        # 
        # > This parameter is not required for a serverless instance which is only available on the China site (aliyun.com).
        self.replication_factor = replication_factor  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.extra_param is not None:
            result['ExtraParam'] = self.extra_param
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExtraParam') is not None:
            self.extra_param = m.get('ExtraParam')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyDBInstanceSpecResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSpecResponseBody, self).to_map()
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


class ModifyDBInstanceSpecResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ModifyDBInstanceTDERequest(TeaModel):
    def __init__(self, dbinstance_id=None, encryption_key=None, encryptor_name=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, role_arn=None, security_token=None,
                 tdestatus=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the custom key.
        self.encryption_key = encryption_key  # type: str
        # The encryption method. Set the value to **aes-256-cbc**.
        # 
        # > This parameter is valid only when the **TEDStatus** parameter is set to **enabled**.
        self.encryptor_name = encryptor_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The Alibaba Cloud Resource Name (ARN) of the specified Resource Access Management (RAM) role. The ARN is displayed in the `acs:ram::$accountID:role/$roleName` format.
        # 
        # > 
        # 
        # *   `$accountID`: specifies the ID of the Alibaba Cloud account. To view the account ID, log on to the Alibaba Cloud Management Console, move your pointer over your profile picture in the upper-right corner, and then click Security Settings.
        # 
        # *   `$roleName`: specifies the name of the RAM role. To view the RAM role name, log on to the RAM console. In the left-side navigation pane, choose Identities > Roles. On the Roles page, view the name of the RAM role.
        self.role_arn = role_arn  # type: str
        self.security_token = security_token  # type: str
        # The TDE status. When the value of this parameter is set to **Enabled**, TDE is enabled.
        # 
        # > You cannot disable TDE after it is enabled. Proceed with caution.
        self.tdestatus = tdestatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceTDERequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryptor_name is not None:
            result['EncryptorName'] = self.encryptor_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptorName') is not None:
            self.encryptor_name = m.get('EncryptorName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class ModifyDBInstanceTDEResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceTDEResponseBody, self).to_map()
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


class ModifyDBInstanceTDEResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceTDEResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceTDEResponse, self).to_map()
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
            temp_model = ModifyDBInstanceTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGlobalSecurityIPGroupRequest(TeaModel):
    def __init__(self, gip_list=None, global_ig_name=None, global_security_group_id=None, owner_account=None,
                 owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.gip_list = gip_list  # type: str
        self.global_ig_name = global_ig_name  # type: str
        self.global_security_group_id = global_security_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gip_list is not None:
            result['GIpList'] = self.gip_list
        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')
        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyGlobalSecurityIPGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupResponseBody, self).to_map()
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


class ModifyGlobalSecurityIPGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyGlobalSecurityIPGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupResponse, self).to_map()
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
            temp_model = ModifyGlobalSecurityIPGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGlobalSecurityIPGroupNameRequest(TeaModel):
    def __init__(self, global_ig_name=None, global_security_group_id=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.global_ig_name = global_ig_name  # type: str
        self.global_security_group_id = global_security_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyGlobalSecurityIPGroupNameResponseBodyGlobalSecurityIPGroup(TeaModel):
    def __init__(self, gip_list=None, global_ig_name=None, global_security_group_id=None, region_id=None):
        self.gip_list = gip_list  # type: str
        self.global_ig_name = global_ig_name  # type: str
        self.global_security_group_id = global_security_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupNameResponseBodyGlobalSecurityIPGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gip_list is not None:
            result['GIpList'] = self.gip_list
        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')
        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyGlobalSecurityIPGroupNameResponseBody(TeaModel):
    def __init__(self, global_security_ipgroup=None, request_id=None):
        self.global_security_ipgroup = global_security_ipgroup  # type: list[ModifyGlobalSecurityIPGroupNameResponseBodyGlobalSecurityIPGroup]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.global_security_ipgroup:
            for k in self.global_security_ipgroup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GlobalSecurityIPGroup'] = []
        if self.global_security_ipgroup is not None:
            for k in self.global_security_ipgroup:
                result['GlobalSecurityIPGroup'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.global_security_ipgroup = []
        if m.get('GlobalSecurityIPGroup') is not None:
            for k in m.get('GlobalSecurityIPGroup'):
                temp_model = ModifyGlobalSecurityIPGroupNameResponseBodyGlobalSecurityIPGroup()
                self.global_security_ipgroup.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyGlobalSecurityIPGroupNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyGlobalSecurityIPGroupNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupNameResponse, self).to_map()
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
            temp_model = ModifyGlobalSecurityIPGroupNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGlobalSecurityIPGroupRelationRequest(TeaModel):
    def __init__(self, dbcluster_id=None, global_security_group_id=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        self.dbcluster_id = dbcluster_id  # type: str
        self.global_security_group_id = global_security_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyGlobalSecurityIPGroupRelationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupRelationResponseBody, self).to_map()
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


class ModifyGlobalSecurityIPGroupRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyGlobalSecurityIPGroupRelationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyGlobalSecurityIPGroupRelationResponse, self).to_map()
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
            temp_model = ModifyGlobalSecurityIPGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, auto_renew=None, dbinstance_id=None, duration=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If this parameter is set to **true**, you must set the **Duration** parameter.
        self.auto_renew = auto_renew  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The auto-renewal period. Valid values: **1** to **12**. Unit: month.
        # 
        # >  This parameter is valid only when **AutoRenew** is set to **true**.
        self.duration = duration  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the region ID of the instance.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAutoRenewalAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.duration is not None:
            result['Duration'] = self.duration
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyInstanceAutoRenewalAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAutoRenewalAttributeResponseBody, self).to_map()
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


class ModifyInstanceAutoRenewalAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceAutoRenewalAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceAutoRenewalAttributeResponse, self).to_map()
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
            temp_model = ModifyInstanceAutoRenewalAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVpcAuthModeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, vpc_auth_mode=None):
        # The operation that you want to perform. Set the value to **ModifyInstanceVpcAuthMode**.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The ID of the mongos node in the specified sharded cluster instance.
        # 
        # >  This parameter can be used only when the instance type is sharded cluster.
        self.vpc_auth_mode = vpc_auth_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceVpcAuthModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        if self.vpc_auth_mode is not None:
            result['VpcAuthMode'] = self.vpc_auth_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        if m.get('VpcAuthMode') is not None:
            self.vpc_auth_mode = m.get('VpcAuthMode')
        return self


class ModifyInstanceVpcAuthModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Specifies whether to enable authentication to allow access within a VPC. Valid values:
        # 
        # *   **Open**: enables password-free access.
        # *   **Close**: disables password-free access.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceVpcAuthModeResponseBody, self).to_map()
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


class ModifyInstanceVpcAuthModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceVpcAuthModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceVpcAuthModeResponse, self).to_map()
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
            temp_model = ModifyInstanceVpcAuthModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodeSpecRequest(TeaModel):
    def __init__(self, auto_pay=None, business_info=None, client_token=None, coupon_no=None, dbinstance_id=None,
                 effective_time=None, from_app=None, node_class=None, node_id=None, node_storage=None, order_type=None,
                 owner_account=None, owner_id=None, readonly_replicas=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None, switch_time=None):
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # 
        # *   **true**: enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment.
        self.auto_pay = auto_pay  # type: bool
        # The business information. This is an additional parameter.
        self.business_info = business_info  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The time when the changed configurations take effect. Default value: Immediately. Valid values:
        # 
        # *   **Immediately**: The new configurations immediately take effect.
        # *   **MaintainTime**: The new configurations take effect during the maintenance window of the instance.
        self.effective_time = effective_time  # type: str
        # The source of the request. Valid values:
        # 
        # *   **OpenApi**: the ApsaraDB for MongoDB API
        # *   **mongo_buy**: the ApsaraDB for MongoDB console
        self.from_app = from_app  # type: str
        # The specifications of the shard or mongos node. For more information, see [Instance types](~~57141~~).
        self.node_class = node_class  # type: str
        # The ID of the shard or mongos node in the sharded cluster instance. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the node ID.
        # 
        # > If you set this parameter to the ID of the shard node, you must also specify the **NodeStorage** parameter.
        self.node_id = node_id  # type: str
        # The storage capacity of the shard node. Unit: GB.
        # 
        # *   Valid values are **10** to **2000** if the instance uses local SSDs.
        # *   Valid values are **20** to **16000** if the instance uses enhanced SSDs (ESSDs) at PL1.
        # 
        # > The value must be a multiple of 10.
        self.node_storage = node_storage  # type: int
        # The order type. Valid values:
        # 
        # *   **UPGRADE**\
        # *   **DOWNGRADE**\
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of read-only nodes in the shard node.
        # 
        # Valid values: **0** to **5**. The value must be an integer. Default value: **0**.
        self.readonly_replicas = readonly_replicas  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        # The execution time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.switch_time = switch_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodeSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_storage is not None:
            result['NodeStorage'] = self.node_storage
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeStorage') is not None:
            self.node_storage = m.get('NodeStorage')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class ModifyNodeSpecResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodeSpecResponseBody, self).to_map()
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


class ModifyNodeSpecResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyNodeSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNodeSpecResponse, self).to_map()
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
            temp_model = ModifyNodeSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodeSpecBatchRequest(TeaModel):
    def __init__(self, auto_pay=None, business_info=None, client_token=None, coupon_no=None, dbinstance_id=None,
                 effective_time=None, nodes_info=None, order_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # Specifies whether to enable automatic payment for the instance. Valid values:
        # 
        # *   **true**: enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. You can perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > User Center to go to the **Billing Management** console. In the left-side navigation pane, click **Orders**. On the **Orders** page, find the order and complete the payment.
        # 
        # Default value: **true**.
        self.auto_pay = auto_pay  # type: bool
        # The business information.
        self.business_info = business_info  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The ID of the instance whose configurations you want to modify.
        self.dbinstance_id = dbinstance_id  # type: str
        # The time when the modified configurations take effect. Valid values:
        # 
        # *   **Immediately**: The configurations immediately take effect.
        # *   **MaintainTime**: The configurations take effect during the maintenance window of the instance.
        # 
        # > 
        # 
        # *   You can call the [ModifyDBInstanceMaintainTime](~~62008~~) operation to modify the maintenance window of an instance.
        # 
        # *   You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to view the maintenance window of an instance.
        # 
        # Default value: **Immediately**.
        self.effective_time = effective_time  # type: str
        # The configuration information of the mongos nodes or shard nodes whose configurations you want to modify. For more information, see [Instance types](~~57141~~).
        self.nodes_info = nodes_info  # type: str
        # The type of configuration modifications. Valid values:
        # 
        # *   **UPGRADE**\
        # *   **DOWNGRADE**\
        # 
        # > This parameter is available only if the billing method of the instance is subscription.
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the region. You can call the [DescribeRegions](~~61933~~) operation to query the latest available regions.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodeSpecBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.nodes_info is not None:
            result['NodesInfo'] = self.nodes_info
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('NodesInfo') is not None:
            self.nodes_info = m.get('NodesInfo')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyNodeSpecBatchResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodeSpecBatchResponseBody, self).to_map()
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


class ModifyNodeSpecBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyNodeSpecBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNodeSpecBatchResponse, self).to_map()
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
            temp_model = ModifyNodeSpecBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParametersRequest(TeaModel):
    def __init__(self, character_type=None, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None,
                 parameters=None, region_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The role of the instance. Valid values:
        # 
        # *   **db**: a shard node
        # *   **cs**: a Configserver node
        # *   **mongos**: a mongos node
        # *   **logic**: a sharded cluster instance
        self.character_type = character_type  # type: str
        # The ID of the instance.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the NodeId parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the mongos or shard node in the specified sharded cluster instance.
        # 
        # >  This parameter is valid only when DBInstanceId is set to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The instance parameters that you want to modify and their values. Specify this parameter in a JSON string. Sample format: {"ParameterName1":"ParameterValue1","ParameterName2":"ParameterValue2"}.
        # 
        # >  You can call the [DescribeParameterTemplates](~~67618~~) operation to query a list of default parameter templates.
        self.parameters = parameters  # type: str
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyParametersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class ModifyResourceGroupRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, region_id=None,
                 resource_group_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeRegions](~~61933~~) operation to query the region ID.
        self.region_id = region_id  # type: str
        # The ID of the resource group. For more information, see [View basic information of a resource group](~~151181~~).
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
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
        return self


class ModifyResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyResourceGroupResponseBody, self).to_map()
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


class ModifyResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyResourceGroupResponse, self).to_map()
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
            temp_model = ModifyResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_group_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The ID of the ECS security group.
        # 
        # > * You can bind up to 10 ECS security groups to an ApsaraDB for MongoDB instance.
        # > * You can call the [DescribeSecurityGroup](~~25556~~) operation of ECS to query the security groups in the specified region.
        self.security_group_id = security_group_id  # type: str
        self.security_token = security_token  # type: str

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifySecurityGroupConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ModifySecurityIpsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, modify_mode=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_ip_group_attribute=None, security_ip_group_name=None,
                 security_ips=None, security_token=None):
        # The ID of an instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The method of modification. Valid values:
        # 
        # *   **Cover**: overwrites the whitelist.
        # *   **Append**: appends data to the whitelist.
        # *   **Delete**: deletes the whitelist.
        # 
        # The default value is **Cover**.
        self.modify_mode = modify_mode  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The attributes of an IP address whitelist. It can contain a maximum of 120 characters in length and can contain uppercase letters, lowercase letters, and digits.
        # 
        # This parameter is empty by default.
        self.security_ip_group_attribute = security_ip_group_attribute  # type: str
        # The name of the IP address whitelist to be modified. The default value is **default**.
        self.security_ip_group_name = security_ip_group_name  # type: str
        # The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. You can add IP addresses in one of the following two formats:
        # 
        # *   IP addresses. Example: 10.23.12.24.
        # *   Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.24/24, where 24 indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value within the range of 1 to 32.
        self.security_ips = security_ips  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_ip_group_attribute is not None:
            result['SecurityIpGroupAttribute'] = self.security_ip_group_attribute
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityIpGroupAttribute') is not None:
            self.security_ip_group_attribute = m.get('SecurityIpGroupAttribute')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class ReleaseNodePrivateNetworkAddressRequest(TeaModel):
    def __init__(self, dbinstance_id=None, network_type=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the sharded cluster instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The network type of the internal endpoint. Valid values:
        # 
        # *   **VPC**\
        # *   **Classic**\
        # 
        # >  You can call the [DescribeShardingNetworkAddress](~~62135~~) operation to query the network type of the internal endpoint.
        self.network_type = network_type  # type: str
        # The ID of the shard or Configserver node.
        # 
        # >  You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the ID of the shard or Configserver node.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseNodePrivateNetworkAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class ReleaseNodePrivateNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseNodePrivateNetworkAddressResponseBody, self).to_map()
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


class ReleaseNodePrivateNetworkAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseNodePrivateNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseNodePrivateNetworkAddressResponse, self).to_map()
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
            temp_model = ReleaseNodePrivateNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePublicNetworkAddressRequest(TeaModel):
    def __init__(self, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        self.dbinstance_id = dbinstance_id  # type: str
        # A sharded cluster instance consists of three components: mongos, shard, and Configserver.
        # 
        # > * This parameter is valid only if you set the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        # > * You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the ID of the mongos, shard, or Configserver node.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleasePublicNetworkAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class ReleasePublicNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleasePublicNetworkAddressResponseBody, self).to_map()
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


class ReleasePublicNetworkAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleasePublicNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleasePublicNetworkAddressResponse, self).to_map()
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
            temp_model = ReleasePublicNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewDBInstanceRequest(TeaModel):
    def __init__(self, auto_pay=None, business_info=None, client_token=None, coupon_no=None, dbinstance_id=None,
                 owner_account=None, owner_id=None, period=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        # Specifies whether to enable automatic payment for the instance. Valid values:
        # 
        # *   **true**: enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. You must perform the following operations to pay for the instance: Payment instructions: Log on to the console. In the upper-right corner, click **Billing Management** and select **Billing Management** from the drop-down list. The Billing Management page appears. In the left-side navigation pane, click **Bills**. On the Unpaid tab, click Make a Payment in the Actions column corresponding to the bill you want to pay.
        # 
        # Default value: **true**.
        self.auto_pay = auto_pay  # type: bool
        # The business information.
        self.business_info = business_info  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # The coupon code. Default value: **youhuiquan_promotion_option_id_for_blank**.
        self.coupon_no = coupon_no  # type: str
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The period you set for the instance to implement payment renewal. Unit: months. Valid values: **1-9, 12, 24, and 36**.
        self.period = period  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RenewDBInstanceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewDBInstanceResponseBody, self).to_map()
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


class RenewDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewDBInstanceResponse, self).to_map()
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
            temp_model = RenewDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, character_type=None, dbinstance_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The operation that you want to perform. Set the value to **ResetAccountPassword**.
        self.account_name = account_name  # type: str
        # The ID of the instance.
        self.account_password = account_password  # type: str
        # The type of the database account. Valid values:
        # 
        # *   mongos: an account that can be used to log on to mongos
        # *   shard: an account that can be used to log on to shards
        self.character_type = character_type  # type: str
        # com.aliyun.abs.dds.service.v20151201.domain.ResetDdsAccountPasswordRequest
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The account for which you want to reset the password. Set the value to **root**.
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
    def __init__(self, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The instance ID.
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the shard or mongos node in the sharded cluster instance.
        # 
        # > The sharded cluster instance is restarted if you do not specify this parameter.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        return self


class RestartDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
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


class RestoreDBInstanceRequest(TeaModel):
    def __init__(self, backup_id=None, dbinstance_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the backup.
        # 
        # >  You can call the [DescribeBackups](~~62172~~) operation to query the backup ID.
        self.backup_id = backup_id  # type: int
        # The ID of an instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreDBInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RestoreDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreDBInstanceResponseBody, self).to_map()
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


class RestoreDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestoreDBInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreDBInstanceResponse, self).to_map()
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
            temp_model = RestoreDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchDBInstanceHARequest(TeaModel):
    def __init__(self, dbinstance_id=None, node_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, role_ids=None, security_token=None, switch_mode=None):
        # The ID of the instance
        self.dbinstance_id = dbinstance_id  # type: str
        # The ID of the shard node in the sharded cluster instance.
        # 
        # > You must specify this parameter if you set the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The IDs of the roles who switch the primary and secondary nodes for the instance. You can call the [DescribeRoleZoneInfo](~~123802~~) operation to view the IDs and information of roles of nodes.
        # 
        # > 
        # 
        # *   Separate role IDs with commas (,). If this parameter is not specified, the primary and secondary nodes are switched.
        # 
        # *   If you set the **DBInstanceId** parameter to the ID of a sharded cluster instance, the roles who switch the primary and secondary nodes for the instance must belong to one shard node.
        self.role_ids = role_ids  # type: str
        self.security_token = security_token  # type: str
        # The time when the primary and secondary nodes are switched. Valid values:
        # 
        # *   0: The primary and secondary nodes are immediately switched.
        # *   1: The primary and secondary nodes are switched during the O\&M time period.
        self.switch_mode = switch_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchDBInstanceHARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')
        return self


class SwitchDBInstanceHAResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchDBInstanceHAResponseBody, self).to_map()
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


class SwitchDBInstanceHAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchDBInstanceHAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchDBInstanceHAResponse, self).to_map()
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
            temp_model = SwitchDBInstanceHAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag.
        # 
        # N specifies the serial number of the tag. The following example shows how to calculate consumption intervals:
        # 
        # - **Tag.1.Key** specifies the key of the first tag.
        # - **Tag.2.Key** specifies the key of the second tag.
        self.key = key  # type: str
        # The value of tag.
        # 
        # N specifies the serial number of the tag. The following example shows how to calculate consumption intervals: 
        # 
        # - **Tag.1.Value** specifies the value of the first tag.
        # - **Tag.2.Value** specifies the value of the second tag.
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
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_group_id=None, resource_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None, tag=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The list of resource IDs.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The resource type. Set the value to **INSTANCE**.
        self.resource_type = resource_type  # type: str
        # The tags that are attached to the resources.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The ID of the request.
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


class TransferClusterBackupRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferClusterBackupRequest, self).to_map()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class TransferClusterBackupResponseBody(TeaModel):
    def __init__(self, already_done=None, request_id=None):
        self.already_done = already_done  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferClusterBackupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_done is not None:
            result['AlreadyDone'] = self.already_done
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlreadyDone') is not None:
            self.already_done = m.get('AlreadyDone')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransferClusterBackupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferClusterBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferClusterBackupResponse, self).to_map()
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
            temp_model = TransferClusterBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransformInstanceChargeTypeRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, business_info=None, charge_type=None, coupon_no=None,
                 instance_id=None, owner_account=None, owner_id=None, period=None, pricing_cycle=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # > Default value: **true**.
        self.auto_pay = auto_pay  # type: bool
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # > Default value: **false**.
        self.auto_renew = auto_renew  # type: str
        # The business information. This is an additional parameter.
        self.business_info = business_info  # type: str
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The ID of the instance
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The subscription duration of the instance. Unit: months. Valid values: **1, 2, 3, 4, 5, 6, 7, 8, 9******, **12**, **24**, and **36**.
        self.period = period  # type: long
        self.pricing_cycle = pricing_cycle  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransformInstanceChargeTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class TransformInstanceChargeTypeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransformInstanceChargeTypeResponseBody, self).to_map()
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


class TransformInstanceChargeTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransformInstanceChargeTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransformInstanceChargeTypeResponse, self).to_map()
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
            temp_model = TransformInstanceChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransformToPrePaidRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, business_info=None, coupon_no=None, instance_id=None,
                 owner_account=None, owner_id=None, period=None, resource_owner_account=None, resource_owner_id=None,
                 security_token=None):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: enables automatic payment.
        # *   **false**: disables automatic payment. For more information, see [Renew an ApsaraDB for MongoDB subscription instance](~~85052~~).
        # 
        # >  Default value: **true**.
        self.auto_pay = auto_pay  # type: bool
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  Default value: **false**.
        self.auto_renew = auto_renew  # type: str
        # The business information. This is an additional parameter.
        self.business_info = business_info  # type: str
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The subscription duration of the instance. Unit: months. Valid values: **1, 2, 3, 4, 5, 6, 7, 8, 9******, **12**, **24**, and **36**.
        self.period = period  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransformToPrePaidRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class TransformToPrePaidResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransformToPrePaidResponseBody, self).to_map()
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


class TransformToPrePaidResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransformToPrePaidResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransformToPrePaidResponse, self).to_map()
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
            temp_model = TransformToPrePaidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, owner_account=None, owner_id=None, region_id=None, resource_group_id=None,
                 resource_id=None, resource_owner_account=None, resource_owner_id=None, resource_type=None, tag_key=None):
        # Specifies whether to remove all tags from the instances. Valid values:
        # 
        # *   **true**: removes all tags from the instances.
        # *   **false**: does not remove all tags from the instances.
        # 
        # > 
        # 
        # *   Default value: **false**.
        # 
        # *   If you specify the **TagKey** parameter together with this parameter, this parameter does not take effect.
        self.all = all  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](~~62010~~) operation to query the region ID of the instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The resource IDs.
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # The resource type. Set the value to **INSTANCE**.
        self.resource_type = resource_type  # type: str
        # The tag keys of the resource.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The ID of the request.
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


class UpgradeDBInstanceEngineVersionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, engine_version=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        # The database version to which you want to upgrade. Valid values: **3.4**, **4.0**, and **4.2**.
        # 
        # >  This database version must be later than the current database version of the instance.
        self.engine_version = engine_version  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
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
        return self


class UpgradeDBInstanceEngineVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class UpgradeDBInstanceKernelVersionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, security_token=None):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class UpgradeDBInstanceKernelVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


